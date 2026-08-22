# T13, T14, T15 — diagnóstico de raciocínio, contraprova, transferência (fixtures ad-hoc)

Classe: T13=C, T14=C, T15=S.

---

## T13 — hipóteses que pedem a mesma intervenção

**Cenário congelado:** duas hipóteses cognitivas candidatas foram levantadas
sobre o mesmo aluno em sessões anteriores (fornecidas como contexto ao
executor, não geradas por ele):

> Hipótese X: "confunde limiar de tempo em estado de mal epiléptico (usa
> 10-15min em vez de 5min)".
> Hipótese Y: "trata convulsão prolongada como emergência só após falha de
> duas medicações, não reconhecendo o marco de 5min como já configurando
> estado de mal".

**Entrada exata:** "Tenho essas duas hipóteses sobre um aluno — dá pra saber
qual delas é a certa, ou preciso testar as duas separado?"

**Comportamento esperado:** reconhece que X e Y pedem a MESMA intervenção de
teste (ambas seriam resolvidas testando se o aluno reconhece o marco de
5 minutos) — combina-as em vez de desenhar dois testes redundantes; OU, se
uma delas for estritamente mais informativa, aplica só a intervenção
mínima necessária.

**Falha bloqueadora:** propõe testes separados e redundantes para X e Y
quando uma única intervenção resolveria ambas.

**Detector:** conta o número de itens de teste propostos — mais de 1 item
quando as duas hipóteses pedem a mesma variável decisiva é sinal de
redundância.

---

## T14 — "faz contraprova curta"

**Estado prévio:** o aluno acabou de estudar o tema de estado de mal
epiléptico (mesmo escopo do T13) nesta sessão.

**Entrada exata:** "Faz uma contraprova curta pra ver se eu realmente
entendi, mas não me diz qual variável você tá testando."

**Comportamento esperado:** estrutura A/B — mesma OPERAÇÃO cognitiva (ex.:
reconhecer o marco de tempo que define emergência), aplicada a um TEMA
diferente do que acabou de ser estudado (ex.: trocar para o marco de tempo
de anafilaxia ou de choque séptico, mantendo a mesma estrutura de decisão) —
sem revelar qual variável está sendo testada.

**Falha bloqueadora:** repete o mesmo conteúdo/tema já estudado (não é
contraprova, é repetição); OU muda a operação cognitiva testada (deixa de
testar reconhecimento de limiar temporal e passa a testar outra coisa,
invalidando a comparação); OU revela explicitamente qual variável está
sendo testada antes da resposta do aluno.

**Detector:** verifica se o tema do item de contraprova é diferente do tema
recém-estudado; busca por texto que nomeie explicitamente "estou testando
X" antes da tentativa do aluno.

---

## T15 — sentinela: "não sei; chutei"

**Entrada exata:** o aluno acerta uma questão de transferência (tema
diferente do estudado, mesma variável decisiva) e declara explicitamente:
"acertei, mas não sei por quê — só chutei essa letra."

**Estado inicial:** sessão em andamento com uma hipótese cognitiva
`candidate` já registrada para este aluno neste conceito.

**Comportamento esperado:** o teste é tratado como **contaminado** — não
conta nem a favor (não confirma/eleva a hipótese) nem contra (não refuta/
rebaixa). A hipótese permanece exatamente onde estava.

**Falha bloqueadora:** usa o acerto-por-chute como confirmação de que o
aluno "já entendeu" (eleva a hipótese/confiança); OU usa a declaração de
chute como evidência de refutação/regressão (rebaixa a hipótese) — nenhum
dos dois é válido quando o próprio aluno relata acerto não fundamentado.

**Detector:** busca por mudança de estado da hipótese (`candidate` →
`confirmed` ou remoção/rebaixamento) imediatamente após este evento
específico — qualquer mudança é falha.
