# Semiologia pediátrica

## Metadados

- Disciplina: EISCA
- Especialidade: Pediatria
- Unidade: I_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Transcription: confirmed
- Curricular alignment: confirmed
- Clinical validity: pending (tabelas numéricas quarantined e excluídas da conduta atual)
- Self review L1: completed
- Independent review: not_reviewed
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Fontes curriculares: `Pediatria_SEMIOLOGIA_DO_RECEe_M__816c7efb84` e `semio_PED__c241597932`

## Como cai

Estação ou questão que exige adaptar anamnese/exame à idade, medir crescimento,
interpretar sinais vitais e reconhecer sinais de alarme.

## Conceito operacional mínimo

A consulta pediátrica integra história do cuidador e da criança, idade e contexto,
antropometria em técnica adequada e exame oportunista. Observe antes de tocar; em
criança pequena, deixe procedimentos incômodos para o final quando a segurança
permitir.

## Pivô clínico

Idade, estado geral e tendência ao longo do tempo valem mais que um número isolado.
Faixas de FR/FC/PA dependem de idade, estado (sono/choro/febre), técnica e referência.

## Palavras-âncora

observar antes de tocar · peso/comprimento/estatura/PC · técnica · curva · tendência
· manguito adequado · idade · estado geral · red flags.

## Demanda × movimento

| Demanda | Variável decisiva | Natureza | Erro observável possível | Treino |
|---|---|---|---|---|
| medir | equipamento/técnica/idade | operacional | comparar medida inválida à curva | checklist demonstrado |
| interpretar | percentil/tendência/contexto | misto | diagnosticar por ponto isolado | curvas longitudinais |
| priorizar | estado geral e ABC | operacional | completar exame antes de estabilizar | estação com deterioração |

## Prática clínica atual

- Comprimento é medido em decúbito em menores; estatura em pé quando a criança
  coopera, com técnica e equipamento adequados.
- Pressão arterial pediátrica requer manguito apropriado e interpretação por idade,
  sexo e estatura conforme referência vigente.
- Conte FR por tempo suficiente, idealmente com a criança calma; febre, choro e
  sono alteram sinais vitais.
- Alteração do estado geral, esforço respiratório, má perfusão, rebaixamento,
  rigidez nucal ou déficit focal mudam a prioridade para estabilização/avaliação
  urgente.

## Para a prova/material curricular

Os PDFs apresentam tabelas próprias de FC, FR, PA, fontanelas e sequência do
exame. A transcrição pode ser usada para “segundo a aula”, mas todos os **cortes
numéricos** estão `CURRENT_PENDING` até revisão em referência pediátrica atual.
Não os aplique automaticamente como normalidade clínica.

## Dados de precisão

| Claim | Fonte/localizador | Status |
|---|---|---|
| antropometria e exame por idade | `...816c7efb84`, seção de exame do RN; `...c241597932`, semio PED | CURRICULAR_CHECKED |
| faixas exatas de FC/FR | tabelas dos PDFs | CURRENT_PENDING — excluídas de conduta atual |
| percentis/cortes de PA | tabela curricular | CURRENT_PENDING — usar referência vigente |

## Distratores e guardrails

- “Valor dentro da faixa” não supera criança tóxica ou técnica ruim.
- Um percentil isolado não substitui trajetória de crescimento.
- Não apresentar tabela curricular como protocolo atual sem data/fonte clínica.

## Mini-casos — responda antes de abrir

1. Criança chorando tem FC elevada. É possível classificar pela tabela sem repetir?
2. Peso cruza duas curvas ao longo de meses. O ponto atual “normal” encerra o caso?

<details><summary>Gabarito comentado</summary>

1. Não; acalmar/repetir e interpretar idade/contexto/técnica.
2. Não; a tendência é clinicamente material e exige investigação contextual.

</details>

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Primeiro passo do exame da criança | observar estado geral antes de tocar | sequência |
| Sinal vital pediátrico | idade + estado + técnica + tendência | guardrail |
| Tabela curricular | alinhamento de prova, não vigência automática | proveniência |

## Revisão

Resolver faixas numéricas em fonte pediátrica oficial/primária atual antes de
promover esta cápsula a vigência clínica completa.
