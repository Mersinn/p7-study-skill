# T18 — calibração: erro confiante vs. acerto frágil (fixture ad-hoc)

**Classe:** C.

## Cenário congelado (histórico fornecido ao executor como estado inicial)

Um único aluno, múltiplos itens ao longo de uma sessão, com confiança
declarada ANTES de cada tentativa:

| Item (tema) | Confiança declarada | Resultado |
|---|---|---|
| 1. Dose de adrenalina na RCP neonatal | 90% (alta) | **Errado** |
| 2. Corte de PSA para biópsia prostática | 90% (alta) | **Errado** |
| 3. Sinal de asterisco em desidratação | 25% (baixa) | **Certo** (frágil — respondeu rápido, sem justificativa) |
| 4. Janela de trombólise no AVCi | 25% (baixa) | **Certo** (frágil) |
| 5. Sequência de tratamento SNM | 80% (alta) | **Certo** — robusto, justificativa completa, independente |
| 6. Marco de tempo do estado de mal | 85% (alta) | **Certo** — robusto, justificativa completa, independente |

## Entrada exata a fornecer ao executor (verbatim, sessão limpa, após o
histórico acima já registrado)

> Baseado no que eu fiz até agora, o que eu mais preciso revisar?

## Estado inicial

Sessão em andamento com os 6 eventos da tabela já registrados (confiança +
resultado + qualidade de evidência para cada um).

## Comportamento esperado (critério de aprovação)

- **Prioriza os erros com alta confiança** (itens 1 e 2 — 90% de confiança,
  errados) como o que mais precisa de revisão — esse é o sinal de maior
  risco (o aluno não sabe que não sabe).
- **Mantém os acertos frágeis (itens 3, 4) como não-confirmados** — não
  trata "acertou" como "domina o assunto" quando a evidência é frágil/
  chute com baixa confiança.
- **Só os acertos robustos e de alta confiança (itens 5, 6) elevam** o
  status de domínio daquele conceito especificamente.

## Falha bloqueadora

- Trata todos os itens errados com o mesmo peso (não distingue erro
  confiante de erro com baixa confiança já esperado).
- Confunde as duas dimensões de confiança: usa a confiança PRÉ-tentativa do
  aluno como se fosse a confiança DIAGNÓSTICA do sistema sobre a hipótese
  cognitiva (são coisas diferentes — ver `references/LEARNER_STATE_PROTOCOL.md`).
- Declara "domínio confirmado" com base nos acertos frágeis (itens 3, 4).

## Detector automatizado

- Verifica que os itens 1 e 2 (erro + alta confiança) aparecem citados como
  prioridade na resposta.
- Verifica que os itens 3 e 4 (acerto frágil) NÃO são citados como
  "dominado"/"confirmado".
- Busca por confusão terminológica entre "confiança do aluno" e "confiança
  da hipótese/diagnóstico" tratadas como sinônimos na resposta.
