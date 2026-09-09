# Imunizações — calendário PNI 2026 e princípios

## Metadados

- Disciplina: EISCA
- Especialidade: Pediatria/Imunizações
- Unidade: IV_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l2
- Transcription: confirmed
- Curricular alignment: confirmed (slide 2021)
- Clinical validity: current para sentinelas registradas; calendário integral exige consulta datada
- Independent review: reviewed_l2
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Fonte curricular: `Imunizac_a_o_ativa_e_Passiva_2021_Joa_o_Medeiros__830d00b9a4` (A)
- Overlay: Ministério da Saúde, Instrução Normativa do Calendário Nacional de Vacinação 2026 e calendário da criança atualizado em 29/07/2026

## Como cai

As questões misturam mecanismo (ativa/passiva), idade oportuna, recuperação de
esquema e contraindicações. Toda resposta de calendário deve declarar **PNI + ano**;
não misture PNI, SBIm e CRIE como se fossem a mesma agenda.

## Conceito operacional mínimo

Imunização ativa induz resposta do hospedeiro; passiva entrega anticorpos e tem
proteção imediata, geralmente temporária. Em atraso vacinal, não reinicie séries
automaticamente: reconstrua histórico, idade, grupo especial e regra vigente.

## Pivô clínico

Idade exata, histórico documentado, condição especial e jurisdição (PNI/SUS,
CRIE ou rede privada) mudam a conduta.

## Palavras-âncora

PNI 2026 · agenda oportuna · atualização do cartão · não reiniciar · HPV4 dose
única · menC 3/5 meses · menACWY 12 meses · transição VPC10→VPC20 · CRIE.

## Demanda × movimento

| Demanda | Variável decisiva | Natureza | Erro observável possível | Treino |
|---|---|---|---|---|
| recuperar esquema | idade + doses comprovadas | operacional | reiniciar série | três cartões incompletos |
| aplicar janela | vacina, grupo e ano | misto | usar tabela 2021 | comparar PNI 2021×2026 |
| discriminar | PNI vs CRIE/SBIm | factual | atribuir vacina privada ao SUS | classificação de fonte |

## Dados de precisão — sentinelas PNI 2026

| Claim | PNI 2026 | Localizador | Status |
|---|---|---|---|
| HPV4 rotina | 9 a 14a11m29d; dose única na rotina | IN 2026, pp.45–46 | CURRENT_VERIFIED |
| HPV resgate | 15 a 19a11m29d, estratégia conforme organização estadual, dose única | IN 2026, p.46 | CURRENT_VERIFIED |
| meningocócica | menC aos 3 e 5 meses; reforço menACWY aos 12 meses | IN 2026, pp.22–23 | CURRENT_VERIFIED |
| adolescente menACWY | dose/reforço aos 11 anos; oportunidade até 14a11m29d | IN 2026, p.34 | CURRENT_VERIFIED |
| pneumocócica | transição VPC10→VPC20; esquema depende do histórico | IN 2026, pp.17–21 | CURRENT_VERIFIED |
| dengue | 10 a 14a11m29d; 2 doses, intervalo 3 meses | IN 2026, pp.48–49 | CURRENT_VERIFIED |

O calendário completo é dinâmico. Para qualquer decisão individual, abra a versão
oficial vigente e use a tabela/nota correspondente; esta cápsula não substitui a
agenda integral nem o Manual CRIE.

## Para a prova/material histórico

O slide 2021 ensina HPV com faixas diferentes por sexo e duas doses, além de
esquemas meningocócicos/pneumocócicos anteriores. Esses dados ficam
`CURRICULAR_CHECKED` e `HISTORICAL_ONLY`; não são prática PNI 2026.

## Pegadinhas e distratores

| Distrator | Por que seduz | Por que erra |
|---|---|---|
| “HPV: meninas 9–14, meninos 11–14, duas doses” | era regra do slide | rotina PNI 2026 é 9–14a11m29d, dose única |
| “MenC também é o reforço de 12 meses” | mantém o produto da série | reforço 2026 é menACWY |
| “VPC20 já substituiu VPC10 em toda dose” | incorporação anunciada | há fase de transição dependente do histórico |

## Conduta e guardrails

- Confira cartão e sistema, idade em dia/mês/ano e condição especial.
- Consulte o calendário PNI datado e a seção de atualização, sem reiniciar série
  por conta própria.
- Não extrapole rotina para imunossuprimido, exposição, violência sexual ou CRIE.

## Mini-casos — responda antes de abrir

1. Menino de 10 anos sem HPV: qual esquema de rotina PNI 2026?
2. Lactente completou menC aos 3 e 5 meses: qual reforço aos 12 meses?
3. Criança em transição VPC10/VPC20: pode-se decidir sem histórico?

<details><summary>Gabarito comentado</summary>

1. Uma dose HPV4 na rotina.
2. Uma dose menACWY.
3. Não; a regra de transição depende das doses comprovadas.

</details>

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| HPV rotina PNI 2026 | 9–14a11m29d, dose única | janela |
| menC/menACWY criança | 3 e 5 meses; reforço menACWY aos 12 | sequência |
| VPC10→VPC20 | transição dependente do histórico | guardrail |

## Fontes de vigência clínica

- Ministério da Saúde. Instrução Normativa CNV 2026: https://www.gov.br/saude/pt-br/vacinacao/publicacoes/instrucao-normativa-que-instrui-o-calendario-nacional-de-vacinacao-2026.pdf
- Calendário da criança, atualizado 29/07/2026: https://www.gov.br/saude/pt-br/vacinacao/arquivos/calendario-nacional-de-vacinacao-crianca/view

## Revisão

Revisar mensalmente e sempre antes de responder calendário individual, porque o
PNI pode mudar durante o ano.
