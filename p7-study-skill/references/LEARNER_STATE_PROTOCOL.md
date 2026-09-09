# Learner State, adaptação e continuidade

## 1. Fronteira do Pattern Analyzer: separação de domínios

`Question Intelligence` descreve a questão: comando, operação exigida, natureza
da demanda, variável decisiva, validade, solução e distratores. É compartilhável
e não contém perfil do estudante. Não altere o Plano A para fazê-lo combinar com
a resposta do aluno.

`Learner State` é pessoal e privado. Ele reúne eventos observados de tentativa,
hipóteses sobre movimentos, intervenções, confiança pré-feedback, revisões e
transferências. Sua unidade diagnóstica é:

```text
operação_exigida_no_item × movimento_observado_na_tentativa
```

A operação vem do contrato objetivo do item. O movimento vem de sinais presentes
na produção ou trajetória do aluno. Acerto, erro, silêncio, dificuldade do item ou
natureza factual/operacional, isoladamente, não revelam o movimento.

Mantenha quatro planos ortogonais:

1. `curriculum_faculty_evidence`: o que foi ensinado, enfatizado ou cobrado;
2. `clinical_validity`: se um claim médico está vigente, histórico, pendente, em
   conflito ou em quarentena;
3. `learner_evidence`: o que este aluno efetivamente fez nesta tentativa;
4. `learner_state`: projeção longitudinal, sempre reconstruível a partir dos
   eventos elegíveis.

Evidência curricular pode priorizar o próximo item. Validade clínica pode permitir,
limitar ou excluir uma inferência. Nenhuma das duas pode aumentar a frequência ou
a confiança de um déficit pessoal: recorrência na aula não alimenta hipótese de
recorrência pessoal.

Nunca grave dado identificável de paciente. Não transforme baixa energia, atraso,
afastamento ou condição de saúde em traço persistente.

## 2. Contrato mínimo do evento

Separe campos observados de campos inferidos. Um evento utilizável pelo Pattern
Analyzer deve preservar, quando disponíveis:

```yaml
learner_event_id: ""
learner_id: ""                 # vínculo pseudônimo e verificável
item_id: ""
attempted_at: ""
observed:
  response_initial: null
  response_final: ""
  justification_excerpt: null  # mínimo necessário; nunca dado de paciente
  changed_response: null
  hint_level: none | nondiagnostic | decisive
  answer_exposed_before_attempt: false
  learner_confidence_before_feedback: null
item_contract:
  operation_required: ""
  demand_nature: factual | operational | mixed
  item_validity: full | partial | ambiguous | insufficient
  movement_detectability: []   # sinais necessários para cada movimento testável
  content_scope: ""
  source_id: ""
  clinical_validity: current | historical_only | pending | conflict | quarantined | not_applicable
inference:
  inference_scope: curricular_performance | reasoning_operation | clinical_current_practice
  movement_candidates: []
  evidence_supporting: []
  evidence_opposing: []
  attempt_movement_confidence: insufficient | low | moderate | high
  exclusion_reasons: []
links:
  parent_event_id: null
  transfer_from_event_id: null
  review_task_id: null
```

Campos ausentes permanecem ausentes; não os complete por plausibilidade. Em especial,
não reconstrua resposta inicial, confiança pré-feedback, justificativa, tempo ou
exposição a pistas.

## 3. Elegibilidade e força da evidência

Antes de contar uma tentativa para uma hipótese de movimento, aplique estes gates
na ordem:

1. **atribuição:** evento vinculado ao aprendiz atual;
2. **validade:** item e gabarito suficientes para o escopo da inferência;
3. **detectabilidade:** o evento contém o sinal exigido para aquele movimento;
4. **não contaminação:** resposta não foi resolvida por gabarito, pista decisiva,
   duplicata conhecida ou intervenção que entregou o discriminador;
5. **especificidade:** o sinal favorece o movimento sobre alternativas plausíveis;
6. **independência:** o evento não é repetição do mesmo rastro já contado.

Se qualquer gate necessário falhar, registre `exclusion_reasons` e não force uma
classificação. `indeterminate` é uma saída válida, não um erro do sistema.

