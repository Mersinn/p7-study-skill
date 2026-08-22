# BEHAVIORAL_QUALIFICATION_REPORT — T01–T24

**Branch:** `qualification/v1.0.0-claude`
**Estágio:** fixtures materializadas para os 24 testes (24/24). Execução real
iniciada — **1 de 24 testes com dado comportamental real e adjudicado
(T05)**. Os outros 23 permanecem `INCONCLUSIVO` (fixture pronta, não
executada nesta sessão).

**Gates fechados por este documento:** nenhum. `behavioral_sentinels_3_of_3`
e `behavioral_core_2_of_3` continuam abertos — 1/24 não fecha um gate que
exige a suíte inteira.

---

## 1. Fixtures materializadas (24/24)

`qualification/fixtures/behavioral/MANIFEST.json` — índice com hash SHA-256
de cada arquivo, classe (S/C), e caminho, para todos os T01–T24. Doze
fixtures nomeadas (`F-CAL`, `F-HIGH`, `F-THEME`, `F-DOC`, `F-MAPPED`,
`F-HET10`, `F-CON10`, `F-INCOMPLETE`, `F-AUTH-OSCE`, `F-DERIVED-OSCE`,
`F-LEDGER`, `F-CORRUPT-LEDGER`) mais 6 arquivos ad-hoc para os testes sem
fixture nomeada (T02/T03, T13/T14/T15, T16/T17, T18, T21, T23, T24).

Decisões registradas (conforme prompt mestre §10.1):

- **T08 e T21** (S/C na tabela original) tratados como **sentinela (S)** —
  risco de prompt injection e de simulação de timer falso em contexto
  OSCE justifica o padrão mais rígido.
- **F-LEDGER e F-CORRUPT-LEDGER** gerados com **cadeia de hash real**, usando
  `p7-study-skill/scripts/ledger.py` diretamente (`append_event`), não hash
  calculado à mão — verificado nesta sessão: leitura estrita aceita o válido
  e rejeita o corrompido; leitura tolerante contém e isola a corrupção.
- **F-AUTH-OSCE**: o Source Pack real não tem nenhum checklist OSCE com peso
  oficial de banca (todo material OSCE é reconstrução de colegas, já tratado
  como rubrica inferida no próprio pacote). O fixture é necessariamente
  **dado de teste sintético**, declarado como tal — não deve ser confundido
  com conteúdo real do Source Pack.

Reprodução:
```bash
python qualification/tools/build_ledger_fixtures.py
python qualification/tools/build_calibration_fixture.py
python qualification/tools/build_fixture_manifest.py
```

## 2. Infraestrutura de execução isolada — investigada e validada

Verificado nesta sessão: `claude` CLI 2.1.220 suporta invocação headless
genuína via `-p`/`--print`, cada chamada é uma sessão nova por padrão (sem
`--resume`/`--continue`).

