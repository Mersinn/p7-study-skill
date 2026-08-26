# T16 multipasso / final run 1 — raw integral

- surface: Codex
- model: `gpt-5.6-terra`, reasoning `high`; serving revision não exposta
- agent: `01a03de4-c30e-7fc3-b87a-008480b71b19`
- session: nova; `fork_context=false`; sem adjudicação/oracle
- skill snapshot: `ff0d021`

## User turn 1

Simula 10 questões de EISCA pra mim.

## Assistant turn 1

Vamos de simulado adaptativo: 10 questões geradas no estilo EISCA, uma por vez, com correção após cada resposta.

**1/10 — Neonatologia**

RN a termo, nascido por cesariana eletiva, inicia desconforto respiratório nas primeiras 2 horas de vida. Apresenta taquipneia leve, sem febre, boa perfusão e melhora progressiva nas primeiras 24–48 horas. Radiografia mostra hiperinsuflação pulmonar e líquido nas fissuras interlobares.

O diagnóstico mais provável é:

a) Doença da membrana hialina  
b) Taquipneia transitória do recém-nascido  
c) Pneumonia neonatal precoce  
d) Aspiração meconial  
e) Hérnia diafragmática congênita  

Responda no formato: `1-B · confiança 80%`.

## User turn 2

Na primeira, marco B com 60% de confiança.

## Assistant turn 2

**1. B → B. Acertou.**

O pivô foi: RN a termo, cesárea eletiva, taquipneia precoce e autolimitada, com líquido nas fissuras → **taquipneia transitória do RN**.

- Operação: reconhecer diagnóstico.
- Demanda: operacional.
- Pegadinha: membrana hialina é mais típica de prematuridade e tende a piorar inicialmente.
- Confiança prévia: 60%; acerto válido, mas ainda isolado.

**2/10 — Convulsão febril**

Criança de 18 meses, previamente hígida, apresenta febre de 39 °C e crise tônico-clônica generalizada que dura 8 minutos, sem recorrência nas 24 horas seguintes. Após o evento, recupera-se completamente e o exame neurológico é normal.

Assinale a alternativa **incorreta**:

a) O quadro é compatível com convulsão febril simples.  
b) A duração inferior a 15 minutos favorece a classificação como simples.  
c) A generalização da crise favorece a classificação como simples.  
d) A recorrência de crises no mesmo período de 24 horas é critério de convulsão febril simples.  
e) Não há, pelo caso descrito, sinal de focalidade.  

Responda: `2-D · confiança 80%`.

## User turn 3

Na segunda, marco A com 50% de confiança.

## Assistant turn 3

**2. A → D. Incorreta.** Seu conteúdo estava certo: a alternativa **A** descreve corretamente convulsão febril simples. Porém, o comando pedia a alternativa **incorreta**.

A incorreta é **D**: recorrência em até 24 horas torna a convulsão febril **complexa**, não simples.

- Placar: **1/2**
- Sinal observado: possível troca de comando inverso (“incorreta”) — hipótese de baixa confiança, pois é um único item.
- Regra de prova: em EISCA, “EXCETO/incorreta” é pegadinha muito frequente; circule mentalmente o comando antes de olhar as opções.

**3/10 — Convulsão febril**

Uma criança de 2 anos teve duas crises tônico-clônicas generalizadas de 5 minutos durante o mesmo episódio febril, com recuperação completa entre elas e exame neurológico normal.

Qual achado torna essa apresentação uma **convulsão febril complexa**?

a) Idade de 2 anos  
b) Recorrência de crises em 24 horas  
c) Duração inferior a 15 minutos  
d) Crise generalizada  
e) Recuperação neurológica completa  

Responda: `3-B · confiança 80%`.

## Adjudicação

`PASS`: exatamente uma questão nova por resposta, sequência 1→2→3, correção
somente após cada tentativa, sem duplicação nem feedback de item futuro.
