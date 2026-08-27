"""Regression tests for the v1.5.0 structural inventory workstream."""

from __future__ import annotations

import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
TOOL_PATH = REPO / "qualification" / "tools" / "build_occurrence_inventory.py"
SPEC = importlib.util.spec_from_file_location("build_occurrence_inventory", TOOL_PATH)
assert SPEC and SPEC.loader
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


def detector_row(detection_id: str, text: str, *, category: str = "dose_via_intervalo", risk: str = "high", links: str = "") -> dict[str, str]:
    return {
        "detection_id": detection_id,
        "capsule_id": "capsule:test:one",
        "capsule_path": "capsules/TEST/one.md",
        "discipline": "TEST",
        "risk": risk,
        "line_no": "10",
        "section": "conduta",
        "section_class": "assertive_clinical",
        "category": category,
        "tier": "strong",
        "critical_category": "True",
        "in_sweep_denominator": "True",
        "capsule_has_registered_claims": "False",
        "linked_claim_ids": links,
        "link_basis": "shared_numeric_tokens" if links else "",
        "resolved": "True" if links else "False",
        "source": "single_line",
        "text": text,
    }


class CandidateEquivalenceTests(unittest.TestCase):
    def test_exact_formatting_variant_merges(self) -> None:
        left = detector_row("left", "Administrar 5 mg por via oral.")
        right = detector_row("right", "Administrar 5 mg por via oral .")
        self.assertEqual(inventory.candidate_key(left), inventory.candidate_key(right))

    def test_number_unit_route_population_and_context_differences_do_not_merge(self) -> None:
        base = detector_row("base", "Adultos: administrar 5 mg por via oral na urgencia.")
        variants = [
            detector_row("number", "Adultos: administrar 10 mg por via oral na urgencia."),
            detector_row("unit", "Adultos: administrar 5 mcg por via oral na urgencia."),
            detector_row("route", "Adultos: administrar 5 mg por via intramuscular na urgencia."),
            detector_row("population", "Criancas: administrar 5 mg por via oral na urgencia."),
            detector_row("context", "Adultos: administrar 5 mg por via oral no ambulatorio."),
        ]
        for variant in variants:
            with self.subTest(variant=variant["detection_id"]):
                self.assertNotEqual(inventory.candidate_key(base), inventory.candidate_key(variant))


class InventoryCoverageTests(unittest.TestCase):
    def test_ambiguous_link_becomes_named_pending_candidate(self) -> None:
        rows = [detector_row("ambiguous", "Administrar 5 mg.", links="claim:one claim:two")]
        registry = {
            "claim:one": {"claim_id": "claim:one", "states": {"clinical_validity": "current"}},
            "claim:two": {"claim_id": "claim:two", "states": {"clinical_validity": "current"}},
        }
        _, dispositions, canonical, candidates = inventory.build_inventory(rows, registry, "0" * 64)
        self.assertEqual(dispositions[0]["disposition"], "candidate_claim_pending")
        self.assertTrue(dispositions[0]["target_claim_id"].startswith("candidate-claim:"))
        self.assertEqual(candidates[0]["clinical_validity"], "pending")
        self.assertEqual(candidates[0]["practice_current_eligibility"], "blocked")
        inventory.validate_inventory(rows, *inventory.build_inventory(rows, registry, "0" * 64)[:3])
        self.assertTrue(any(item["claim_id"] == dispositions[0]["target_claim_id"] for item in canonical))

    def test_real_denominator_is_fully_accounted(self) -> None:
        detections = REPO / "qualification" / "reports" / "CRITICAL_CLAIM_DETECTIONS.csv"
        claims = REPO / "p7-study-skill" / "registry" / "clinical_claims.jsonl"
        rows = inventory.load_primary_occurrences(detections)
        registry = inventory.load_registry(claims)
        occurrences, dispositions, canonical, _ = inventory.build_inventory(rows, registry, inventory.sha256_file(detections))
        metrics = inventory.validate_inventory(rows, occurrences, dispositions, canonical)
        self.assertEqual(metrics["occurrences"], 3602)
        self.assertEqual(sum(row["risk"] == "high" for row in rows), 2817)
        self.assertEqual(len(dispositions), 3602)
        self.assertFalse(any(not row["target_claim_id"] for row in dispositions))

    def test_pipeline_is_deterministic(self) -> None:
        rows = [
            detector_row("first", "Administrar 5 mg por via oral."),
            detector_row("second", "Administrar 10 mg por via oral."),
        ]
        registry = {}
        with tempfile.TemporaryDirectory() as first, tempfile.TemporaryDirectory() as second:
            first_path, second_path = Path(first), Path(second)
            for target in (first_path, second_path):
                occurrences, dispositions, canonical, candidates = inventory.build_inventory(rows, registry, "0" * 64)
                negative = inventory.negative_merge_sample(rows)
                summary = inventory.build_summary(rows, dispositions, canonical, candidates, negative, "0" * 64, "1" * 64)
                inventory.write_jsonl(target / "occurrences.jsonl", occurrences)
                inventory.write_jsonl(target / "dispositions.jsonl", dispositions)
                inventory.write_json(target / "summary.json", summary)
            self.assertEqual((first_path / "occurrences.jsonl").read_bytes(), (second_path / "occurrences.jsonl").read_bytes())
            self.assertEqual((first_path / "dispositions.jsonl").read_bytes(), (second_path / "dispositions.jsonl").read_bytes())
            self.assertEqual((first_path / "summary.json").read_bytes(), (second_path / "summary.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
