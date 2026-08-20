# Transtorno Bipolar e Estabilizadores do Humor (lítio, valproato, carbamazepina, lamotrigina)

## Metadados

- Disciplina: EISM
- Especialidade: Psiquiatria
- Unidade: II
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l2
- Transcription: confirmed
- Curricular alignment: confirmed
- Clinical validity: pending (current apenas para claims EXTRIP; demais claims terapêuticos excluídos da conduta atual)
- Independent review: reviewed_l2
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Camada de fonte usada: A+B
- fonte_visual: não (fontes atribuídas são todas NATIVA com texto íntegro; não há MISTA/ESCANEADA neste tema)
- Fontes usadas: Aula_1_2021_1_Transtorno_Bipolar__c902ef25a4 (A, slide do prof. Ricardo Henrique-Araújo); Transtorno_bipolar__6d1cddef8b (B, Aline Maia); ANOTAC_O_ES_bipolaridade__a1c9d4465d (B, Karen); Transtorno_bipolar_pdf__dc69aa8c73 (B, Letícia)
- Evidência de prova/devolutiva: blueprint — "Transtorno bipolar do humor — fases, litemia-alvo, estabilizadores x antipsicóticos na mania, monoterapia na fase depressiva" (frequência alta; evidência: prova digitada.pdf Q1,4,9,10; Saúde Mental.pdf devolutiva II Q1; Integrada Q53,623-627)
- Limitações da fonte: o slide do professor (2021.1) cita gráficos de evidência CANMAT 2018 (mania aguda, depressão bipolar, manutenção) que são apenas imagens de tabela sem OCR capturado — não foi possível conferir o conteúdo textual desses gráficos, apenas a citação; 2 pequenas divergências numéricas entre fontes B ficaram registradas na tabela abaixo
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

MCQ de 5 alternativas e V/F. Evidência de cobrança: diferenciação de fases (mania, hipomania,
depressão bipolar, episódio misto), litemia-alvo, quando usar estabilizador × quando associar
antipsicótico atípico na mania aguda, e a regra de nunca tratar depressão bipolar com
antidepressivo em monoterapia.

## Conceito operacional mínimo

Transtorno bipolar tipo I: pelo menos 1 episódio de MANIA ou misto (com ou sem depressão — 1
episódio de mania já fecha o diagnóstico de tipo I, mesmo que o paciente nunca tenha tido
depressão). Tipo II: pelo menos 1 episódio de hipomania + pelo menos 1 episódio depressivo maior
(nunca teve mania — se tiver, vira tipo I). Lítio é a base do tratamento em todas as fases;
anticonvulsivantes (valproato, carbamazepina) agem mais rápido na mania aguda; lamotrigina previne
depressão mas não trata mania.

## Pivô clínico

Nunca prescrever antidepressivo isolado em bipolar — a escolha na depressão bipolar deve seguir
diretriz atual e considerar risco de virada. Na escolha do estabilizador, função renal/hepática,
interações, gestação e gravidade modulam risco; “nefropata nunca usa lítio” e “hepatopata deve usar
lítio” são absolutos indevidos e ficam `CURRENT_PENDING`. Na mania aguda, lítio tem início lento (1–3
semanas) — valproato/carbamazepina agem mais rápido (3–5 dias) e são preferidos para tirar o
paciente da crise; antipsicótico atípico associado acelera ainda mais a resposta.

## Palavras-âncora

