# Síndrome de Abstinência Alcoólica, Delirium Tremens e Encefalopatia de Wernicke-Korsakoff

## Metadados

- Disciplina: EISM
- Especialidade: Psiquiatria
- Unidade: III
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l2
- Transcription: confirmed
- Curricular alignment: confirmed
- Clinical validity: pending (current para claims ASAM; alta dose excluída sem protocolo)
- Independent review: reviewed_l2
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Camada de fonte usada: A+B
- fonte_visual: sim (`Transtornos_por_abuso_de_substancias___136c015a4a` pp. 3–5)
- Fontes usadas: Mariah_Carvalho_Mo_dulo_Sau_de_Mental__2b7d072985; Psiquiatria_DEPENDE_NCIA_QUI_MICA__e854a68d79; A_lcool_e_Outras_Drogas__ebaba69a52; transtornos_por_uso_de_subst_ncias__554a1a793f; Transtornos_por_abuso_de_substancias___136c015a4a
- Evidência de prova/devolutiva: sem questão registrada; a regra “tiamina antes
  da glicose” aparece como orientação curricular histórica, não como prática atual.
- Limitações da fonte: dose profilática de tiamina pré-glicose diverge entre fontes (ver tabela); a camada A disponível (slide "Henrique Araújo, 2024") não cobre a intoxicação aguda, só a abstinência/DT já estabelecidos — não foi possível confirmar visualmente esse número específico.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

Sem evidência de questão registrada no Source Pack para este tema específico. Segue o padrão geral do cluster: vinheta de paciente etilista em emergência ou internado desenvolvendo confusão, pedindo conduta imediata.

## Conceito operacional mínimo

Síndrome de Abstinência Alcoólica (SAA) surge após interrupção/redução do consumo
crônico. Delirium Tremens é sua forma grave. Wernicke é emergência por deficiência
de tiamina em pessoa de risco; trate tiamina prontamente, sem transformar isso em
motivo para atrasar correção de hipoglicemia.

## Pivô clínico

Na hipoglicemia verdadeira, **não atrase glicose**. Administre tiamina antes ou
concomitantemente quando viável, mas a ordem não pode prolongar neuroglicopenia.
Separe profilaxia em pessoa de risco de tratamento da encefalopatia de Wernicke
suspeita/estabelecida, que usa protocolos de dose maior.

## Palavras-âncora

CIWA-Ar; tríade de Wernicke (confusão + nistagmo + ataxia); Korsakoff (confabulação, geralmente irreversível); microzoopsias/alucinações filamentares; diazepam padrão-ouro.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| conduta inicial | hipoglicemia: glicose imediata; tiamina antes/concomitante quando viável, sem atrasar | sequencia | operacional | regra mal-aprendida | casos com e sem hipoglicemia documentada |
| reconhecer contraindicação | BZD contraindicado na intoxicação aguda (soma GABAérgica) × padrão-ouro na abstinência/DT — a prova troca os dois contextos | contraindicacao | operacional | pivô perdido | par de vinhetas idênticas na apresentação motora, trocando só intoxicação × abstinência, forçando nomear o contexto antes de escolher o fármaco |
| identificar complicação | confusão aguda em etilista não é automaticamente DT — excluir TCE, meningite, hepatopatia descompensada antes de fechar | sinal-achado | operacional | fechamento precoce | checklist diferencial obrigatório (TCE/meningite/hepatopatia) antes de aceitar delirium tremens como diagnóstico |
| aplicar critério | janela temporal que diferencia SAA inicial (horas), pico (24–36h) e Delirium Tremens (72–96h) | limiar | factual | valor errado | card de linha do tempo + vinhetas no valor exato de cada corte |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Profilaxia de Wernicke em risco | tiamina 100 mg IV/IM/dia por 3–5 dias é o regime típico ASAM; via parenteral preferida em má nutrição/malabsorção/abstinência grave | ASAM 2020, Recomendação V.7 | CURRENT_VERIFIED |
| Ordem glicose/tiamina | podem ser dadas em qualquer ordem ou concomitantemente; glicose não deve ser atrasada na hipoglicemia | ASAM 2020, Recomendação V.7 | CURRENT_VERIFIED |
| Wernicke suspeita/estabelecida | dose alta é protocolo-dependente; não fundir com dose profilática | MS Linha de Cuidado, avaliação/conduta hospitalar | PROTOCOL_DEPENDENT |
| Início da SAA | poucas horas; slide especifica “a partir de 6h” | fontes curriculares | CURRICULAR_CHECKED; CURRENT_PENDING |
| Pico da SAA | 24–36h | 3 fontes NATIVA | CONFIRMADO |
| Duração (autolimitada) | 7–10 dias | 3 fontes NATIVA + visual p.4 | CONFIRMADO |
| SAA leve-moderada | 90% dos dependentes; 10% grave, metade destes evolui para Delirium Tremens | Psiquiatria_DEPENDE_NCIA p.4 | CONFIRMADO |
| CIWA-Ar (10 itens) | Leve 0–9; Moderada 10–18; Grave >18 | fonte curricular única | QUARANTINED para conduta atual |
| Delirium Tremens — janela de início | entre 72–96h (24–150h) após interrupção, em ~5% das SAA; visual descreve "a partir do 3º dia" | 3 fontes NATIVA; Transtornos_por_abuso p.3 | CONFIRMADO |
| Mortalidade do DT | 5–10% se tratado; até 25% se não tratado | 3 fontes NATIVA + visual p.3 | CONFIRMADO |
| Tríade de Wernicke | confusão mental + nistagmo + ataxia | Psiquiatria_DEPENDE_NCIA p.4; A_lcool_e_Outras_Drogas p.5 | CONFIRMADO |
| Tiamina — regra antiga pré-glicose | 100 vs 300 mg em fontes divergentes | fontes curriculares | HISTORICAL_ONLY; substituída pelo overlay ASAM |
| Tiamina — Wernicke suspeita | 100–250 mg vs 500 mg 3x/dia no acervo | fontes curriculares | QUARANTINED; seguir protocolo atual |
| Diazepam/lorazepam — esquemas do slide | doses/intervalos antigos | fontes curriculares | CURRENT_PENDING; excluídos da prescrição atual |
| Redução gradual dos sedativos | idealmente em até 14 dias, para não gerar dependência de BZD | Psiquiatria_DEPENDE_NCIA p.5 | confirmar no slide (só 1 fonte cita o prazo) |
| Agitação na intoxicação alcoólica aguda | Haloperidol 5mg VO/IM; evitar BZD (mesmo receptor GABAérgico do álcool → efeito somatório deprime mais o SNC) | 3 fontes NATIVA; Mariah_Carvalho | CONFIRMADO |

