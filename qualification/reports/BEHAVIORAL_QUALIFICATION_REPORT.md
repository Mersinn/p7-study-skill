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

## 3. T05 — execução real, 2 rodadas (metodologia corrigida em tempo real)

### 3.1 Rodada 1 (entrada ambígua) — achado real, não descartado

**Entrada:** "Quero estudar asma na infância agora — a parte de crise aguda."
(pedido amplo, sem sinal explícito de prática/teste).

**Resultado:** 3/3 execuções revelaram pivô clínico já resolvido (tabela de
corte completa), conduta terapêutica completa (doses, escada) e cards, **antes**
de qualquer pergunta ao aluno — nas 3 vezes. Transcritos completos e hash em
`qualification/runs/behavioral/T05/run{1,2,3}_{transcript.md,record.json}`.

**Por que isto não é automaticamente "T05 FAIL":** o usuário revisou o
achado e determinou que, para um pedido amplo sem sinal de prática, entregar
o guia completo de uma vez **é um comportamento de produto aceitável** — a
entrada original não representa fielmente o que T05 pretende medir (que é o
comportamento quando o aluno especificamente busca recuperação ativa). Editar
`SKILL.md` para fechar essa leitura mais permissiva **foi feito e depois
revertido** nesta sessão, por decisão do usuário — ver histórico do commit
para o diff completo, preservado para auditoria. Isso é uma correção de
metodologia de teste, registrada honestamente, não um resultado escondido.

### 3.2 Rodada 2 (entrada redesenhada, inequívoca) — resultado vigente

**Entrada corrigida:** "Quero estudar asma na infância agora — crise aguda.
Mas quero que você me teste primeiro, não me explica nada ainda — me dá um
caso pra eu tentar resolver antes." (sinal explícito e inequívoco de pedido
de prática).

**Resultado: PASS 3/3.** Nas 3 execuções (sessões novas, isoladas,
`qualification/runs/behavioral/T05_v2/`), a skill:
- não revelou pivô resolvido, conduta ou cards em nenhuma das 3;
- apresentou uma vinheta clínica rica e específica (variando entre as 3
  execuções — sem repetição de caso) com perguntas estruturadas;
- terminou explicitamente em espera pela tentativa ("Não vou explicar nada
  ainda", "Não consulte a cápsula nem o slide", "Responda antes de continuar").

**T05: PASS confirmado 3/3** sob a entrada corrigida.

### 3.3 Lição de método preservada

A ambiguidade da entrada original do fixture não tinha sido detectada na
fase de materialização — só apareceu ao rodar de verdade e ao usuário
revisar o resultado. Isso valida por que "executar de verdade" não é
opcional: um fixture pode parecer bem desenhado e ainda assim testar a coisa
errada. `F-THEME/theme_brief.md` documenta o redesenho com data e motivo.

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

Nenhuma. `SKILL.md` foi editado e revertido na mesma sessão (net diff zero);
`reconcile_package.py --check` e `run_tests.py` confirmados limpos após o
revert. Nenhum gate fechado ou reaberto por este bloco.
