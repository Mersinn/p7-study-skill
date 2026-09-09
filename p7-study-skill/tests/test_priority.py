from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from p7lib import calculate_priority, load_json  # noqa: E402


class PriorityTests(unittest.TestCase):
    def setUp(self):
        self.policy = load_json(ROOT / "config" / "priority-policy.json")

    def test_formula_is_auditable(self):
        inputs = {
            "exam_recurrence": 3,
            "clinical_risk": 3,
            "curriculum_imminence": 2,
            "learner_gap": 2,
            "transfer_value": 2,
        }
        self.assertEqual(calculate_priority(inputs, self.policy), {"score": 28, "label": "high", "missing": []})

    def test_missing_input_never_reuses_legacy_label(self):
        inputs = {
            "exam_recurrence": 3,
            "clinical_risk": None,
            "curriculum_imminence": 2,
            "learner_gap": 2,
            "transfer_value": 2,
        }
        result = calculate_priority(inputs, self.policy)
        self.assertEqual(result["label"], "unscored")
        self.assertIsNone(result["score"])
        self.assertEqual(result["missing"], ["clinical_risk"])

    def test_out_of_range_rejected(self):
        inputs = {
            "exam_recurrence": 4,
            "clinical_risk": 0,
            "curriculum_imminence": 0,
            "learner_gap": 0,
            "transfer_value": 0,
        }
        with self.assertRaises(ValueError):
            calculate_priority(inputs, self.policy)


if __name__ == "__main__":
    unittest.main()
