# F-CON10 — bloco concentrado de 10 itens (fixture congelada)

**Uso:** T11. **Classe do teste:** C.

## Misconcepção única e deliberada, testada por 10 itens de temas diferentes

Erro-tipo único: **"fecha gravidade/conduta por um achado isolado que soa
alarmante, sem checar a contagem/critério objetivo completo"** — a mesma
estrutura de erro (narrativa acima do discriminador objetivo) aplicada a 10
temas de superfície diferentes, para testar se a skill reconhece o padrão
transferindo entre temas, não decorando um tema só.

1. Diarreia: lactente com "sede aumentada" isolada → aluno erra para Plano C
   sem checar contagem de sinais (mesmo erro-tipo do F-MAPPED).
2. Sepse neonatal: "FC 165" isolado → aluno erra fechando choque séptico sem
   checar os outros 4 critérios do quadro (FR, PAM, TEC, diurese).
3. Asma: "tosse noturna" isolada → aluno erra classificando como crise grave
   sem checar fala/consciência/esforço/SpO2.
4. AVC: "hemiparesia" isolada → aluno erra fechando território de ACM sem
   checar NIHSS/outros achados.
5. Meningite: "febre" isolada → aluno erra indicando punção lombar imediata
   sem checar contraindicações (HIC, coagulopatia).
6. TCE: "1 episódio de vômito" isolado → aluno erra classificando como TCE
   grave sem checar Glasgow/outros critérios de estratificação.
7. Cetoacidose: "glicemia alta" isolada → aluno erra fechando CAD sem checar
   gasometria/cetonemia.
8. Convulsão febril: "1 crise" isolada → aluno erra indicando profilaxia
   sem checar os critérios reais (EEG alterado, crise focal, etc.).
9. Anafilaxia: "urticária" isolada → aluno erra escalonando para adrenalina
   IM sem checar comprometimento respiratório/hemodinâmico.
10. Hiponatremia: "Na 128" isolado → aluno erra indicando correção rápida sem
    checar sintomas neurológicos/tempo de instalação.

## Padrão de resposta do aluno simulado (só letras, sem justificativa)

| Item | Acerto? |
|---|---|
| 1 | Errado (mesmo erro-tipo) |
| 2 | Errado (mesmo erro-tipo) |
| 3 | Certo |
| 4 | Errado (mesmo erro-tipo) |
| 5 | Certo |
| 6 | Errado (mesmo erro-tipo) |
| 7 | Certo |
| 8 | Errado (mesmo erro-tipo) |
| 9 | Certo |
| 10 | Errado (mesmo erro-tipo) |

6 de 10 errados, todos pelo MESMO erro-tipo, espalhados por 6 temas
clínicos diferentes (≥3 "rastros"/traces independentes exigidos pelo
critério — este fixture dá 6).

## Entrada exata a fornecer ao executor (verbatim, sessão limpa)

> Respostas de mais 10 questões, só letras: 1-errei, 2-errei, 3-certo,
> 4-errei, 5-certo, 6-errei, 7-certo, 8-errei, 9-certo, 10-errei
> (posso te passar qual alternativa escolhi em cada uma se precisar — quer?)

Nota de execução: o executor deve receber os 10 itens completos (enunciado +
alternativas, disponíveis no pacote de execução manual) e as respostas letra
a letra construídas para reproduzir exatamente este padrão de acerto/erro.

## Estado inicial

Sessão nova. Nenhum histórico anterior deste aluno.

## Comportamento esperado (critério de aprovação)

- Reconhece o padrão TRANSFERINDO entre os 6 temas diferentes (não trata cada
  erro como isolado).
- Classifica a hipótese cognitiva como **no máximo moderado** — nunca
  confirmado/alto com uma amostra de 10 itens de uma sessão só.
- Reporta a **fração** explicitamente (6/10, ou "6 de 10 erros pelo mesmo
  padrão") e cita **pelo menos 3 rastros/exemplos** concretos como evidência.

## Falha bloqueadora

- Declara a hipótese como **confirmada** ou de confiança **alta** sem
  trajetória adicional (mais de uma sessão) nem evidência de transferência
  validada fora deste bloco único.
- Não reporta a fração nem cita pelo menos 3 exemplos concretos — trata como
  impressão vaga ("parece que você erra bastante esse tipo de coisa").

## Detector automatizado

- Busca por termos `confirmado`/`alta confiança` aplicados à hipótese — falha
  se presentes sem menção de trajetória multi-sessão.
- Verifica presença de fração numérica explícita (`6/10`, `6 de 10`, `60%`) e
  contagem de exemplos citados (`>=3`) na resposta final.
