# CONTRAPROVA DIAGNOS — testar o diagnóstico do erro, não só declará-lo

> "Não me diga só por que eu errei. Tente provar que a sua explicação sobre meu
> erro está certa."

## 1. O problema que este modo resolve

O `Resolver Questão` produz uma hipótese sobre o movimento do aluno. Hoje essa
hipótese **morre ali**: é declarada, o aluno concorda ou não, e ninguém testa.

Isso é exatamente a falha que o piloto controlado Diagnos 1C-A expôs em 2026-07-28.
No cenário S7, o motor afirmou como hipótese líder que o aluno *"não processou o
comando temporal"* — quando o cartão oculto dizia que ele **leu o comando** e apenas
não sabia qual exame era o inicial. O adjudicador nomeou a falha: **conversão de
silêncio em fato**. Foi a única refutação limpa do piloto, e ela aconteceu porque
a hipótese nunca foi submetida a teste.

Contraprova transforma o diagnóstico cognitivo em **hipótese falsificável**.

## 2. Quando ativar

Não é para toda questão. Ative quando:

- há **duas hipóteses concorrentes** que explicam o mesmo erro, e elas pedem
  intervenções diferentes;
- ao menos uma hipótese é de **movimento**; a concorrente pode ser outro
  movimento ou lacuna de conteúdo;
- o mesmo movimento já apareceu antes (`ERROR_NOTEBOOK_REVIEW_QUEUE.md`);
- o aluno discorda do diagnóstico.

Não ative quando o erro é claramente factual e único ("não sabia o valor"), nem
quando não há qualquer sinal observado para formular concorrentes. O estado pode
continuar `INDETERMINADO` durante o teste; testar hipótese sem hipótese é teatro.

## 3. O fluxo

### Passo 1 — a tentativa
O aluno responde. Idealmente com três rastros: **resposta · justificativa ·
confiança**. Sem justificativa ainda funciona (§8.1 do `QUESTION_INTELLIGENCE_P7`):
a alternativa marcada já mapeia movimento em confiança baixa.

### Passo 2 — hipóteses concorrentes internas, não veredito

Antes da segunda tentativa, registre internamente — **não mostre ao aluno**:

```text
Hipótese A: <movement_id> — suporte observado — evidência contra
Hipótese B: <movement_id ou lacuna específica> — suporte observado — evidência contra
Predição exclusiva se A estiver certa:
Predição exclusiva se B estiver certa:
Observação que enfraquece/falsifica A:
Observação que enfraquece/falsifica B:
Contaminadores que tornam a rodada indeterminada:
```

Sem predições diferentes e falsificadores observáveis, não há contraprova: há
apenas outra questão. Nunca escreva "você tem fechamento precoce"; antes do teste,
o aluno recebe somente a sonda do Passo 4.

Se A e B não produzem predições diferentes ou levam à mesma intervenção, distingui-las
não muda a decisão: junte as duas.

**Contrato duro contra redundância:** antes de criar a lista de sondagens,
extraia a variável decisiva de cada hipótese. Se as duas hipóteses são duas
descrições do mesmo limiar, discriminador ou operação (por exemplo, ambas
dependem de reconhecer o marco de 5 minutos), elas formam uma única hipótese
composta para fins de teste. Faça **uma sonda conjunta**, com uma única
pergunta/caso que avalie a variável compartilhada; não divida em “teste de X”
e “teste de Y”. Só proponha duas sondas quando houver duas variáveis
decisivas realmente diferentes. O diagnóstico continua candidato/indeterminado
até haver evidência, mas o desenho não pode desperdiçar duas sondas para o
mesmo discriminador.

### Passo 3 — a menor sonda que discrimina

Não dê aula, card, regra, pista nem intervenção corretiva antes do teste. Selecione
a menor **sonda** que produz resultados diferentes sob A e B. Frequentemente é
uma única pergunta. A intervenção pedagógica vem depois da leitura do resultado.

### Passo 4 — a questão de transferência

Segunda questão com o mesmo `operacao_id` e tema diferente. Registre internamente
o rótulo humano, a variável decisiva e o mapa de distratores conforme
`QUESTION_INTELLIGENCE_P7.md`, mas não os revele antes da resposta.

Tema diferente é o ponto. Se A é "fechamento precoce" e B é "lacuna de conteúdo
sobre pré-eclâmpsia", repetir pré-eclâmpsia não discrimina nada — o aluno pode
acertar por ter acabado de estudar. Outro tema, mesma operação, separa as duas.

**Contrato duro de transferência:** mudar idade, duração, medicação ou detalhes
da mesma doença não muda o tema. Depois de estudar estado de mal epiléptico, por
exemplo, um segundo caso de convulsão/status continua sendo repetição, não
contraprova. Troque para outro tema clínico e preserve somente a operação
(como reconhecer um limiar temporal); não anuncie essa variável antes da
tentativa.

Use o `00_MAPA_OPERACAO_MOVIMENTO.md` para achar um item real com a mesma operação.

Para separar movimento operacional de lacuna factual, prefira item em que o fato
necessário esteja dado no enunciado ou já tenha domínio observado; caso contrário,
o erro não discrimina. Para separar dois movimentos, cada alternativa/traço de
resposta deve corresponder a previsões diferentes no quadro do Passo 2. Se o
conteúdo-base da transferência não estiver assegurado, faça a rodada e marque-a
`indeterminada`; não converta o novo erro em movimento.

