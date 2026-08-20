# AVC isquêmico: urgência, trombólise e trombectomia

## Metadados

- Disciplina: EISA_II
- Especialidade: Neurologia
- Unidade: I_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l2
- Transcription: confirmed
- Curricular alignment: confirmed
- Clinical validity: current (overlay AHA/ASA 2026)
- Independent review: reviewed_l2
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Fonte curricular: `P7_avc_1__5ccf1d6c11` (A) e `AVCI_urge_ncia_neurolo_gica_II_unidade__bec5d0b3b8` (B)
- Overlay clínico: AHA/ASA, *2026 Guideline for the Early Management of Patients With Acute Ischemic Stroke*, DOI 10.1161/STR.0000000000000513

## Conceito operacional mínimo

AVC é uma emergência clínica **tecidual**, não “déficit >24 h”. Sintomas que
regridem podem ser AIT ou AVC com infarto; duração isolada não fecha o diagnóstico.
Registre última vez visto bem, faça TC sem contraste rapidamente para excluir
hemorragia e avalie reperfusão sem atrasos evitáveis.

## Pivô clínico

O déficit é incapacitante? Qual foi a última vez visto bem? A TC excluiu
hemorragia? Há oclusão de grande vaso e critérios clínico-radiológicos para EVT?

## Palavras-âncora

última vez visto bem · déficit incapacitante · TC sem contraste · alteplase ou
tenecteplase · 4,5 h · DWI–FLAIR/perfusão · grande vaso · seleção até 24 h.

## Demanda × movimento

| Demanda | Variável decisiva | Natureza | Erro observável possível | Treino |
|---|---|---|---|---|
| priorizar | TC e avaliação de IVT sem atraso | operacional | esperar angio/perfusão na janela padrão | linha do tempo |
| discriminar | incapacitante vs NIHSS numérico | misto | excluir NIHSS baixo automaticamente | casos pares |
| selecionar | vaso, tempo e imagem para EVT | misto | tratar 24 h como autorização automática | três cenários de imagem |

Só nomeie movimento cognitivo após evidência da resposta; caso contrário,
registre `INDETERMINADO`.

## Prática clínica atual — AHA/ASA 2026

### Trombólise intravenosa

- Alteplase **ou tenecteplase** podem ser usadas em pacientes elegíveis dentro de
  4,5 h, conforme protocolo.
- Déficit **incapacitante** pode justificar trombólise mesmo com NIHSS baixo; não
  use `NIHSS ≥4` como corte obrigatório.
- Dentro da janela padrão, neuroimagem avançada não deve atrasar a trombólise.
- Déficit não incapacitante (por exemplo, sensitivo isolado) costuma favorecer
  dupla antiagregação de curto prazo em vez de trombólise, se o paciente preencher
  os critérios correspondentes.
- Início desconhecido não é contraindicação automática: pacientes selecionados
  podem receber trombólise por mismatch DWI–FLAIR ou perfusional; seleção por
  imagem também pode alcançar casos de 4,5–9 h.

### Trombectomia mecânica

- Suspeita de oclusão de grande vaso requer imagem vascular rápida, adquirida em
  paralelo quando possível; ela não deve atrasar trombólise elegível.
- Trombectomia pode beneficiar pacientes selecionados até 24 h, conforme vaso,
  déficit, imagem e critérios do serviço. “Até 24 h” não significa elegibilidade
  automática sem seleção.
- A diretriz 2026 ampliou a indicação para alguns pacientes com grande core; isso
  não transforma ASPECTS baixo em indicação universal.
- Oclusão de basilar em até 24 h com NIHSS ≥10 tem recomendação forte quando os
  demais critérios são atendidos.

### Suporte que não deve virar alvo automático

Controle intensivo de glicose para 80–130 mg/dL não melhora desfecho e não é
recomendado. Redução intensiva de PAS para <140 mmHg após trombólise/trombectomia
também não deve ser automatizada; siga os limites do protocolo de reperfusão.

## Para a prova/material histórico