### 3.1 Evidência por tentativa

- distrator especificamente mapeado, sem justificativa, pode gerar apenas
  `candidate` com `attempt_movement_confidence: low`;
- justificativa explícita alinhada ao discriminador pode elevar a confiança da
  tentativa para `moderate`; `high` exige sinal direto e discriminante, como
  trajetória observada completa ou contraprova que separa explicações concorrentes;
- confiança declarada, tempo, acerto ou erro isolados nunca identificam movimento;
- auto-relato obtido após o gabarito é evidência auxiliar e não pode, sozinho,
  exceder `low`;
- sinais conflitantes sem desempate produzem `indeterminate`;
- ausência de justificativa ou de menção não é evidência de ausência de raciocínio.

Uma tentativa isolada (`N=1`) gera, no máximo, `candidate` de confiança baixa.
Nunca a apresente como padrão, tendência, déficit ou traço do aluno.

### 3.2 Independência e transferência

Dois eventos são independentes quando vêm de tentativas separadas e a segunda não
é mero reuso da resposta, do gabarito ou do mesmo discriminador já revelado.
Duplicata, recontagem, retry imediato após feedback e versões isomórficas com a
mesma pista decisiva contam como um único rastro para confiança longitudinal.

`transfer` exige a mesma operação em conteúdo diferente, item válido, recuperação
sem pista decisiva e vínculo explícito por `transfer_from_event_id`. Falta de
conteúdo, chute, reconhecimento após exposição ou claim clínico inelegível torna a
transferência `contaminated`: ela não fortalece nem enfraquece a hipótese.

## 4. Pattern Analyzer — agregação implementável

O Pattern Analyzer recebe somente eventos atribuíveis e o contrato objetivo dos
itens. `source_id`, ênfase da professora, recorrência em prova, dificuldade,
cobertura curricular e `clinical_validity` são contexto; não são evidência de um
traço do aprendiz. Toda hipótese deve apontar IDs de eventos reais.

### 4.1 Saída mínima por hipótese

```yaml
movement_id: ""
operation_scope: []
content_scopes: []
inference_scope: curricular_performance | reasoning_operation | clinical_current_practice
state: candidate | confirmed | weakened | abandoned | indeterminate
pattern_confidence: insufficient | low | moderate | high
supporting_event_ids: []
opposing_event_ids: []
excluded_event_ids: []
exclusion_reasons: {}
eligible_opportunities: 0
supporting_events: 0
observed_errors: 0
coverage_status: unobserved | sparse | observed
previous_state: null
last_updated_at: ""
next_discriminating_test: ""
```

`diagnostic_confidence` é um alias de apresentação para `pattern_confidence`; não
é um segundo cálculo. Sempre exiba numerador, denominador, exclusões e escopo ao
resumir um padrão.

### 4.2 Thresholds e estados

- `indeterminate` + `insufficient`: nenhum sinal específico elegível, sinais em
  conflito ou denominador inadequado;
- `candidate` + `low`: ao menos um evento elegível de apoio; com `N=1`, este é o
  teto;
- `candidate` + `moderate`: ao menos dois apoios independentes, ainda sem cumprir
  o gate de transferência;
- `confirmed` + `moderate`: ao menos dois apoios independentes em itens/contextos
  distintos, sendo pelo menos um uma transferência válida da mesma operação em
  outro conteúdo;
- `confirmed` + `high`: ao menos quatro apoios independentes, em três ou mais
  conteúdos, com duas transferências válidas e sem explicação concorrente forte
  não resolvida;
- `weakened`: nova evidência discriminante contrária reduz uma hipótese antes
  sustentada; preserve `previous_state` e todos os rastros;
- `abandoned`: uma contraprova decisiva falsifica a hipótese, ou duas evidências
  contrárias independentes após teste direcionado superam os apoios restantes.

Confiança nunca sobe por mera passagem do tempo, repetição de fonte, frequência
docente ou quantidade de itens inelegíveis. Um padrão de bloco só pode ser
resumido com numerador, denominador e pelo menos três oportunidades elegíveis;
abaixo disso, reporte os eventos sem linguagem de tendência. Satisfazer um
threshold permite o estado, não obriga a conclusão: explicações concorrentes ou
evidência de baixa especificidade exigem abstenção.

