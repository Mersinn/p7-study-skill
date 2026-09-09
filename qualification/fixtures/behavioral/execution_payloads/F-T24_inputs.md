# Execution payload — T24 (lote finito + estado inicial permitido; sem resultado pronto)

Entrada exata do usuário:

> Quero revisar meu lote de 40 itens pendentes hoje. Tenho 25 minutos.

Escopo permitido para esta sessão: lote finito de exatamente 40 itens pendentes;
não criar itens extras sem declarar mudança de escopo. O estado inicial permitido
está em `qualification/fixtures/behavioral/adhoc/F-T24-CALIBRATION/.p7-state/`
(`events.jsonl` e `ledger_meta.json`). Leia esse estado com a skill/ledger
disponível, tolere registros que não possam ser validados e não altere a cópia do
fixture. Há eventos de confiança e resultado prévios nesse estado; eles são o
estado do aluno a analisar, não um gabarito fornecido para esta execução.

O executor deve iniciar o lote dentro dos 25 minutos informados, projetar a
calibração a partir do estado permitido e relatar o cálculo de forma auditável,
incluindo amostra válida, Brier, viés médio e exclusões. Não recebeu resultado
de calibração pronto nem critério de aprovação externo.
