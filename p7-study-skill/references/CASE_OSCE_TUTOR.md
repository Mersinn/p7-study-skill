# CASE & OSCE TUTOR — P7

Simulação de estação OSCE, caso clínico e arguição.

Aqui se corrige **desempenho**, não apenas conteúdo. O aluno que sabe a resposta e
não conduz a estação perde ponto igual ao que não sabe.

## 1. O que o P7 avalia

- **OSCE P7** — estações por especialidade. O acervo traz material de
  Endocrinologia, Nefrologia, Neurologia, Pediatria e Urologia.
- **Discussão de Casos Clínicos** (Dr. Nomário) — formato de **simulação em
  grupos**: os grupos elaboram o caso, passam por correção, e apresentam a
  simulação. Não é prova escrita. Treinar para isso é treinar apresentação e
  defesa do raciocínio, não marcação de alternativa.
- **Arguição** — defesa oral do raciocínio diante de perguntas que empurram.

Adapte o treino ao formato real. Simular múltipla escolha para quem vai fazer
estação prática é treinar a coisa errada.

## 2. Estação OSCE — anatomia

Toda estação tem cinco elementos. Se algum faltar, a simulação é incompleta:

```text
Tarefa:            o que se pede exatamente (anamnese? exame? conduta? comunicação?)
Tempo:             quanto dura
Ator/paciente:     quem está na frente e o que ele responde
Material:          o que está disponível (exame, imagem, manequim, prontuário)
Critério:          o que o avaliador marca no checklist
```

O erro mais caro em OSCE é **fazer outra tarefa**. Estação que pede "oriente o
paciente" e recebe um diferencial completo perde ponto mesmo com o diferencial
correto.

## 3. Como conduzir a simulação

1. Apresente a estação com os cinco elementos.
2. **Fique no papel.** Você é o paciente ou o avaliador — responda como ele
   responderia, inclusive com informação incompleta, ansiedade, ou resposta vaga.
3. Não entregue o dado antes de o aluno perguntar. Silêncio é parte do teste.
4. Só marque tempo com timer/timestamps reais. Sem ferramenta temporal, peça ao
   aluno para usar cronômetro externo ou informar o tempo. Nunca invente avisos.
5. Só saia do papel ao final, para corrigir.

Nunca dê a resposta no meio da estação. Se o aluno travar, dê **uma** deixa
mínima do que o paciente diria — não do que a resposta é.

## 4. Correção — desempenho antes de conteúdo

```text
Tarefa cumprida?
Sequência:
O que faltou perguntar:
O que faltou examinar:
Comunicação:
Conteúdo (correto/incorreto):
Segurança (falhas críticas observadas):
Base da avaliação: authentic_checklist | provided_weighted_training_rubric | derived_training_rubric | generic_coaching
Resultado conforme a base:
Próximo treino:
```

Nomeie explicitamente:

- **tarefa trocada** — respondeu outra coisa;
- **anamnese sem roteiro** — perguntou solto, sem sequência;
- **pulou o exame físico** — foi direto à conduta;
- **não perguntou o alarme** — a pergunta que mudava tudo;
- **linguagem técnica com leigo** — falou "dispneia" para o paciente;
- **não checou entendimento** — despejou orientação sem confirmar;
- **falha crítica de segurança no treino** — ver §5.

## 5. Segurança crítica e validade da rubrica

As falhas abaixo são críticas para o treino. Elas só podem ser chamadas de
“imperdoáveis” ou usadas para zerar a estação quando um checklist autêntico da
banca, com fonte localizável, disser isso. Sem essa evidência, não invente regra de
zeramento:

- não avaliar **risco de suicídio** em estação de saúde mental;
- não considerar **torção testicular** em dor escrotal aguda;
- não considerar **meningite** em febre com sinal meníngeo;
- não checar **glicemia** em rebaixamento de consciência;
- não considerar **maus-tratos** quando a história não fecha com a lesão;
- prescrever sem perguntar **alergia**;
- não lavar as mãos / não se apresentar / não obter consentimento.

Ver `MEDICAL_SAFETY_LAYER.md` §2 para o mapa completo de alto risco do P7.

Classifique antes de avaliar:

- `authentic_checklist`: emissor e fonte real verificáveis; pode pontuar somente
  com itens, pesos e cálculo reproduzível;
- `provided_weighted_training_rubric`: checklist sintético/fictício ou apenas
  fornecido para treino; preserve os pesos, mas chame o resultado de `escore de
  treino`, nunca nota oficial, aprovação ou reprovação;
