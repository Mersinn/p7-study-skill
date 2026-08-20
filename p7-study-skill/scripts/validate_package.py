#!/usr/bin/env python3
"""Validate P7 structure, joins, normalized enums, artifacts and release gates."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from p7lib import (
    PACKAGE_ROOT,
    build_capsule_catalog,
    build_manifest,
    build_metrics,
    index_capsule_paths,
    load_json,
    load_source_rows,
    precision_rows,
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    message: str
    release_blocker: bool = False


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[Finding]]:
    records = []
    findings = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            records.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            findings.append(Finding("ERROR", "INVALID_JSONL", f"{path.name}:{number}: {exc}", True))
    return records, findings


def validate_schemas(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    ids: set[str] = set()
    expected = {
        "capsule.schema.json",
        "clinical-claim.schema.json",
        "source.schema.json",
        "source-version.schema.json",
        "assessment-evidence.schema.json",
        "learner-event.schema.json",
        "learner-hypothesis.schema.json",
        "review-task.schema.json",
        "priority-assessment.schema.json",
        "reviewer.schema.json",
        "release-gates.schema.json",
    }
    schema_dir = root / "schemas" / "v1"
    present = {path.name for path in schema_dir.glob("*.schema.json")}
    for missing in sorted(expected - present):
        findings.append(Finding("ERROR", "MISSING_SCHEMA", missing, True))
    for path in sorted(schema_dir.glob("*.schema.json")):
        try:
            schema = load_json(path)
        except (OSError, json.JSONDecodeError) as exc:
            findings.append(Finding("ERROR", "INVALID_SCHEMA_JSON", f"{path.name}: {exc}", True))
            continue
        schema_id = schema.get("$id")
        if not schema_id:
            findings.append(Finding("ERROR", "SCHEMA_ID_MISSING", path.name, True))
        elif schema_id in ids:
            findings.append(Finding("ERROR", "DUPLICATE_SCHEMA_ID", schema_id, True))
        ids.add(schema_id)
    return findings


def validate_catalog(root: Path) -> tuple[list[dict[str, Any]], list[Finding]]:
    catalog = build_capsule_catalog(root)
    findings: list[Finding] = []
    ids: set[str] = set()
    for item in catalog:
        if item["capsule_id"] in ids:
            findings.append(Finding("ERROR", "DUPLICATE_CAPSULE_ID", item["capsule_id"], True))
        ids.add(item["capsule_id"])
        for field in ("discipline", "unit", "risk"):
            if item[field] is None:
                findings.append(Finding("ERROR", "UNNORMALIZED_ENUM", f"{item['path']}: {field}={item['legacy_metadata'].get(field)!r}", True))
        if item["legacy_priority_normalized"] is None:
            findings.append(Finding("ERROR", "UNNORMALIZED_ENUM", f"{item['path']}: priority={item['legacy_metadata'].get('priority')!r}", True))
        if not item["source_ids"]:
            findings.append(Finding("WARN", "CAPSULE_METADATA_ONLY", f"{item['path']} has no resolvable source_id", False))
    discovered = {item["path"] for item in catalog}
    indexed = index_capsule_paths(root)
    for path in sorted(discovered - indexed):
        findings.append(Finding("ERROR", "CAPSULE_NOT_INDEXED", path, True))
    for path in sorted(indexed - discovered):
        findings.append(Finding("ERROR", "INDEX_PATH_MISSING", path, True))
    if len(catalog) < 156:
        findings.append(Finding("ERROR", "CAPSULE_COUNT_REGRESSION", f"baseline is 156 physical capsules, found {len(catalog)}", True))
    return catalog, findings


def validate_aliases(root: Path, catalog: list[dict[str, Any]]) -> list[Finding]:
    findings: list[Finding] = []
    known = {item["capsule_id"] for item in catalog}
    aliases = load_json(root / "registry" / "aliases.json")
    alias_ids: set[str] = set()
    for item in aliases.get("topic_aliases", []):
        alias_id = item.get("alias_id")
        if alias_id in alias_ids:
            findings.append(Finding("ERROR", "DUPLICATE_ALIAS_ID", str(alias_id), True))
        alias_ids.add(alias_id)
        if item.get("coverage") not in {"partial", "complete"}:
            findings.append(Finding("ERROR", "INVALID_ALIAS_COVERAGE", str(alias_id), True))
        for target in item.get("target_capsule_ids", []):
            if target not in known:
                findings.append(Finding("ERROR", "ALIAS_TARGET_MISSING", f"{alias_id} -> {target}", True))
    return findings


def validate_sources(root: Path) -> list[Finding]:
    rows = load_source_rows(root)
    ids = [row.get("source_id", "") for row in rows]
    findings = []
    if any(not source_id for source_id in ids):
        findings.append(Finding("ERROR", "EMPTY_SOURCE_ID", "source manifest contains an empty source_id", True))
    duplicates = sorted({source_id for source_id in ids if ids.count(source_id) > 1})
    for source_id in duplicates:
        findings.append(Finding("ERROR", "DUPLICATE_SOURCE_ID", source_id, True))
    return findings


def validate_canonical_registries(root: Path) -> tuple[set[str], set[str], set[str], list[Finding]]:
    findings: list[Finding] = []
    source_records, source_findings = read_jsonl(root / "registry" / "sources.jsonl")
    version_records, version_findings = read_jsonl(root / "registry" / "source_versions.jsonl")
    findings.extend(source_findings)
    findings.extend(version_findings)
    source_ids: set[str] = set()
    for record in source_records:
        source_id = record.get("source_id")
        if source_id in source_ids:
            findings.append(Finding("ERROR", "DUPLICATE_CANONICAL_SOURCE_ID", str(source_id), True))
        source_ids.add(source_id)
    version_ids: set[str] = set()
    for record in version_records:
        version_id = record.get("source_version_id")
        if version_id in version_ids:
            findings.append(Finding("ERROR", "DUPLICATE_SOURCE_VERSION_ID", str(version_id), True))
        version_ids.add(version_id)
        if record.get("source_id") not in source_ids:
            findings.append(Finding("ERROR", "SOURCE_VERSION_FK_MISSING", f"{version_id} -> {record.get('source_id')}", True))
        availability = record.get("availability")
        if availability == "local_only" and not record.get("local_reference"):
            findings.append(Finding("ERROR", "LOCAL_SOURCE_REFERENCE_MISSING", str(version_id), True))
        if availability == "metadata_only" and not record.get("url"):
            findings.append(Finding("ERROR", "REMOTE_SOURCE_URL_MISSING", str(version_id), True))
    reviewer_doc = load_json(root / "registry" / "reviewers.json")
    reviewer_ids: set[str] = set()
    for reviewer in reviewer_doc.get("reviewers", []):
        reviewer_id = reviewer.get("reviewer_id")
        if reviewer_id in reviewer_ids:
            findings.append(Finding("ERROR", "DUPLICATE_REVIEWER_ID", str(reviewer_id), True))
        reviewer_ids.add(reviewer_id)
        if not reviewer.get("model") or reviewer.get("exact_serving_version") is None:
            findings.append(Finding("ERROR", "REVIEWER_PROVENANCE_INCOMPLETE", str(reviewer_id), True))
    unexpected = sorted(path.name for path in (root / "registry").glob("*clinical*.jsonl") if path.name != "clinical_claims.jsonl")
    for name in unexpected:
        findings.append(Finding("ERROR", "SECOND_MANUAL_REGISTRY", name, True))
    manual_csv = root / "references" / "CLINICAL_CLAIM_REGISTRY.csv"
    if manual_csv.exists():
        findings.append(Finding("ERROR", "SECOND_MANUAL_REGISTRY", str(manual_csv.relative_to(root)), True))
    return source_ids, version_ids, reviewer_ids, findings


def validate_claims(root: Path, version_ids: set[str], reviewer_ids: set[str], capsule_ids: set[str]) -> list[Finding]:
    path = root / "registry" / "clinical_claims.jsonl"
    if not path.exists():
        return [Finding("WARN", "CLAIM_REGISTRY_PENDING", "clinical_claims.jsonl has not been materialized", True)]
    records, findings = read_jsonl(path)
    ids: set[str] = set()
    allowed_types = {"dose", "concentration", "threshold", "time_window", "contraindication", "emergency", "treatment_sequence", "guideline_dependent", "other"}
    for line, claim in enumerate(records, start=1):
        claim_id = claim.get("claim_id")
        if claim_id in ids:
            findings.append(Finding("ERROR", "DUPLICATE_CLAIM_ID", str(claim_id), True))
        ids.add(claim_id)
        required = {"schema_version", "claim_id", "capsule_id", "statement", "claim_type", "criticality", "population", "curricular_context", "evidence", "states", "reviewer_id"}
        missing = sorted(required - claim.keys())
        if missing:
            findings.append(Finding("ERROR", "CLAIM_REQUIRED_FIELD", f"line {line}: {', '.join(missing)}", True))
            continue
        if claim.get("capsule_id") not in capsule_ids:
            findings.append(Finding("ERROR", "CLAIM_CAPSULE_FK_MISSING", f"{claim_id} -> {claim.get('capsule_id')}", True))
        states = claim.get("states", {})
        if "self_review_l1" not in states:
            findings.append(Finding("ERROR", "CLAIM_SELF_REVIEW_STATE_MISSING", str(claim_id), True))
        reviewer_id = claim.get("reviewer_id")
        if reviewer_id is not None and reviewer_id not in reviewer_ids:
            findings.append(Finding("ERROR", "CLAIM_REVIEWER_FK_MISSING", f"{claim_id} -> {reviewer_id}", True))
        for evidence in claim.get("evidence", []):
            version_id = evidence.get("source_version_id")
            if version_id not in version_ids:
                findings.append(Finding("ERROR", "CLAIM_SOURCE_VERSION_FK_MISSING", f"{claim_id} -> {version_id}", True))
            if not evidence.get("locator"):
                findings.append(Finding("ERROR", "CLAIM_LOCATOR_MISSING", str(claim_id), True))
        if claim["claim_type"] not in allowed_types:
            findings.append(Finding("ERROR", "CLAIM_TYPE_INVALID", f"{claim_id}: {claim['claim_type']}", True))
        if claim["criticality"] == "high":
            validity = states.get("clinical_validity")
            if validity not in {"current", "historical_only", "quarantined"}:
                findings.append(Finding("ERROR", "HIGH_RISK_CLAIM_UNRESOLVED", f"{claim_id}: {validity}", True))
            if validity in {"current", "historical_only"}:
                if not claim.get("evidence") or not claim.get("reviewed_at") or not claim.get("reviewer_id"):
                    findings.append(Finding("ERROR", "HIGH_RISK_CLAIM_UNTRACEABLE", str(claim_id), True))
                if states.get("independent_review") == "not_reviewed":
                    findings.append(Finding("ERROR", "HIGH_RISK_CLAIM_NOT_INDEPENDENTLY_REVIEWED", str(claim_id), True))
    if not records:
        findings.append(Finding("WARN", "CLAIM_REGISTRY_EMPTY", "clinical claim sweep is not complete", True))
    return findings


def validate_artifacts(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    artifact_dir = root / "artifacts"
    expected_json = {
        "PACKAGE_MANIFEST.json": build_manifest(root),
        "METRICS.json": build_metrics(root),
    }
    for name, expected in expected_json.items():
        path = artifact_dir / name
        if not path.exists():
            findings.append(Finding("ERROR", "ARTIFACT_MISSING", name, True))
        else:
            try:
                actual = load_json(path)
            except (OSError, json.JSONDecodeError) as exc:
                findings.append(Finding("ERROR", "ARTIFACT_INVALID", f"{name}: {exc}", True))
                continue
            if actual != expected:
                findings.append(Finding("ERROR", "ARTIFACT_STALE", name, True))
    for name in ("CAPSULE_CATALOG.json", "CAPSULE_INDEX.generated.md", "PRECISION_ROWS.csv", "CLINICAL_CLAIMS.csv"):
        if not (artifact_dir / name).exists():
            findings.append(Finding("ERROR", "ARTIFACT_MISSING", name, True))
    return findings


def validate_release(root: Path) -> list[Finding]:
    findings = []
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"1\.0\.0-rc\.\d+", version):
        findings.append(Finding("ERROR", "NOT_RELEASE_CANDIDATE", version, True))
    gates = load_json(root / "registry" / "release_gates.json")
    gate_ids: set[str] = set()
    open_gates = 0
    for gate in gates.get("gates", []):
        gate_id = gate.get("gate_id")
        if gate_id in gate_ids:
            findings.append(Finding("ERROR", "DUPLICATE_RELEASE_GATE", str(gate_id), True))
        gate_ids.add(gate_id)
        status = gate.get("status")
        if status == "passed" and not gate.get("evidence"):
            findings.append(Finding("ERROR", "PASSED_GATE_WITHOUT_EVIDENCE", str(gate_id), True))
        if status != "passed":
            open_gates += 1
            findings.append(Finding("WARN", "RELEASE_GATE_OPEN", f"{gate_id}: {status}", True))
    expected_decision = "GO" if open_gates == 0 else "HOLD"
    if gates.get("decision") != expected_decision:
        findings.append(Finding("ERROR", "RELEASE_DECISION_INCONSISTENT", f"expected {expected_decision}", True))
    for directory in ("corpus_text", "vision_png"):
        if not (root / directory).is_dir():
            findings.append(Finding("INFO", "OPTIONAL_SOURCE_LAYER_ABSENT", f"{directory}: metadata-only fallback required", False))
    return findings


def collect(root: Path) -> list[Finding]:
    findings = validate_schemas(root)
    catalog, catalog_findings = validate_catalog(root)
    findings.extend(catalog_findings)
    findings.extend(validate_aliases(root, catalog))
    findings.extend(validate_sources(root))
    _, version_ids, reviewer_ids, registry_findings = validate_canonical_registries(root)
    findings.extend(registry_findings)
    findings.extend(validate_claims(root, version_ids, reviewer_ids, {item["capsule_id"] for item in catalog}))
    findings.extend(validate_artifacts(root))
    findings.extend(validate_release(root))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=PACKAGE_ROOT)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--release-gate", action="store_true", help="also fail on unresolved release blockers")
    args = parser.parse_args()
    findings = collect(args.root.resolve())
    if args.json:
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2, sort_keys=True))
    else:
        for item in findings:
            marker = " [release blocker]" if item.release_blocker else ""
            print(f"{item.severity} {item.code}{marker}: {item.message}")
        counts = {level: sum(item.severity == level for item in findings) for level in ("ERROR", "WARN", "INFO")}
        print("summary: " + ", ".join(f"{key.lower()}={value}" for key, value in counts.items()))
    structural_failure = any(item.severity == "ERROR" for item in findings)
    gate_failure = args.release_gate and any(item.release_blocker for item in findings)
    return 1 if structural_failure or gate_failure else 0


if __name__ == "__main__":
    raise SystemExit(main())
