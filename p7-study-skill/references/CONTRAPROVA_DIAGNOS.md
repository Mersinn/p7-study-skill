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
- a hipótese principal é de **movimento** (operacional), não de conteúdo;
- o mesmo movimento já apareceu antes (`ERROR_NOTEBOOK_REVIEW_QUEUE.md`);
- o aluno discorda do diagnóstico.

Não ative quando o erro é claramente factual e único ("não sabia o valor"), nem
quando a evidência é `INDETERMINADO`. Testar hipótese sem hipótese é teatro.

## 3. O fluxo

### Passo 1 — a tentativa
O aluno responde. Idealmente com três rastros: **resposta · justificativa ·
confiança**. Sem justificativa ainda funciona (§8.1 do `QUESTION_INTELLIGENCE_P7`):
a alternativa marcada já mapeia movimento em confiança baixa.

### Passo 2 — hipóteses concorrentes, não veredito
Nunca escreva "você tem fechamento precoce". Escreva:

```text
Hipótese A: <movimento> — evidência a favor: <sinal observado>
Hipótese B: <alternativa> — evidência a favor: <sinal observado>
Evidência contra A:
O que ainda não sabemos:
Confiança: insuficiente | baixa | moderada | alta
```

Se A e B não pedem intervenções diferentes, não vale contraprova — junte as duas.

### Passo 3 — a menor intervenção que discrimina
Não dê a aula inteira do tema. Selecione a **menor intervenção que separa A de B**.
Frequentemente é uma única pergunta.

### Passo 4 — a questão de transferência
Segunda questão com a **mesma operação exigida** e **tema diferente**.

Tema diferente é o ponto. Se A é "fechamento precoce" e B é "lacuna de conteúdo
sobre pré-eclâmpsia", repetir pré-eclâmpsia não discrimina nada — o aluno pode
acertar por ter acabado de estudar. Outro tema, mesma operação, separa as duas.

Use o `00_MAPA_OPERACAO_MOVIMENTO.md` para achar um item real com a mesma operação.

### Passo 5 — não revele a hipótese antes
**Não diga o que está testando.** Se você anunciar "vou ver se você fecha cedo",
o aluno passa a vigiar exatamente isso e o teste se contamina.

Diga apenas:

```text
Quero te dar uma segunda questão curta antes de explicar.
```

Só depois da resposta, revele:

```text
Eu estava distinguindo entre <A> e <B>.
```

Isso não é manipulação — é cegamento, e é o que torna o resultado interpretável.
Se o aluno perguntar diretamente o que você está testando, **responda a verdade**
e registre que a rodada ficou contaminada.

### Passo 6 — o resultado
```text
Tentativa A: <o que ele fez>
Hipótese testada: <A vs B>
Intervenção aplicada: <a menor>
Transferência B: <o que ele fez na segunda>
Resultado: hipótese A ficou mais forte | mais fraca | indeterminada
Confiança atualizada:
Próximo passo:
```

Regras de leitura do resultado:

- executou o processo corretamente na segunda → **A enfraquece**;
- repetiu o movimento em tema onde sabia o conteúdo → **A fortalece**;
- errou por não saber o conteúdo da segunda → **indeterminado**, o teste falhou
  (item mal escolhido, não conclusão sobre o aluno);
- uma rodada não confirma padrão. Padrão exige **3 ocorrências independentes**.

## 4. O que muda no registro

A unidade deixa de ser "errei cardiologia" e passa a ser:

> tentativa A → hipótese → intervenção X → transferência B → hipótese ficou
> mais forte / mais fraca / indeterminada

Isso é o esqueleto de um modelo do aprendiz de verdade: ele separa **evento
observado** de **hipótese cognitiva** de **padrão confirmado** de **histórico de
intervenção e resultado**.

## 5. O snapshot de sessão

Ao final de uma sessão com contraprova, ofereça gerar:

```
capsules/_deltas/DIAGNOSTIC_SNAPSHOT_<AAAA-MM-DD>.md
```

com as hipóteses abertas, as fortalecidas, as refutadas e as intervenções que já
falharam. A sessão seguinte lê esse arquivo e continua de onde parou, em vez de
rediagnosticar do zero.

## 6. Limites — não invente capacidade

- **Não há banco, não há motor de confiança, não há persistência automática.** A
  confiança é política ordinal seguida pelo modelo, não cálculo determinístico.
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
- hesitação captada em aula → `AULA_VIVA.md` (lente pessoal)
