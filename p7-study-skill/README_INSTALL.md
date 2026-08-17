# P7 Diagnos — instalação e uso

Skill privada de estudo do P7 (sétimo período, ciclo clínico — FAMENE).

Sucede a `p6-study-skill` v2.1.0, herdando a arquitetura e corrigindo dois
defeitos conhecidos dela (ver `CHANGELOG` abaixo).

## Instalação

A skill é invocada pelo slug `p7-study-skill`. O diretório instalado é:

```
~/.claude/skills/p7-study-skill/
```

Este repositório (`Documents/P7-Study-Skill/p7-study-skill/`) é a **cópia
canônica versionada**. O diretório em `~/.claude/skills/` é a cópia instalada.
Edite aqui, depois sincronize.

## Estrutura

```
SKILL.md                  roteador principal — modos, estado, contrato de fontes
references/               protocolos operacionais (carregar UM por tarefa)
p7_source_pack/           índices curriculares e evidência de cobrança
capsules/                 pacotes de tema, ancorados no professor
capsule_generation/       contrato de geração e verificação de cápsulas
```

## Os quatro modos externos

1. `Plano de Guerra` — tenho prova, prazo, escopo grande demais
2. `Estudar Tema` — quero aprender X
3. `Resolver Questão` — corrija esta questão e diagnostique meu raciocínio
4. `Simular Prova / Arguição / OSCE` — me teste

Mais o ponto de entrada de desbloqueio: `igor me salva!`

Linguagem natural é aceita. Não existem comandos com barra.

## O acervo por trás

423 fontes indexadas, extraídas de 9 arquivos do Drive do P7:

| Disciplina | Fontes |
|---|---|
| EISA II — Saúde do Adulto II (9 especialidades) | 166 |
| EISCA — Saúde da Criança e Adolescente | 71 |
| Provas antigas + devolutivas | 65 |
| Resumos das Unidades | 47 |
| EISM — Saúde Mental | 46 |
| Casos Clínicos · Farmacologia · OSCE · RESUmed | 28 |

99 dessas fontes não têm camada de texto — a maioria são slides do professor
fotografados da tela do projetor. Eles são densos e cruciais, e continuam sendo a
camada de maior autoridade; muda só o método de acesso, que é leitura visual das
páginas pré-renderizadas. Ver `references/SOURCE_POLICY.md` §2 e §2.1.

## CHANGELOG — o que mudou em relação à P6

**1. Verificação de cápsula em dois níveis.**
A P6 v2.1.0 declara em `SKILL.md §10` que a verificação por segundo agente está
PENDENTE. No P7 há dois níveis: o **nível 1** (releitura dos dados de precisão pelo
próprio gerador) roda sempre e produz cápsula utilizável; o **nível 2**
(verificação independente adversarial) roda em lote no fim do roadmap, priorizando
risco clínico alto e farmacologia. O estado fica visível no índice em vez de virar
tarefa manual do aluno. Ver `capsule_generation/CAPSULE_GENERATION_POLICY.md` §4.

**2. Regra do silêncio no diagnóstico de raciocínio.**
O piloto controlado Diagnos 1C-A (2026-07-28, 40 agentes cegos) refutou a
hipótese H4 com um achado preciso: o motor converteu **silêncio em fato** —
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
integração com o MedPattern · parser de PDF em runtime.

As cápsulas são construídas offline e versionadas. Nada é processado ao vivo.
