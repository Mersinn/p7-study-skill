# Learner State, adaptação e continuidade

## 1. Separação de domínios

`Question Intelligence` descreve a questão: comando, operação, natureza da demanda,
variável decisiva, validade, solução e distratores. É compartilhável e não contém
perfil do estudante.

`Learner State` é pessoal e privado. Ele reúne eventos observados de tentativa,
hipóteses cognitivas, intervenções, confiança pré-feedback, revisão e
transferência. Não altere o Plano A para fazê-lo combinar com a resposta do aluno.

Nunca grave dado identificável de paciente. Não transforme baixa energia, atraso
ou condição de saúde em traço persistente.

## 2. Ciclo de evidência

Uma tentativa isolada (`N=1`) pode gerar apenas `candidate` em confiança baixa. Um
distrator só sustenta candidato quando o item é válido e o mapeamento é específico.
Silêncio, ausência de justificativa ou natureza operacional do item não provam
movimento.

Estados: `candidate | confirmed | weakened | abandoned | indeterminate`.

- repetição em itens independentes pode elevar a confiança do candidato;
- `confirmed` exige pelo menos **duas evidências independentes** em itens/contextos
  distintos, sendo ao menos uma transferência válida da mesma operação em outro
  conteúdo;
- transferência contaminada por falta de conteúdo, chute, pista decisiva ou item
  inválido não fortalece nem enfraquece a hipótese;
- evidência contrária enfraquece; contraprova discriminante pode abandonar;
- sem sinal suficiente, registre a tentativa, se útil, mas mantenha a hipótese
  `indeterminate` e não invente lacuna.

Um padrão de bloco precisa de numerador, denominador e ao menos três rastros
observados. Mesmo consistente, continua hipótese no máximo moderada até
cumprir o gate de confirmação acima.

## 3. Confianças diferentes

- `diagnostic_confidence`: confiança da skill na hipótese sobre o movimento —
  `insuficiente | baixa | moderada | alta`;
- `learner_confidence_before_feedback`: previsão do aluno — `0 | 25 | 50 | 75 |
  100`, coletada **antes** de revelar gabarito quando o aluno aceitar o modo
  calibrado. Entrada compacta: `B · 75%`.

Nunca descreva confiança diagnóstica como “você estava confiante”. Sem confiança
pré-feedback não há medida de calibração.

Com menos de 10 tentativas válidas, mostre apenas acertos/confianças brutos e
`amostra insuficiente para calibração agregada`. Com `n >= 10`:

```text
p = learner_confidence_before_feedback / 100
y = 1 se correto, 0 se incorreto
Brier = media((p - y)^2)
vies = media(p - y)
```

Informe `n`, fórmula, linhas excluídas e bins. Brier menor é melhor; viés positivo
sugere excesso de confiança e negativo, subconfiança. Não diagnostique traço
pessoal com esse escore.

## 4. Dificuldade adaptativa — default

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
novidade do contexto. Diga brevemente por que mudou.

## 5. Ledger e persistência honesta

O estado vale apenas na conversa atual, salvo se um ledger foi realmente criado e
está acessível. Nova sessão:

1. se houver ledger, leia vencidos e hipóteses abertas antes de gerar novos itens;
2. crie um novo `learner_event_id` ligado ao evento anterior e atualize/complete o
   mesmo `review_task_id` quando for a mesma tarefa; não sobrescreva tentativa;
3. se não houver, diga `sessão sem histórico` e peça o ledger ou ofereça revisão
   genérica rotulada;
4. nunca alegue lembrar outra conversa sem mecanismo real.

Eventos são imutáveis; correções viram novos eventos ligados ao anterior. Estado de
domínio, hipóteses e fila são projeções reconstruíveis, não fatos sobrescritos.

## 6. Scheduler 48h → 7d → 21d por resultado

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

## 7. Retomada e saída

Ao retomar, mostre somente: itens vencidos selecionados · hipótese aberta relevante
· intervenção anterior · próximo item. Ao encerrar, diga se o registro existe só na
conversa ou foi efetivamente persistido e forneça o próximo vencimento calculado.
