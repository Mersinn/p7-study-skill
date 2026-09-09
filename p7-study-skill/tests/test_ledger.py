from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from ledger import append_event, calibration, project_hypotheses, project_reviews, read_events, write_projections  # noqa: E402


def event(event_id, event_type, occurred_at, interaction, payload, **extra):
    return {
        "event_id": f"event:{event_id}",
        "learner_id": "learner:test",
        "occurred_at": occurred_at,
        "event_type": event_type,
        "interaction_id": interaction,
        "payload": payload,
        **extra,
    }


class LedgerTests(unittest.TestCase):
    def test_chain_is_immutable_and_tampering_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            append_event(state, event("c1", "confidence_recorded", "2026-08-20T12:00:00Z", "i1", {"confidence": 0.7}))
            append_event(
                state,
                event("a1", "answer_submitted", "2026-08-20T12:01:00Z", "i1", {"result": "correct", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:test"),
            )
            self.assertEqual(len(read_events(state)), 2)
            content = (state / "events.jsonl").read_text(encoding="utf-8").replace('"correct"', '"incorrect"')
            (state / "events.jsonl").write_text(content, encoding="utf-8")
            with self.assertRaises(ValueError):
                read_events(state)

    def test_t15_fragile_or_assisted_correct_does_not_advance(self):
        base = event("a", "answer_submitted", "2026-08-20T10:00:00Z", "i1", {"result": "correct"}, capsule_id="capsule:eisca:test", concept_id="concept:test")
        fragile = event("r1", "review_completed", "2026-08-22T10:00:00Z", "i2", {"result": "correct", "retrieval_quality": "fragile", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:test")
        decisive = event("r2", "review_completed", "2026-08-24T10:00:00Z", "i3", {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "decisive"}, capsule_id="capsule:eisca:test", concept_id="concept:test")
        recognized = event("r3", "review_completed", "2026-08-26T10:00:00Z", "i4", {"result": "correct", "retrieval_quality": "robust", "independent": False, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:test")
        task = project_reviews([base, fragile, decisive, recognized])[0]
        self.assertEqual(task["stage"], 0)
        self.assertEqual(task["due_at"], "2026-08-28T10:00:00Z")

    def test_robust_independent_review_advances_48h_7d_21d_and_deduplicates(self):
        events = [
            event("a", "answer_submitted", "2026-08-20T10:00:00Z", "i1", {"result": "correct"}, capsule_id="capsule:eisca:test", concept_id="concept:test"),
            event("r1", "review_completed", "2026-08-22T10:00:00Z", "i2", {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:test"),
            event("r2", "review_completed", "2026-08-29T10:00:00Z", "i3", {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:test"),
        ]
        tasks = project_reviews(events)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["stage"], 2)
        self.assertEqual(tasks[0]["status"], "scheduled")
        self.assertEqual(tasks[0]["due_at"], "2026-09-19T10:00:00Z")

    def test_review_after_21_days_completes_cycle_without_infinite_reschedule(self):
        events = [
            event("a", "answer_submitted", "2026-08-20T10:00:00Z", "i1", {"result": "correct"}, capsule_id="capsule:eisca:test", concept_id="concept:test"),
            event("r1", "review_completed", "2026-08-22T10:00:00Z", "i2", {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:test"),
            event("r2", "review_completed", "2026-08-29T10:00:00Z", "i3", {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:test"),
            event("r3", "review_completed", "2026-09-19T10:00:00Z", "i4", {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:test"),
        ]
        task = project_reviews(events)[0]
        self.assertEqual(task["status"], "completed")
        self.assertIsNone(task["due_at"])

    def test_t18_hypothesis_requires_repetition_and_at_least_one_valid_transfer(self):
        one = event("a1", "answer_submitted", "2026-08-20T10:00:00Z", "i1", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": True, "independent": True, "hint_level": "none", "retrieval_quality": "robust", "transfer_context": "case-a"}, capsule_id="capsule:eisca:test", concept_id="concept:a")
        same_context = event("a2", "answer_submitted", "2026-08-21T10:00:00Z", "i2", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": True, "independent": True, "hint_level": "none", "retrieval_quality": "robust", "transfer_context": "case-a"}, capsule_id="capsule:eisca:test", concept_id="concept:b")
        self.assertEqual(project_hypotheses([one, same_context])[0]["status"], "candidate")
        other = event("a3", "answer_submitted", "2026-08-22T10:00:00Z", "i3", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": True, "independent": True, "hint_level": "none", "retrieval_quality": "robust", "transfer_context": "case-b"}, capsule_id="capsule:eisca:test", concept_id="concept:c")
        result = project_hypotheses([one, same_context, other])[0]
        self.assertEqual(result["status"], "confirmed")
        self.assertEqual(result["independent_context_count"], 2)
        self.assertGreaterEqual(result["valid_transfer_count"], 1)

    def test_two_independent_contexts_without_transfer_remain_candidate(self):
        first = event("a1", "answer_submitted", "2026-08-20T10:00:00Z", "i1", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": False, "independent": True, "hint_level": "none", "retrieval_quality": "robust"}, capsule_id="capsule:eisca:test", concept_id="concept:a")
        second = event("a2", "answer_submitted", "2026-08-21T10:00:00Z", "i2", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": False, "independent": True, "hint_level": "none", "retrieval_quality": "robust"}, capsule_id="capsule:eisca:test", concept_id="concept:b")
        result = project_hypotheses([first, second])[0]
        self.assertEqual(result["status"], "candidate")
        self.assertEqual(result["valid_transfer_count"], 0)

    def test_one_independent_nontransfer_plus_one_independent_transfer_confirms(self):
        first = event("a1", "answer_submitted", "2026-08-20T10:00:00Z", "i1", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": False, "independent": True, "hint_level": "none", "retrieval_quality": "robust"}, capsule_id="capsule:eisca:test", concept_id="concept:a")
        second = event("a2", "answer_submitted", "2026-08-21T10:00:00Z", "i2", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": True, "independent": True, "hint_level": "none", "retrieval_quality": "robust", "transfer_context": "case-b"}, capsule_id="capsule:eisca:test", concept_id="concept:b")
        result = project_hypotheses([first, second])[0]
        self.assertEqual(result["status"], "confirmed")
        self.assertEqual(result["valid_transfer_count"], 1)

    def test_t24_calibration_requires_ten_and_exposes_exclusions_bias_and_brier(self):
        events = []
        for index in range(9):
            events.extend([
                event(f"c{index}", "confidence_recorded", f"2026-08-{index + 1:02d}T10:00:00Z", f"i{index}", {"confidence": 0.8}),
                event(f"a{index}", "answer_submitted", f"2026-08-{index + 1:02d}T10:01:00Z", f"i{index}", {"result": "correct", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id=f"concept:{index}"),
            ])
        events.extend([
            event("cx", "confidence_recorded", "2026-08-15T10:00:00Z", "ix", {"confidence": 0.9}),
            event("ax", "answer_submitted", "2026-08-15T10:01:00Z", "ix", {"result": "correct", "independent": False, "hint_level": "decisive"}, capsule_id="capsule:eisca:test", concept_id="concept:x"),
        ])
        insufficient = calibration(events)
        self.assertEqual(insufficient["status"], "insufficient_data")
        self.assertEqual(insufficient["exclusions"]["assisted_or_nonindependent"], 1)
        events.extend([
            event("c9", "confidence_recorded", "2026-08-16T10:00:00Z", "i9", {"confidence": 0.2}),
            event("a9", "answer_submitted", "2026-08-16T10:01:00Z", "i9", {"result": "incorrect", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id="concept:9"),
        ])
        result = calibration(events)
        self.assertEqual(result["status"], "available")
        self.assertEqual(result["sample_size"], 10)
        self.assertIn("brier_score", result)
        self.assertIn("mean_confidence_bias", result)
        self.assertEqual(len(result["bins"]), 4)
        self.assertEqual(sum(item["n"] for item in result["bins"]), 10)

    def test_t15_decisive_hint_or_fragile_transfer_does_not_confirm(self):
        valid = event("a1", "answer_submitted", "2026-08-20T10:00:00Z", "i1", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": True, "independent": True, "hint_level": "none", "retrieval_quality": "robust", "transfer_context": "case-a"}, capsule_id="capsule:eisca:test", concept_id="concept:a")
        contaminated = event("a2", "answer_submitted", "2026-08-21T10:00:00Z", "i2", {"result": "incorrect", "movement_candidate": "premature_closure", "transfer_valid": True, "independent": True, "hint_level": "decisive", "retrieval_quality": "fragile", "transfer_context": "case-b"}, capsule_id="capsule:eisca:test", concept_id="concept:b")
        result = project_hypotheses([valid, contaminated])[0]
        self.assertEqual(result["status"], "candidate")
        self.assertEqual(result["independent_context_count"], 1)

    def test_t22_review_append_requires_existing_parent_and_stable_review_key(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            first = append_event(state, event("a1", "answer_submitted", "2026-08-20T10:00:00Z", "i1", {"result": "incorrect"}, capsule_id="capsule:eisca:test", concept_id="concept:test"))
            review_payload = {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "none"}
            with self.assertRaises(ValueError):
                append_event(state, event("r0", "review_completed", "2026-08-22T10:00:00Z", "i2", review_payload, capsule_id="capsule:eisca:test", concept_id="concept:test", parent_event_id="event:missing", review_task_id="wrong"))
            stored = append_event(state, event("r1", "review_completed", "2026-08-22T10:00:00Z", "i2", review_payload, capsule_id="capsule:eisca:test", concept_id="concept:test", parent_event_id=first["event_id"], review_task_id="learner:test|capsule:eisca:test|concept:test"))
            self.assertEqual(stored["parent_event_id"], first["event_id"])
            chained = append_event(state, event("r2", "review_completed", "2026-08-29T10:00:00Z", "i3", review_payload, capsule_id="capsule:eisca:test", concept_id="concept:test", parent_event_id=stored["event_id"], review_task_id="learner:test|capsule:eisca:test|concept:test"))
            self.assertEqual(chained["parent_event_id"], stored["event_id"])

    def test_t22_rejects_cross_concept_capsule_and_learner_parents(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            cross_concept = append_event(state, event("pc", "answer_submitted", "2026-08-20T09:00:00Z", "pc", {"result": "incorrect"}, capsule_id="capsule:eisca:test", concept_id="concept:other"))
            cross_capsule = append_event(state, event("pk", "answer_submitted", "2026-08-20T09:01:00Z", "pk", {"result": "incorrect"}, capsule_id="capsule:eisca:other", concept_id="concept:test"))
            cross_learner = append_event(state, event("pl", "answer_submitted", "2026-08-20T09:02:00Z", "pl", {"result": "incorrect"}, learner_id="learner:other", capsule_id="capsule:eisca:test", concept_id="concept:test"))
            payload = {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "none"}
            for index, parent in enumerate((cross_concept, cross_capsule, cross_learner)):
                with self.assertRaises(ValueError):
                    append_event(state, event(f"bad{index}", "review_completed", f"2026-08-22T10:0{index}:00Z", f"bad{index}", payload, capsule_id="capsule:eisca:test", concept_id="concept:test", parent_event_id=parent["event_id"], review_task_id="learner:test|capsule:eisca:test|concept:test"))

    def test_t24_corrupt_line_is_quarantined_for_projection_but_strict_validation_fails(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            for index in range(10):
                append_event(state, event(f"c{index}", "confidence_recorded", f"2026-08-{index + 1:02d}T10:00:00Z", f"i{index}", {"confidence": 0.75}))
                append_event(state, event(f"a{index}", "answer_submitted", f"2026-08-{index + 1:02d}T10:01:00Z", f"i{index}", {"result": "correct", "independent": True, "hint_level": "none"}, capsule_id="capsule:eisca:test", concept_id=f"concept:{index}"))
            path = state / "events.jsonl"
            lines = path.read_text(encoding="utf-8").splitlines()
            lines.insert(5, "{corrupt-json")
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            with self.assertRaises(Exception):
                read_events(state)
            write_projections(state)
            import json
            report = json.loads((state / "corrupt_records.json").read_text(encoding="utf-8"))
            calibrated = json.loads((state / "calibration.json").read_text(encoding="utf-8"))
            self.assertGreaterEqual(report["count"], 1)
            self.assertEqual(calibrated["status"], "available")
            self.assertGreaterEqual(calibrated["exclusions"]["corrupt_records"], 1)

    def test_feedback_requires_prior_confidence_or_explicit_decline(self):
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            with self.assertRaises(ValueError):
                append_event(state, event("f1", "feedback_shown", "2026-08-20T10:00:00Z", "i1", {}))
            append_event(state, event("f2", "feedback_shown", "2026-08-20T10:01:00Z", "i2", {"confidence_declined": True}))


if __name__ == "__main__":
    unittest.main()