Fixe também `answer_key_scope` antes da tentativa. Se a questão pede prática
atual, exija `clinical_validity: current`; material curricular `pending |
historical_only | conflict | quarantined` não serve como controle de conteúdo
clínico. Se o alvo é recordação curricular, declare ao aluno apenas esse **escopo**
antes da questão — sem revelar chave, variável decisiva ou hipótese — e limite a
inferência ao escopo curricular.

### Passo 5 — portão sem revelação

Antes de bloquear a resposta — e, quando coletadas, justificativa e confiança —
não revele: hipótese, `operacao_id`/rótulo, variável decisiva, mapa de
distratores, gabarito, regra, card, dica ou movimento-alvo. Se você anunciar "vou
ver se você fecha cedo", o aluno passa a vigiar exatamente isso e o teste se
contamina.

Diga apenas:

```text
Quero te dar uma segunda questão curta antes de explicar.
```

Só depois de uma tentativa — inclusive `não sei` — revele e corrija:

```text
Eu estava distinguindo entre <A> e <B>.
```

Isso não é manipulação — é cegamento, e é o que torna o resultado interpretável.
Se o aluno perguntar diretamente o que você está testando, **responda a verdade**
e registre que a rodada ficou contaminada; ela pode servir como treino, mas não
fortalece, enfraquece nem confirma movimento.

### Passo 6 — o resultado
```text
Tentativa A: <o que ele fez>
Hipótese testada: <A vs B>
Sonda aplicada: <a menor>
Transferência B: <o que ele fez na segunda>
Resultado por hipótese: strengthened | weakened | abandoned | indeterminate
Confiança atualizada:
Intervenção pós-teste / próximo passo:
```

Regras de leitura do resultado:

- aplique as predições escritas **antes** da sonda; não invente a explicação após
  ver a resposta;
- observou o falsificador de A em rodada limpa → A `weakened` ou `abandoned` para
  aquele evento; isso não prova automaticamente B;
- observou a predição exclusiva de A e o falsificador de B → A `strengthened`, B
  `weakened`;
- ambas as hipóteses predizem o resultado → `indeterminate`; redesenhe a sonda;
- nenhuma prediz o resultado → abandone ambas para o evento e formule novas
  concorrentes apenas com sinal observado;
- errou por não saber o conteúdo, acertou por pista, recebeu revelação precoce ou
  enfrentou item/escopo inválido → `indeterminate` (falha do teste, não do aluno);
- uma rodada não confirma padrão. `confirmed` exige pelo menos duas evidências
  independentes em contextos distintos, sendo ao menos uma transferência válida;
  mantenha `candidate` enquanto isso não existir.

## 4. O que muda no registro

A unidade deixa de ser "errei cardiologia" e passa a ser:

> tentativa A → hipóteses → sonda de transferência B → resultado por hipótese →
> intervenção pós-teste

Isso é o esqueleto de um modelo do aprendiz de verdade: ele separa **evento
observado** de **hipótese cognitiva** de **padrão confirmado** de **histórico de
intervenção e resultado**.

## 5. Registro longitudinal

Ao final, só ofereça persistir se houver ledger realmente gravável. Crie um novo
`learner_event` ligado à tentativa anterior e atualize/complete o mesmo
`review_task_id` quando a contraprova pertence àquela revisão. Registre:

```text
tentativa → hipótese candidate → sonda/transferência →
resultado (strengthened | weakened | abandoned | indeterminate) → intervenção → próximo vencimento
```

Sem ledger acessível, diga que o resultado vale apenas na conversa atual. Não crie
snapshot solto nem prometa que a sessão seguinte o encontrará automaticamente.

## 6. Limites — não invente capacidade

- **Não há persistência automática.** A confiança diagnóstica é ordinal. A
  calibração do aluno é outro dado e só recebe Brier/viés com `n >= 10`, conforme
  `LEARNER_STATE_PROTOCOL.md`.
- Contraprova sintética **não** prova aprendizagem. O piloto 1C-A com 40 agentes
  simulados foi declarado `PILOT_SYNTHETIC_DESIGN_INCONCLUSIVE`, e nenhum dado
  sintético entra em prioridade ou recorrência.
- Uma rodada não fecha padrão. Não escreva "você tem" — escreva "a hipótese X
  ficou mais forte".
- Marcadores conflitantes (certeza declarada + chute confessado) → **abster**,
  não escolher vencedor.
- Se o aluno estiver cansado ou com prova amanhã, contraprova é luxo: entregue a
  intervenção direta e registre a hipótese para depois.

## 7. Integração

- hipótese e movimento → `QUESTION_INTELLIGENCE_P7.md` §5 e §8
- item real com a mesma operação → `00_MAPA_OPERACAO_MOVIMENTO.md`
- intervenção por movimento → `ERROR_NOTEBOOK_REVIEW_QUEUE.md` §3
- geração da questão de transferência → `SIMULATION_PROTOCOL.md`
- persistência, confiança e estados da hipótese → `LEARNER_STATE_PROTOCOL.md`
- hesitação captada em aula → `AULA_VIVA.md` (lente pessoal)
