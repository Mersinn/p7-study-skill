# Asma em pediatria — crise aguda e lactente sibilante

## Metadados

- Disciplina: EISCA
- Especialidade: Pneumologia pediátrica
- Unidade: I_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l2
- Transcription: confirmed
- Curricular alignment: confirmed
- Clinical validity: pending (current apenas para claims 6–11 anos registrados; doses ≤5 anos excluídas da conduta atual)
- Independent review: reviewed_l2
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Fonte curricular: `Asma_em_Pediatria__3def9bfd99` (A, MISTA)
- Overlay clínico: GINA 2026 Strategy Report, seções de exacerbação pediátrica

## Conceito operacional mínimo

Na crise, classifique rapidamente por consciência, fala, esforço respiratório,
frequência respiratória/cardíaca e SpO2. Trate em paralelo: SABA inalatório,
oxigênio se hipoxemia e corticoide sistêmico precoce nos casos além dos mais leves.
Não force uma “escada” que espere o SABA falhar para só então administrar o
corticoide.

## Pivô clínico

Há ameaça à vida, hipoxemia, fadiga ou resposta insuficiente? Idade e dispositivo
mudam a dose; SpO2 isolada não escolhe suporte ventilatório.

## Palavras-âncora

fala/consciência · esforço · SpO2 · SABA · pMDI + espaçador · O2 ≥94% ·
corticoide na primeira hora · ipratrópio grave · magnésio não rotineiro.

## Demanda × movimento

| Demanda | Variável decisiva | Natureza | Erro observável possível | Treino |
|---|---|---|---|---|
| classificar | conjunto fala/consciência/esforço/SpO2 | operacional | usar um número isolado | casos com sinais discordantes |
| ordenar | tratamentos concorrentes na primeira hora | operacional | postergar corticoide | linha do tempo |
| prescrever | idade, formulação e dispositivo | misto | usar “gotas” sem concentração | exercícios com formulações |

Sem resposta/justificativa do aluno, o movimento cognitivo é `INDETERMINADO`.

## Prática clínica atual — GINA 2026, 6–11 anos

- SpO2 <92% prediz maior probabilidade de hospitalização; <90% exige terapia
  agressiva. Durante a exacerbação, titule O2 para alvo ≥94%.
- Salbutamol inalatório é a base; pMDI + espaçador é eficiente quando exequível.
- Corticoide sistêmico deve ser administrado na primeira hora em todas as crises,
  exceto as mais leves. Prednisolona: 1–2 mg/kg/dia, máximo 40 mg/dia, por 3–5
  dias no regime citado pelo GINA.
- Ipratrópio é adjuvante nas exacerbações graves, junto ao SABA inicial.
- Sulfato de magnésio IV não é rotina; considerar após falha do tratamento inicial,
  especialmente com hipoxemia persistente ou função pulmonar muito reduzida.
- A evidência para VNI é fraca. SpO2 <94% **não** é indicação automática de VNI;
  alteração de consciência **não** é um simples gatilho isolado de IOT. Decisão de
  suporte ventilatório requer avaliação global, resposta, fadiga e equipe apta.
  Se VNI for tentada, não sedar a criança agitada e monitorar de perto.

## Crianças ≤5 anos

O material traz algoritmos/doses antigos e divergentes. Até que a faixa ≤5 anos
seja revisada em fonte atual específica, os valores de “gotas”, cortes de FC
180/200 e tetos por idade ficam `CURRENT_PENDING`. Para prática, consulte a seção
≤5 anos do GINA/protocolo pediátrico local e prescreva por formulação e dispositivo,
não por “número de gotas” desacompanhado da concentração.

## Para a prova/material histórico

O slide contém tabelas que podem ser cobradas, inclusive prednisona/prednisolona
com tetos diferentes, salbutamol em gotas e algoritmos de GINA anterior. Preserve
esses valores como `CURRICULAR_CHECKED`, sempre em painel separado. A frase
“fenoterol em gotas está suspenso” não recebeu fonte regulatória resolvível nesta
auditoria e fica `QUARANTINED`; não deve ser ensinada como proibição atual.