### 4.3 Evolução longitudinal

Atualize por append; nunca reescreva o passado:

```text
evento elegível de apoio
  indeterminate → candidate
apoio independente + transferência válida
  candidate → confirmed
evidência contrária discriminante
  candidate/confirmed → weakened
contraprova decisiva ou duas contrárias independentes
  weakened → abandoned
novo apoio após weakened/abandoned
  reabre como candidate; não restaura confirmed automaticamente
```

Correção após intervenção é novo evento, não apagamento do erro. Registre a
intervenção entre eventos para distinguir evolução espontânea de desempenho com
apoio. `stale`/tempo sem observação pode ser um metadado de recência, mas não é
evidência a favor ou contra e não muda o estado sozinho.

## 5. Cobertura não é erro

Use denominadores diferentes para perguntas diferentes:

```text
desempenho = tentativas corretas / tentativas elegíveis
erro observado = erros reais / tentativas elegíveis
taxa do movimento = eventos que sustentam o movimento /
                    oportunidades em que esse movimento era detectável
cobertura = temas/operações com tentativa elegível / escopo declarado
```

Não use `itens atribuídos`, `aulas dadas`, `slides existentes` ou `questões em que
o aluno não respondeu` como denominador de erro pessoal. `coverage_status:
unobserved` ou `sparse` significa falta de observação, não falha.

Regras duras:

- frequência da professora, recorrência em provas e peso curricular priorizam o
  que testar; nunca viram frequência pessoal de erro;
- tema ainda não treinado, não coberto ou sem tentativa elegível é lacuna de
  cobertura, nunca déficit de conteúdo ou raciocínio;
- dificuldade prevista do item não altera o número de erros observados;
- erro em gabarito curricular histórico mede `curricular_performance`, não
  `clinical_current_practice`;
- item de conduta vigente apoiado em claim `historical_only`, `pending`,
  `conflict` ou `quarantined` não pode produzir déficit clínico pessoal nem
  inferência de prática atual; corrija a validade ou reescopo para histórico;
- claim não atual nunca sustenta “o aluno não sabe a conduta atual”;
- material da turma ou frequência de coorte não é evidência sobre este aluno.

O resumo correto para baixa cobertura é `ainda não observado/testado`, seguido do
próximo teste discriminante. Não use “fraqueza”, “déficit” ou “não domina”.

## 6. Eixos de confiança não intercambiáveis

- `attempt_movement_confidence`: força da inferência de movimento em uma tentativa;
- `pattern_confidence` / `diagnostic_confidence`: força da hipótese longitudinal;
- `learner_confidence_before_feedback`: previsão do aluno — `0 | 25 | 50 | 75 |
  100`, coletada antes do feedback quando ele aceitar o modo calibrado;
- `item_validity` e `clinical_validity`: gates de elegibilidade, não confiança do
  aluno nem do padrão;
- `coverage_status`: quantidade de observação, não certeza diagnóstica.

Não propague automaticamente um eixo para outro. Tentativa de alta confiança não
confirma padrão; aluno muito confiante não torna o diagnóstico mais certo; fonte
forte não transforma ausência de tentativa em déficit. Nunca descreva confiança
diagnóstica como “você estava confiante”.

Sem confiança pré-feedback não há medida de calibração. Com menos de 10 tentativas
válidas, mostre apenas acertos/confianças brutos e `amostra insuficiente para
calibração agregada`. Com `n >= 10`:

```text
p = learner_confidence_before_feedback / 100
y = 1 se correto, 0 se incorreto
Brier = media((p - y)^2)
vies = media(p - y)
```

Informe `n`, fórmula, linhas excluídas e bins. Brier menor é melhor; viés positivo
sugere excesso de confiança e negativo, subconfiança. Não diagnostique traço
pessoal com esse escore.

## 7. Dificuldade adaptativa — default

O primeiro item depende de `starting_level`:

