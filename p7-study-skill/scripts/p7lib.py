"""Deterministic helpers shared by P7 release tooling (stdlib only)."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "1.0.0"
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CAPSULE_METADATA_FIELDS = {
    "Disciplina": "discipline",
    "Unidade": "unit",
    "Prioridade": "priority",
    "Risco clínico": "risk",
    "Status": "review_status",
}
EXCLUDED_PARTS = {".git", "__pycache__", ".p7-state", ".pytest_cache"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fold(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value.strip())
    return "".join(ch for ch in decomposed if not unicodedata.combining(ch)).casefold()


def stable_slug(value: str) -> str:
    normalized = fold(value)
    normalized = re.sub(r"[^a-z0-9]+", "_", normalized).strip("_")
    return normalized or "unknown"


def relpath(path: Path, root: Path = PACKAGE_ROOT) -> str:
    return path.relative_to(root).as_posix()


def capsule_paths(root: Path = PACKAGE_ROOT) -> list[Path]:
    base = root / "capsules"
    return sorted(
        (path for path in base.rglob("*.md") if path.name != "CAPSULE_INDEX.md"),
        key=lambda path: relpath(path, root),
    )


def parse_capsule_metadata(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for display_name, key in CAPSULE_METADATA_FIELDS.items():
        match = re.search(rf"^- {re.escape(display_name)}:\s*(.+?)\s*$", text, re.MULTILINE)
        if match:
            result[key] = match.group(1).strip()
    return result


def capsule_title(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def load_normalization(root: Path = PACKAGE_ROOT) -> dict[str, dict[str, str]]:
    return load_json(root / "config" / "normalization.json")


def normalize_metadata(kind: str, value: str | None, mapping: dict[str, dict[str, str]]) -> str | None:
    if value is None:
        return None
    direct = mapping.get(kind, {})
    if value in direct:
        return direct[value]
    folded = fold(value)
    for alias, canonical in direct.items():
        if fold(alias) == folded:
            return canonical
    return None


def load_source_rows(root: Path = PACKAGE_ROOT) -> list[dict[str, str]]:
    path = root / "p7_source_pack" / "00_SOURCE_MANIFEST.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


@lru_cache(maxsize=16)
def _source_match_index(ids: tuple[str, ...]) -> tuple:
    """Cache immutable source patterns only; changed ID sets get a new index."""
    levels = {level: [] for level in ("stem", "folded", "placeholder")}
    for source_id in ids:
        suffix = re.search(r"__[0-9a-fA-F]{10}$", source_id)
        if suffix is None:
            continue
        stem = source_id[:suffix.start()]
        if len(stem) < 6:
            continue
        normalized_stem = fold(stem)
        for level in levels:
            needle = stem if level == "stem" else normalized_stem
            if level == "placeholder":
                if "_" not in needle:
                    continue
                pattern = "".join(r"\w" if char == "_" else re.escape(char) for char in needle)
            else:
                pattern = re.escape(needle)
            levels[level].append((source_id, needle, re.compile(r"(?:^|[;|\n])\s*`?" + pattern + r"(?!\w)")))
    return tuple((level, tuple(patterns)) for level, patterns in levels.items())


def referenced_source_ids(text: str, known_ids: Iterable[str]) -> dict[str, Any]:
    """Resolve a reference, not clinical support; retain its strongest match level.

    Only terminal ``__hash10`` IDs participate in inferred L1-L3 matching. A
    placeholder consumes one Unicode word character, never a separator. Stem
    boundaries prevent substrings inside longer names or unknown full IDs.
    Inferred citations must start the cell or a semicolon/pipe/newline segment;
    words buried in explanatory prose are not treated as document names.
    Distinct explicit full IDs in nonoverlapping spans are multiple citations;
    competing inferred IDs at one level remain ambiguous, even in a long cell.
    """
    normalized_text = fold(text)
    result: dict[str, Any] = {
        "source_ids": [], "status": "unresolved_source_reference",
        "level": None, "candidates": [],
    }
    if any(marker in normalized_text for marker in ("conhecimento geral", "ausente da fonte")):
        result["status"] = "declared_no_source"
        return result

    ids = tuple(sorted({source_id for source_id in known_ids if source_id}))
    exact = [source_id for source_id in ids if source_id in text]
    if exact:
        spans = [(match.start(), match.end(), source_id) for source_id in exact
                 for match in re.finditer(re.escape(source_id), text)]
        competing = any(a[2] != b[2] and a[0] < b[1] and b[0] < a[1]
                        for index, a in enumerate(spans) for b in spans[index + 1:])
        result.update(level="exact", candidates=exact)
        if competing:
            result["status"] = "ambiguous"
        else:
            result.update(source_ids=exact, status="resolved:exact")
        return result

    for level, patterns in _source_match_index(ids):
        candidates = []
        haystack = text if level == "stem" else normalized_text
        for source_id, needle, pattern in patterns:
            if level != "placeholder" and needle not in haystack:
                continue
            if pattern.search(haystack):
                candidates.append(source_id)
        if candidates:
            result.update(level=level, candidates=candidates)
            if len(candidates) == 1:
                result.update(source_ids=candidates, status=f"resolved:{level}")
            else:
                result["status"] = "ambiguous"
            return result
    return result


def build_capsule_catalog(root: Path = PACKAGE_ROOT) -> list[dict[str, Any]]:
    normalization = load_normalization(root)
    source_ids = {row["source_id"] for row in load_source_rows(root) if row.get("source_id")}
    catalog: list[dict[str, Any]] = []
    precision_by_path: dict[str, list[dict[str, Any]]] = {}
    for row in precision_rows(root):
        precision_by_path.setdefault(row["capsule_path"], []).append(row)
    for path in capsule_paths(root):
        text = path.read_text(encoding="utf-8")
        legacy = parse_capsule_metadata(text)
        relative = relpath(path, root)
        discipline_from_path = path.parent.name
        discipline = normalize_metadata(
            "discipline", legacy.get("discipline", discipline_from_path), normalization
        ) or normalize_metadata("discipline", discipline_from_path, normalization)
        unit = normalize_metadata("unit", legacy.get("unit"), normalization)
        legacy_priority = normalize_metadata("priority", legacy.get("priority"), normalization)
        risk = normalize_metadata("risk", legacy.get("risk"), normalization)
        # A no-source declaration applies to its cell, never the whole capsule.
        # Inferred titles in clinical prose are not evidence of a citation.
        resolutions = []
        for line in text.splitlines():
            cells = line.strip().strip("|").split("|") if line.lstrip().startswith("|") else [line]
            for cell in cells:
                literal_ids = [source_id for source_id in source_ids if source_id in cell]
                if literal_ids:
                    resolutions.append(referenced_source_ids(cell, literal_ids))
            source_metadata = re.match(r"^- Fontes? usadas?:\s*(.*)$", line)
            if source_metadata:
                resolutions.append(referenced_source_ids(source_metadata.group(1), source_ids))
        for row in precision_by_path.get(relative, []):
            resolutions.append({
                "source_ids": row["source_ids"].split(";") if row["source_ids"] else [],
                "status": row["source_reference_status"],
            })
        levels_by_id: dict[str, set[str]] = {}
        for resolution in resolutions:
            for source_id in resolution["source_ids"]:
                levels_by_id.setdefault(source_id, set()).add(resolution["status"])
        ids = sorted(levels_by_id)
        statuses = sorted({resolution["status"] for resolution in resolutions})
        resolved_levels = sorted({level for levels in levels_by_id.values() for level in levels})
        catalog.append(
            {
                "schema_version": SCHEMA_VERSION,
                "capsule_id": f"capsule:{(discipline or stable_slug(discipline_from_path)).lower()}:{stable_slug(path.stem)}",
                "path": relative,
                "title": capsule_title(text, path.stem),
                "discipline": discipline,
                "unit": unit,
                "priority": "unscored",
                "legacy_priority_normalized": legacy_priority,
                "risk": risk,
                "legacy_metadata": legacy,
                "review_status": legacy.get("review_status"),
                "source_ids": ids,
                "source_resolution": ";".join(resolved_levels) if ids else "unresolved_source_reference",
                "source_reference_statuses": statuses,
                "source_match_levels_by_id": {key: sorted(value) for key, value in sorted(levels_by_id.items())},
                "source_resolution_policy": "union_of_explicit_cell_citations_and_precision_references; levels_preserved; not_clinical_support",
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return catalog


def index_capsule_paths(root: Path = PACKAGE_ROOT) -> set[str]:
    text = (root / "capsules" / "CAPSULE_INDEX.md").read_text(encoding="utf-8")
    return {match.replace("\\", "/") for match in re.findall(r"`(capsules/[^`]+?\.md)`", text)}


def precision_rows(root: Path = PACKAGE_ROOT) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    source_ids = {row["source_id"] for row in load_source_rows(root) if row.get("source_id")}
    for path in capsule_paths(root):
        text = path.read_text(encoding="utf-8")
        section = re.search(r"^## Dados de precisão\s*$([\s\S]*?)(?=^##\s|\Z)", text, re.MULTILINE)
        if not section:
            continue
        source_column: int | None = None
        for line_no, line in enumerate(section.group(1).splitlines(), start=1):
            stripped = line.strip()
            if not stripped.startswith("|") or re.match(r"^\|?\s*:?-+", stripped):
                continue
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if not cells or all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                continue
            if any(fold(cell) in {"dado", "valor", "fonte", "status"} for cell in cells):
                source_column = next((index for index, cell in enumerate(cells)
                                      if fold(cell).startswith("fonte")), None)
                continue
            row_text = " | ".join(cells)
            # Preserve literal L0 anywhere in the historical row and absence
            # precedence. Infer L1-L3 only from the declared source column.
            literal_ids = [source_id for source_id in source_ids if source_id in row_text]
            resolution = referenced_source_ids(row_text, literal_ids)
            if resolution["status"] == "unresolved_source_reference" and source_column is not None and source_column < len(cells):
                resolution = referenced_source_ids(cells[source_column], source_ids)
            rows.append(
                {
                    "capsule_path": relpath(path, root),
                    "section_row": line_no,
                    "claim_text": row_text,
                    "source_ids": ";".join(resolution["source_ids"]),
                    "source_reference_status": resolution["status"],
                }
            )
    return rows


def build_operation_counts(root: Path = PACKAGE_ROOT) -> dict[str, Any]:
    """Derive canonical operation counts from the 152 dissected item rows."""
    normalization = load_json(root / "config" / "normalization.json")
    configured = {key.casefold(): value for key, value in normalization.get("operation", {}).items()}
    source = root / "p7_source_pack" / "00_MAPA_OPERACAO_MOVIMENTO.md"
    in_item_bank = False
    counts: Counter[str] = Counter()
    labels: dict[str, set[str]] = {}
    rows = 0
    for raw in source.read_text(encoding="utf-8").splitlines():
        if raw.strip() == "## Banco de itens dissecados":
            in_item_bank = True
            continue
        if not in_item_bank or not raw.startswith("|"):
            continue
        fields = [field.strip() for field in raw.strip().strip("|").split("|")]
        if len(fields) != 6 or fields[0] == "Tema" or set(fields[0]) <= {"-", ":"}:
            continue
        label = fields[1]
        operation_id = configured.get(label.casefold())
        if operation_id is None:
            ascii_label = "".join(
                char for char in unicodedata.normalize("NFKD", label.casefold())
                if not unicodedata.combining(char)
            )
            operation_id = re.sub(r"[^a-z0-9]+", "_", ascii_label).strip("_")
        rows += 1
        counts[operation_id] += 1
        labels.setdefault(operation_id, set()).add(label)
    return {
        "schema_version": "1.0.0",
        "source": "p7_source_pack/00_MAPA_OPERACAO_MOVIMENTO.md#banco-de-itens-dissecados",
        "taxonomy_rows": rows,
        "operations": [
            {
                "operation_id": operation_id,
                "count": counts[operation_id],
                "observed_labels": sorted(labels[operation_id]),
            }
            for operation_id in sorted(counts, key=lambda key: (-counts[key], key))
        ],
    }


def package_files(root: Path = PACKAGE_ROOT) -> list[Path]:
    result: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if relative.parts and relative.parts[0] == "artifacts":
            continue
        # The active attestation hashes PACKAGE_MANIFEST.json in standalone
        # mode. Excluding the attestation itself avoids a circular hash while
        # every substantive package file remains covered.
        if relative.as_posix() == "registry/release_evidence.json":
            continue
        if path.suffix == ".pyc":
            continue
        result.append(path)
    return sorted(result, key=lambda path: relpath(path, root))


def build_manifest(root: Path = PACKAGE_ROOT) -> dict[str, Any]:
    files = [
        {"path": relpath(path, root), "bytes": path.stat().st_size, "sha256": sha256_file(path)}
        for path in package_files(root)
    ]
    return {
        "schema_version": SCHEMA_VERSION,
        "strategy": "stable-v1; artifacts/ and the manifest itself are excluded",
        "file_count": len(files),
        "total_bytes": sum(item["bytes"] for item in files),
        "files": files,
    }


def build_metrics(root: Path = PACKAGE_ROOT) -> dict[str, Any]:
    catalog = build_capsule_catalog(root)
    source_rows = load_source_rows(root)
    precision = precision_rows(root)
    claims = load_jsonl(root / "registry" / "clinical_claims.jsonl")
    canonical_sources = load_jsonl(root / "registry" / "sources.jsonl")
    source_versions = load_jsonl(root / "registry" / "source_versions.jsonl")
    fallback = {}
    for name in ("corpus_text", "vision_png"):
        path = root / name
        fallback[name] = {
            "availability": "bundled" if path.is_dir() else "absent",
            "behavior": "read_source" if path.is_dir() else "metadata_only_do_not_claim_inspection",
        }
    operations = build_operation_counts(root)
    return {
        "schema_version": SCHEMA_VERSION,
        "capsules": {
            "baseline_before_recovery": 156,
            "total": len(catalog),
            "net_recovered_since_baseline": len(catalog) - 156,
            "by_discipline": dict(sorted(Counter(item["discipline"] or "UNKNOWN" for item in catalog).items())),
            "by_risk": dict(sorted(Counter(item["risk"] or "UNKNOWN" for item in catalog).items())),
            "by_review_status": dict(sorted(Counter(item["review_status"] or "UNKNOWN" for item in catalog).items())),
            "without_resolved_source_id": sum(not item["source_ids"] for item in catalog),
            "source_count_policy": "any named match level identifies a referenced document only; levels are not evidence of equivalent reliability or clinical support",
            "source_reference_levels": dict(sorted(Counter(level for item in catalog for level in item["source_resolution"].split(";")).items())),
            "bytes": sum(item["bytes"] for item in catalog),
        },
        "sources": {"manifest_rows": len(source_rows), "unique_ids": len({row.get("source_id") for row in source_rows})},
        "canonical_evidence_registry": {
            "sources": len(canonical_sources),
            "source_versions": len(source_versions),
            "clinical_claims": len(claims),
            "claims_by_validity": dict(sorted(Counter(claim.get("states", {}).get("clinical_validity", "UNKNOWN") for claim in claims).items())),
        },
        "precision_rows": len(precision),
        "precision_provenance": dict(sorted(Counter(row["source_reference_status"] for row in precision).items())),
        "operation_taxonomy": {
            "taxonomy_rows": operations["taxonomy_rows"],
            "canonical_operations": len(operations["operations"]),
        },
        "runtime_source_availability": fallback,
    }


def calculate_priority(inputs: dict[str, int | None], policy: dict[str, Any]) -> dict[str, Any]:
    specs = policy["inputs"]
    missing = [name for name in specs if inputs.get(name) is None]
    if missing:
        return {"score": None, "label": "unscored", "missing": missing}
    score = 0
    for name, spec in specs.items():
        value = inputs[name]
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(f"{name} must be an integer")
        if not spec["min"] <= value <= spec["max"]:
            raise ValueError(f"{name} must be between {spec['min']} and {spec['max']}")
        score += value * spec["weight"]
    for label in ("high", "medium", "low"):
        limits = policy["thresholds"][label]
        if limits["min"] <= score <= limits["max"]:
            return {"score": score, "label": label, "missing": []}
    raise ValueError(f"score {score} is outside configured thresholds")
