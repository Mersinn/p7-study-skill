#!/usr/bin/env python3
"""Calculate a study priority from explicit, auditable inputs."""

from __future__ import annotations

import argparse
import json

from p7lib import PACKAGE_ROOT, calculate_priority, load_json


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exam-recurrence", type=int)
    parser.add_argument("--clinical-risk", type=int)
    parser.add_argument("--curriculum-imminence", type=int)
    parser.add_argument("--learner-gap", type=int)
    parser.add_argument("--transfer-value", type=int)
    args = parser.parse_args()
    inputs = {
        "exam_recurrence": args.exam_recurrence,
        "clinical_risk": args.clinical_risk,
        "curriculum_imminence": args.curriculum_imminence,
        "learner_gap": args.learner_gap,
        "transfer_value": args.transfer_value,
    }
    policy = load_json(PACKAGE_ROOT / "config" / "priority-policy.json")
    output = {"formula_version": policy["formula_version"], "inputs": inputs, **calculate_priority(inputs, policy)}
    print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
