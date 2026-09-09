"""Build a claim-level coverage view without changing the frozen detector.

The lexical detector answers an occurrence-level question. This view answers a
different question: which canonical registry claims exist, what clinical state
they carry, whether their evidence has a source-version/locator, and whether
the detector happened to link any occurrence to them. A missing lexical link is
not treated as a missing registry claim.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any


FIELDNAMES = [
    "claim_id",
    "capsule_id",
    "claim_type",
    "clinical_validity",
    "criticality",
    "source_version_ids",
    "source_version_fk_status",
    "locator_count",
    "evidence_locator_status",
    "detector_linked_occurrences",
    "detector_linkage_status",
    "coverage_interpretation",
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def load_detections(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def unique(values: list[str]) -> list[str]:
    return sorted({value for value in values if value})


def build_rows(
    claims: list[dict[str, Any]],
    source_versions: set[str],
    detections: list[dict[str, str]],
) -> list[dict[str, Any]]:
    linked_occurrences: Counter[str] = Counter()
    denominator_by_capsule: Counter[str] = Counter()
    for detection in detections:
        if detection.get("in_sweep_denominator") != "True":
            continue
        denominator_by_capsule[detection["capsule_id"]] += 1
        if detection.get("resolved") != "True":
            continue
        for claim_id in detection.get("linked_claim_ids", "").split():
            linked_occurrences[claim_id] += 1

    rows: list[dict[str, Any]] = []
    for claim in sorted(claims, key=lambda item: item["claim_id"]):
        evidence = claim.get("evidence", [])
        source_ids = unique([item.get("source_version_id", "") for item in evidence])
        locators = [item.get("locator", "") for item in evidence if item.get("locator")]
        fk_complete = bool(source_ids) and all(
            source_version_id in source_versions for source_version_id in source_ids
        )
        locator_complete = bool(evidence) and len(locators) == len(evidence)
        claim_id = claim["claim_id"]
        capsule_id = claim["capsule_id"]
        linked = linked_occurrences[claim_id]
        if linked:
            linkage_status = "linked"
            interpretation = "registry claim and lexical occurrence linkage are both present"
        elif claim.get("claim_type") == "time_window" and denominator_by_capsule[capsule_id]:
            linkage_status = "not_linked_known_temporal_token_limit"
            interpretation = (
                "claim is registered; detector linkage is absent because bare temporal "
                "values are intentionally excluded by the frozen conservative matcher"
            )
        else:
            linkage_status = "not_linked_conservative"
            interpretation = (
                "claim is registered; no material detector linkage was inferred, "
                "which is not evidence that the claim is absent"
            )

        rows.append(
            {
                "claim_id": claim_id,
                "capsule_id": capsule_id,
                "claim_type": claim.get("claim_type", ""),
                "clinical_validity": claim.get("states", {}).get(
                    "clinical_validity", "unknown"
                ),
                "criticality": claim.get("criticality", "unknown"),
                "source_version_ids": " ".join(source_ids),
                "source_version_fk_status": "complete" if fk_complete else "incomplete",
                "locator_count": len(locators),
                "evidence_locator_status": "complete" if locator_complete else "incomplete",
                "detector_linked_occurrences": linked,
                "detector_linkage_status": linkage_status,
                "coverage_interpretation": interpretation,
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "view": "canonical_claim_coverage",
        "claims_total": len(rows),
        "claims_by_clinical_validity": dict(
            sorted(Counter(row["clinical_validity"] for row in rows).items())
        ),
        "claims_by_evidence_locator_status": dict(
            sorted(Counter(row["evidence_locator_status"] for row in rows).items())
        ),
        "claims_by_detector_linkage_status": dict(
            sorted(Counter(row["detector_linkage_status"] for row in rows).items())
        ),
        "time_window_claims": {
            "total": sum(row["claim_type"] == "time_window" for row in rows),
            "linked": sum(
                row["claim_type"] == "time_window"
                and row["detector_linked_occurrences"] > 0
                for row in rows
            ),
            "known_temporal_token_limit": sum(
                row["detector_linkage_status"] == "not_linked_known_temporal_token_limit"
                for row in rows
            ),
        },
        "interpretation": (
            "This view counts each canonical registry claim once. Clinical validity "
            "and evidence locator status are independent from occurrence-level lexical "
            "linkage. It does not close any release gate."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("p7-study-skill"))
    parser.add_argument("--reports", type=Path, default=Path("qualification/reports"))
    args = parser.parse_args()

    root = args.root.resolve()
    reports = args.reports.resolve()
    claims = load_jsonl(root / "registry" / "clinical_claims.jsonl")
    source_versions = {
        item["source_version_id"]
        for item in load_jsonl(root / "registry" / "source_versions.jsonl")
    }
    detections = load_detections(reports / "CRITICAL_CLAIM_DETECTIONS.csv")
    rows = build_rows(claims, source_versions, detections)
    write_csv(reports / "CANONICAL_CLAIM_COVERAGE.csv", rows)
    summary = build_summary(rows)
    (reports / "CANONICAL_CLAIM_COVERAGE_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
