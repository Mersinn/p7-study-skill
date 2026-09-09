# F-CAL — Escopo e calendário (fixture congelada)

**Uso:** T01. **Classe do teste:** C.

## Entrada exata a fornecer ao executor (verbatim, sessão limpa)

> Minha prova de EISM (Saúde Mental) é em 48 horas. Cai a II unidade inteira.
> Tenho 90 minutos por dia de estudo até lá. Monta meu plano.

## Estado inicial

- Sessão nova, sem histórico de ledger fornecido.
- Nenhum arquivo anexado — o executor deve trabalhar só com o texto acima e o
  Source Pack embarcado da skill.
- "II unidade" de EISM no Source Pack corresponde às cápsulas cujo campo
  `Unidade` é `UNIT_2` — o executor NÃO recebe essa lista pronta; extrair a
  lista real é parte do que o teste avalia (o plano deve refletir cápsulas que
  genuinamente existem na unidade certa, não uma lista inventada).

## Comportamento esperado (critério de aprovação)

- Usa os dados fornecidos (48h, II unidade, 90 min/dia) para dimensionar o
  plano — não produz um plano genérico "estude aos poucos".
- Declara explicitamente o que está DENTRO e o que está FORA do escopo (ex.:
  "isto cobre X cápsulas da II unidade; Y ficou de fora por falta de tempo,
  priorizado por Z").
- Inicia already o primeiro bloco de estudo (não só entrega um cronograma e
  para) — "declara exclusões/parada e inicia bloco" por texto do critério.
- Orçamento de tempo é respeitado: ~2 sessões de 90 min em 48h, não mais.

## Falha bloqueadora

- Repete a mesma pergunta/tema mais de uma vez dentro do plano sem motivo
  declarado (redundância não intencional).
- Excede o orçamento de tempo declarado (ex.: propõe 4h/dia quando o aluno
  disse 90 min) sem justificar e sem alertar o aluno da mudança.

## Detector automatizado

- Contagem de minutos/blocos propostos vs. 90 min × número de dias até 48h;
  sinaliza se exceder por >15%.
- Verificação de que cápsulas citadas no plano existem de fato em
  `capsules/EISM/` com `Unidade: UNIT_2` (contra falso escopo).
