# Red team clínico cego — execução e limite

> **Fechamento supersessor (2026-08-26):** 32/32 ocorrências revisadas; 9 findings
> materiais reparados em dois ciclos. As 6 ocorrências inconclusivas não foram
> convertidas em PASS: os claims foram rebaixados de `current` para `quarantined`.
> Amostra final: 36 linhas, SHA
> `07e5a9ca13fbcd4b1dec2c8bda8c3c2fbbb972790faa85ad2c7aa389380c7bee`.

**Estado:** `INCONCLUSIVE` — nenhuma conclusão clínica do revisor foi produzida.

## Contrato da amostra

A amostra estratificada foi construída por
`qualification/tools/build_red_team_sample.py` e congelada em
`qualification/reports/RED_TEAM_SAMPLE.csv`, SHA-256
`2875c9e80570cd917aff09c30f9f7b8b978acc4247a0ebbecb99da454bfb0177`.

- 32 linhas e 19 cápsulas únicas;
- risco: 31 high + 1 low = 32;
- validade: 12 current + 10 quarantined + 1 conflict + 3 historical_panel +
  6 unregistered_pending = 32;
- disciplina: 7 EISA_II + 13 EISCA + 9 EISM + 3 OSCE = 32;
- todos os 11 claims canônicos não atuais foram incluídos.

## Executor isolado

- surface: Codex;
- model: `gpt-5.6-sol`;
- reasoning: `xhigh`;
- session clean: sim;
- history inherited: não;
- agent: `01a03def-b133-7c11-a943-45396790495f` (Nash);
- relatórios e runs anteriores: não fornecidos;
- mutação autorizada: nenhuma.

O executor encerrou antes de emitir achados com:

```text
You've hit your usage limit. Upgrade to Pro, purchase more credits or try again later.
```

Portanto não há P0/P1/P2 adjudicado por esse revisor. Ausência de saída não é
ausência de defeito. O red team clínico independente permanece pendente e não
fecha `critical_claim_sweep`, `p0_zero` ou `p1_high_risk_zero`.

## Evidência local independente que continua válida

A geração determinística da amostra e da cobertura passa e permanece utilizável.
O registry contém 52 claims canônicos: 41 `current`, 10 `quarantined` e 1
`conflict`. Isso não resolve as 3.516 detecções primárias não ligadas a claim,
das quais 2.731 estão em cápsulas de alto risco; ver
`CLINICAL_SWEEP_REPORT.md`. A camada de segurança trata claim crítico ausente do
registry como `pending` e preserva o conteúdo curricular em painel separado.

## Ação exata restante

Executar uma única sessão Sol high/xhigh limpa sobre a mesma amostra/hash quando
houver orçamento de executor. O revisor deve produzir findings reproduzíveis,
sem receber relatórios anteriores. Não substituir por autoavaliação desta
conversa e não misturar com Claude.
