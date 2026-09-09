# Pattern Analyzer — fronteira canônica v1

> **Status:** contrato comportamental da skill. Define a interface que um futuro
> MedPattern pode consumir; não afirma backend, banco, API, analytics ou
> persistência implementados.

## 1. Invariante nuclear

O Diagnos compara:

> `operation_required(item) × learner_movement(attempt | observed_evidence)`

Em linguagem de domínio, a mesma relação é
`operação_exigida(item) × movimento_candidato(tentativa)`: o segundo termo é
uma hipótese sustentada por evidência observada, nunca leitura direta da mente.

`operation_required` pertence ao item e não muda entre alunos. O lado do aluno
só pode ser sustentado por sinais presentes na tentativa, trajetória ou
transferência. Resposta, justificativa e confiança declarada são observações;
o rótulo taxonômico do movimento é uma **inferência** sobre essas observações.

Por isso, a saída normal é `movement_candidate` ou `indeterminate`, nunca uma
leitura direta da mente do aluno. Uma tentativa isolada (`N=1`) tem teto
`candidate`/confiança baixa.

Tema, dificuldade, frequência na prova, ênfase da professora e validade clínica
não são movimentos do aluno.

## 2. Domínios ortogonais

| Domínio | Pergunta | Pode provar movimento pessoal? |
|---|---|---|
| **Item / Question Intelligence** | O que o item exige? | Não; fornece o contrato objetivo e o contexto. |
| **Evidência curricular/faculty** | O que foi ensinado ou cobrado, por qual fonte? | Não. |
| **Validade clínica** | O claim está vigente para prática atual? | Não; governa o escopo da chave e da inferência. |
| **Evento do aluno** | O que foi realmente respondido, escrito, declarado ou transferido? | Sim, quando o sinal é elegível. |
| **Learner State** | Qual movimento é compatível com os eventos? | É inferência pessoal, privada e falsificável. |

Nunca use recorrência curricular para aumentar recorrência pessoal. Nunca use
artefato derivado — card, cápsula, projeção ou recomendação — como nova evidência
do evento que o gerou.

## 3. Contrato objetivo do item

### 3.1 IDs estáveis de operação

Os rótulos humanos podem ser traduzidos; estes IDs de integração não mudam:

| `operation_id` | Rótulo P7 |
|---|---|
| `OP_RECOGNIZE_DIAGNOSIS` | reconhecer diagnóstico |
| `OP_INITIAL_MANAGEMENT` | conduta inicial |
| `OP_DEFINITIVE_MANAGEMENT` | conduta definitiva |
| `OP_INITIAL_EXAM` | exame inicial |
| `OP_BEST_EXAM` | melhor exame |
| `OP_DIFFERENTIATE` | diferenciar próximos |
| `OP_IDENTIFY_COMPLICATION` | identificar complicação |
| `OP_APPLY_CRITERION` | aplicar critério |
| `OP_PRIORITIZE_EMERGENCY` | priorizar emergência |
| `OP_INTERPRET_IMAGE_ECG_LABS` | interpretar imagem/ECG/laboratório |
| `OP_RECOGNIZE_CONTRAINDICATION` | reconhecer contraindicação |
| `OP_COMPARE_FUNCTION` | comparar função |

`natureza_da_demanda: factual | operacional | mista` descreve a demanda do item. Não
diagnostica a causa do acerto ou erro.

### 3.2 Variável decisiva tipada

`tipo_discriminador` usa o enum:

`fato | valor | limiar | função | sequência | prioridade | contraindicação |
sinal-achado`

Registre a variável que efetivamente separa as opções. Se o item exigir mais de
uma variável material, preserve a combinação; não invente um pivô único.

### 3.3 Mapa distrator 1:N

`distractor_map` é `alternativa_errada → [movement_candidate, ...]`. Um
distrator pode ser compatível com mais de uma explicação; alternativa sem
mapeamento específico recebe lista vazia.

