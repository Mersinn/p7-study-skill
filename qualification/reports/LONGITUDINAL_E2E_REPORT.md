# LONGITUDINAL_E2E_REPORT — ledger local ponta a ponta

**Data:** 22/08/2026  
**Fonte:** cópia instalada do commit `f56a1e5`  
**Executor:** `work/ledger_e2e_check.py`, usando diretamente
`p7-study-skill/scripts/ledger.py`.

## Cenário executado

- sessão A criou confiança e tentativa incorreta;
- sessão B foi uma nova sessão após export/import do `.p7-state`;
- a mesma `review_key` foi retomada com relógio injetado em 48h, 7d e 21d;
- a linha corrompida foi isolada para projeção, enquanto validação estrita a
  rejeitou;
- parent cross-capsule foi rejeitado;
- estado sem ledger permaneceu sem `events.jsonl`.

## Resultado reproduzido

```json
{
  "session_a_events": 2,
  "session_b_imported_events": 2,
  "stages": [0, 1, 2, "completed"],
  "review_task_id": "learner:e2e|capsule:eisca:e2e|concept:e2e",
  "export_import_events": 5,
  "duplicate_review_task_ids": 0,
  "corrupt_projection_contained": true,
  "strict_validation_rejected_corruption": true,
  "cross_parent_rejected": true,
  "no_ledger_state": true
}
```

## Interpretação

O mecanismo determinístico de ledger/scheduler passa este E2E local e não
duplica o estado. Isso não prova ainda retomada através da superfície real de
estudo, nem a declaração textual de ausência de memória pelo agente; essas
partes dependem das jornadas headless, que permanecem `INCONCLUSIVO` pelo
bloqueio de API registrado em `BEHAVIORAL_EXECUTION_BLOCKER.md`.