- `zero`: mapa mínimo → worked example → item isomórfico com pistas;
- `parcial`: diagnóstico curto → completar lacuna → item com apoio moderado;
- `revisao`: pivô/teste direto, sem aula introdutória.

Depois, adapte por desempenho observável:

- erro + confiança alta → priorize Contraprova ou diferencial próximo;
- erro + confiança baixa → microexplicação + item guiado da mesma operação;
- dois erros seguidos → aumente apoio ou reduza uma dimensão de dificuldade;
- acerto + confiança baixa → acerto frágil; mantenha dificuldade e revise em 48h;
- dois acertos independentes, um atrasado ou em transferência → reduza pistas ou
  aproxime distratores;
- erro de conteúdo não aumenta complexidade; erro operacional recebe transferência
  em outro tema.

Mude uma dimensão por vez: apoio, distância entre distratores, número de etapas ou
novidade do contexto. Diga brevemente por que mudou. Adapte ao evento observado;
não apresente hipótese `candidate`, tema não treinado ou baixa cobertura como
déficit estabelecido.

## 8. Ledger, privacidade e persistência honesta

O estado vale apenas na conversa atual, salvo se um ledger foi realmente criado,
está acessível e está vinculado ao aprendiz atual. Persista o mínimo necessário:
ID pseudônimo, contrato do item, resposta, sinal probatório mínimo, intervenção,
confiança pré-feedback, vínculos e timestamps. Prefira locators ou excertos mínimos
a texto livre integral.

Não persista: nome/contato sem necessidade operacional; dado identificável de
paciente; hipótese diagnóstica sobre o próprio aluno; causa presumida de atraso,
baixa energia ou afastamento; informação de saúde; comentário docente sobre outro
aluno; dado de turma convertido em atributo individual. Esses dados também não
podem ser usados como proxy de movimento.

Nova sessão:

1. valide `learner_id` contra o vínculo/escopo fornecido pela sessão; ausência de
   vínculo verificável produz `histórico não atribuível`, e mismatch nunca é
   retomado automaticamente;
2. se houver ledger vinculado, leia vencidos e hipóteses abertas antes de gerar
   novos itens;
3. crie um novo `learner_event_id` ligado ao evento anterior e atualize/complete o
   mesmo `review_task_id` quando for a mesma tarefa; não sobrescreva tentativa;
4. se não houver, diga `sessão sem histórico` e peça o ledger ou ofereça revisão
   genérica rotulada;
5. nunca alegue lembrar outra conversa sem mecanismo real;
6. só confirme `salvo/registrado` após append, releitura estrita e presença do novo
   evento com hash/parent válidos. Se for legível mas read-only, declare
   explicitamente `histórico lido; atualização não persistida`.

Eventos são imutáveis; correções viram novos eventos ligados ao anterior. Estado de
domínio, hipóteses e fila são projeções reconstruíveis, não fatos sobrescritos. Não
misture ledgers, identidades ou agregados de coorte. Se a atribuição for perdida,
interrompa a personalização longitudinal sem apagar a possibilidade de estudo
genérico na sessão.

## 9. Scheduler 48h → 7d → 21d por resultado

- erro, chute, acerto frágil, pista decisiva ou reconhecimento sem recuperação →
  `48h`;
- na revisão de 48h, resposta correta, independente e com confiança compatível →
  `7d`; caso contrário, volta a `48h` e muda a intervenção;
- em 7d, nova recuperação independente correta, preferencialmente em transferência
  → `21d`; caso contrário, `48h`;
- em 21d, acerto robusto → arquive do bloco ativo ou mova para manutenção conforme
  risco; erro → `48h`.

Tema de alto risco pode ter manutenção mensal, mas não fica eternamente na fila
ativa. Selecione lote finito por `vencimento × risco × fragilidade pessoal` e pelo
tempo disponível. Não tente revisar toda fila.

## 10. Retomada e saída

Ao retomar, mostre somente: itens vencidos selecionados · hipótese aberta relevante
· intervenção anterior · próximo item. Ao encerrar, diga se o registro existe só na
conversa ou foi efetivamente persistido e forneça o próximo vencimento calculado.
