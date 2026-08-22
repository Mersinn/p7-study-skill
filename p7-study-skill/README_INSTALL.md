# P7 Study Companion — instalação e uso

Skill privada de estudo do P7 (sétimo período, ciclo clínico — FAMENE).

> **Estado: `1.0.0-rc.1` / HOLD.** Esta candidata não é a v1.0.0 final e
> permanece bloqueada até os gates clínicos, comportamentais, de longitudinalidade,
> jornadas sintéticas e instalação limpa.

Sucede a `p6-study-skill` v2.1.0, herdando a arquitetura e recuperando
regressões e defeitos conhecidos (ver `CHANGELOG` abaixo).

## Instalação portátil

Mantenha a pasta `p7-study-skill/` completa. O slug é `p7-study-skill`; o
diretório pai depende do cliente e do sistema operacional.

- **Codex:** copie/instale a pasta no diretório local de skills do Codex
  (`$CODEX_HOME/skills/` ou o caminho exibido pelo próprio cliente).
- **Claude com skills locais:** copie a pasta para o diretório de skills
  configurado pelo Claude; `~/.claude/skills/` é apenas o padrão comum, não um
  caminho universal.
- **Mobile/cliente sem skill local:** use o recurso de importar projeto/skill se
  existir. Caso contrário, forneça `SKILL.md` e somente os arquivos pertinentes à
  tarefa. Sem filesystem persistente, não há retomada automática do ledger.

Não edite a cópia instalada como fonte canônica. Faça mudanças no clone
versionado, valide e só então sincronize para o cliente.

## Estrutura

```
SKILL.md                  roteador principal — modos, estado, contrato de fontes
references/               protocolos operacionais (carregar UM por tarefa)
p7_source_pack/           índices curriculares e evidência de cobrança
capsules/                 pacotes de tema, ancorados no professor
capsule_generation/       contrato de geração e verificação de cápsulas
schemas/                   contratos canônicos versionados
config/                    normalização e fórmula de prioridade
scripts/                   validação, reconciliação e ledger
artifacts/                 saídas determinísticas; não editar manualmente
```

## Validação e ledger

Os scripts requerem Python 3.11+ e usam somente a biblioteca padrão:

```text
python scripts/run_tests.py
python scripts/reconcile_package.py --write
python scripts/reconcile_package.py --check
python scripts/validate_package.py
```

O gate final é intencionalmente mais estrito:

```text
python scripts/validate_package.py --release-gate
```

Inicie e reprojete o estado local privado assim:

```text
python scripts/ledger.py --state-dir .p7-state init
python scripts/ledger.py --state-dir .p7-state project
```

Leia `PRIVACY.md` antes de registrar dados e `COMPATIBILITY.md` para limites por
superfície.

## Comece por uma intenção

1. `Plano de Guerra` — tenho prova, prazo, escopo grande demais
2. `Estudar Tema` — quero aprender X
3. `Resolver Questão` — corrija esta questão e diagnostique meu raciocínio
4. `Simular Prova / Arguição / OSCE` — me teste
5. `Aula Viva` — acabei de ter aula; capture o que o professor enfatizou
6. `Contraprova` — teste se a hipótese sobre meu erro realmente se sustenta

Também pode dizer: `transforma este PDF em guia ativo`, `corrige minha resposta
discursiva` ou `continua minhas revisões a partir deste ledger`.

Ponto de entrada para desbloqueio: `igor me salva!`

Linguagem natural é aceita. Não existem comandos com barra.

### Exemplos rápidos

- `Tenho prova de EISM em 48h e 90 minutos hoje.`
- `Nunca estudei delirium; começa do zero e me testa.`
- `Simula 10 questões de EISCA.` — por padrão, uma por vez;
- `Simulado fechado de 10, todas juntas.` — lote sem feedback até a resposta;
- `Não concordo com o diagnóstico do meu erro; faz uma contraprova.`
- `Você lembra da sessão passada?` — só há continuidade se um ledger real estiver
  acessível; sem ele, a skill declara sessão sem histórico.

## O acervo por trás

Não mantenha contagens copiadas manualmente neste documento. Os totais vigentes
de cápsulas, fontes, bytes e dados de precisão são recalculados em
`artifacts/METRICS.json`; hashes e arquivos ficam em
`artifacts/PACKAGE_MANIFEST.json`.

`corpus_text/` e `vision_png/` são camadas locais opcionais e não acompanham o
pacote portátil. Quando ausentes, a skill degrada para `metadata_only`: pode citar
a referência registrada, mas não pode afirmar que abriu ou conferiu a fonte bruta
naquela sessão.

## CHANGELOG — o que mudou em relação à P6

**1. Verificação de cápsula em dois níveis.**
A P6 v2.1.0 declara em `SKILL.md §10` que a verificação por segundo agente está
PENDENTE. No P7 há dois níveis: o **nível 1** (releitura dos dados de precisão pelo
próprio gerador) confere transcrição/alinhamento curricular; o **nível 2**
(verificação independente adversarial) roda em lote no fim do roadmap, priorizando
risco clínico alto e farmacologia. Vigência clínica permanece um estado separado:
claim crítico pendente/conflitante fica em quarentena, mesmo com L1. Ver
`capsule_generation/CAPSULE_GENERATION_POLICY.md` §4.

**2. Regra do silêncio no diagnóstico de raciocínio.**
A análise adversarial registrada para o Diagnos 1C-A refutou a hipótese H4 com
um achado preciso: o motor converteu **silêncio em fato** —
concluiu que o aluno "não processou o comando" apenas porque ele não mencionou o
comando. `references/QUESTION_INTELLIGENCE_P7.md` §8 proíbe **essa** inferência
específica — e, no mesmo movimento, §8.1 protege o motor: alternativa marcada,
padrão do bloco, estrutura do item, semântica do enunciado e trajetória continuam
sendo sinal legítimo. Responder só com a letra **não** é `INDETERMINADO`.

**3. Camada de segurança médica reescrita para o P7.**
Os blocos de alto risco da P6 eram obstétricos e cardiológicos. Os do P7 são
psiquiátricos, neurológicos, endócrinos, urológicos, oftalmológicos, oncológicos
e pediátricos. Ver `references/MEDICAL_SAFETY_LAYER.md` §2 e §6.

**4. Drill trocado.**
`ECG_DRILL` (P6) → `EXAME_ESTADO_MENTAL_DRILL` (P7). Mesma mecânica — forçar a
sequência antes do diagnóstico — aplicada ao erro dominante da psiquiatria de
graduação: pular a semiologia e ir direto ao rótulo.

## Limites declarados

Esta skill **não** é: app · banco de dados · API · RAG · sistema de embeddings ·
integração com o MedPattern · parser próprio de PDF em runtime. Quando a superfície
consegue ler um anexo, ela pode transformá-lo em guia ativo sem gravá-lo como
cápsula.

As cápsulas são construídas offline e versionadas. Nada é processado ao vivo.
