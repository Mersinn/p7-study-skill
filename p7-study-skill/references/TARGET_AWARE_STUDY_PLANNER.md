# TARGET_AWARE_STUDY_PLANNER — P7

Motor do modo `Plano de Guerra`.

Planejar é **decidir o que fica de fora**. Um plano que cobre tudo não é plano; é
uma lista de desejos que produz paralisia.

## 1. Estado do alvo

```yaml
active_study_target:
  exam_type: prova_unidade | integrada | reposicao | final | osce | casos_clinicos | p7_completo | livre
  discipline_scope: EISA_II | EISCA | EISM | CASOS_CLINICOS | OSCE | MULTI | A_DEFINIR
  especialidade_scope: []        # só EISA_II: Angiologia, Endocrino, Nefro, Neuro, Oftalmo, Onco, Otorrino, Patologia, Uro
  unit_scope: I_UNIDADE | II_UNIDADE | III_UNIDADE | IV_UNIDADE | MULTI_UNIDADE | SEM_UNIDADE | A_DEFINIR
  assessment_period: primeira_prova | segunda_prova | terceira_prova | quarta_prova | integrada | reposicao | final | osce | a_definir
  deadline: ""
  available_time: ""
  starting_level: zero | parcial | revisao | a_definir
  preferred_method: questoes | teoria_ativa | casos | misto | a_definir
  energy_constraint: estavel | variavel | baixa_agora | a_definir
  declared_topics: []
  urgency: low | medium | high | critical
  priority_layer: ""
  source_layer: ""
  stop_condition: ""
  current_phase: ""
  current_block: ""
```

## 2. Como inferir o alvo sem interrogatório

O aluno raramente chega com o alvo formatado. Ele chega assim:

- "tenho integrada em 48h" → `exam_type: integrada`, `urgency: critical`
- "prova de saúde mental sexta" → `discipline_scope: EISM`, prazo curto
- "segunda prova de EISA, só nefro e neuro" → `unit_scope: II_UNIDADE`,
  `especialidade_scope: [Nefrologia, Neurologia]`
- "tô perdido no P7 inteiro" → `p7_completo`, e o trabalho é **reduzir escopo**

Pergunte no máximo **duas** coisas, e só se a resposta mudar o plano. Prazo,
recorte de unidade e tempo realmente disponível mudam o número/tamanho dos
blocos. Infira nível, método e energia quando já estiverem evidentes; faça no
máximo uma pergunta de personalização se ela mudar o primeiro bloco.

Alvo indefinido não bloqueia. Assuma o mais provável, **declare a suposição**, e
comece.

## 3. Urgência governa a profundidade

| Urgência | Prazo | O que entra | O que sai |
|---|---|---|---|
| `critical` | 0–72h | pivôs · regras de prova · provas antigas e devolutivas · minicasos · erros prováveis · distratores frequentes · cards mínimos · simulado curto | fisiologia longa · resumo completo · leitura ampla · tema de baixa prioridade · plano perfeito |
| `high` | 3–7 dias | acima + temas de alta prioridade com fonte forte · simulado por bloco | temas de fonte fraca e baixa cobrança |
| `medium` | 1–3 semanas | cobertura por unidade · cápsulas em ordem de prioridade · revisão espaçada | exaustividade |
| `low` | > 3 semanas | cobertura ampla · construção de base · OSCE e casos | pressa |

Em `critical`, a pergunta não é "o que eu preciso saber?" — é **"o que me faz
perder ponto amanhã?"**.

## 4. Ordem de prioridade dos temas

Prioridade final = função de, nesta ordem de peso:

1. **evidência de cobrança** (`00_EXAM_BLUEPRINT.md`, devolutivas) — cai?
2. **risco clínico** — errar mata? (herda `MEDICAL_SAFETY_LAYER.md` §2)
3. **força da fonte** — dá para estudar bem? (`SOURCE_POLICY.md` §6)

Um tema com fonte média que cai toda prova vence um tema com fonte forte que nunca
caiu. Um tema de risco alto entra mesmo com fonte média — e a fraqueza da fonte é
declarada.

Tema oficial, de alta cobrança ou alto risco com `forca_fonte: ausente` continua
no plano como lacuna/pendência. A força da fonte define a rota:
`pedir_slide | validar_diretriz | conhecimento_geral_rotulado | aguardar_fonte`.
Tema baixo, não oficial e sem fonte pode ficar fora com justificativa.

## 5. Saída do Plano de Guerra

```text
Alvo ativo:
Prazo:
Urgência:
Nível · método · energia:
Prioridade:
Fontes principais:
Plano:
O que fica fora:
Critério de parada:
Próximo bloco:
```

Regras da saída:

- `O que fica fora` é **obrigatório** e não pode ser vazio. Se nada ficou de fora,
  o escopo não foi decidido.
- `Próximo bloco` é uma ação única e imediata, não uma lista. O aluno tem de poder
  começar no segundo seguinte.
- `Critério de parada` é observável ("quando acertar 8/10 dos minicasos de X"),
  não subjetivo ("quando se sentir seguro").

## 6. Recorte por unidade

`00_UNIT_TOPIC_MAP.md` é a **autoridade de escopo** para prova de unidade,
reposição e final. Ele responde "o que cai na II unidade de EISA II".

Regras:

- o mapa de unidade define o escopo; a prioridade da integrada é sinal
  **secundário** e nunca remove um tema listado na unidade;
- `unidade: A_DEFINIR` não bloqueia o estudo — limita a precisão do recorte, e
  isso deve ser dito em uma linha;
- EISCA tem **quatro** provas; as demais têm três. Não presuma simetria.

## 7. Blocos de execução

Quebre o plano em blocos que cabem numa sessão real de estudo:

- bloco = 1 tema (ou 2 se forem irmãos, ex.: hipo/hipertireoidismo);
- cada bloco termina com produção ativa: minicaso, questão, ou card;
- nunca enfileire mais de 3 blocos à frente. O plano se reajusta depois do bloco 3.

Para `energy_constraint: variavel | baixa_agora`, ofereça versão essencial de
20 minutos, extensão opcional de 15–25 minutos, produto observável e parada. Um
plano de 30 minutos não pode ter o mesmo número de blocos de um plano de 3 horas.

Empilhar 15 blocos é o mesmo que não planejar.

## 8. Anti-loop

Quando o aluno abre uma frente nova sem evidência nova:

```text
Este refinamento não muda a decisão para o alvo atual. Fechamos [X] e começamos [Y].
```

Quando a fase está suficiente:

```text
Fase fechada. Próximo passo: [X]. Não reabrir sem informação nova.
```

Reabra com: erro real · dado novo relevante · risco de perda de informação · teste
falhado · mudança de prazo/energia/alvo · ou o aluno dizer que não entendeu.

Redirecione refinamento sem efeito para o bloco atual, sem atribuir intenção,
preguiça ou fuga. Dúvida legítima recebe outra representação e novo teste curto.

## 9. Falhas proibidas

- plano sem `O que fica fora`;
- plano que cobre o P7 inteiro em urgência crítica;
- mais de duas perguntas antes de entregar o primeiro bloco;
- prometer cobertura de tema com fonte ausente;
- critério de parada subjetivo;
- replanejar em vez de executar.
