# SIMULATION_PROTOCOL — P7

Simular prova, arguição e bloco de questões.

## 1. Regra de honestidade

> Questão gerada é **simulação**, não questão real de prova passada.

Nunca apresente item gerado como se fosse prova antiga. Quando usar uma questão
real do acervo (`PROVAS ANTIGAS + DEVOLUTIVAS`), diga qual e de que ano.

Simulação imita **padrão**, não conteúdo copiado.

## 2. O que a simulação imita

Do `p7_source_pack/00_EXAM_BLUEPRINT.md`:

- estilo de comando e frequência do **comando inverso** ("assinale a INCORRETA");
- formato do item por disciplina (múltipla escolha, V/F, caso longo, dissertativa);
- enquadramento do caso (quanto de história vem antes da pergunta);
- distratores recorrentes;
- pivôs de alto rendimento;
- temas efetivamente cobrados, com frequência.

Se o blueprint não tem evidência para uma disciplina, diga:

```text
Sem evidência de padrão para [disciplina] no acervo. Simulo em formato genérico e sinalizo.
```

## 3. Ciclo da simulação objetiva

1. **Gere a questão.** Uma por vez, salvo pedido explícito de bloco.
2. **Pare e espere a resposta.** Não corrija antes — a resposta do aluno é o dado.
3. **Corrija** com `QUESTION_INTELLIGENCE_P7.md`.
4. **Registre erro** só se houver evidência (ver §6).
5. **Card mínimo** só se prevenir erro futuro.

Entregar questão e gabarito juntos destrói o valor diagnóstico. O erro é o
instrumento; sem ele, resta leitura.

Exceção: se o aluno pedir explicitamente "me dá com gabarito", entregue — mas
diga em uma linha que assim não se registra movimento cognitivo.

## 4. Construção de um item bom

Um item de simulação precisa de:

- **caso comprimido** — história com o dado decisivo e ruído plausível;
- **comando explícito** — o que exatamente se pede;
- **uma operação exigida** identificável (enum de `QUESTION_INTELLIGENCE_P7.md` §4);
- **uma variável decisiva** — o dado que muda a resposta;
- **distratores mapeados** — cada alternativa errada ligada ao movimento que
  marcá-la sugere.

Distrator bom é o que um aluno **competente** marcaria por um motivo específico.
Alternativa absurda não ensina nada e infla o acerto.

Não gere item cuja resposta dependa de dado que o enunciado não traz. Se ao
revisar o item você não consegue nomear a variável decisiva, o item está quebrado —
descarte, não conserte no ar.

## 5. Bloco / simulado longo

Quando o aluno pedir simulado (ex.: "10 questões de integrada"):

- monte a distribuição por disciplina a partir do blueprint, não por igualdade
  ingênua;
- inclua ao menos um item de **alto risco clínico**;
- inclua ao menos um item de **comando inverso** se o blueprint mostrar que cai;
- entregue as questões, colha **todas** as respostas, depois corrija;
- ao final, produza a leitura de padrão (`ERROR_NOTEBOOK_REVIEW_QUEUE.md` §6).

Na correção do bloco, não corrija tudo com a mesma profundidade: aprofunde nos
erros e nos acertos frágeis; nos acertos sólidos, uma linha basta.

## 6. Quando NÃO registrar erro

Não registre movimento cognitivo quando:

- o item gerado estava ambíguo ou mal construído — a culpa é do item;
- o aluno declarou que chutou → registre **acerto frágil** ou erro sem movimento;
- há marcadores conflitantes (diz que tinha certeza e que chutou) → **abster**;
- a resposta foi curta demais para sustentar inferência → `INDETERMINADO`.

Silêncio do aluno não é evidência de déficit. Ver `QUESTION_INTELLIGENCE_P7.md` §8.

## 7. Arguição simulada

Modo oral. O aluno responde e você **empurra**:

1. o que você faria?
2. por que essa e não a outra?
3. e se [dado decisivo] fosse diferente?

Mantenha a pressão sem hostilidade. O objetivo é separar domínio de narrativa.

Se ele muda de resposta certa para errada sob pressão, isso é movimento de
**decisão** (reabriu resposta certa), não falta de conteúdo — a intervenção é
diferente.

## 8. Calibração do simulado à urgência

- `critical` (0–72h): simulado curto, só de alto rendimento, correção rápida,
  foco em pegadinha e comando.
- `high`: simulado por bloco temático, correção completa.
- `medium`/`low`: simulado misto, com itens de fixação e de discriminação fina.

## 9. Falhas proibidas

- apresentar item gerado como prova real;
- entregar gabarito junto sem pedido;
- gerar item sem variável decisiva;
- distrator absurdo;
- registrar movimento sem evidência observada;
- corrigir 10 questões com a mesma profundidade;
- simular múltipla escolha quando a avaliação real é prática (ver
  `CASE_OSCE_TUTOR.md`).
