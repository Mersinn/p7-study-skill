# F-LEDGER-B — raw visível integral

## Metadados do executor

- `surface = Codex`
- `model = gpt-5.6-terra`
- `reasoning_effort = high`
- `session_clean = true`
- `history_inherited = false`
- executor: subagente Codex `01a03df4-712e-77c2-925c-10f261780fe3` (Kant)
- snapshot recebido: commit `0d5073cf18593ca5b08af4f545337f190d3fb609`
- skill tree: `418f7dc3bbeac0b5c1676cd4657625bf63086b75`
- entrada congelada: `qualification/fixtures/longitudinal/F-LEDGER-B/input.md`
- estado permitido e gravável: `qualification/fixtures/longitudinal/F-LEDGER-B/.p7-state/`
- nenhum relatório, adjudicação ou histórico da auditoria foi fornecido

## Turno 1 — entrada do aluno

> Voltei para revisar. O que está pendente pra mim hoje?

## Turno 1 — saída do executor

> Hoje não há revisão vencida. Sua próxima revisão sobre indicações do Plano C está prevista para 18/09. Vamos antecipar: em que situação clínica você indicaria o Plano C? Responda antes de eu corrigir.

## Turno 2 — entrada do aluno

> Desidratação grave, especialmente incapacidade de beber ou alteração do sensório, indica Plano C com reidratação venosa. Confiança 80%.

## Turno 2 — saída do executor

> Correto. Você identificou o pivô e a conduta: desidratação grave, com sinais como incapacidade de beber ou alteração do sensório, indica Plano C com reidratação venosa.
>
> Registrei como recuperação independente, correta e robusta, com confiança de 80%. A persistência foi confirmada por releitura estrita e validação do ledger.

## Verificação independente pós-sessão

```text
valid ledger: 8 events
events before: 6
events after: 8
final events.jsonl sha256: 4726ea3931f109d244150518e38257596fb2d2a541936e856a6131f7a6848721
learner_id: learner:fixture-t22
new event types: confidence_recorded, review_completed
new interaction_id: i4
new review parent: event:f-r2
```

Adjudicação: `PASS`. A sessão não alegou revisão vencida: em 16/09 a próxima
data projetada era 18/09. O PASS cobre retomada fiel, recuperação ativa,
append encadeado e persistência verificada; não cobre uma falsa alegação de
item vencido.
