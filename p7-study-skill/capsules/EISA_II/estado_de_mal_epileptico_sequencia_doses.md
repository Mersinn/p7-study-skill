# Estado de mal epiléptico — fases terapêuticas e doses

## Metadados

- Disciplina: EISA_II
- Especialidade: Neurologia
- Unidade: II_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l2
- Transcription: confirmed
- Curricular alignment: confirmed
- Clinical validity: current (overlay ILAE 2026 + ESETT)
- Independent review: reviewed_l2
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Fonte curricular: `FAMENE_FARMACOTERAPIA_DAS_CONVULSO_ES_2024_2__f60caaf147` (slide A)
- Overlay clínico: ILAE, *Status Epilepticus Pocket Card* (2026), seções “Early SE” e “Established SE”; ESETT, doses e desfecho primário

## Como cai

A prova pode reproduzir a sequência histórica do slide. Na prática atual, porém,
há **fases**, não uma fila universal de quatro fármacos. A pergunta decisiva é:
benzodiazepínico adequado já foi administrado em dose suficiente? Se sim e a crise
persiste, escolha uma opção de segunda linha conforme contraindicações e protocolo.

## Conceito operacional mínimo

Crise tônico-clônica contínua por 5 minutos deve ser tratada como estado de mal.
Em paralelo: ABC, monitorização, glicemia, acesso e investigação da causa. Não
atrase o benzodiazepínico para completar exames.

## Pivô clínico

Qual fase já foi tratada adequadamente, e quais contraindicações mudam a opção da
fase seguinte? “Qual fármaco é mais forte?” não é o pivô.

## Palavras-âncora

5 minutos · benzodiazepínico adequado · fase estabelecida · alternativas de
segunda linha · função hepática/renal · ECG/PA · refratário · EEG contínuo.

## Demanda × movimento

| Demanda do item | Variável decisiva | Natureza | Erro observável possível | Treino |
|---|---|---|---|---|
| aplicar limiar | crise tônico-clônica ≥5 min | factual | aguardar 30 min | decisão em casos com 4, 5 e 7 min |
| ordenar | ABC/glicemia em paralelo, benzodiazepínico sem atraso | operacional | aguardar exame antes de tratar | reconstrução temporal |
| discriminar | contraindicações entre opções de segunda linha | misto | recitar fila fixa | casos pareados por comorbidade |

Não inferir “fechamento precoce” ou outro movimento cognitivo sem resposta,
justificativa ou trajetória do aluno; sem sinal, registrar `INDETERMINADO`.

## Prática clínica atual — 2026

### 1. Fase inicial (5–10 min)

Em adultos e crianças >1 ano, a ILAE 2026 lista uma das opções:

| Opção | Dose | Limite/observação |
|---|---:|---|
| Lorazepam IV | 0,1 mg/kg | máx. 4 mg/dose; máx. total 8 mg |
| Diazepam IV | 0,1 mg/kg | 5–10 mg/dose; máx. total 20 mg |
| Midazolam IV/IM | 0,1–0,2 mg/kg | máx. 10 mg/dose; máx. total 20 mg |

Pode-se repetir uma vez após 5–10 minutos se necessário. Via e opção dependem de
acesso, cenário e protocolo; não existe obrigação de começar sempre por diazepam.

### 2. Estado estabelecido

Após benzodiazepínico adequado, são alternativas — não degraus obrigatórios:

| Fármaco | Dose de ataque ILAE 2026 | Precauções centrais |
|---|---:|---|
| Levetiracetam | 60 mg/kg, máx. 4.500 mg, em 15 min | ajustar manutenção à função renal |
| Valproato | 30–40 mg/kg, máx. 3.000 mg, em 10–20 min | evitar quando contraindicado, inclusive contextos hepáticos/gestacionais relevantes |
| Fosfenitoína | 30 mg PE/kg; máx. 150 mg PE/min | dose do pocket card ILAE 2026; contraindicado em bloqueio AV/hipotensão grave; ECG e PA |
| Fenitoína | 20 mg/kg, máx. 1.500 mg; máx. 50 mg/min | ECG e PA; interações e cardiotoxicidade |

No ESETT, levetiracetam 60 mg/kg, **fosfenitoína 20 mg PE/kg** e valproato 40 mg/kg
tiveram eficácia semelhante, controlando o episódio em aproximadamente metade
dos pacientes. A diferença 30 mg PE/kg (pocket card ILAE 2026) × 20 mg PE/kg
(regime do ensaio ESETT) é de **fonte/protocolo**, não deve ser combinada nem
resolvida por média. A prescrição segue o protocolo local aplicável.

