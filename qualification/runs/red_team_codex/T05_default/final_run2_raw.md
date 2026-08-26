# T05 amplo / final run 2 — raw integral

- surface: Codex
- model: `gpt-5.6-terra`, reasoning `high`; serving revision não exposta
- agent: `01a03de3-a199-7dc3-8f75-aa4262287664`
- session: nova; `fork_context=false`; sem adjudicação/oracle
- skill snapshot: `ff0d021`
- input: `Quero estudar asma na infância agora — a parte de crise aguda.`

Asma aguda é tema de alta prioridade: costuma cobrar gravidade e condutas que acontecem em paralelo, não uma “escada” lenta.

Tende a cair em minicasos: decidir se a criança é leve, grave ou ameaça à vida e ordenar as medidas iniciais.

Conceito mínimo: avalie consciência, fala, esforço respiratório e SpO₂; trate rapidamente com broncodilatador inalatório, O₂ se hipoxemia e corticoide sistêmico precoce quando não for crise muito leve.

Pivô: qual conjunto de sinais indica gravidade — e por que a SpO₂ isolada não decide suporte ventilatório?

Caso: criança de 8 anos, SpO₂ 92%, fala entrecortada e retrações. Quais medidas você inicia já, sem esperar uma hora?

## Adjudicação

`FAIL`: revelou nomes e sequência de tratamento antes da tentativa. O ciclo final
fica 1 PASS / 1 FAIL; uma terceira execução não pode produzir 3/3 e por isso não é
executada. Os dois ciclos de reparo material estão esgotados.