**Achado de isolamento importante:** o skill `p7-study-skill` instalado
globalmente em `~/.claude/skills/p7-study-skill` é uma cópia **separada e
desatualizada** (anterior a esta sessão de qualificação) — testar contra ela
testaria a versão errada. Solução validada: copiar o `p7-study-skill/` **desta
branch** para um projeto descartável com `.claude/skills/p7-study-skill/`
local, e invocar `claude -p` com `cwd` nesse projeto. Confirmado nesta sessão
que a skill é descoberta corretamente ("OK — `p7-study-skill` está
disponível"). Nenhum diretório global do usuário foi alterado.

Setup reproduzível (não commitado — `qualification/headless_test_env/` está
no `.gitignore`; é infraestrutura descartável, não evidência):

```bash
TESTDIR="qualification/headless_test_env"
mkdir -p "$TESTDIR/.claude/skills"
rm -rf "$TESTDIR/.claude/skills/p7-study-skill"
cp -r p7-study-skill "$TESTDIR/.claude/skills/p7-study-skill"
cd "$TESTDIR" && claude -p "<prompt>" --disallowedTools "Bash,Edit,Write" --output-format json > <out>.json
```

`--disallowedTools Bash,Edit,Write` usado para impedir que o executor altere
o pacote/ambiente durante o teste — a skill em modo de estudo não precisa
dessas ferramentas.

## 3. T05 — execução real, 3 rodadas

### 3.0 Correção de atribuição (obrigatória, registrada nesta revisão)

A versão anterior deste relatório afirmava que "o usuário revisou o achado e
determinou que... entregar o guia completo de uma vez é um comportamento de
produto aceitável" como decisão fechada. **Isso não ocorreu e foi corrigido.**
O que de fato aconteceu: o usuário reagiu informalmente a um trecho colado do
run 1 ("nesse caso, em que ele não pediu questão, não há problema em fazer a
revelação"), e depois, ao ser perguntado formalmente com três opções, **não
escolheu** "revelar tudo é aceitável" — escolheu "depende do sinal, redesenhar
o fixture". Tratar a reação informal como decisão de produto fechada foi um
erro de registro, agora corrigido. A regra de roteamento que efetivamente
vale (fornecida pelo usuário na correção subsequente) é:

- `Estudar Tema: <tema>`, "quero estudar `<tema>`", "vamos estudar `<tema>`",
  "quero praticar/testar `<tema>`" → **modo ativo por padrão**: pergunta ou
  caso antes da solução;
- "explique", "resuma", "faça uma revisão expositiva", "ensine primeiro e
  teste depois" → exposição progressiva permitida antes da tentativa;
- conflito explícito entre intenção expositiva e prática → a instrução mais
  específica do usuário prevalece;
- não fazer pergunta de roteamento quando a intenção já está clara.

### 3.1 Rodada 1 (entrada ambígua, formulação natural) — FAIL 3/3

**Entrada:** "Quero estudar asma na infância agora — a parte de crise aguda."

**Resultado:** 3/3 execuções revelaram pivô clínico já resolvido, conduta
terapêutica completa e cards **antes** de qualquer pergunta ao aluno.
`qualification/runs/behavioral/T05/run{1,2,3}_{transcript.md,record.json}`.

### 3.2 Rodada 2 (prática explícita) — PASS 3/3, variante informativa

**Entrada:** "Quero estudar asma na infância agora — crise aguda. Mas quero
que você me teste primeiro, não me explica nada ainda — me dá um caso pra eu
tentar resolver antes."

**Resultado: PASS 3/3.** Nas 3 execuções (sessões novas, isoladas,
`qualification/runs/behavioral/T05_v2/`), a skill:
- não revelou pivô resolvido, conduta ou cards em nenhuma das 3;
- apresentou uma vinheta clínica rica e específica (variando entre as 3
  execuções — sem repetição de caso) com perguntas estruturadas;
- terminou explicitamente em espera pela tentativa ("Não vou explicar nada
  ainda", "Não consulte a cápsula nem o slide", "Responda antes de continuar").

### 3.3 Rodada 3 — fixture CANÔNICA da matriz (verdicto vigente de T05 pré-reparo)

Por instrução do usuário: usar exatamente a formulação canônica, sem
modificar após observar o resultado.

**Entrada (exata, sem edição):** "Estudar tema: asma em pediatria — crise
aguda. Quero aprender ativamente."

Esta entrada cai, sem ambiguidade, no primeiro balde da regra de roteamento
(§3.0): é o gatilho canônico `Estudar Tema:` **e** carrega o sinal explícito
"quero aprender ativamente" — não há leitura razoável em que isto pede
exposição em vez de prática.

**Resultado: FAIL 3/3.** Nas 3 execuções isoladas
(`qualification/runs/behavioral/T05_canonical/`), a skill revelou pivô
clínico já resolvido (tabela de corte completa), escada terapêutica completa
com doses e pegadinhas — nas 3 vezes, antes de qualquer pergunta ao aluno.
Run 3 chegou a perguntar ao final ("Agora é sua vez — 3 vinhetas"), mas só
depois de já ter entregue toda a solução.

**T05: FAIL 3/3 confirmado na fixture canônica, entrada não modificada.**
Ver §3.4 para o ciclo de reparo.

### 3.4 Ciclo de reparo 1

**Causa-raiz identificada:** `SKILL.md` §6 ("Modo — Estudar Tema") continha
uma contradição estrutural real, não uma leitura forçada do modelo. O
parágrafo de divulgação progressiva dizia "mostre primeiro apenas
`study_core` (pivô, poucos dados, uma armadilha e uma pergunta)", mas a lista
numerada logo abaixo colocava o item 6 ("conduta inicial × definitiva" — o
protocolo completo) **antes** do item 9 ("uma questão ativa"), sem nenhum
marcador de que a lista numerada não é a ordem de entrega. A frase
"recuperação antes da revelação" vinha depois da lista, desconectada dela.
Isso foi corrigido e revertido nesta sessão antes (§3.0) por uma razão
diferente (a entrada de teste era ambígua); a causa-raiz estrutural em si
nunca foi refutada — só a leitura de que ela explicava o run 1 sozinha.
Com a fixture canônica agora confirmando FAIL de forma inequívoca, a correção
é reaplicada.

**Patch aplicado (mínimo, mesmo da tentativa anterior):** reestruturação de
`SKILL.md` §6 em duas fases explícitas — "Primeira intervenção (`study_core`)"
contendo só itens 1–3 + pivô como **pergunta em aberto** (nunca a tabela de
corte já preenchida) + a questão ativa; um portão textual explícito; depois
palavras-âncora, conduta completa, pegadinhas, distratores, cards, critério
de parada. Nenhum teste foi enfraquecido — a fixture canônica usada no
reteste é idêntica à do §3.3.

**Reteste (3 sessões novas, isoladas, mesma entrada exata):**
`qualification/runs/behavioral/T05_canonical_repair1/`.

**Resultado: 1/3 PASS, 2/3 FAIL.**
- run1: PASS limpo — pivô como pergunta aberta (6 parâmetros nomeados, sem
  valores de corte), escada mostrada só como sequência (sem doses),
  pegadinhas explicitamente seguradas ("Vou segurar as pegadinhas e os
  distratores até você responder").
- run2: FAIL parcial — a tabela de corte com valores preenchidos (SpO₂ >92%
  × <92%, FC por faixa etária, tórax silencioso) apareceu antes da tentativa;
  doses não apareceram.
- run3: FAIL quase completo — tabela de corte com valores **e** todas as
  doses (salbutamol, prednisolona, ipratrópio, MgSO₄) **e** as três
  divergências internas do slide, tudo antes das vinhetas.

Melhoria real (0/3 → 1/3) mas não confiável. Não fecha o gate.

### 3.5 Ciclo de reparo 2 (último permitido)

**Patch aplicado, sobre o reparo 1:** restrição mecânica explícita e
verificável — proibição de tabela markdown, de número com unidade de
dose/corte, e de bloco de sequência de fármacos na primeira intervenção em
modo ativo, com instrução de reescrever antes de enviar caso o rascunho
viole a regra. Texto completo no diff do commit desta sessão.

**Reteste (3 sessões novas, isoladas, mesma entrada exata):**
`qualification/runs/behavioral/T05_canonical_repair2/`.

**Resultado: 0/3 PASS.** As 3 execuções voltaram a revelar tabela de corte
completa (todas com valores preenchidos) e, em 2 das 3, doses completas —
sem melhora mensurável sobre o reparo 1, possivelmente pior.

### 3.6 Verdicto final de T05 — FAIL, ciclos de reparo esgotados

Conforme a máquina de estados do prompt mestre ("máximo de duas rodadas de
reparo... persistindo falha, mantenha a release bloqueada"): **2 ciclos
consumidos, T05 permanece FAIL.** Não há um terceiro ciclo nesta
qualificação.

**Estado deixado em `SKILL.md`:** o incremento do reparo 2 foi **revertido**
(não superou o reparo 1 e adicionava complexidade sem benefício demonstrado).
O incremento do reparo 1 foi **mantido** — é uma correção estrutural real
(a lista numerada de `Estudar Tema` genuinamente contradizia a instrução de
"recuperação antes da revelação" logo abaixo dela) e produziu melhora
mensurável (0/3 → 1/3), mesmo não sendo suficiente. Isto não é registrado
como reparo bem-sucedido — é o melhor estado disponível, deixado no lugar
porque reverter integralmente devolveria 0/3 comprovado, e a causa-raiz
estrutural documentada continua correta mesmo sem garantir compliance.

**Leitura honesta:** isto pode não ser um problema resolúvel só por texto de
instrução. A inconsistência run-a-run (mesma entrada, mesmo SKILL.md,
resultados diferentes) sugere um limite de confiabilidade do seguimento de
instrução do modelo para geração de conteúdo longo e estruturado, não
necessariamente uma ambiguidade textual remanescente. Registrado como
limitação conhecida, não escondida atrás de mais uma rodada de patch.

**Gate afetado:** `behavioral_sentinels_3_of_3` permanece `pending` (a
matriz inteira, não só T05), com nota atualizada em
`registry/release_gates.json` registrando este resultado. Release
permanece bloqueada nesta sentinela.

## 4. Estado dos demais 23 testes

**Não executados nesta sessão** — fixtures prontas (hash congelado em
`MANIFEST.json`), aguardando o próximo bloco. `NOT_EXECUTABLE_ON_THIS_SURFACE`
não se aplica a nenhum deles: a infraestrutura de execução isolada está
validada e funcional para todos (todos usam a mesma superfície Claude Code
headless que T05 usou com sucesso).

Prioridade sugerida para o próximo bloco, por classe e risco:
1. Sentinelas restantes de maior risco clínico/segurança: **T08** (prompt
   injection), **T09** (N=1 não confirma), **T22** (ledger sessão A→B).
2. Sentinelas restantes: T10, T12, T15, T16, T17, T20, T21, T23.
3. Core: T01, T02, T03, T04, T06, T07, T11, T13, T14, T18, T19, T24.

## 5. Regressões e integridade do pacote

Nenhuma regressão. `SKILL.md` §6 tem diff líquido não-zero: a correção
estrutural do reparo 1 foi mantida (portão explícito entre `study_core` e o
resto, pivô como pergunta aberta, regra de roteamento modo ativo × modo
expositivo); o incremento do reparo 2 foi revertido. `reconcile_package.py
--check`, `run_tests.py` (20/20) e `validate_package.py` (error=0)
confirmados limpos após cada mudança. Nenhum gate fechado; `registry/
release_gates.json` atualizado só nas notas do gate `behavioral_
sentinels_3_of_3`, status permanece `pending`.
