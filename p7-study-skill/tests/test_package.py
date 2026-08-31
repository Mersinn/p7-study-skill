from __future__ import annotations

import sys
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from p7lib import build_capsule_catalog, build_manifest, build_metrics, build_operation_counts, index_capsule_paths  # noqa: E402


class PackageTests(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_manifest_is_stable_and_excludes_artifacts(self):
        first = build_manifest(ROOT)
        second = build_manifest(ROOT)
        self.assertEqual(first, second)
        self.assertTrue(all(not item["path"].startswith("artifacts/") for item in first["files"]))
        self.assertTrue(all(item["path"] != "registry/release_evidence.json" for item in first["files"]))

    def test_capsule_index_reconciles_by_path(self):
        discovered = {item["path"] for item in build_capsule_catalog(ROOT)}
        self.assertGreaterEqual(len(discovered), 156)
        self.assertEqual(discovered, index_capsule_paths(ROOT))

    def test_legacy_enums_have_one_canonical_join_value(self):
        catalog = build_capsule_catalog(ROOT)
        self.assertTrue(all(item["unit"] in {"UNIT_1", "UNIT_2", "UNIT_3", "UNIT_4", "UNASSIGNED"} for item in catalog))
        self.assertTrue(all(item["legacy_priority_normalized"] in {"high", "medium", "low"} for item in catalog))
        self.assertTrue(all(item["priority"] == "unscored" for item in catalog))

    def test_operation_taxonomy_uses_canonical_ids(self):
        result = build_operation_counts(ROOT)
        self.assertEqual(result["taxonomy_rows"], 152)
        by_id = {item["operation_id"]: item for item in result["operations"]}
        merged = by_id["differentiate_close_alternatives"]
        self.assertEqual(merged["count"], 17)
        self.assertEqual(merged["observed_labels"], ["diferenciar proximos", "diferenciar próximos"])

    def test_missing_runtime_sources_degrade_honestly(self):
        metrics = build_metrics(ROOT)
        for name in ("corpus_text", "vision_png"):
            if metrics["runtime_source_availability"][name]["availability"] == "absent":
                self.assertEqual(metrics["runtime_source_availability"][name]["behavior"], "metadata_only_do_not_claim_inspection")

    def test_quarantine_recovery_requires_exact_persisted_transition(self):
        safety = self.read("references/MEDICAL_SAFETY_LAYER.md")
        for required in (
            "o enunciado exato",
            "população, cenário, jurisdição, versão/data",
            "persistir a transição no registry canônico",
            "não reescreve nem “desquarentena” o registry",
        ):
            self.assertIn(required, safety)

    def test_synthetic_weighted_osce_is_not_authentic_or_official(self):
        skill = self.read("SKILL.md")
        osce = self.read("references/CASE_OSCE_TUTOR.md")
        self.assertIn("references/CASE_OSCE_TUTOR.md", skill)
        self.assertIn("provided_weighted_training_rubric", skill)
        for required in (
            "provided_weighted_training_rubric",
            "escore de",
            "treino`, nunca nota oficial",
            "emissor verificável",
        ):
            self.assertIn(required, osce)
        self.assertIn("Nunca classifique checklist ponderado fornecido e sintético", osce)
        self.assertIn("pontuação binária por item", osce)
        self.assertIn("peso original`, `evidência", osce)
        self.assertIn("escore de treino", osce)

    def test_medical_safety_does_not_override_question_first_in_stable_study(self):
        safety = self.read("references/MEDICAL_SAFETY_LAYER.md")
        self.assertIn("Precedência no estudo ativo", safety)
        self.assertIn("não abre o portão de revelação antes", safety)
        self.assertIn("emergência real", safety)

    def test_longitudinal_memory_requires_identity_and_verified_write(self):
        skill = self.read("SKILL.md")
        protocol = self.read("references/LEARNER_STATE_PROTOCOL.md")
        self.assertIn("learner_id_binding: verified | mismatch | unknown", skill)
        self.assertIn("histórico não atribuível", skill)
        self.assertIn("append, releitura estrita", protocol)
        self.assertIn("atualização não persistida", protocol)

    def test_personalization_fields_and_incomplete_discursive_are_operational(self):
        planner = self.read("references/TARGET_AWARE_STUDY_PLANNER.md")
        skill = self.read("SKILL.md")
        for field in ("starting_level", "preferred_method", "energy_constraint"):
            self.assertIn(f"`{field}` controla", planner)
        self.assertIn("comando e pontos obrigatórios não avaliáveis", skill)

    def test_behavioral_manifest_separates_executor_payload_from_oracle(self):
        manifest_path = ROOT.parent / "qualification" / "fixtures" / "behavioral" / "MANIFEST.json"
        if not manifest_path.is_file():
            self.skipTest("qualification fixture manifest is not shipped in standalone installs")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema_version"], "1.1.0")
        self.assertEqual(len(manifest["tests"]), 24)
        for item in manifest["tests"]:
            self.assertTrue(item["adjudication_spec_files"])
            self.assertTrue(item["executor_payload_files"])
            spec_paths = {entry["path"] for entry in item["adjudication_spec_files"]}
            payload_paths = {entry["path"] for entry in item["executor_payload_files"]}
            self.assertFalse(spec_paths & payload_paths, item["test_id"])

    def test_release_contract_never_uses_legacy_go(self):
        validator = self.read("scripts/validate_package.py")
        gates = json.loads(self.read("registry/release_gates.json"))
        self.assertNotIn('expected_decision = "GO"', validator)
        self.assertIn(gates["decision"], {"HOLD", "READY_FOR_RELEASE"})

    def test_curriculum_clinical_validity_and_pattern_analyzer_stay_orthogonal(self):
        skill = self.read("SKILL.md")
        question = self.read("references/QUESTION_INTELLIGENCE_P7.md")
        learner = self.read("references/LEARNER_STATE_PROTOCOL.md")
        safety = self.read("references/MEDICAL_SAFETY_LAYER.md")
        pattern = self.read("references/PATTERN_ANALYZER_CONTRACT.md")
        schema = json.loads(self.read("schemas/v1/assessment-evidence.schema.json"))
        self.assertIn("Três planos ligados, nunca fundidos", skill)
        self.assertIn("Quarentena clínica não", skill)
        self.assertIn("apaga conteúdo curricular", skill)
        self.assertIn("answer_key_scope: curricular", skill)
        self.assertIn("Três planos de proveniência e escopo", question)
        self.assertIn("inference_scope: curricular_performance", question)
        self.assertIn("Fronteira do Pattern Analyzer", learner)
        self.assertIn("não alimenta hipótese", learner)
        self.assertIn("Quarentena não apaga o currículo", safety)
        self.assertIn("operação_exigida(item) × movimento_candidato(tentativa)", pattern)
        self.assertIn("Toda hipótese", pattern)
        self.assertIn("evidence_event_ids", pattern)
        self.assertIn("Percentual sem numerador/denominador é proibido", pattern)
        self.assertIn("sessão sem histórico", pattern)
        required = set(schema["required"])
        self.assertTrue({"item_validity", "curricular_frame", "clinical_validity_at_attempt", "answer_key_scope", "inference_scope"} <= required)


if __name__ == "__main__":
    unittest.main()