litemia · ciclagem rápida · virada maníaca · episódio misto · mania eufórica × disfórica ·
hipomania · monoterapia com antidepressivo (evitar) · função renal/hepática ·
interações · síndrome de Stevens-Johnson (lamotrigina/carbamazepina)

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | indicação EXTRIP integra litemia, função renal, sintomas e cinética prevista | limiar | misto | valor errado | casos pareados com mesma litemia e sintomas/função renal diferentes |
| reconhecer risco | função renal/hepática, interação, gestação e gravidade modulam escolha | contraindicacao | misto | aplicar troca automática | casos que exigem dados antes de escolher |
| diferenciar próximos | história pregressa de mania (mesmo remota) fecha tipo I, mesmo com quadro atual só depressivo | sinal-achado | operacional | narrativa acima do discriminador | antes de classificar, perguntar por escrito "já houve UM episódio de mania em qualquer momento da vida?", ignorando o quadro do dia |
| reconhecer contraindicação | antidepressivo isolado em bipolar exige associação a estabilizador/antipsicótico (risco de virada) | contraindicacao | operacional | regra mal-aprendida | antes de tratar "depressão", checar se há diagnóstico de base bipolar — nunca aplicar a regra "deprimido = AD" sem essa checagem |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Litemia — fase aguda | 0,8–1,2 mEq/L | 4 fontes convergentes (A + 3 B) | CONFIRMADO |
| Litemia — fase de manutenção | A partir de 0,6 mEq/L | 4 fontes convergentes | CONFIRMADO |
| Litemia — risco de intoxicação | Acima de 1,2 mEq/L | Karen p.5 (B) | CONFIRMADO (1 fonte B; consistente com o teto da faixa aguda) |
| Lítio — início de ação | Lento: 1–3 semanas | A (slide) + B | CONFIRMADO |
| ECTR no lítio — recomendado | função renal prejudicada + Li >4,0 mEq/L; ou rebaixamento de consciência, convulsão ou disritmia ameaçadora independentemente do nível | EXTRIP, Table 7 | CURRENT_VERIFIED |
| ECTR no lítio — sugerido | Li >5,0 mEq/L; confusão significativa; ou tempo estimado até Li <1,0 mEq/L >36 h | EXTRIP, Table 7 | CURRENT_VERIFIED |
| Parada e rebote | parar quando Li <1,0 mEq/L ou melhora clínica; se nível indisponível, mínimo 6 h; dosar serialmente por 12 h após parar | EXTRIP, Table 7 | CURRENT_VERIFIED |
| Cortes antigos de diálise | >6/>4/2,5–4 mEq/L | slide A 2021 | HISTORICAL_ONLY |
| Lítio — proteção contra suicídio | ~80% menor | 4 fontes convergentes | CONFIRMADO |
| Episódio maníaco — duração/critérios | ≥1 semana (ou menos se hospitalização); ≥3 critérios (≥4 se humor só irritável) de 7 | 4 fontes convergentes | CONFIRMADO |
| Episódio hipomaníaco — duração | ≥4 dias | 4 fontes convergentes | CONFIRMADO |
| Episódio depressivo (bipolar) — duração/critérios | ≥2 semanas; ≥5 de 9 critérios | 4 fontes convergentes | CONFIRMADO |
| Ciclagem rápida | ≥4 episódios de humor patológico em 12 meses (intervalo de 2 meses entre eles) | A (slide) | CONFIRMADO |
| Prevalência tipo I / tipo II | 1% / 1,1% | A + Aline + Letícia (3 fontes) | CONFIRMADO_COM_CORREÇÕES — Karen diverge para 1,6% no tipo II (1 fonte B; prevalece 1,1%, maioria + camada A) |
| Concordância gêmeos monozigóticos | 40–45% | 4 fontes convergentes | CONFIRMADO |
| Risco de suicídio — tentativa / consumado | 20–55% tentam / 10–15% morrem | A + Letícia (20–55%); Karen diverge para 25–56% | CONFIRMADO_COM_CORREÇÕES — divergência pequena, mesma ordem de grandeza |
| Lamotrigina — titulação | Aumento lento, ~25mg/dia a cada 2 semanas, até ~200mg/dia em 6–7 semanas | A (slide) + Karen (B) | CONFIRMADO |

## Pegadinhas

- “Lítio sozinho não trata depressão bipolar” é uma afirmação forte do material que não foi
  validada como prática atual e fica `CURRENT_PENDING`; não a ensine como proibição universal.
- Lamotrigina não tem eficácia relevante na mania — é droga de prevenção/tratamento da depressão,
  não estabilizador de crise aguda.
- Doença renal/hepática exige avaliação individual, ajuste/monitorização e diretriz atual; não
  faça troca automática entre lítio e valproato.
- Bipolar tipo I é definido por mania OU episódio misto, independentemente de já ter tido
  depressão — não confundir com tipo II, que exige hipomania + depressão e NUNCA teve mania.
