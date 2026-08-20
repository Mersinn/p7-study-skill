# AULA VIVA — capturar a aula enquanto ela ainda está quente

> "Não me resuma a aula. Descubra o que essa aula mudou no meu mapa."

## 1. O que é, e por que é o inverso do Estudar Tema

`Estudar Tema` parte do que já está organizado: cápsula → fonte → pivô.
**Aula Viva parte do que ainda não está.**

O aluno acabou de sair de uma aula. Ele traz slides, anotações, uma transcrição
parcial, ou simplesmente conversa sobre o que foi dado. A skill **não** responde
com o resumo do tema. Ela pergunta, internamente:

> Que informação nova apareceu aqui, e o que ela muda no mapa?

## 2. Gatilhos

- "acabei de ter aula de X"
- "a professora falou muito de Y"
- "tive aula hoje, vou te contar"
- aluno cola anotação de aula, foto de slide, ou transcrição
- "o professor insistiu em..."

Não ative para "estudar tema X" — isso é o outro modo.

## 3. As quatro lentes

Processe a aula por quatro lentes **separadas**. Não as funda: a força do modo
está em manter fato médico, ênfase do professor, sinal de prova e reação do aluno
como camadas distintas.

### Lente médica — o que é conteúdo
O conteúdo clínico propriamente dito. Sujeito às mesmas regras de sempre:
`SOURCE_POLICY.md` e `MEDICAL_SAFETY_LAYER.md`. Ênfase de professor **não**
transforma afirmação errada em correta.

### Lente curricular — o que ESTE professor fez com o tema
O que ele enfatizou, aprofundou, repetiu, tratou de passagem, ou **ignorou de
propósito**. "Não quero que decorem a classificação antiga" é sinal curricular
forte — significa que o peso migrou para outra coisa.

### Lente de avaliação — o que tem arquitetura de cobrança
Marcadores que a experiência mostra virarem questão:

- "isso é importante" / "isso cai" / "prestem atenção aqui";
- comparação entre duas entidades próximas;
- algoritmo ou fluxograma;
- exceção a uma regra;
- **threshold numérico** dito em voz alta;
- caso clínico apresentado em aula.

Cruze com `00_MAPA_OPERACAO_MOVIMENTO.md`: se a ênfase for de `sequência` ou
`prioridade`, o item provável é **operacional**, e o treino muda.

### Lente pessoal — o que o aluno demonstrou
Onde ele hesitou, perguntou, associou errado, ou já sabia. Aqui vale a regra do
silêncio (`QUESTION_INTELLIGENCE_P7.md` §8): não afirme que ele não sabia algo
só porque não comentou. Use o que ele **produziu**.

## 4. Saída — o delta, não o resumo

```text
Aula: <tema> · <disciplina/subárea> · <professor, se souber> · <data>

Sinal curricular forte:
Sinal de banca:
Mudança de prioridade:
Pontos que exigem a fonte original:
O que isso muda na cápsula existente:
Treino recomendado:
Incerto / a confirmar:
```

**`O que isso muda na cápsula existente` é obrigatório** e tem três formas:

- `acrescenta` — informação nova, não conflitante;
- `corrige` — o professor contradiz a cápsula. Camada A vence: registre a
  divergência com as duas versões;
- `reprioriza` — o conteúdo já estava lá, mudou o peso.

Nunca sobrescreva a cápsula inteira com a aula nova. O formato é sempre
**o que já sabíamos → o que esta aula acrescentou → o que continua incerto**.

## 5. O artefato CLASS_DELTA

Ao final, ofereça gerar um arquivo:

```
capsules/_deltas/CLASS_DELTA_<disciplina>_<tema>_<AAAA-MM-DD>.md
```

com os campos acima mais as questões geradas e o próximo teste.

Ele é **aditivo e versionado**. Não entra no manifesto, não recalcula prioridade,
não vira fonte — vale a mesma anti-circularidade das cápsulas
(`CAPSULE_GENERATION_POLICY.md` §5).

Só gere o arquivo se o aluno confirmar. Aula sem sinal novo não merece artefato.
Se o ambiente tiver registro canônico de ocorrências, indexe o delta nele e ligue
o próximo teste a um `review_task_id`. Sem índice/ledger acessível, declare que o
arquivo não será retomado automaticamente em outra sessão; nunca finja memória.

## 6. Ocorrência × tópico canônico

Distinção que sustenta o modo:

> Pré-eclâmpsia não "pertence ao P6". Ela é um **tópico canônico**.
> O que pertence ao semestre é a **ocorrência**:
> tópico → período → disciplina → professor → aula → profundidade → prova.

Por isso o conhecimento médico do P6 continua válido no P7 sem que uma skill
chame a outra. O que muda entre períodos não é o fato clínico — é a ocorrência
dele: quem ensinou, com que profundidade, e como cobrou.

Ao registrar um delta, registre a **ocorrência**, nunca o tópico como se ele
tivesse nascido agora.

## 7. Limites

- Aula Viva **não** grava em banco. Ele escreve markdown; nada é automático.
- Ênfase do professor eleva **evidência de cobrança**, nunca **autoridade médica**.
  Se ele disser algo clinicamente errado, a lente médica corrige e a lente
  curricular registra que ele disse.
- Aula sem material e sem anotação gera delta fraco — diga isso em vez de inflar.
- Não invente o que o professor falou a partir do tema. Se o aluno não contou,
  não aconteceu.

## 8. Integração

- delta de conteúdo → cápsula do tema (`CAPSULE_INDEX.md`)
- sinal de banca → `00_MAPA_OPERACAO_MOVIMENTO.md` e `00_EXAM_BLUEPRINT.md`
- treino gerado → `SIMULATION_PROTOCOL.md`
- hesitação do aluno → `CONTRAPROVA_DIAGNOS.md`
- data da aula → `00_CALENDARIO_2026_2.md`
