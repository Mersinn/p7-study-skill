#!/usr/bin/env python3
"""Build the deterministic, stratified sample used by the P7 release red team.

The sample is deliberately finite and conservative:

* every non-current canonical claim (quarantined or conflict) is included;
* 4 current claims per clinical discipline with current registry coverage are
  selected by stable hash (EISA_II, EISCA and EISM);
* one high-risk capsule with an explicit historical/current split is selected
  per discipline when available;
* two high-risk metadata-only capsules are selected per discipline where that
  stratum exists.

Selection is mechanical. Adjudication happens later and is not encoded here.
"""

from __future__ import annotations

import csv
import hashlib
import json
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = REPO_ROOT / "p7-study-skill"
REPORTS = REPO_ROOT / "qualification" / "reports"

FIELDNAMES = [
    "sample_id",
    "sample_kind",
    "claim_id",
    "capsule_id",
    "capsule_path",
    "discipline",
    "risk",
    "clinical_validity",
    "criticality",
    "claim_type",
    "source_layers",
    "source_types",
    "source_availability",
    "capsule_source_resolution",
    "statement_or_title",
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stable_key(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def fold(value: str) -> str:
    normalized = unicodedata.normalize("NFD", value)
    return "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn").lower()


def discipline_from_claim(claim: dict[str, Any]) -> str:
    return claim["capsule_id"].split(":")[1].upper()


def claim_row(
    claim: dict[str, Any],
    catalog_by_id: dict[str, dict[str, Any]],
    versions: dict[str, dict[str, Any]],
    sources: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    capsule = catalog_by_id[claim["capsule_id"]]
    version_rows = [
        versions[item["source_version_id"]]
        for item in claim.get("evidence", [])
        if item.get("source_version_id") in versions
    ]
    source_rows = [
        sources[item["source_id"]]
        for item in version_rows
        if item.get("source_id") in sources
    ]
    validity = claim.get("states", {}).get("clinical_validity", "unknown")
    return {
        "sample_id": "rt:" + stable_key("claim|" + claim["claim_id"])[:16],
        "sample_kind": f"{validity}_claim",
        "claim_id": claim["claim_id"],
        "capsule_id": claim["capsule_id"],
        "capsule_path": capsule["path"],
        "discipline": discipline_from_claim(claim),
        "risk": capsule.get("risk", "unknown"),
        "clinical_validity": validity,
        "criticality": claim.get("criticality", "unknown"),
        "claim_type": claim.get("claim_type", "unknown"),
        "source_layers": " ".join(sorted({item.get("layer", "unknown") for item in source_rows})),
        "source_types": " ".join(sorted({item.get("source_type", "unknown") for item in source_rows})),
        "source_availability": " ".join(sorted({item.get("availability", "unknown") for item in version_rows})),
        "capsule_source_resolution": capsule.get("source_resolution", "unknown"),
        "statement_or_title": claim.get("statement", ""),
    }


def capsule_row(capsule: dict[str, Any], kind: str) -> dict[str, Any]:
    return {
        "sample_id": "rt:" + stable_key(kind + "|" + capsule["capsule_id"])[:16],
        "sample_kind": kind,
        "claim_id": "",
        "capsule_id": capsule["capsule_id"],
        "capsule_path": capsule["path"],
        "discipline": capsule["discipline"],
        "risk": capsule.get("risk", "unknown"),
        "clinical_validity": "historical_panel" if kind == "historical_panel" else "unregistered_pending",
        "criticality": "sampled_by_capsule_risk",
        "claim_type": "capsule_surface",
        "source_layers": "curricular_mixed",
        "source_types": "capsule",
        "source_availability": capsule.get("source_resolution", "unknown"),
        "capsule_source_resolution": capsule.get("source_resolution", "unknown"),
        "statement_or_title": capsule.get("title", ""),
    }


def choose_current(claims: list[dict[str, Any]], per_discipline: int = 4) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    for discipline in ("EISA_II", "EISCA", "EISM"):
        candidates = [
            item
            for item in claims
            if item.get("states", {}).get("clinical_validity") == "current"
            and discipline_from_claim(item) == discipline
        ]
        candidates.sort(key=lambda item: stable_key(item["claim_id"]))
        unique_capsules: list[dict[str, Any]] = []
        seen_capsules: set[str] = set()
        for item in candidates:
            if item["capsule_id"] in seen_capsules:
                continue
            unique_capsules.append(item)
            seen_capsules.add(item["capsule_id"])
        picked = unique_capsules[:per_discipline]
        if len(picked) < per_discipline:
            picked_ids = {item["claim_id"] for item in picked}
            picked.extend(
                item
                for item in candidates
                if item["claim_id"] not in picked_ids
            )
        selected.extend(picked[:per_discipline])
    return selected


def choose_historical(catalog: list[dict[str, Any]]) -> list[dict[str, Any]]:
    candidates = []
    for capsule in catalog:
        if capsule.get("risk") != "high":
            continue
        path = SKILL_ROOT / capsule["path"]
        text = fold(path.read_text(encoding="utf-8"))
        if "material historico" in text or "para a prova" in text and "pratica clinica atual" in text:
            candidates.append(capsule)
    selected = []
    for discipline in sorted({item["discipline"] for item in candidates}):
        group = [item for item in candidates if item["discipline"] == discipline]
        group.sort(key=lambda item: stable_key(item["capsule_id"]))
        selected.append(group[0])
    return selected


def choose_metadata_only(catalog: list[dict[str, Any]], per_discipline: int = 2) -> list[dict[str, Any]]:
    selected = []
    disciplines = sorted(
        {
            item["discipline"]
            for item in catalog
            if item.get("source_resolution") == "metadata_only" and item.get("risk") == "high"
        }
    )
    for discipline in disciplines:
        group = [
            item
            for item in catalog
            if item["discipline"] == discipline
            and item.get("source_resolution") == "metadata_only"
            and item.get("risk") == "high"
        ]
        group.sort(key=lambda item: stable_key(item["capsule_id"]))
        selected.extend(group[:per_discipline])
    return selected


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    claims_path = SKILL_ROOT / "registry" / "clinical_claims.jsonl"
    versions_path = SKILL_ROOT / "registry" / "source_versions.jsonl"
    sources_path = SKILL_ROOT / "registry" / "sources.jsonl"
    catalog_path = SKILL_ROOT / "artifacts" / "CAPSULE_CATALOG.json"

    claims = load_jsonl(claims_path)
    versions = {item["source_version_id"]: item for item in load_jsonl(versions_path)}
    sources = {item["source_id"]: item for item in load_jsonl(sources_path)}
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))["capsules"]
    catalog_by_id = {item["capsule_id"]: item for item in catalog}

    non_current = [
        item
        for item in claims
        if item.get("states", {}).get("clinical_validity") != "current"
    ]
    claim_selection = choose_current(claims) + sorted(
        non_current, key=lambda item: item["claim_id"]
    )
    rows = [claim_row(item, catalog_by_id, versions, sources) for item in claim_selection]
    rows.extend(capsule_row(item, "historical_panel") for item in choose_historical(catalog))
    rows.extend(capsule_row(item, "metadata_only_capsule") for item in choose_metadata_only(catalog))
    rows.sort(key=lambda item: (item["sample_kind"], item["discipline"], item["sample_id"]))

    REPORTS.mkdir(parents=True, exist_ok=True)
    csv_path = REPORTS / "RED_TEAM_SAMPLE.csv"
    write_csv(csv_path, rows)
    summary = {
        "schema_version": "1.0.0",
        "sample_rows": len(rows),
        "unique_capsules": len({item["capsule_id"] for item in rows}),
        "rows_by_kind": dict(sorted(Counter(item["sample_kind"] for item in rows).items())),
        "rows_by_discipline": dict(sorted(Counter(item["discipline"] for item in rows).items())),
        "rows_by_risk": dict(sorted(Counter(item["risk"] for item in rows).items())),
        "rows_by_clinical_validity": dict(
            sorted(Counter(item["clinical_validity"] for item in rows).items())
        ),
        "rows_by_source_layer": dict(
            sorted(Counter(item["source_layers"] or "unknown" for item in rows).items())
        ),
        "dependencies": {
            str(path.relative_to(REPO_ROOT)).replace("\\", "/"): sha256_file(path)
            for path in (claims_path, versions_path, sources_path, catalog_path, Path(__file__).resolve())
        },
        "sample_csv_sha256": sha256_file(csv_path),
        "selection_contract": {
            "current_claims": "4 stable-hash selections per EISA_II, EISCA and EISM",
            "non_current_claims": "all canonical non-current claims",
            "historical_panels": "one high-risk explicit historical/current split per discipline when available",
            "metadata_only": "two high-risk capsules per discipline with metadata-only source resolution",
        },
    }
    summary_path = REPORTS / "RED_TEAM_SAMPLE_SUMMARY.json"
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