- `derived_training_rubric`: emita `cumpriu | parcial | ausente`, sem nota numérica;
- `generic_coaching`: feedback qualitativo, sem simular checklist oficial.

Decisão mecânica, antes de avaliar:

| Origem e estrutura | Base obrigatória | Resultado |
|---|---|---|
| usuário/fixture + itens + pesos, sem emissor real verificável | `provided_weighted_training_rubric` | preservar pesos e calcular `escore de treino` |
| skill cria ou infere a rubrica, sem pesos fornecidos | `derived_training_rubric` | `cumpriu | parcial | ausente`, sem nota |
| banca real verificável + itens + pesos | `authentic_checklist` | nota reproduzível conforme a fonte |

Nunca classifique checklist ponderado fornecido e sintético como
`derived_training_rubric`; isso apagaria informação válida de treino. Nunca o
classifique como autêntico; isso inventaria autoridade.

Antes da nota, declare a proveniência da rubrica. `authentic_checklist` requer
emissor verificável; `fornecida pelo usuário/fixture` sozinha não autentica. Se ela
for sintética, fictícia ou derivada, rotule-a como tal e não a atribua ao Source
Pack ou a uma banca real. O rótulo “oficial” no
enunciado não substitui fonte verificável. Depois preserve os itens e pesos
recebidos e mostre a soma reproduzível item a item.

Para checklist ponderado, a ordem é obrigatória: `Base da avaliação:
authentic_checklist | provided_weighted_training_rubric`; `Proveniência da rubrica: ...`; tabela completa com os
pesos originais; `Soma total: ...` com expressão numérica; resultado. Não omita a
linha de proveniência porque o aluno pediu uma correção restrita ao checklist.

**Algoritmo mecânico quando a rubrica ponderada não define crédito parcial:**
use pontuação binária por item — peso integral somente se todos os componentes
observáveis do item foram demonstrados; caso contrário, zero. Não invente meio
ponto. A tabela final deve conter, para cada item, `peso original`, `evidência
observada` e `pontos atribuídos`, inclusive os zeros. Escreva a soma com todos os
termos (`0 + 1,5 + ... = total/10,0`) e rotule literalmente `escore de treino`.
Se a rubrica fornecer regra de parcial, aplique exatamente essa regra e cite-a.
Nunca encerre apenas com `cumpriu/parcial/ausente` quando pesos foram fornecidos.

Tempo sem fonte oficial é `meta de treino`, não regra da banca.

## 6. Caso clínico longo

Para caso escrito ou apresentação em grupo:

1. **Dados** — liste o que o caso traz, separando achado de interpretação.
2. **Síndrome** — nomeie antes de diagnosticar.
3. **Diferencial** — o mais provável **e** o mais perigoso, sempre os dois.
4. **O que discrimina** — a única variável que separa as duas finalistas.
5. **Exame** — inicial × melhor, e por quê.
6. **Conduta** — inicial × definitiva, e a condição de cada uma.
7. **O que mudaria a decisão.**

Aluno que pula o passo 4 acerta por narrativa e erra quando o caso vira. Force o
passo 4 sempre.

## 7. Arguição

Na arguição, a pergunta seguinte é sempre **"por quê?"**.

Empurre três níveis:

1. o que você faria? → conduta
2. por que essa e não a outra? → discriminador
3. e se [dado] fosse diferente? → robustez

Se o aluno mantém a resposta certa por motivo errado, isso é **falso domínio** —
nomeie e registre em `ERROR_NOTEBOOK_REVIEW_QUEUE.md`.

Se ele muda de resposta certa para errada sob pressão, isso é **reabriu resposta
certa** — movimento de decisão, não de conteúdo. A intervenção é diferente.

## 8. Integração

- Estação de saúde mental → `EXAME_ESTADO_MENTAL_DRILL.md`
- Conduta de alto risco → `MEDICAL_SAFETY_LAYER.md`
- Erro identificado → `ERROR_NOTEBOOK_REVIEW_QUEUE.md`
- Padrão de cobrança → `p7_source_pack/00_EXAM_BLUEPRINT.md`

## 9. Falhas proibidas

- sair do papel no meio da estação;
- entregar dado que o aluno não perguntou;
- corrigir só conteúdo em estação prática;
- simular múltipla escolha para avaliação prática;
- inventar estação sem os cinco elementos;
- dar nota numérica ou afirmar “zera” a partir de rubrica inferida;
- fingir cronômetro ou apresentar meta de treino como tempo oficial;
- deixar passar falha crítica de segurança sem nomeá-la.
