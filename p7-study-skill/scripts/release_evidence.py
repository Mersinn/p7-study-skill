"""Mechanical validation for release-gate evidence attestations (stdlib only)."""

from __future__ import annotations

import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from p7lib import sha256_file


EVIDENCE_MANIFEST = Path("registry/release_evidence.json")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
COMMIT_RE = re.compile(r"^[a-f0-9]{40}$")


@dataclass(frozen=True)
class EvidenceFinding:
    code: str
    message: str


@dataclass(frozen=True)
class EvidenceContext:
    mode: str
    artifact_root: Path
    git_commit: str | None = None
    package_root: Path | None = None


def repository_snapshot(package_root: Path) -> tuple[Path, str] | None:
    """Return repository root and HEAD, or None when this is not a Git checkout."""
    try:
        root = subprocess.run(["git", "-C", str(package_root), "rev-parse", "--show-toplevel"], check=True, capture_output=True, text=True).stdout.strip()
        commit = subprocess.run(["git", "-C", str(package_root), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip().lower()
    except (OSError, subprocess.CalledProcessError):
        return None
    if not root or not COMMIT_RE.fullmatch(commit):
        return None
    return Path(root), commit


def evidence_context(package_root: Path, requested_mode: str = "auto") -> tuple[EvidenceContext | None, list[EvidenceFinding]]:
    if requested_mode not in {"auto", "repository", "standalone"}:
        return None, [EvidenceFinding("RELEASE_EVIDENCE_MODE_INVALID", requested_mode)]
    snapshot = repository_snapshot(package_root)
    if requested_mode == "repository" or (requested_mode == "auto" and snapshot is not None):
        if snapshot is None:
            return None, [EvidenceFinding("REPOSITORY_SNAPSHOT_UNAVAILABLE", "repository mode requires a readable Git HEAD")]
        root, commit = snapshot
        return EvidenceContext("repository", root, commit, package_root), []
    return EvidenceContext("standalone", package_root, package_root=package_root), []


def _compatible_evidence_followup(context: EvidenceContext, declared_commit: str) -> bool:
    """Allow a tested parent commit only when HEAD adds release evidence metadata."""
    if context.mode != "repository" or context.git_commit is None or context.package_root is None:
        return False
    try:
        subprocess.run(
            ["git", "-C", str(context.artifact_root), "merge-base", "--is-ancestor", declared_commit, context.git_commit],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        package_relative = context.package_root.relative_to(context.artifact_root).as_posix()
        changed = subprocess.run(
            ["git", "-C", str(context.artifact_root), "diff", "--name-only", f"{declared_commit}..{context.git_commit}", "--", package_relative],
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
    except (OSError, ValueError, subprocess.CalledProcessError):
        return False
    allowed = {
        f"{package_relative}/registry/release_evidence.json",
        f"{package_relative}/artifacts/PACKAGE_MANIFEST.json",
    }
    return bool(changed) and set(changed) <= allowed


def _safe_relative_path(value: Any) -> Path | None:
    if not isinstance(value, str) or not value or "\\" in value:
        return None
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or "." in path.parts:
        return None
    return path


def _valid_datetime(value: Any) -> bool:
    if not isinstance(value, str) or not value:
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return True


def _load_active_manifest(package_root: Path) -> tuple[dict[str, Any] | None, list[EvidenceFinding]]:
    path = package_root / EVIDENCE_MANIFEST
    if not path.is_file():
        return None, []
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, [EvidenceFinding("RELEASE_EVIDENCE_MANIFEST_INVALID", str(exc))]
    if not isinstance(document, dict) or document.get("template") is True:
        return None, [EvidenceFinding("RELEASE_EVIDENCE_MANIFEST_INVALID", "active evidence manifest must be a non-template object")]
    return document, []


def _validate_metrics(record: dict[str, Any], findings: list[EvidenceFinding], label: str) -> None:
    quantitative = record.get("quantitative")
    if not isinstance(quantitative, bool):
        findings.append(EvidenceFinding("EVIDENCE_QUANTITATIVE_FLAG_INVALID", label))
        return
    metrics = record.get("metrics")
    if not quantitative:
        if metrics is not None:
            findings.append(EvidenceFinding("EVIDENCE_METRICS_UNEXPECTED", label))
        return
    if not isinstance(metrics, dict):
        findings.append(EvidenceFinding("EVIDENCE_METRICS_MISSING", label))
        return
    numerator, denominator, components = metrics.get("numerator"), metrics.get("denominator"), metrics.get("components")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (numerator, denominator)) or denominator < 1 or numerator < 0 or numerator > denominator:
        findings.append(EvidenceFinding("EVIDENCE_METRICS_RANGE_INVALID", label))
    if not isinstance(components, dict) or not components:
        findings.append(EvidenceFinding("EVIDENCE_METRIC_COMPONENTS_MISSING", label))
        return
    values = list(components.values())
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in values):
        findings.append(EvidenceFinding("EVIDENCE_METRIC_COMPONENT_INVALID", label))
    elif isinstance(denominator, int) and not isinstance(denominator, bool) and sum(values) != denominator:
        findings.append(EvidenceFinding("EVIDENCE_METRIC_SUM_INVALID", f"{label}: components={sum(values)}; denominator={denominator}"))


def _validate_record(record: Any, *, gate_id: str, expected_path: str, context: EvidenceContext) -> list[EvidenceFinding]:
    label = f"{gate_id}:{expected_path}"
    findings: list[EvidenceFinding] = []
    if not isinstance(record, dict):
        return [EvidenceFinding("EVIDENCE_RECORD_INVALID", label)]
    if record.get("gate_id") != gate_id:
        findings.append(EvidenceFinding("EVIDENCE_GATE_MISMATCH", label))
    artifact = record.get("artifact")
    if not isinstance(artifact, dict):
        return findings + [EvidenceFinding("EVIDENCE_ARTIFACT_MISSING", label)]
    path_value = artifact.get("path")
    relative = _safe_relative_path(path_value)
    if relative is None:
        findings.append(EvidenceFinding("EVIDENCE_ARTIFACT_PATH_INVALID", label))
    else:
        if path_value != expected_path:
            findings.append(EvidenceFinding("EVIDENCE_ARTIFACT_DECLARATION_MISMATCH", label))
        path = context.artifact_root / relative
        if not path.is_file():
            findings.append(EvidenceFinding("EVIDENCE_ARTIFACT_MISSING", f"{label}: {path_value}"))
        else:
            expected_hash = artifact.get("sha256")
            if not isinstance(expected_hash, str) or not SHA256_RE.fullmatch(expected_hash):
                findings.append(EvidenceFinding("EVIDENCE_SHA256_INVALID", label))
            elif sha256_file(path) != expected_hash:
                findings.append(EvidenceFinding("EVIDENCE_SHA256_MISMATCH", label))
    snapshot = record.get("snapshot")
    if not isinstance(snapshot, dict) or snapshot.get("mode") != context.mode:
        findings.append(EvidenceFinding("EVIDENCE_SNAPSHOT_MODE_MISMATCH", label))
    elif context.mode == "repository":
        commit = snapshot.get("git_commit")
        if not isinstance(commit, str) or not COMMIT_RE.fullmatch(commit):
            findings.append(EvidenceFinding("EVIDENCE_GIT_COMMIT_INVALID", label))
        elif commit != context.git_commit and not _compatible_evidence_followup(context, commit):
            findings.append(EvidenceFinding("EVIDENCE_GIT_COMMIT_MISMATCH", label))
    else:
        manifest_path = _safe_relative_path(snapshot.get("package_manifest_path"))
        manifest_hash = snapshot.get("package_manifest_sha256")
        if manifest_path is None:
            findings.append(EvidenceFinding("EVIDENCE_PACKAGE_SNAPSHOT_PATH_INVALID", label))
        elif not isinstance(manifest_hash, str) or not SHA256_RE.fullmatch(manifest_hash):
            findings.append(EvidenceFinding("EVIDENCE_PACKAGE_SNAPSHOT_HASH_INVALID", label))
        else:
            manifest = context.artifact_root / manifest_path
            if not manifest.is_file():
                findings.append(EvidenceFinding("EVIDENCE_PACKAGE_SNAPSHOT_MISSING", f"{label}: {manifest_path.as_posix()}"))
            elif sha256_file(manifest) != manifest_hash:
                findings.append(EvidenceFinding("EVIDENCE_PACKAGE_SNAPSHOT_HASH_MISMATCH", label))
    scope = record.get("scope")
    included = scope.get("included_paths") if isinstance(scope, dict) else None
    excluded = scope.get("excluded_paths") if isinstance(scope, dict) else None
    if not isinstance(included, list) or not included:
        findings.append(EvidenceFinding("EVIDENCE_SCOPE_MISSING", label))
    elif any(_safe_relative_path(item) is None for item in included) or path_value not in included:
        findings.append(EvidenceFinding("EVIDENCE_SCOPE_INCOHERENT", label))
    if not isinstance(excluded, list) or any(_safe_relative_path(item) is None for item in excluded):
        findings.append(EvidenceFinding("EVIDENCE_SCOPE_INVALID", label))
    adjudication = record.get("adjudication")
    if not isinstance(adjudication, dict):
        findings.append(EvidenceFinding("EVIDENCE_ADJUDICATION_MISSING", label))
    else:
        if not isinstance(adjudication.get("adjudicator"), str) or not adjudication["adjudicator"].strip():
            findings.append(EvidenceFinding("EVIDENCE_ADJUDICATOR_MISSING", label))
        if not _valid_datetime(adjudication.get("adjudicated_at")):
            findings.append(EvidenceFinding("EVIDENCE_ADJUDICATION_DATE_INVALID", label))
        if adjudication.get("outcome") != "passed":
            findings.append(EvidenceFinding("EVIDENCE_ADJUDICATION_OUTCOME_INVALID", label))
    _validate_metrics(record, findings, label)
    limitations = record.get("limitations")
    if not isinstance(limitations, list) or not limitations or any(not isinstance(item, str) or not item.strip() for item in limitations):
        findings.append(EvidenceFinding("EVIDENCE_LIMITATIONS_MISSING", label))
    return findings


def validate_gate_evidence(package_root: Path, gates: dict[str, Any], version: str, requested_mode: str = "auto") -> list[EvidenceFinding]:
    """Validate active attestations for passed gates without changing gate state."""
    context, findings = evidence_context(package_root, requested_mode)
    if context is None:
        return findings
    document, document_findings = _load_active_manifest(package_root)
    findings.extend(document_findings)
    passed = [gate for gate in gates.get("gates", []) if isinstance(gate, dict) and gate.get("status") == "passed"]
    if document is None:
        for gate in passed:
            findings.append(EvidenceFinding("PASSED_GATE_EVIDENCE_MANIFEST_MISSING", str(gate.get("gate_id"))))
        return findings
    if document.get("schema_version") != "1.0.0":
        findings.append(EvidenceFinding("RELEASE_EVIDENCE_SCHEMA_VERSION_INVALID", str(document.get("schema_version"))))
    if document.get("release") != version:
        findings.append(EvidenceFinding("RELEASE_EVIDENCE_VERSION_DIVERGENCE", f"VERSION={version}; evidence={document.get('release')}"))
    if document.get("reported_decision") != gates.get("decision"):
        findings.append(EvidenceFinding("RELEASE_REPORT_DECISION_CONTRADICTORY", f"registry={gates.get('decision')}; report={document.get('reported_decision')}"))
    records = document.get("evidence")
    if not isinstance(records, list):
        findings.append(EvidenceFinding("RELEASE_EVIDENCE_RECORDS_INVALID", "evidence must be an array"))
        return findings
    indexed: dict[tuple[str, str], list[Any]] = {}
    for record in records:
        if not isinstance(record, dict):
            findings.append(EvidenceFinding("EVIDENCE_RECORD_INVALID", "evidence[]"))
            continue
        artifact = record.get("artifact")
        key = (record.get("gate_id"), artifact.get("path")) if isinstance(artifact, dict) else (None, None)
        if isinstance(key[0], str) and isinstance(key[1], str):
            indexed.setdefault(key, []).append(record)
        else:
            findings.append(EvidenceFinding("EVIDENCE_RECORD_UNINDEXABLE", "gate_id and artifact.path are required"))
    declared: set[tuple[str, str]] = set()
    for gate in passed:
        gate_id, evidence_paths = gate.get("gate_id"), gate.get("evidence")
        if not isinstance(gate_id, str) or not isinstance(evidence_paths, list) or not evidence_paths:
            findings.append(EvidenceFinding("PASSED_GATE_WITHOUT_EVIDENCE", str(gate_id)))
            continue
        for expected_path in evidence_paths:
            key = (gate_id, expected_path)
            declared.add(key)
            matches = indexed.get(key, [])
            if not matches:
                findings.append(EvidenceFinding("PASSED_GATE_EVIDENCE_ATTESTATION_MISSING", f"{gate_id}:{expected_path}"))
            elif len(matches) > 1:
                findings.append(EvidenceFinding("EVIDENCE_ATTESTATION_DUPLICATE", f"{gate_id}:{expected_path}"))
            else:
                findings.extend(_validate_record(matches[0], gate_id=gate_id, expected_path=expected_path, context=context))
    for key in sorted(indexed):
        if key not in declared:
            findings.append(EvidenceFinding("EVIDENCE_ATTESTATION_ORPHAN", f"{key[0]}:{key[1]}"))
    return findings
