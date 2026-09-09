# Assistência ao recém-nascido em sala de parto e reanimação neonatal

## Metadados

- Disciplina: EISCA
- Especialidade: Neonatologia
- Unidade: I_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l2
- Transcription: confirmed
- Curricular alignment: confirmed (material baseado em SBP 2016)
- Clinical validity: current (overlay SBP 2026)
- Independent review: reviewed_l2
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Fonte curricular: `Assiste_ncia_ao_RN_pdf__bc4a064524` — anotação de aula, camada B
- Overlay clínico: Diretrizes SBP/PRN 2026 para RN ≥34 semanas e RN <34 semanas

## Conceito operacional mínimo

Ao nascimento, avalie **respiração/choro** e **tônus flexor**. “Ser a termo” não é
uma terceira pergunta de boa vitalidade na Diretriz SBP 2026. Idade gestacional
define qual algoritmo e qual preparo usar, mas prematuridade isolada não significa
ausência de vitalidade.

## Pivô clínico

Respira/chora e tem tônus flexor? Se não, os passos iniciais produziram ventilação
efetiva e elevação da FC? A qualidade da ventilação vem antes de compressões e
drogas.

## Palavras-âncora

SBP 2026 · respiração/choro + tônus · 15 s · passos iniciais ≤30 s · minuto de
ouro · FC <100 · VPP 30–60/min · FC <60 · 3:1 · adrenalina 1:10.000.

## Demanda × movimento

| Demanda | Variável decisiva | Natureza | Erro observável possível | Treino |
|---|---|---|---|---|
| aplicar critério | respiração/choro + tônus | operacional | usar prematuridade como falha de vitalidade | casos por idade gestacional |
| ordenar | ventilação efetiva antes de compressões | operacional | avançar sem corrigir máscara/via aérea | fluxograma sem respostas |
| calcular dose | concentração, peso e via | misto | confundir mg com mL | cálculo com dupla checagem |

Movimento cognitivo só pode ser atribuído após resposta/justificativa; sem sinal,
use `INDETERMINADO`.

## Prática clínica atual — SBP 2026, RN ≥34 semanas

| Momento | Decisão/ação |
|---|---|
| Boa vitalidade | contato pele a pele, manter normotermia e cuidados de rotina; clampeamento ≥60 s, preferencialmente após iniciar respiração |
| Sem boa vitalidade | estímulo tátil por cerca de 15 s antes do clampeamento; se persistirem apneia/respiração irregular ou flacidez, clampear e levar ao berço aquecido |
| Passos iniciais | calor, posicionar via aérea, secar e estimular; completar em até 30 s; não aspirar de rotina, inclusive no mecônio, salvo obstrução |
| Indicação de VPP | apneia/respiração irregular ou FC <100 bpm após os passos iniciais; iniciar dentro do primeiro minuto |
| VPP inicial ≥34 semanas | ar ambiente (O2 21%), com ajuste por oximetria pré-ductal e resposta |
| VPP | 30–60 ventilações/min; com peça T, pressão inicial usual 20–30 cmH2O e PEEP 5 cmH2O, ajustando à expansão/FC |
| Compressões | FC <60 apesar de ventilação efetiva com movimento torácico; preferir via aérea alternativa; relação 3:1 |
| Adrenalina | após 60 s de compressões coordenadas + ventilação adequada se FC persistir <60; via intravascular preferida |

Adrenalina intravascular 1:10.000: 0,01–0,03 mg/kg (0,1–0,3 mL/kg), podendo
repetir a cada 3–5 min. A via traqueal, enquanto o acesso é obtido, usa dose maior
0,05–0,1 mg/kg (0,5–1 mL/kg). Prescrição real exige protocolo e conferência de
concentração/volume.

Para RN <34 semanas, aplique a diretriz SBP 2026 específica. Não transporte
automaticamente valores do algoritmo ≥34. A concentração inicial de O2 e o suporte
térmico dependem da idade gestacional e devem ser titulados às metas pré-ductais.

## Para a prova/material histórico

