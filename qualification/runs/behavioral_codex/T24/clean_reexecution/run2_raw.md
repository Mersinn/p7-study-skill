# T24 / Codex / clean session 2 — raw transcript

## Frozen input

Quero revisar meu lote de 40 itens pendentes hoje. Tenho 25 minutos.

Estado permitido: `qualification/fixtures/behavioral/adhoc/F-T24-CALIBRATION/.p7-state/events.jsonl` e `ledger_meta.json`. Sessão nova, sem histórico, adjudicação ou resultado pronto fornecido.

## Executor output

Projeção concluída em memória, sem alterar o fixture.

Plano finito:

- Exatamente 40 itens.
- 5 blocos de 8 itens.
- 5 minutos por bloco; 37,5 segundos por item.
- Em cada item: tentativa → confiança antes do resultado → correção breve.
- Encerrar no item 40; não criar itens extras.

O ledger projetou apenas 1 tarefa de revisão agendada; não a multipliquei artificialmente para 40.

Amostra válida: `n = 11`:

`i1 .90→1, i2 .90→0, i3 .90→1, i4 .85→0, i5 .80→1, i7 .70→0, i8 .60→1, i9 .50→1, i10 .40→0, i11 .30→0, i12 .20→1`

- Brier: **0,3075**
- Viés médio: **+0,095455** — confiança média acima do resultado, indicando sobreconfiança.

Exclusões:

- Linha 11, `event:t24-c6`: `record_hash_mismatch`; contida/quarentenada e excluída.
- Linha 12, `event:t24-a6`: `chain_discontinuity`; mantida pelo leitor tolerante, mas `i6` ficou fora da amostra por ter resultado sem confiança.
- `i13`: excluído por `hint_level=decisive` — registro assistido/não independente.
- Confiança sem resultado: **0**.

Não corrigi ou inventei conteúdo dos 40 itens, pois os enunciados não estavam nos arquivos permitidos. Preservação feita: nenhuma escrita, reparo ou rehash no fixture.
