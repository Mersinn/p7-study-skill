"""Deterministic helpers shared by P7 release tooling (stdlib only)."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter
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


def referenced_source_ids(text: str, known_ids: Iterable[str]) -> list[str]:
    return sorted(source_id for source_id in known_ids if source_id and source_id in text)


def build_capsule_catalog(root: Path = PACKAGE_ROOT) -> list[dict[str, Any]]:
    normalization = load_normalization(root)
    source_ids = {row["source_id"] for row in load_source_rows(root) if row.get("source_id")}
    catalog: list[dict[str, Any]] = []
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
        ids = referenced_source_ids(text, source_ids)
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
                "source_resolution": "resolved" if ids else "metadata_only",
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
        for line_no, line in enumerate(section.group(1).splitlines(), start=1):
            stripped = line.strip()
            if not stripped.startswith("|") or re.match(r"^\|?\s*:?-+", stripped):
                continue
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if not cells or all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                continue
            if any(fold(cell) in {"dado", "valor", "fonte", "status"} for cell in cells):
                continue
            row_text = " | ".join(cells)
            rows.append(
                {
                    "capsule_path": relpath(path, root),
                    "section_row": line_no,
                    "claim_text": row_text,
                    "source_ids": ";".join(referenced_source_ids(row_text, source_ids)),
                }
            )
    return rows


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
    return {
        "schema_version": SCHEMA_VERSION,
        "capsules": {
            "baseline_before_recovery": 156,
            "total": len(catalog),
            "net_recovered_since_baseline": len(catalog) - 156,
            "by_discipline": dict(sorted(Counter(item["discipline"] or "UNKNOWN" for item in catalog).items())),
            "by_risk": dict(sorted(Counter(item["risk"] or "UNKNOWN" for item in catalog).items())),
            "by_review_status": dict(sorted(Counter(item["review_status"] or "UNKNOWN" for item in catalog).items())),
            "without_resolved_source_id": sum(item["source_resolution"] != "resolved" for item in catalog),
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
