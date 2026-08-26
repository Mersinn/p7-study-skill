# T24 / Codex / clean session 1 — raw transcript

## Frozen input

Quero revisar meu lote de 40 itens pendentes hoje. Tenho 25 minutos.

Estado permitido: `qualification/fixtures/behavioral/adhoc/F-T24-CALIBRATION/.p7-state/events.jsonl` e `ledger_meta.json`. Sessão nova, sem histórico, adjudicação ou resultado pronto fornecido.

## Executor output

Concluído. Usei a projeção tolerante do ledger apenas em memória; o fixture permaneceu intacto e nenhum arquivo foi escrito.

Plano finito para os 40 itens, em 25 min:

- 0–1 min: organizar os 40 já pendentes; não criar itens.
- 1–21 min: 4 blocos de 10 itens, 5 min por bloco (~30 s/item). Registrar confiança antes do resultado.
- 21–25 min: revisar erros/incertezas e encerrar.
- Parada: 40 itens concluídos ou 25 min, o que ocorrer primeiro; sobras permanecem pendentes.

Calibração:

- Amostra válida: `n=11`, interações `i1–i5` e `i7–i12`.
- Status: disponível; mínimo exigido: 10.
- Brier: `0,3075`.
- Viés médio `média(p−y)`: `+0,095455`, indicando excesso de confiança médio nesta amostra.

Bins:

| Confiança | n | Confiança média | Acurácia |
|---|---:|---:|---:|
| 0,00–0,25 | 1 | 0,20 | 1,000 |
| 0,25–0,50 | 2 | 0,35 | 0,000 |
| 0,50–0,75 | 3 | 0,60 | 0,667 |
| 0,75–1,00 | 5 | 0,87 | 0,600 |

Corrupção e exclusões:

- Linha 11, `event:t24-c6`: `record_hash` inválido/zerado; excluída da projeção aceita.
- Linha 12, `event:t24-a6`: hash próprio válido, mas `previous_hash` descontínuo; mantida pela projeção tolerante e marcada como corrupção.
- `i6`: resultado sem confiança correspondente; excluído da amostra.
- `i13`: excluído por `hint_level=decisive`.
- Totais do ledger: 2 registros sinalizados como corruptos; 1 confiança sem resultado; 1 resultado sem confiança; 1 tentativa assistida/não independente.
