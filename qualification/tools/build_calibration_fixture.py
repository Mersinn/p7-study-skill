#!/usr/bin/env python3
"""Gera o ledger de F-T24-CALIBRATION (hash real via ledger.py). 13 pares
confianca+resultado independente sem dica (12 validos para calibracao + 1
assistido por dica, que deve ser EXCLUIDO — testa 'pista nao gradua'), mais
1 linha corrompida inserida no meio."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "p7-study-skill" / "scripts"))

from ledger import append_event, init_state  # noqa: E402

CAPSULE = "capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao"
CONCEPT = "concept:t24-calibration-fixture"

# (confidence, correct, hint_level) — 12 itens validos, desenhados para dar
# vies de excesso de confianca claro (Brier > 0 significativo), mais 1 item
# assistido por dica (excluido do calculo).
ITEMS = [
    (0.9, True, "none"), (0.9, False, "none"), (0.9, True, "none"), (0.85, False, "none"),
    (0.8, True, "none"), (0.8, True, "none"), (0.7, False, "none"), (0.6, True, "none"),
    (0.5, True, "none"), (0.4, False, "none"), (0.3, False, "none"), (0.2, True, "none"),
    (0.9, True, "decisive"),  # assistido por dica pista decisiva — deve ser EXCLUIDO
]


def event(event_id, event_type, occurred_at, interaction, payload, **extra):
    return {
        "event_id": f"event:{event_id}", "learner_id": "learner:fixture-t24",
        "occurred_at": occurred_at, "event_type": event_type, "interaction_id": interaction,
        "payload": payload, **extra,
    }


def build(state_dir: Path) -> None:
    init_state(state_dir)
    base_minute = 0
    for i, (conf, correct, hint) in enumerate(ITEMS, start=1):
        interaction = f"i{i}"
        ts_c = f"2026-08-20T09:{base_minute:02d}:00Z"
        ts_a = f"2026-08-20T09:{base_minute + 1:02d}:00Z"
        base_minute += 2
        append_event(state_dir, event(f"t24-c{i}", "confidence_recorded", ts_c, interaction, {"confidence": conf}))
        append_event(
            state_dir,
            event(f"t24-a{i}", "answer_submitted", ts_a, interaction,
                  {"result": "correct" if correct else "incorrect", "independent": True, "hint_level": hint},
                  capsule_id=CAPSULE, concept_id=CONCEPT),
        )


def corrupt(events_path: Path) -> None:
    lines = events_path.read_text(encoding="utf-8").splitlines()
    idx = 10  # linha no meio do lote
    rec = json.loads(lines[idx])
    rec["record_hash"] = "0" * 64
    lines[idx] = json.dumps(rec, ensure_ascii=False)
    events_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    out = REPO_ROOT / "qualification" / "fixtures" / "behavioral" / "adhoc" / "F-T24-CALIBRATION" / ".p7-state"
    build(out)
    corrupt(out / "events.jsonl")

    sys.path.insert(0, str(REPO_ROOT / "p7-study-skill" / "scripts"))
    from ledger import read_events_tolerant, calibration
    ok, corrupt_entries = read_events_tolerant(out)
    result = calibration(ok, minimum=10, corrupt_count=len(corrupt_entries))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("corrupt entries:", corrupt_entries)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