O material curricular baseado em SBP 2016 traz “termo? / respira ou chora? / bom
tônus?”, VPP 40–60/min e O2 30% de forma ampla para prematuros. Esses itens ficam
`CURRICULAR_CHECKED`, mas os números que divergem da SBP 2026 estão
`HISTORICAL_ONLY` e não podem orientar prática atual.

## Pegadinhas e segurança

- APGAR descreve adaptação; não decide se deve iniciar VPP e não pode atrasá-la.
- Mecônio não indica aspiração traqueal rotineira.
- Se a FC não sobe, corrija ventilação antes de avançar para compressões/drogas.
- Hérnia diafragmática suspeita exige estratégia específica e descompressão
  gástrica; não aplique ventilação por máscara como rotina.
- Não misture os algoritmos de ≥34 e <34 semanas.

## Dados de precisão

| Claim | Valor atual | Fonte/localizador | Status |
|---|---|---|---|
| boa vitalidade | respiração/choro + tônus flexor | SBP 2026 ≥34, algoritmo inicial | CURRENT_VERIFIED |
| VPP | 30–60/min, no primeiro minuto quando indicada | SBP 2026 ≥34, VPP | CURRENT_VERIFIED |
| compressões | FC <60 após ventilação efetiva; 3:1 | SBP 2026 ≥34, massagem cardíaca | CURRENT_VERIFIED |
| VPP 40–60/min | material antigo | anotação baseada em SBP 2016 | HISTORICAL_ONLY |

## Distratores sedutores

| Distrator | Por que seduz | Por que erra |
|---|---|---|
| “Prematuro = sem boa vitalidade” | algoritmo antigo começa perguntando se é termo | IG seleciona protocolo; vitalidade usa respiração/choro e tônus |
| “Mecônio exige aspiração” | regra antiga | aspiração não é rotineira sem obstrução |
| “FC 50: comprimir imediatamente” | urgência aparente | primeiro confirme ventilação efetiva com movimento torácico |

## Conduta e guardrails

- Inicial: preparar por IG, avaliar vitalidade, passos iniciais e VPP no minuto de
  ouro quando indicada.
- Definitiva: corrigir ventilação; depois compressões/via alternativa/adrenalina
  conforme FC e tempo.
- Guardrail: dose real exige peso, concentração, via, protocolo SBP vigente e
  dupla checagem.

## Mini-casos ativos — responda antes de abrir

1. RN de 39 semanas, chorando e com tônus flexor. Qual a conduta?
2. RN de 38 semanas, apneico, FC 80 após passos iniciais. Próximo passo?
3. FC 50 após VPP. Que evidência deve existir antes de comprimir?

<details><summary>Gabarito comentado</summary>

1. Rotina/pele a pele e clampeamento oportuno.
2. VPP efetiva dentro do primeiro minuto com O2 21%, reavaliando FC e tórax.
3. Movimento torácico/ventilação efetiva; então via alternativa e compressões 3:1.

</details>

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Boa vitalidade na SBP 2026 | respiração/choro + tônus flexor | critério |
| VPP: quando e quando iniciar? | apneia/irregular ou FC <100; no primeiro minuto | sequência |
| Frequência VPP | 30–60/min | valor |
| Compressões | FC <60 após ventilação efetiva; 3:1 | limiar |

## Fontes de vigência clínica

- SBP/PRN. *Reanimação do RN ≥34 semanas*, 12 jun. 2026: https://www.sbp.com.br/wp-content/uploads/2026/06/PRN-SBP-Diretrizes-2026-Reanimacao-RN-igual-maior-34-semanas-12junho2026.pdf
- SBP/PRN. *Reanimação do RN <34 semanas*, 12 jun. 2026: https://www.sbp.com.br/wp-content/uploads/2026/06/PRN-SBP-Diretrizes-2026-Reanimacao-RN-menor-34-semanas-12junho2026.pdf

## Revisão

- Revisar a cada atualização do PRN/SBP.
- Critério de parada: executar três cenários sem usar APGAR como gatilho, sem
  pular correção da ventilação e sem misturar algoritmo de prematuro.
