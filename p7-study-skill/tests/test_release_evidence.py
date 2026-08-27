from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_package import validate_release  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ReleaseEvidenceTests(unittest.TestCase):
    def build_package(self, *, version: str = "1.5.0", status: str = "passed", decision: str = "READY_FOR_USER_REVIEW") -> tuple[Path, dict]:
        directory = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, directory, ignore_errors=True)
        package = directory / "package"
        (package / "registry").mkdir(parents=True)
        (package / "artifacts").mkdir()
        (package / "VERSION").write_text(version + "\n", encoding="utf-8")
        proof = package / "proof.txt"
        proof.write_text("immutable evidence\n", encoding="utf-8")
        manifest = package / "artifacts" / "PACKAGE_MANIFEST.json"
        manifest.write_text('{"snapshot":"standalone"}\n', encoding="utf-8")
        gates = {"schema_version": "1.0.0", "release": version, "decision": decision, "gates": [{"gate_id": "evidence_integrity", "status": status, "evidence": ["proof.txt"]}]}
        (package / "registry" / "release_gates.json").write_text(json.dumps(gates), encoding="utf-8")
        evidence = {
            "schema_version": "1.0.0",
            "release": version,
            "reported_decision": decision,
            "evidence": [
                {
                    "gate_id": "evidence_integrity",
                    "artifact": {"path": "proof.txt", "sha256": sha256(proof)},
                    "snapshot": {"mode": "standalone", "package_manifest_path": "artifacts/PACKAGE_MANIFEST.json", "package_manifest_sha256": sha256(manifest)},
                    "scope": {"included_paths": ["proof.txt"], "excluded_paths": []},
                    "adjudication": {"adjudicator": "reviewer:qa", "adjudicated_at": "2026-08-27T12:00:00-03:00", "outcome": "passed"},
                    "quantitative": True,
                    "metrics": {"numerator": 1, "denominator": 1, "components": {"pass": 1, "fail": 0}},
                    "limitations": ["Only the frozen proof artifact was adjudicated."],
                }
            ],
        }
        return package, evidence

    def validate(self, package: Path, evidence: dict, mode: str = "standalone") -> set[str]:
        (package / "registry" / "release_evidence.json").write_text(json.dumps(evidence), encoding="utf-8")
        return {item.code for item in validate_release(package, mode) if item.severity == "ERROR"}

    def test_standalone_passed_gate_accepts_complete_attestation(self):
        package, evidence = self.build_package()
        self.assertEqual(self.validate(package, evidence), set())

    def test_repository_mode_accepts_matching_commit(self):
        package, evidence = self.build_package()
        commit = "a" * 40
        evidence["evidence"][0]["snapshot"] = {"mode": "repository", "git_commit": commit}
        with patch("release_evidence.repository_snapshot", return_value=(package, commit)):
            self.assertEqual(self.validate(package, evidence, "repository"), set())

    def test_missing_artifact_path_is_rejected(self):
        package, evidence = self.build_package()
        (package / "proof.txt").unlink()
        self.assertIn("EVIDENCE_ARTIFACT_MISSING", self.validate(package, evidence))

    def test_modified_artifact_hash_is_rejected(self):
        package, evidence = self.build_package()
        (package / "proof.txt").write_text("tampered\n", encoding="utf-8")
        self.assertIn("EVIDENCE_SHA256_MISMATCH", self.validate(package, evidence))

    def test_repository_commit_mismatch_is_rejected(self):
        package, evidence = self.build_package()
        evidence["evidence"][0]["snapshot"] = {"mode": "repository", "git_commit": "a" * 40}
        with patch("release_evidence.repository_snapshot", return_value=(package, "b" * 40)):
            self.assertIn("EVIDENCE_GIT_COMMIT_MISMATCH", self.validate(package, evidence, "repository"))

    def test_quantitative_component_sum_must_match_denominator(self):
        package, evidence = self.build_package()
        evidence["evidence"][0]["metrics"] = {"numerator": 1, "denominator": 3, "components": {"pass": 1, "fail": 1}}
        self.assertIn("EVIDENCE_METRIC_SUM_INVALID", self.validate(package, evidence))

    def test_registry_version_divergence_is_rejected(self):
        package, evidence = self.build_package()
        gates_path = package / "registry" / "release_gates.json"
        gates = json.loads(gates_path.read_text(encoding="utf-8"))
        gates["release"] = "1.5.1"
        gates_path.write_text(json.dumps(gates), encoding="utf-8")
        self.assertIn("RELEASE_VERSION_DIVERGENCE", self.validate(package, evidence))

    def test_rc_cannot_be_reported_as_final(self):
        package, evidence = self.build_package(version="1.5.0-rc.1")
        self.assertIn("RELEASE_CANDIDATE_CANNOT_CLOSE_GATES", self.validate(package, evidence))

    def test_final_version_with_open_gate_is_rejected(self):
        package, evidence = self.build_package(status="pending", decision="HOLD")
        self.assertIn("FINAL_VERSION_WITH_OPEN_GATES", self.validate(package, evidence))

    def test_report_decision_contradicting_registry_is_rejected(self):
        package, evidence = self.build_package()
        evidence["reported_decision"] = "HOLD"
        self.assertIn("RELEASE_REPORT_DECISION_CONTRADICTORY", self.validate(package, evidence))

    def test_schema_exposes_complete_passed_gate_attestation_contract(self):
        schema = json.loads((ROOT / "schemas" / "v1" / "release-gates.schema.json").read_text(encoding="utf-8"))
        attestation = schema["$defs"]["evidence_attestation"]
        self.assertTrue({"artifact", "snapshot", "scope", "adjudication", "quantitative", "limitations"} <= set(attestation["required"]))
        self.assertIn("metrics", attestation["properties"])


if __name__ == "__main__":
    unittest.main()
