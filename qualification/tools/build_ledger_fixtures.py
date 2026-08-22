#!/usr/bin/env python3
"""Gera F-LEDGER e F-CORRUPT-LEDGER com cadeia de hash REAL (usa o proprio
scripts/ledger.py em vez de recalcular hash a mao, para o fixture ser
genuinamente carregavel pela implementacao de producao, nao so 'parecido').

F-LEDGER: sessao A completa — confianca, tentativa inicial incorreta,
feedback, revisao robusta e independente (48h depois) que fecha o ciclo ate
o proximo estagio. Usado no T22 (sessao B deve reabrir e reconhecer so a
tarefa vencida, sem duplicar).

F-CORRUPT-LEDGER: mesma base de F-LEDGER + uma linha com record_hash
adulterado inserida no meio — projecao tolerante deve conter e isolar a
linha corrompida; validacao estrita (read_events) deve falhar.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "p7-study-skill" / "scripts"))

from ledger import append_event, init_state  # noqa: E402


def event(event_id, event_type, occurred_at, interaction, payload, **extra):
    return {
        "event_id": f"event:{event_id}",
        "learner_id": "learner:fixture-t22",
        "occurred_at": occurred_at,
        "event_type": event_type,
        "interaction_id": interaction,
        "payload": payload,
        **extra,
    }


def build_valid(state_dir: Path) -> None:
    init_state(state_dir)
    append_event(
        state_dir,
        event("f-c1", "confidence_recorded", "2026-08-18T14:00:00Z", "i1",
              {"confidence": 0.4},
              capsule_id="capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao",
              concept_id="concept:plano-c-indicacoes"),
    )
    append_event(
        state_dir,
        event("f-a1", "answer_submitted", "2026-08-18T14:01:00Z", "i1",
              {"result": "incorrect", "independent": True, "hint_level": "none"},
              capsule_id="capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao",
              concept_id="concept:plano-c-indicacoes"),
    )
    append_event(
        state_dir,
        event("f-fb1", "feedback_shown", "2026-08-18T14:01:30Z", "i1",
              {"shown": True},
              capsule_id="capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao",
              concept_id="concept:plano-c-indicacoes", parent_event_id="event:f-a1"),
    )
    review_task_id = "|".join([
        "learner:fixture-t22",
        "capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao",
        "concept:plano-c-indicacoes",
    ])
    append_event(
        state_dir,
        event("f-r1", "review_completed", "2026-08-20T14:00:00Z", "i2",
              {"result": "correct", "retrieval_quality": "robust", "independent": True, "hint_level": "none"},
              capsule_id="capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao",
              concept_id="concept:plano-c-indicacoes",
              parent_event_id="event:f-a1",
              review_task_id=review_task_id),
    )


def corrupt(events_path: Path) -> None:
    lines = events_path.read_text(encoding="utf-8").splitlines()
    idx = 2  # a linha do feedback_shown (f-fb1) — corrompida sem quebrar a leitura das outras
    rec = json.loads(lines[idx])
    rec["record_hash"] = "0" * 64  # hash deliberadamente invalido
    lines[idx] = json.dumps(rec, ensure_ascii=False)
    events_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    out = REPO_ROOT / "qualification" / "fixtures" / "behavioral"
    valid_dir = out / "F-LEDGER" / ".p7-state"
    corrupt_dir = out / "F-CORRUPT-LEDGER" / ".p7-state"
    build_valid(valid_dir)
    build_valid(corrupt_dir)
    corrupt(corrupt_dir / "events.jsonl")
    print("F-LEDGER events:", (valid_dir / "events.jsonl").read_text(encoding="utf-8").count("\n"))
    print("F-CORRUPT-LEDGER events:", (corrupt_dir / "events.jsonl").read_text(encoding="utf-8").count("\n"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
