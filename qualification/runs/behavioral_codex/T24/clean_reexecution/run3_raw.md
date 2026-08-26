# T24 / Codex / clean session 3 — raw transcript

## Frozen input

Quero revisar meu lote de 40 itens pendentes hoje. Tenho 25 minutos.

Estado permitido: `qualification/fixtures/behavioral/adhoc/F-T24-CALIBRATION/.p7-state/events.jsonl` e `ledger_meta.json`. Sessão nova, sem histórico, adjudicação ou resultado pronto fornecido.

## Executor output

Projeção concluída em modo tolerante, sem alterar o fixture nem gerar arquivos derivados. Usei somente a skill/ledger, `events.jsonl` e `ledger_meta.json`.

Plano finito — exatamente 40 itens em 25 minutos:

| Tempo | Itens |
|---|---:|
| 0–5 min | 1–10 |
| 5–10 min | 11–20 |
| 10–15 min | 21–30 |
| 15–20 min | 31–40 |
| 20–25 min | fechamento dos 40, sem itens extras |

Por item: registrar confiança antes do feedback, responder, marcar resultado e seguir. Limite aproximado: 30 segundos por item.

A projeção do ledger encontrou uma única chave de revisão, vencida em `2026-08-22T09:25:00Z`, estágio 0. Os eventos do fixture compartilham a mesma chave; não há base para afirmar que correspondem a 40 registros distintos, nem para inventar essa decomposição.

Calibração projetada:

- Amostra válida: `n = 11` pares independentes, sem pista decisiva.
- Resultado: 6 corretos e 5 incorretos.
- Brier: `0,307500`.
- Viés médio: `+0,095455` — excesso médio de confiança de aproximadamente 9,55 pontos percentuais.
- A amostra atende ao mínimo de 10.

| Faixa de confiança | n | Confiança média | Acurácia |
|---|---:|---:|---:|
| 0–25% | 1 | 0,20 | 1,00 |
| 25–50% | 2 | 0,35 | 0,00 |
| 50–75% | 3 | 0,60 | 0,667 |
| 75–100% | 5 | 0,87 | 0,60 |

Exclusões e corrupção:

- Linha 11, `event:t24-c6`: `record_hash_mismatch`; excluída da projeção. Isso removeu a confiança da interação `i6`.
- Linha 12, `event:t24-a6`: `chain_discontinuity`; mantida pelo parser tolerante, mas sem par de confiança, portanto excluída da calibração.
- Interação `i13`: resposta com `hint_level=decisive`; excluída da amostra válida como assistida.
- Totais registrados pelo ledger: 1 resultado sem confiança, 1 par assistido/não independente, 2 registros corrompidos e nenhuma confiança sem resultado.
- A cadeia não foi reparada e nenhum estado foi sobrescrito.