## Pegadinhas

- Tiamina sempre antes (ou junto) da glicose, nunca depois — inverter a ordem pode precipitar Wernicke.
- Na intoxicação alcoólica aguda (não na abstinência), BZD é contraindicado para agitação — usar haloperidol. Na abstinência/delirium tremens, BZD é o tratamento de escolha. A prova troca esses dois contextos.
- Wernicke não tratada evolui para Korsakoff (dano cognitivo, confabulação), predominantemente irreversível.
- Nem todo paciente etilizado está hipoglicêmico. Se houver hipoglicemia, trate-a
  imediatamente e dê tiamina antes/concomitante quando viável; não espere a
  tiamina para corrigir neuroglicopenia.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Aguardar tiamina para tratar hipoglicemia grave | repete a regra “tiamina primeiro” | regra mal-aprendida | ASAM permite qualquer ordem/concomitância; neuroglicopenia não deve ser prolongada |
| Abstinência alcoólica agitada: usar haloperidol isolado, como na intoxicação aguda | Mesmo fármaco "seguro" já usado antes | pivô perdido | Na abstinência/DT, o sedativo de escolha é BZD (diazepam), não haloperidol isolado |
| Diazepam IM para abstinência grave, buscando absorção rápida | Via IM parece garantir absorção mais rápida | premissa não checada | Absorção IM do diazepam é errática — via oral ou EV é a preferida |

## Conduta

- Inicial: reconhecer síndrome, medir glicemia e tratar hipoglicemia sem atraso;
  tiamina parenteral antes/concomitante quando possível.
- Definitiva: benzodiazepínico e nível de cuidado conforme gravidade/protocolo;
  profilaxia típica ASAM 100 mg IV/IM/dia por 3–5 dias. Suspeita de Wernicke exige
  regime de alta dose do protocolo local, sem adotar automaticamente um dos três
  valores divergentes do material.
- Condição da conduta: confusão mental/ataxia/nistagmo (Wernicke) → aumentar dose de tiamina; hepatopatia → preferir lorazepam a diazepam; abstinência leve-moderada → manejo ambulatorial possível (90% dos casos); grave/delirium tremens → internação hospitalar, considerar UTI.
- Diferencial perigoso: não atribuir toda confusão aguda a delirium tremens sem excluir TCE (queda durante embriaguez), meningite, hepatopatia descompensada — exame neurológico cuidadoso é obrigatório.
- O que mudaria a decisão: sinais da tríade de Wernicke → escalar dose de tiamina; doença hepática → trocar diazepam por lorazepam; necessidade de manejo de via aérea/parada respiratória → diazepam EV com retaguarda.

## Mini-casos ativos

Etilista crônico, 30h sem beber, tremores/sudorese/taquicardia, sem confusão mental → SAA leve-moderada, provável manejo ambulatorial com BZD.

Mesmo paciente, no 4º dia, confuso, alucinações visuais de pequenos animais, hiperatividade autonômica → Delirium Tremens, internação, diazepam + tiamina em dose alta se houver nistagmo/ataxia associados.

Variável decisiva: paciente etilista desnutrido chega em coma hipoglicêmico. O que
não pode ser atrasado? <details><summary>Resposta</summary>Glicose imediata; tiamina
antes ou concomitante quando viável, sem prolongar a hipoglicemia.</details>

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Ordem tiamina x glicose na hipoglicemia | não atrasar glicose; tiamina antes/concomitante quando viável | pegadinha |
| Tríade de Wernicke | Confusão mental + nistagmo + ataxia | dado |
| BZD na intoxicação aguda por álcool | Contraindicado (soma efeito GABAérgico) | pegadinha |
| BZD na abstinência/Delirium Tremens | Tratamento de escolha (diazepam VO, padrão-ouro) | conduta |
| Mortalidade do Delirium Tremens não tratado | Até 25% | dado |
| Pico da SAA | 24–36h | dado |
| Wernicke não tratada evolui para | Korsakoff (confabulação, geralmente irreversível) | dado |

## Revisão

- Revisar quando: antes de vinheta com etilista em emergência ou paciente internado que evolui com confusão.
- Critério de parada: diferenciar profilaxia de Wernicke suspeita e não atrasar
  glicose em três vinhetas.

## Fonte de vigência clínica

- ASAM. *Clinical Practice Guideline on Alcohol Withdrawal Management*,
  Recomendação V.7: https://www.asam.org/docs/default-source/quality-science/the_asam_clinical_practice_guideline_on-alcohol-1.pdf
- Ministério da Saúde. Linha de Cuidado — manejo inicial: https://linhasdecuidado.saude.gov.br/portal/transtornos-por-uso-de-alcool-no-adulto/servico-de-atendimento-movel/manejo-inicial/