O mapa só é elegível quando o item é válido e a ligação entre alternativa e
movimento é específica. Distrator isolado:

- gera, no máximo, `candidate`/confiança baixa;
- preserva explicações concorrentes;
- não transforma ausência de justificativa em evidência negativa;
- nunca produz `confirmed`.

## 4. Envelope observado × inferido

Uma integração pode renomear campos para o idioma da aplicação, mas deve manter
os blocos e os significados separados:

```json
{
  "contract_version": "p7-pattern-v1",
  "question_analysis": {
    "operation_id": "OP_INITIAL_MANAGEMENT",
    "natureza_da_demanda": "operacional",
    "variavel_decisiva": "",
    "tipo_discriminador": "sequência",
    "validade_do_item": "full",
    "distractor_map": {},
    "source_id": null,
    "claim_id": null,
    "curricular_frame": null,
    "clinical_validity": "not_applicable",
    "answer_key_scope": "reasoning_only"
  },
  "observed_event": {
    "event_id": null,
    "initial_answer": null,
    "final_answer": "",
    "changed_answer": null,
    "raw_justification": null,
    "learner_confidence_before_feedback": null
  },
  "learner_inference": {
    "inference_scope": "reasoning_operation",
    "movement_candidates": [],
    "evidence_event_ids": [],
    "evidence_supporting": [],
    "evidence_opposing": [],
    "alternative_explanations": [],
    "hypothesis_status": "indeterminate",
    "attempt_movement_confidence": "insuficiente",
    "metacognitive_validity": "evidencia_insuficiente"
  }
}
```

Campo não capturado permanece `null`. Não reconstrua resposta inicial,
justificativa, troca de resposta, confiança pré-feedback ou latência. Em fluxo
copiar-colar, latência por questão não existe.

Toda hipótese deve citar sinal positivo observado e, quando houver IDs de evento,
apontar os `evidence_event_ids` correspondentes. Texto bruto não vira campo
inferido; interpretação não vira observação.

## 5. Evidência, estado e confiança

Estados de hipótese:

`candidate | confirmed | weakened | abandoned | indeterminate`

Gates v1:

- `N=1` → no máximo `candidate`/baixa; sem sinal específico → `indeterminate`;
- padrão de bloco → exige numerador, denominador e ao menos três rastros
  observados em itens independentes; teto `candidate`/moderada;
- `confirmed` → pelo menos duas evidências independentes em itens/contextos
  distintos, incluindo uma transferência válida da mesma operação em outro
  conteúdo;
- item ambíguo ou insuficiente, pista decisiva, chute ou falta de conteúdo que
  contamine o teste não confirma nem refuta;
- marcadores conflitantes e hipóteses sem discriminador entre si →
  `indeterminate`;
- casos sintéticos, reconstruções históricas e respostas geradas não contam como
  recorrência ou aprendizagem humana.

Qualificação comportamental usa sessão sem histórico da auditoria e sem chave
oculta; o executor recebe somente skill, entrada congelada e arquivos permitidos.

Ausência de menção nunca prova ausência de operação. A alternativa marcada, uma
justificativa explícita, a trajetória da resposta e uma transferência real podem
ser sinais; o silêncio não pode ser convertido em déficit.

### 5.1 Eixos que não podem ser colapsados

- `attempt_movement_confidence` — força da hipótese nesta tentativa; na skill,
  corresponde à confiança diagnóstica;
- `learner_pattern_confidence` — força longitudinal, somente com eventos
  independentes da sessão ou de ledger real;
- `cohort_pattern_confidence` — força de agregado de turma; pertence ao futuro
  MedPattern, não à skill;
- `learner_confidence_before_feedback` — segurança declarada pelo aluno antes do
  feedback;
- `metacognitive_validity` — elegibilidade do evento para inferência.