### 3. Estado refratário

Persistência após benzodiazepínico e uma terapia de segunda linha exige UTI,
proteção de via aérea conforme necessidade, EEG contínuo e anestésico em protocolo
especializado. A evidência não sustenta uma ordem universal
“fenobarbital → tiopental/propofol” para todos.

## Para a prova/material histórico

O slide de 2024 ensina `diazepam → fenitoína → fenobarbital →
tiopental/propofol`, com doses próprias. Esse encadeamento está
`CURRICULAR_CHECKED`, mas **não deve ser apresentado como algoritmo clínico
vigente**. Se a questão pedir literalmente “segundo o slide”, responda o painel
histórico e diga que a prática atual usa opções por fase.

## Pegadinhas e segurança

- “Mais forte” não justifica pular o benzodiazepínico inicial.
- Falha ao benzodiazepínico não torna fenitoína obrigatória; há alternativas.
- A velocidade antiga de fenobarbital “100 mg/min” não foi validada como regra
  atual e está `QUARANTINED`.
- Se a atividade não fornece idade, peso, via, função hepática/renal, gestação e
  cardiopatia, não simule uma prescrição completa.

## Dados de precisão

| Claim | Valor atual | Fonte/localizador | Status |
|---|---|---|---|
| início do tratamento | crise tônico-clônica aos 5 min | ILAE 2026, Early SE | CURRENT_VERIFIED |
| repetição do benzodiazepínico | uma vez após 5–10 min | ILAE 2026, Early SE | CURRENT_VERIFIED |
| fosfenitoína | 30 mg PE/kg no pocket card; 20 mg PE/kg no ESETT | ILAE 2026 / ESETT Methods | PROTOCOL_DEPENDENT |
| fila histórica de quatro degraus | consta no slide, não é universal hoje | slide 2024 / ILAE 2026 | HISTORICAL_ONLY |

## Distratores sedutores

| Distrator | Por que seduz | Por que erra |
|---|---|---|
| “Fenitoína é sempre a segunda etapa” | reproduz o slide | opções atuais incluem levetiracetam, valproato e fosfenitoína/fenitoína |
| “Esperar exames antes do benzodiazepínico” | parece mais preciso | prolonga emergência tempo-dependente |
| “Fosfenitoína tem uma dose universal” | há dois números válidos publicados | 20 mg PE/kg foi o regime ESETT; o pocket card ILAE 2026 lista 30 mg PE/kg |

## Conduta e guardrails

- Inicial: ABC/glicemia e benzodiazepínico em paralelo.
- Definitiva: segunda linha compatível com contraindicações; refratário → UTI,
  via aérea e EEG contínuo.
- Guardrail: esta cápsula é educacional; dose real exige peso, via, monitorização,
  protocolo local e dupla checagem.

## Mini-casos ativos — responda antes de abrir

1. Crise tônico-clônica há 7 minutos, sem medicação. O que ocorre em paralelo e
   qual a primeira fase farmacológica?
2. Persistência após benzodiazepínico adequado. Que dados mudam a segunda linha?
3. Persistência após segunda linha. Como classificar e qual o destino?

<details><summary>Gabarito comentado</summary>

1. ABC/monitorização/glicemia/acesso em paralelo e benzodiazepínico adequado.
2. Função hepática/renal, gestação, ECG/PA, interações e disponibilidade; escolher
   uma alternativa, não uma fila rígida.
3. Estado refratário: UTI, via aérea conforme necessidade e EEG contínuo.

</details>

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Marco operacional do estado de mal tônico-clônico | 5 minutos | limiar |
| Primeira fase farmacológica | benzodiazepínico adequado, sem atrasar por exames | sequência |
| Segunda linha após benzodiazepínico | levetiracetam, valproato ou fosfenitoína/fenitoína conforme contexto | discriminação |
| Quando é refratário? | persiste após benzodiazepínico + uma segunda linha | limiar |

## Fontes de vigência clínica

- ILAE. *Status Epilepticus Pocket Card*, 2026: https://www.ilae.org/files/dmfile/StatusEpilepticus_pocket_card.pdf
- Kapur et al. ESETT: https://pmc.ncbi.nlm.nih.gov/articles/PMC7098487/
- Chamberlain et al. ESETT por faixa etária: https://pmc.ncbi.nlm.nih.gov/articles/PMC7241415/

## Revisão

- Revisar quando a ILAE atualizar o algoritmo ou o protocolo local mudar.
- Critério de parada: reconhecer a fase e escolher opção compatível com as
  contraindicações em três casos, sem usar a sequência histórica como universal.
