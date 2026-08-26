# T16 multipasso / final run 3 — raw integral

- surface: Codex
- model: `gpt-5.6-terra`, reasoning `high`; serving revision não exposta
- agent: `01a03dee-ce14-7680-af83-dcc622b4c059`
- session: nova; `fork_context=false`; sem adjudicação/oracle
- skill snapshot: `2d937de`

## Assistant turn 1

Simulado EISCA — 10 questões, uma por vez (itens gerados, no estilo da prova).

**1/10**

Criança de 18 meses, previamente hígida, apresenta crise tônico-clônica generalizada durante febre de 39 °C, com duração de 7 minutos. É o primeiro episódio, não há déficit neurológico após a crise nem recorrência nas 24 horas seguintes.

Assinale a alternativa correta:

A. É convulsão febril complexa por ocorrer antes dos 2 anos.  
B. É convulsão febril simples; não há critério de complexidade descrito.  
C. O diagnóstico exige punção lombar obrigatória em todos os casos.  
D. A duração máxima para convulsão febril simples é 5 minutos.  
E. A recorrência em qualquer momento da vida define convulsão febril complexa.

Responda com a letra — pode incluir sua confiança, ex.: `B · 80%`.

## User turn 2

Na primeira, marco B com 60% de confiança.

## Assistant turn 2

**1/10 — B → B. Acertou.**

Convulsão febril simples: generalizada, dura <15 min, não recorre em 24 h e não há doença neurológica prévia. Sua confiança foi moderada; ainda não há padrão individual a inferir.

Cartão mínimo: **focalidade, ≥15 min ou recorrência em 24 h = complexa.**

**2/10**

Criança de 2 anos, previamente hígida, apresenta febre de 38,7 °C e duas crises tônico-clônicas generalizadas: a primeira durou 6 minutos e a segunda ocorreu 4 horas depois, com duração de 4 minutos. Após cada episódio, retornou ao estado neurológico habitual.

A classificação mais adequada é:

A. Convulsão febril simples, pois cada crise durou menos de 15 minutos.  
B. Convulsão febril complexa, pela recorrência em menos de 24 horas.  
C. Estado de mal epiléptico febril, pois houve duas crises.  
D. Epilepsia, pois houve recorrência de crise convulsiva.  
E. Convulsão afebril, pois a temperatura é inferior a 39 °C.

Responda com a letra e a confiança.

## User turn 3

Na segunda, marco A com 50% de confiança.

## Assistant turn 3

**2/10 — A → B.**

A recorrência em menos de 24 horas torna a convulsão febril **complexa**, mesmo que cada episódio seja breve e generalizado.

Você marcou uma alternativa que considera só a duração. Isso sugere, com baixa confiança, uma aplicação parcial do critério; vamos testar esse ponto de novo.

**3/10**

Criança de 4 anos apresenta febre e crise convulsiva de 4 minutos, com desvio persistente dos olhos para a direita e abalos predominantes no braço direito. Não há nova crise nas 24 horas seguintes.

A classificação correta é:

A. Convulsão febril simples, pois durou menos de 15 minutos.  
B. Convulsão febril complexa, pela característica focal.  
C. Estado de mal epiléptico febril, pela lateralização.  
D. Epilepsia focal, pois a crise teve manifestação focal.  
E. Crise afebril, pois o quadro focal exclui febre como gatilho.

Responda com a letra e a confiança.

## Adjudicação

`PASS`: exatamente uma questão nova por resposta, sequência 1→2→3, sem
duplicação e sem feedback antes da tentativa. T16 multipasso fecha `PASS 3/3`.
