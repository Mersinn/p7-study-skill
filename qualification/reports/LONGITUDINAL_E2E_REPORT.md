# LONGITUDINAL_E2E_REPORT — ledger local ponta a ponta

**Estado vigente (25/08/2026):** `PARTIAL / INCONCLUSIVE` para o gate global.
**Branch:** `qualification/v1.0.0-codex`
**Superfície:** Codex, em duas sessões limpas e sem histórico herdado.
**Skill:** SHA-256 `1dafc05d8ef5d8c1e85c9822a85bc41fdc484c083b3c7bb8cb4b04e2f18eb7e7`.

## Reexecução na superfície Codex

A sessão A recebeu apenas a skill, a entrada congelada e um `.p7-state`
descartável. Leu os 4 eventos, conduziu recuperação ativa e acrescentou
confiança + resultado, levando o estado a 6 eventos com cadeia válida. O raw e
o registro estão em `qualification/runs/behavioral_codex/T22_surface/clean_sessions/`.

A sessão B2 foi um agente novo, sem herdar A ou esta auditoria. Recebeu somente
a cópia do estado resultante e a entrada congelada de retomada em 16/09/2026.
Reconstruiu uma revisão vencida, o histórico erro → acertos robustos, o mesmo
tema e a ausência de hipótese. Ao receber a resposta, aplicou o pivô
corretamente, mas informou que o ambiente do executor estava somente leitura e
não persistiu o novo evento. Portanto, a leitura/retomada passa, mas a gravação
real através da segunda superfície permanece `INCONCLUSIVE`.

| Sessão | Limpa | Resultado observável | Adjudicação |
|---|---:|---|---|
| A | sim | 4 → 6 eventos, confiança e resultado registrados, cadeia estrita válida | PASS |
| B2 | sim | revisão vencida reconstruída e resposta correta; novo evento não gravado pelo executor | INCONCLUSIVE |

O resultado não fecha `longitudinal_resume_end_to_end`; o gate permanece
`pending` até uma segunda sessão com permissão de escrita demonstrar o append
encadeado do mesmo `review_task_id`.

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
duplica o estado. A reexecução Codex demonstrou leitura longitudinal e
recuperação sem memória inventada em sessão nova; contudo, a sessão B2 não teve
permissão de escrita para concluir o append. Isso é uma pendência de execução,
não um PASS por inferência. O gate global permanece HOLD/pending.