## Pegadinhas e segurança

- SABA e corticoide não são necessariamente etapas sequenciais.
- SatO2 é parte da gravidade, não um algoritmo de intubação.
- Tórax silencioso, exaustão ou consciência alterada são sinais de ameaça à vida,
  mas o suporte definitivo depende de avaliação da ventilação e resposta.
- Antibiótico não é rotina sem evidência de infecção bacteriana.
- Nebulização pode ser necessária em cenários específicos; “não recomendada” não
  significa proibida. Prefira pMDI + espaçador quando apropriado.
- Não transforme índice preditivo de sibilância em diagnóstico individual certo.

## Dados de precisão

| Claim | Valor atual | Fonte/localizador | Status |
|---|---|---|---|
| alvo O2, 6–11 anos | ≥94% | GINA 2026, exacerbações 6–11 | CURRENT_VERIFIED |
| prednisolona, 6–11 anos | 1–2 mg/kg/d, máx. 40 mg, 3–5 d | GINA 2026, exacerbações 6–11 | CURRENT_VERIFIED |
| VNI | evidência fraca; sem gatilho por SpO2 isolada | GINA 2026, NIV | CURRENT_VERIFIED |
| doses em gotas e cortes ≤5 antigos | aguardam fonte atual específica | slide A antigo | CURRENT_PENDING |

## Distratores sedutores

| Distrator | Por que seduz | Por que erra |
|---|---|---|
| “Só dar corticoide se SABA falhar em 1 h” | falsa escada | deve ser precoce, exceto nas crises mais leves |
| “SpO2 93% = VNI” | número parece decisivo | suporte depende do conjunto clínico/resposta |
| “Magnésio na chegada” | crise grave pede ação | não é rotina; considerar após falha inicial |

## Conduta e guardrails

- Inicial: avaliar gravidade; SABA, O2 se indicado e corticoide precoce; ipratrópio
  em grave.
- Escalonamento: reavaliar técnica/diagnóstico e considerar magnésio/intensivo se
  falha.
- Guardrail: dose real requer idade, peso, concentração, dispositivo, protocolo e
  dupla checagem.

## Mini-casos ativos — responda antes de abrir

1. Criança de 8 anos, SpO2 92%, fala entrecortada e retrações: quais tratamentos
   devem começar sem esperar uma hora?
2. Criança consciente com SpO2 93%: isso sozinho indica VNI?
3. Falha após tratamento inicial, hipoxemia persistente: próximos passos?

<details><summary>Gabarito comentado</summary>

1. SABA + O2 titulado + corticoide precoce; ipratrópio pela gravidade.
2. Não; trate/reavalie o conjunto clínico e a resposta.
3. Reavaliar diagnóstico/técnica, considerar magnésio e cuidado intensivo conforme
   protocolo.

</details>

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Alvo de O2 no GINA 2026, 6–11 anos | ≥94% | alvo |
| Corticoide sistêmico na crise | na 1ª hora, exceto nas mais leves | sequência |
| SpO2 <94% indica VNI? | não; requer avaliação global e resposta | discriminação |
| Magnésio IV | não rotineiro; considerar após falha inicial em crise grave | sequência |

## Fontes de vigência clínica

- GINA. *Global Strategy for Asthma Management and Prevention*, 2026, seção “Management of asthma exacerbations in children 6–11 years”: https://ginasthma.org/wp-content/uploads/2026/05/GINA-2026-Strategy-Report-WMS.pdf

## Revisão

- Revisar quando houver nova versão GINA e antes de liberar doses para ≤5 anos.
- Critério de parada: classificar três crises e ordenar tratamentos concorrentes
  sem usar SpO2 isolada para decidir VNI/IOT.
