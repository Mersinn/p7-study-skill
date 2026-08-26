# LONGITUDINAL_E2E_REPORT — ledger local ponta a ponta

**Estado vigente (26/08/2026):** `PASS` para o gate longitudinal.
**Branch:** `qualification/v1.0.0-codex`
**Superfície:** Codex, em duas sessões limpas e sem histórico herdado.
**Snapshot efetivo da sessão B:** commit `0d5073cf18593ca5b08af4f545337f190d3fb609`; tree da skill `418f7dc3bbeac0b5c1676cd4657625bf63086b75`.

## Reexecução na superfície Codex

A sessão A recebeu apenas a skill, a entrada congelada e um `.p7-state`
descartável. Leu os 4 eventos, conduziu recuperação ativa e acrescentou
confiança + resultado, levando o estado a 6 eventos com cadeia válida. O raw e
o registro estão em `qualification/runs/behavioral_codex/T22_surface/clean_sessions/`.

A sessão B2 histórica foi um agente novo, sem herdar A ou esta auditoria.
Reconstruiu o histórico, mas o filesystem somente leitura impediu o append;
essa tentativa continua preservada como `INCONCLUSIVE`.

A sessão B final também foi nova e recebeu somente a skill no snapshot
declarado, `input.md` e a cópia versionada e gravável do estado de 6 eventos.
Em 16/09/2026 informou corretamente que não havia revisão vencida e que a
próxima data era 18/09; em seguida antecipou uma recuperação sem revelar a
resposta. Depois da tentativa do aluno, acrescentou `confidence_recorded` e
`review_completed` sob `interaction_id=i4`, mantendo
`learner_id=learner:fixture-t22` e `parent_event_id=event:f-r2`.

A verificação independente releu o arquivo no disco: 6 → 8 eventos, cadeia
estrita válida e SHA-256 final
`4726ea3931f109d244150518e38257596fb2d2a541936e856a6131f7a6848721`.
O raw visível integral e o registro canônico estão em
`qualification/runs/longitudinal_codex/F-LEDGER-B/`.

| Sessão | Limpa | Resultado observável | Adjudicação |
|---|---:|---|---|
| A | sim | 4 → 6 eventos, confiança e resultado registrados, cadeia estrita válida | PASS |
| B2 histórica | sim | histórico reconstruído; novo evento não gravado por filesystem somente leitura | INCONCLUSIVE |
| B final | sim | 6 → 8 eventos, recuperação retida, append encadeado, releitura e validação estrita | PASS |

O par válido A + B final fecha `longitudinal_resume_end_to_end`. A tentativa B2
permanece fora do denominador válido como evidência de infraestrutura, sem ser
promovida retroativamente. O gate longitudinal passa; isso não altera os gates
comportamentais, clínicos ou de jornadas.

## Execução determinística histórica

O E2E determinístico abaixo permanece preservado como evidência do mecanismo
de ledger; ele não é misturado com a qualificação da superfície Codex.

**Fonte:** cópia instalada do commit `f56a1e5`  
**Executor:** `work/ledger_e2e_check.py`, usando diretamente
`p7-study-skill/scripts/ledger.py`.

O E2E foi preservado como execução histórica do ledger; a branch vigente agora
está em `b1cc464`, sem alteração no código do ledger entre os snapshots.

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
duplica o estado. A reexecução Codex demonstrou leitura longitudinal,
recuperação sem memória inventada e persistência real em uma segunda sessão.
O PASS foi dado pelo estado verificado no disco, não pela alegação do executor.
A decisão global continua `HOLD` por gates independentes ainda abertos.
