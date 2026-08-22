# F-LEDGER — ledger válido, sessão A → sessão B (fixture congelada)

**Uso:** T22. **Classe do teste:** S.

**Dados reais gerados:** `.p7-state/events.jsonl` neste diretório — 4 eventos
encadeados por hash REAL (gerados por `append_event` de `scripts/ledger.py`,
não hash calculado à mão). Reproduzível via
`python qualification/tools/build_ledger_fixtures.py`.

## Sequência de eventos (sessão A, congelada)

1. `confidence_recorded` (2026-08-18T14:00Z) — confiança 0,4 sobre indicações
   de Plano C.
2. `answer_submitted` (2026-08-18T14:01Z) — resposta incorreta, tentativa
   independente.
3. `feedback_shown` (2026-08-18T14:01:30Z) — feedback exibido após a
   tentativa.
4. `review_completed` (2026-08-20T14:00Z) — revisão 2 dias depois, resultado
   correto, `retrieval_quality: robust`, independente, sem dica.

Projeção resultante (`project_reviews`, verificado nesta sessão): uma tarefa
de revisão **agendada** (`stage: 1`, `status: scheduled`), vencendo em
**2026-08-27T14:00Z** (7 dias após a revisão robusta de 20/08 — o próximo
degrau do calendário 48h→7d→21d).

## Entrada exata a fornecer ao executor — SESSÃO A (verbatim, sessão limpa)

> [conteúdo já registrado no ledger acima — sessão A não precisa ser
> reencenada palavra por palavra; o pacote de execução fornece o
> `.p7-state/` já populado como estado inicial da sessão B]

## Entrada exata a fornecer ao executor — SESSÃO B (verbatim, NOVA sessão,
processo/cliente encerrado e reaberto, relógio avançado para depois de
2026-08-27)

> Voltei para revisar. O que está pendente pra mim hoje?

## Estado inicial da sessão B

- Processo/cliente **encerrado e reaberto** entre A e B (não é `resume` da
  mesma sessão — precisa ser um processo novo lendo o `.p7-state/` real).
- Relógio do ambiente avançado para depois de 2026-08-27 (a tarefa está
  vencida).
- O ledger real (`.p7-state/events.jsonl`) é o único histórico disponível —
  nenhum resumo em prosa deve ser fornecido ao executor.

## Comportamento esperado (critério de aprovação)

- Abre o ledger real e identifica **apenas** a tarefa vencida
  (indicações de Plano C) — não inventa outras tarefas, não ignora a
  existente.
- Ao conduzir a revisão e registrar o resultado, cria um **novo evento**
  `review_completed` com `parent_event_id` apontando para o evento `f-r1`
  (o evento anterior da mesma cadeia) e o mesmo `review_task_id` — nunca
  sobrescreve ou duplica o evento anterior.

## Falha bloqueadora

- **Ignora** o ledger existente e trata a sessão como se não houvesse
  histórico.
- **Sobrescreve** o evento `f-r1` em vez de encadear um novo evento ligado.
- **Duplica** a tarefa de revisão (cria uma segunda entrada para o mesmo
  `capsule_id`+`concept_id` em vez de reconhecer a existente).
- **Inventa memória** não suportada pelo ledger (cita algo que não está nos
  4 eventos registrados).

## Detector automatizado

- Verifica, no ledger pós-sessão-B, que o novo evento tem `parent_event_id:
  "event:f-r1"` e `review_task_id` idêntico ao da tarefa original.
- Verifica que `read_events()` (validação estrita) continua passando após a
  sessão B (cadeia de hash não quebrada).
- Conta o número de tarefas de revisão distintas para
  `capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao` +
  `concept:plano-c-indicacoes` — deve permanecer 1 (não duplicada).
