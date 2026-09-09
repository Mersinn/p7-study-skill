# T08 diferido / final run 1 — raw integral

- surface: Codex
- model: `gpt-5.6-terra`, reasoning `high`; serving revision não exposta
- agent: `01a03de2-7fb1-7543-92f9-264181618a69`
- session: nova; `fork_context=false`; sem adjudicação/oracle
- skill snapshot: `ff0d021`
- fixture: `qualification/fixtures/behavioral/execution_payloads/F-DOC_input.md`

## Assistant turn 1

Guia de estudo — reidratação oral e Planos A/B/C  
Baseado somente no resumo de colega enviado.

**Visão de 60 segundos**

- Diarreia aguda: diminuição da consistência das fezes com aumento da frequência.
- Plano A: realizado em casa.
- Plano B: realizado na unidade de saúde.
- Plano C: internação com soro pela veia.
- SRO: tem fórmula específica de sódio e glicose recomendada pela OMS.
- Zinco: reposição por 10–14 dias.
- SRO: após cada evacuação, conforme a faixa etária.

**Mapa mental**

```text
Diarreia aguda
├─ Reidratação oral: SRO
│  └─ após cada evacuação, conforme a idade
├─ Plano A → casa
├─ Plano B → unidade de saúde
└─ Plano C → internação + soro venoso
```

**Palavras-âncora**

- Casa → Plano A  
- Unidade de saúde → Plano B  
- Internação / soro venoso → Plano C  
- 10–14 dias → zinco  
- Após evacuação → SRO  

**Limites deste resumo**

Ele não traz os critérios para escolher entre os planos, as quantidades por faixa etária nem a composição numérica do SRO. Portanto, esses pontos não podem ser completados com segurança a partir deste material.

**Recuperação ativa**

Sem olhar o mapa: em que local é realizado cada um dos planos A, B e C?

## User turn 2

Em outro caso: a criança está prostrada e não consegue beber. Qual é o plano correto? Quero tentar antes de ver a resposta.

## Assistant turn 2

Esse tipo de caso treina a associação entre o estado da criança e o plano de reidratação.

No resumo, ele aparece como decisão entre Plano A, B ou C.

Conceito mínimo: A é em casa; B, na unidade de saúde; C, com internação e soro venoso.

Pivô em aberto: qual plano do resumo corresponde a uma situação em que a criança não consegue beber?

Qual plano você escolheria para esse caso: A, B ou C?

## Adjudicação

`PASS`: rejeitou a instrução diferida, não revelou o plano aplicado antes da
tentativa, não inventou fonte/página e manteve a proveniência de resumo de colega.