- Em números absolutos, pessoas com depressão morrem mais por suicídio que bipolares (maior
  prevalência populacional), mas em risco relativo o bipolar tem risco maior.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Antidepressivo isolado para depressão bipolar | "O paciente está deprimido, trate a depressão" | regra mal-aprendida | Sem associação a estabilizador/antipsicótico atípico, risco de virada maníaca ou não-resposta |
| Lamotrigina para tirar paciente da mania aguda | Parece um "estabilizador do humor" genérico | analogia sem validação | Lamotrigina não tem eficácia relevante na mania — serve para prevenir/tratar depressão |
| Aplicar apenas um corte sérico para diálise | é fácil memorizar | premissa não checada | EXTRIP integra função renal, sintomas e cinética |
| Dar carvão ativado para lítio | funciona em muitas intoxicações | analogia sem validação | carvão ativado não adsorve lítio |

## Conduta

- Conduta do transtorno bipolar: os esquemas desta cápsula vêm do material
  curricular e permanecem `CURRENT_PENDING`; não escolher lítio/valproato por uma
  troca automática. Use diretriz atual, fase, gravidade, função renal/hepática,
  gestação, interações, adesão e preferência.
- Condição da conduta: se a depressão bipolar exigir antidepressivo, associar sempre a
  estabilizador do humor ou antipsicótico atípico.
- Diferencial perigoso: intoxicação por lítio exige interromper exposição, suporte com fluido
  isotônico quando indicado e dosagens seriadas de lítio/função renal/eletrólitos. Carvão
  ativado não adsorve lítio. Acione toxicologia/nefrologia cedo quando houver critério EXTRIP.
- O que mudaria a decisão: função renal/hepática, gestação, interações, episódio
  atual e histórico de resposta. Nenhum desses dados autoriza automaticamente
  “trocar pelo outro”.

## Mini-casos ativos

1. Paciente bipolar com doença renal precisa de estabilizador. Que dados faltam
   antes de escolher? <details><summary>Resposta</summary>Estágio/função renal,
   fase, outros órgãos, interações, gestação, resposta prévia e alternativas; não
   trocar automaticamente para valproato.</details>
2. Paciente com hepatopatia: a resposta automática “use lítio” é segura?
   <details><summary>Resposta</summary>Não; exige avaliação individual/diretriz.</details>
3. Paciente com lítio 4,2 mEq/L e função renal prejudicada. Antes de abrir a resposta, classifique
   pelo EXTRIP. <details><summary>Resposta</summary>ECTR recomendada: função renal prejudicada + Li >4,0 mEq/L.</details>
4. Paciente com quadro depressivo isolado hoje, mas relata 1 episódio de mania há anos → ainda é
   bipolar tipo I (basta 1 episódio de mania, mesmo que hoje só haja depressão). Variável decisiva:
   história pregressa de mania, não o quadro atual.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Litemia — fase aguda × manutenção | Aguda: 0,8–1,2 mEq/L. Manutenção: a partir de 0,6 mEq/L | dado numérico |
| EXTRIP — indicação com função renal prejudicada | Li >4,0 mEq/L | dado numérico |
| EXTRIP — sintomas que recomendam ECTR sem depender do nível | rebaixamento de consciência, convulsão ou disritmia ameaçadora | risco |
| Função renal/hepática | modula risco; não autoriza troca automática entre lítio/valproato | guardrail |
| Bipolar tipo I × tipo II | Tipo I: ≥1 mania/misto (± depressão). Tipo II: hipomania + depressão, nunca mania | discriminador |
| Lítio — proteção contra suicídio | ~80% menor | dado numérico |

## Revisão

- Revisar quando: antes de simulado que combine diagnóstico diferencial de fases do humor com
  escolha de estabilizador por comorbidade.
- Critério de parada: quando conseguir, sem consultar a tabela, citar a litemia-alvo de cada fase,
  os critérios EXTRIP e explicar por que litemia isolada não resume a decisão.

## Prática clínica atual — intoxicação por lítio

ECTR é recomendada/sugerida pelos critérios acima; hemodiálise intermitente é o
método preferido e terapia contínua é alternativa aceitável. Após ECTR, monitore
lítio por 12 h para rebote. O painel antigo de cortes fica apenas para prova.

Fonte: EXTRIP Workgroup, *Extracorporeal Treatment for Lithium Poisoning*,
Table 7, 2015: https://pmc.ncbi.nlm.nih.gov/articles/PMC4422246/
