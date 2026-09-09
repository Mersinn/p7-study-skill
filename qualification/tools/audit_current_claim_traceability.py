#!/usr/bin/env python3
"""Derive the v1.5.0 current-claim traceability audit from canonical registries."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    root = args.root.resolve()
    out = (args.out or root / "qualification" / "reports" / "v1.5.0").resolve()
    out.mkdir(parents=True, exist_ok=True)

    skill = root / "p7-study-skill"
    claims = load_jsonl(skill / "registry" / "clinical_claims.jsonl")
    versions = {row["source_version_id"]: row for row in load_jsonl(skill / "registry" / "source_versions.jsonl")}
    reviewers_doc = json.loads((skill / "registry" / "reviewers.json").read_text(encoding="utf-8"))
    reviewers = {row["reviewer_id"]: row for row in reviewers_doc["reviewers"]}

    rows: list[dict] = []
    for claim in claims:
        if claim["states"]["clinical_validity"] != "current":
            continue
        failures: list[str] = []
        evidence_rows = claim.get("evidence", [])
        if not evidence_rows:
            failures.append("missing_evidence")
        for evidence in evidence_rows:
            source_version_id = evidence.get("source_version_id")
            version = versions.get(source_version_id)
            if version is None:
                failures.append(f"missing_source_version:{source_version_id}")
                continue
            if not version.get("version_label") and not version.get("published_or_effective_at"):
                failures.append(f"missing_version_or_date:{source_version_id}")
            if not version.get("accessed_at"):
                failures.append(f"source_not_opened:{source_version_id}")
            if not evidence.get("locator"):
                failures.append(f"missing_locator:{source_version_id}")
        if not claim.get("population"):
            failures.append("missing_population")
        if not claim.get("curricular_context"):
            failures.append("missing_curricular_context")
        reviewer = reviewers.get(claim.get("reviewer_id"))
        if reviewer is None:
            failures.append("missing_reviewer")
        if not claim.get("reviewed_at"):
            failures.append("missing_review_date")
        if claim.get("criticality") == "high":
            if claim["states"].get("independent_review") != "reviewed_l2":
                failures.append("missing_independent_review_l2")
            elif not reviewer or reviewer.get("role") != "independent_reviewer_l2":
                failures.append("reviewer_role_not_l2")
        rows.append({
            "claim_id": claim["claim_id"],
            "criticality": claim["criticality"],
            "claim_type": claim["claim_type"],
            "source_version_ids": [item.get("source_version_id") for item in evidence_rows],
            "locators": [item.get("locator") for item in evidence_rows],
            "reviewer_id": claim.get("reviewer_id"),
            "reviewed_at": claim.get("reviewed_at"),
            "traceability_status": "pass" if not failures else "fail",
            "failures": failures,
        })

    states = Counter(claim["states"]["clinical_validity"] for claim in claims)
    current_by_risk = Counter(row["criticality"] for row in rows)
    passing = sum(row["traceability_status"] == "pass" for row in rows)
    summary = {
        "schema_version": "1.5.0-traceability.1",
        "claims_total": len(claims),
        "claims_by_clinical_validity": dict(sorted(states.items())),
        "current_claims": len(rows),
        "current_claims_by_criticality": dict(sorted(current_by_risk.items())),
        "current_traceable": passing,
        "current_untraceable": len(rows) - passing,
        "gate_result": "PASS" if rows and passing == len(rows) else "FAIL",
        "limitations": [
            "This deterministic audit verifies traceability fields and reviewer independence, not medical truth by itself.",
            "Clinical support is challenged separately by the blind red team against the exact proposition and locator.",
            "metadata_only means the external source is not redistributed; accessed_at records that it was opened.",
        ],
    }
    (out / "CURRENT_CLAIM_TRACEABILITY.json").write_text(
        json.dumps({"summary": summary, "records": rows}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    report = [
        "# Current claim traceability — v1.5.0",
        "",
        f"- Current traceable: **{passing}/{len(rows)}**",
        f"- Current untraceable: **{len(rows) - passing}/{len(rows)}**",
        f"- Gate result: **{summary['gate_result']}**",
        f"- Clinical validity states: `{json.dumps(summary['claims_by_clinical_validity'], ensure_ascii=False, sort_keys=True)}`",
        "",
        "This is a structural traceability audit. Exact clinical support is closed only after the independent red team.",
        "",
        "## Open failures",
        "",
    ]
    failed = [row for row in rows if row["failures"]]
    report.extend(
        [f"- `{row['claim_id']}`: {', '.join(row['failures'])}" for row in failed]
        or ["- None."]
    )
    (out / "CURRENT_CLAIM_TRACEABILITY_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0 if summary["gate_result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