As três primeiras usam `insuficiente | baixa | moderada | alta`; a confiança do
aluno segue a escala calibrada do P7. `hypothesis_status` é estado de evidência,
não outra confiança. Se software calcular confiança, a política deve ser
versionada e auditável; o modelo pode propor evidências e candidatos, mas não
conceder a si mesmo `confirmed`.

## 6. Gate curricular e clínico

Preserve separadamente:

- `source_id` e `curricular_frame` — proveniência curricular/faculty;
- `claim_id` e `clinical_validity` — `current | pending | historical_only |
  conflict | quarantined | not_applicable`;
- `answer_key_scope` — `curricular | clinical_current_practice |
  reasoning_only`;
- `inference_scope` — `curricular_performance | clinical_current_practice |
  reasoning_operation | none`.

Um claim `pending`, `historical_only`, `conflict` ou `quarantined` pode sustentar
uma chave explicitamente curricular. Nesse caso, o resultado mede
`curricular_performance`, não prática clínica vigente.

Se o item pergunta conduta atual e o claim decisivo não é `current`, a chave não
é elegível para inferir erro clínico do aluno: corrija ou reescopo o item e use
`inference_scope: none`. Uma inferência de `reasoning_operation` só é permitida
quando o claim não vigente não determina nem contamina a operação, o
discriminador ou a resposta correta.

Quarentena curricular nunca é promovida silenciosamente a verdade clínica.

## 7. Schema guard obrigatório

Antes de emitir ou ingerir a inferência, o guard aplica estas regras:

1. `operation_id` ou `tipo_discriminador` fora do enum → rejeitar a análise do
   item para integração; não adivinhar o valor.
2. Movimento fora do catálogo vigente → remover o candidato e usar
   `indeterminate`, preservando descrição livre apenas como nota não agregável.
3. Candidato sem sinal positivo observado → remover o candidato e usar
   `indeterminate`.
4. Evento metacognitivamente inelegível → remover candidatos e usar
   `indeterminate`.
5. `N=1` acima de baixa → rebaixar para baixa; `confirmed` sem o gate de
   independência e transferência → rebaixar para `candidate`.
6. Campo observado ausente → manter `null`; nunca preencher por inferência.
7. Claim não vigente usado como `clinical_current_practice` → bloquear a
   inferência clínica e exigir correção ou reescopo do item.

Na skill, essas regras são uma checagem comportamental antes da resposta. Num
backend futuro, devem ser validação determinística, não mera instrução ao modelo.

## 8. Skill v1 × futuro MedPattern

### A skill faz agora

- caracteriza operação, demanda, variável decisiva, discriminador, validade e
  distratores do item;
- registra apenas sinais realmente disponíveis na sessão;
- produz hipótese candidata ou abstém;
- relata padrão de bloco somente quando os gates v1 forem satisfeitos;
- usa ledger apenas quando ele existe, está vinculado e é realmente acessível,
  conforme `LEARNER_STATE_PROTOCOL.md`.

### A skill não afirma nem constrói

Backend, banco, API, dashboard, radar, heatmap, correlação, perfil de turma,
motor estatístico, promoção automática de taxonomia ou memória entre sessões.

### Um futuro MedPattern pode fazer

Projeções longitudinais e agregadas sobre eventos validados. Cada saída deve
declarar população, janela, filtros, inclusão/exclusão, numerador, denominador e
contaminações. Deve distinguir `not_trained`, `missing_data` e erro observado.
Percentual sem numerador/denominador é proibido; correlação não prova causa;
recorrência curricular não vira recorrência pessoal.

## 9. Fontes normativas detalhadas

- item, operação, distratores e regra do silêncio →
  `QUESTION_INTELLIGENCE_P7.md`;
- estados, confirmação, ledger e transferência →
  `LEARNER_STATE_PROTOCOL.md`;
- alinhamento curricular e proveniência → `SOURCE_POLICY.md`;
- vigência e quarentena clínica → `MEDICAL_SAFETY_LAYER.md`.