O slide ensina `AVC >24 h/AIT <24 h`, NIHSS ≥4, apenas alteplase, início
desconhecido como contraindicação e janelas simplificadas. Esses pontos ficam
`CURRICULAR_CHECKED`, mas os que divergem da AHA/ASA 2026 são
`HISTORICAL_ONLY`. Em questão que diga “segundo o slide”, nomeie a diferença;
nunca apresente o painel histórico como cuidado vigente.

## Pegadinhas e segurança

- TC sem hemorragia não “prova” AVC isquêmico; pode estar normal cedo.
- NIHSS baixo não significa déficit não incapacitante.
- Não espere angio-TC para iniciar trombólise elegível, mas também não adie a
  avaliação de grande vaso.
- Início ao despertar não encerra a avaliação de reperfusão.
- AAS não substitui avaliação de trombólise/trombectomia.
- Doses e contraindicações completas dependem do protocolo e do fármaco escolhido;
  não derive uma prescrição de memória a partir desta cápsula.

## Dados de precisão

| Claim | Valor atual | Fonte/localizador | Status |
|---|---|---|---|
| IVT padrão | alteplase ou tenecteplase até 4,5 h se elegível | AHA/ASA 2026, Top Things 2 | CURRENT_VERIFIED |
| NIHSS | incapacidade clínica, não corte ≥4 isolado | AHA/ASA 2026, Top Things 2–3 | CURRENT_VERIFIED |
| início desconhecido | seleção por DWI–FLAIR/perfusão | AHA/ASA 2026, Top Things 2 | CURRENT_VERIFIED |
| EVT até 24 h | seleção clínica e por imagem | AHA/ASA 2026, Top Things 4–6 | CURRENT_VERIFIED |

## Distratores sedutores

| Distrator | Por que seduz | Por que erra |
|---|---|---|
| “NIHSS 3 nunca trombolisa” | antigo corte do slide | déficit incapacitante pode ser elegível |
| “Wake-up stroke é contraindicação” | tempo exato ausente | imagem pode selecionar |
| “Até 24 h = trombectomia para todos” | memoriza janela sem critérios | vaso, déficit e imagem continuam necessários |

## Conduta e guardrails

- Inicial: ABC, glicemia, última vez visto bem, TC sem contraste e equipe de AVC.
- Definitiva: IVT e/ou EVT conforme elegibilidade, sem atrasos sequenciais evitáveis.
- Guardrail: seleção e dose reais exigem protocolo, contraindicações completas,
  neuroimagem e equipe habilitada.

## Mini-casos ativos — responda antes de abrir

1. Afasia incapacitante, NIHSS 3, 2 h, TC sem hemorragia: NIHSS exclui IVT?
2. Hemiparesia ao despertar: qual informação e exame podem reabrir a decisão?
3. Oclusão de grande vaso, 14 h: a janela basta?

<details><summary>Gabarito comentado</summary>

1. Não; incapacidade material importa mesmo com NIHSS baixo.
2. Última vez visto bem e seleção por DWI–FLAIR/perfusão.
3. Não; é necessária seleção clínica e por imagem.

</details>

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| IVT na janela padrão | alteplase ou tenecteplase até 4,5 h, se elegível | janela |
| NIHSS baixo exclui IVT? | não; avalie se o déficit é incapacitante | discriminação |
| Wake-up stroke exclui IVT? | não automaticamente; pode haver seleção por imagem | contraindicação |
| EVT até 24 h | somente pacientes selecionados; não é regra automática | janela |

## Fontes de vigência clínica

- AHA/ASA. Guideline hub e DOI, 26 jan. 2026: https://professional.heart.org/en/guidelines-statements/2026-guideline-for-the-early-management-of-patients-with-acute-ischemic-strokestr0000000000000513
- AHA/ASA. *Top Things to Know*, 2026: https://professional.heart.org/en/science-news/2026-guideline-for-the-early-management-of-patients-with-acute-ischemic-stroke/top-things-to-know

## Revisão

- Revisar a cada atualização AHA/ASA ou protocolo nacional/local.
- Critério de parada: em três vinhetas, distinguir janela padrão, seleção por
  imagem e trombectomia sem usar duração de sintomas ou NIHSS como corte isolado.
