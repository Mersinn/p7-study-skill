#!/usr/bin/env python3
"""Amostragem estratificada para validar precisão do detector (Fase 9.1, validação).

Não mede se o detector está "certo" no sentido de decidir cobertura clínica —
mede se cada detecção do denominador é realmente uma afirmação clínica crítica
(precisão) e produz uma lista de cápsulas para busca manual de falso negativo
(recall), com seed fixa para reprodutibilidade.

Uso:
    python qualification/tools/validate_detector.py \
        --detections qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv \
        --out qualification/reports --seed 20260820 --sample-size 220 --fn-capsules 20
"""
from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path
from typing import Any


def load_denominator(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [row for row in csv.DictReader(handle) if row["in_sweep_denominator"] == "True"]


def stratified_sample(rows: list[dict[str, Any]], seed: int, target: int) -> list[dict[str, Any]]:
    rng = random.Random(seed)
    strata: dict[tuple, list[dict[str, Any]]] = {}
    for row in rows:
        key = (row["discipline"], row["category"], row["capsule_has_registered_claims"])
        strata.setdefault(key, []).append(row)

    n_strata = len(strata)
    per_stratum = max(1, target // n_strata)
    sample: list[dict[str, Any]] = []
    for key in sorted(strata):
        members = strata[key][:]
        rng.shuffle(members)
        sample.extend(members[:per_stratum])

    # completa até o alvo com sorteio adicional determinístico sobre o restante
    remaining = [r for r in rows if r not in sample]
    rng.shuffle(remaining)
    i = 0
    while len(sample) < target and i < len(remaining):
        sample.append(remaining[i])
        i += 1
    return sample


def fn_capsule_sample(rows: list[dict[str, Any]], seed: int, n: int) -> list[str]:
    rng = random.Random(seed + 1)
    by_discipline: dict[str, set[str]] = {}
    for row in rows:
        by_discipline.setdefault(row["discipline"], set()).add(row["capsule_path"])
    disciplines = sorted(by_discipline)
    per = max(1, n // len(disciplines))
    chosen: list[str] = []
    for disc in disciplines:
        pool = sorted(by_discipline[disc])
        rng.shuffle(pool)
        chosen.extend(pool[:per])
    return chosen[:n] if len(chosen) >= n else chosen


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--detections", type=Path, default=Path("qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv"))
    parser.add_argument("--out", type=Path, default=Path("qualification/reports"))
    parser.add_argument("--seed", type=int, default=20260820)
    parser.add_argument("--sample-size", type=int, default=220)
    parser.add_argument("--fn-capsules", type=int, default=20)
    args = parser.parse_args()

    rows = load_denominator(args.detections)
    sample = stratified_sample(rows, args.seed, args.sample_size)
    fn_caps = fn_capsule_sample(rows, args.seed, args.fn_capsules)

    fields = ["detection_id", "capsule_id", "capsule_path", "discipline", "risk", "line_no",
              "section", "category", "tier_placeholder", "capsule_has_registered_claims", "text",
              "manual_verdict", "manual_notes"]
    out_path = args.out / "DETECTOR_PRECISION_SAMPLE.csv"
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in sample:
            writer.writerow(
                {
                    "detection_id": row["detection_id"], "capsule_id": row["capsule_id"],
                    "capsule_path": row["capsule_path"], "discipline": row["discipline"],
                    "risk": row["risk"], "line_no": row["line_no"], "section": row["section"],
                    "category": row["category"], "tier_placeholder": "",
                    "capsule_has_registered_claims": row["capsule_has_registered_claims"],
                    "text": row["text"], "manual_verdict": "", "manual_notes": "",
                }
            )

    fn_path = args.out / "DETECTOR_FN_CAPSULE_LIST.csv"
    with fn_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["capsule_path"])
        for path in fn_caps:
            writer.writerow([path])

    print(f"seed={args.seed}")
    print(f"denominator_size={len(rows)}")
    print(f"sample_size={len(sample)} -> {out_path}")
    print(f"fn_capsules={len(fn_caps)} -> {fn_path}")
    for p in fn_caps:
        print("  ", p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
