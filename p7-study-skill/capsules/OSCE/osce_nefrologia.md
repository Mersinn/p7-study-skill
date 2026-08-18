# OSCE Nefrologia — síndromes glomerulares, glomerulopatias, DRC e injúria renal aguda

## Metadados

- Disciplina: OSCE
- Especialidade: Nefrologia
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: sim (`assuntos OSCE p7 2025.1`, p. 1 — confirma que Doença Renal do Diabetes, DRC, Glomerulopatia primária, Glomerulopatia secundária e IRA são as 5 estações oficiais de Nefro em 2025.1; documento fora do array de fontes do cluster)
- Fontes usadas: `OSCE .pdf` (camada B, ~p. 41-56 — caso clínico completo de GNDA com comandos e gabarito); `OSCE - NEFROLOGIA.pdf` (camada B, ~p. 1-5, formato tabela doença/sinais/diagnóstico/tratamento, cobre glomerulopatias primárias e secundárias); `FACILITA OSCE (1).pdf` (camada B, sumário indica DRC p. 34 e Hipertensão nefrogênica p. 40)
- Evidência de prova/devolutiva: caso clínico com gabarito comentado (GNDA, `OSCE .pdf`); caso-exemplo de diagnóstico diferencial sorológico (menina com síndrome nefrítica pós-IVAS) em `OSCE - NEFROLOGIA.pdf`
- Limitações da fonte: a tabela numérica de estágios da DRC por TFG (G1-G5) e a ordem das 4 principais etiologias de DRC no Brasil se perderam na extração de texto do PDF (ficaram só os rótulos, sem os números/ordem associados) — os valores de estágio abaixo vêm de conhecimento geral de nefrologia (KDIGO), rotulados como tal, não da fonte B. A ordem de preferência de acesso venoso para diálise de urgência também ficou cortada na extração.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

Duas estações inteiramente diferentes de raciocínio: (1) **glomerulopatias** — reconhecer a síndrome (nefrótica vs nefrítica) pelo corte quantitativo de proteinúria e demais achados, depois diferenciar a etiologia pelo padrão sorológico/temporal; (2) **DRC/IRA** — aplicar o critério objetivo (KDIGO-like para IRA; TFG/RAC para estadiar DRC) antes de decidir conduta ou encaminhamento. O caso de GNDA nas fontes mostra o padrão típico: quadro clínico compatível com síndrome nefrítica + tempo de latência pós-infecção estreptocócica compatível + confirmação sorológica, só então a conduta (que aqui é so sintomático).

## A estação

- **Tarefa:** a partir do caso clínico (geralmente pediátrico, com history de infecção prévia ou queixa insidiosa), reconhecer a síndrome (nefrótica/nefrítica), propor etiologia, solicitar/interpretar exames confirmatórios e descrever a conduta.
- **Tempo:** não informado nas fontes.
- **Ator/paciente:** caso clínico escrito, sem exame físico rico — o achado central é laboratorial/sorológico.
- **Material:** resultado de EAS, hemograma, complemento (C3), ASLO/anti-DNAse já disponíveis na cabine quando pedidos.
- **Critério do checklist (inferido):** classificar corretamente nefrótica vs nefrítica pelo corte de proteinúria, nomear a etiologia mais provável pelo tempo de latência/gatilho, citar o exame que a confirma e não pular para conduta sem justificar a etiologia.

## Pivô clínico

O pivô é o **corte quantitativo de proteinúria em 24h (3,5 g)** que separa síndrome nefrótica de nefrítica, combinado com o **tempo de latência entre o gatilho infeccioso e o início dos sintomas** que separa GNDA (7-21 dias pós-faringite, 15-28 dias pós-piodermite) de nefropatia por IgA (2-3 dias pós-IVAS ou durante o próprio quadro). Errar o tempo de latência troca a etiologia inteira mesmo com apresentação clínica idêntica.

## Palavras-âncora

Síndrome nefrótica × nefrítica · proteinúria 24h · complemento C3 · ASLO/anti-DNAse · tempo de latência · biópsia renal (MO/IF/ME) · TFG · RAC (relação albumina/creatinina) · KDIGO.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | diagnóstico de IRA: ΔCr ≥0,3 mg/dL em 48h OU ↑1,5-1,9x o basal em 7 dias OU débito urinário <0,5 mL/kg/h por ≥6h (basta 1 dos 3) | limiar | operacional | valor errado — checar só um dos três critérios e descartar IRA porque a creatinina "só" subiu 0,2, sem olhar o débito urinário | treino de casos com Cr seriada + débito urinário, forçando checar os 3 critérios por escrito antes de decidir |
| diferenciar próximos | corte de proteinúria de 24h que separa nefrótica (>3,5g) de nefrítica (<3,5g) | limiar | factual | trocar o corte ou decidir só por "tem proteinúria" sem checar a quantidade | tabela comparativa nefrótica × nefrítica lado a lado (proteinúria, edema, HAS, hematúria, oligúria), revisada como flashcard de par opositivo |
| interpretar imagem/ecg/laboratório | painel sorológico que diferencia GNDA (C3 baixo, FAN-, anti-DNA-) de nefropatia por IgA (complemento normal, FAN-, anti-DNA-) de nefrite lúpica (C3 baixo, FAN+, anti-DNA+) num quadro clínico idêntico de síndrome nefrítica pós-IVAS | sinal-achado | operacional | fechar a etiologia só pelo quadro clínico (os três quadros se apresentam de forma muito parecida) sem aplicar o painel sorológico completo | treinar o mesmo caso clínico com 3 painéis sorológicos diferentes, decidindo a etiologia só pela combinação FAN/anti-DNA/complemento |
| aplicar critério | estadiamento da DRC por TFG + regra de encaminhamento (acompanhamento por qualquer médico até o estágio 3A; só a partir do 3B encaminha para nefrologista) | limiar | operacional | generalizar "toda DRC vai para o nefrologista" ou, no outro extremo, só encaminhar no estágio 5 | flashcard fixo do corte 3A/3B como ponto de decisão de encaminhamento |
| priorizar emergência | indicação de diálise de urgência: síndrome urêmica franca, refratariedade/recorrência de hipervolemia, hipercalemia ou acidose metabólica, intoxicação exógena | prioridade | operacional | tratar clinicamente uma emergência dialítica (ex.: hipercalemia refratária) sem reconhecer que o critério objetivo já indica diálise, adiando a decisão | checklist de emergência dialítica (síndrome urêmica / distúrbio refratário / intoxicação) aplicado antes de escolher qualquer conduta conservadora |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Síndrome nefrótica — definição | proteinúria 24h >3,5g + hipoalbuminemia + hiperlipidemia (LDL aumentado) + HAS, início progressivo | OSCE - NEFROLOGIA.pdf, p. ~1 (camada B, tabela) | CONFIRMADO |
| Síndrome nefrítica — definição | hematúria de início súbito + proteinúria 24h <3,5g + oligúria (<400mL/dia) + edema periorbitário/anasarca + HAS | OSCE - NEFROLOGIA.pdf, p. ~1 (camada B, tabela) | CONFIRMADO |
| RAC (relação albumina/creatinina) — Doença Renal do Diabetes | <30 mg/g normal · 30-300 mg/g aumentada (DRD) · >300 mg/g muito aumentada | OSCE .pdf, p. ~42 (camada B) | CONFIRMADO |
| Rastreamento de DRD | DM2: no momento do diagnóstico · DM1: 5 anos após o diagnóstico · anual daí em diante | OSCE .pdf, p. ~43 (camada B) | CONFIRMADO |
| Critérios diagnósticos de IRA | ΔCr ≥0,3 mg/dL em 48h OU aumento 1,5-1,9x o basal em 7 dias OU débito urinário <0,5 mL/kg/h por ≥6h | OSCE .pdf, p. ~46 (camada B) | CONFIRMADO |
| Indicação de diálise na IRA | síndrome urêmica franca; refratariedade/recorrência de hipervolemia, hipercalemia e acidose metabólica; intoxicação exógena; ureia >200mg/dL ou creatinina 8-10mg/dL (indicação controversa) | OSCE .pdf, p. ~47 (camada B) | CONFIRMADO |
| Tempo de latência etiológico da GNDA | faringoamigdalite: 7-21 dias · impetigo: 15-28 dias, até o início da nefrite | OSCE .pdf, p. ~50 (camada B) | CONFIRMADO |
| GNDA — achados de biópsia | MO: proliferação endocapilar · IF: depósitos granulares de IgG e C3 · ME: depósitos subepiteliais em "corcova" | OSCE .pdf, p. ~50 / OSCE - NEFROLOGIA.pdf p. ~1 (camada B) | CONFIRMADO |
| Nefropatia por IgA — tempo de latência | hematúria surge durante o quadro infeccioso ou 2-3 dias após a faringite (mais curto que a GNDA — é o principal discriminador) | OSCE .pdf, p. ~54 (camada B) | CONFIRMADO |
| GNLM — tratamento | corticoide (prednisona) 1ª linha; desmame em 8-12 semanas se responsivo; ciclosporina/micofenolato/ciclofosfamida se dependência, recidiva frequente ou resistência | OSCE .pdf, p. ~54 (camada B) | CONFIRMADO |
| GNRP — achados de imunofluorescência por tipo | tipo I: padrão linear (jovens) · tipo II: padrão granular (jovens) · tipo III: ausência de depósitos (meia-idade/homens); tipo I exige associar plasmaférese ao tratamento | OSCE .pdf, p. ~53 / OSCE - NEFROLOGIA.pdf p. ~1-2 (camada B) | CONFIRMADO |
| DRC — definição | TFG <60 mL/min/1,73m² OU alteração estrutural renal por período >3 meses (pode haver DRC com TFG >60 se houver doença estrutural, ex. RAC >30 ou DRPAD) | FACILITA OSCE (1).pdf, p. 34 (camada B) | CONFIRMADO |
| DRC — fórmula mais acurada de TFG | CKD-EPI (mais acurada, sobretudo em TFG mais altas); Cockcroft-Gault é mais simples de calcular | FACILITA OSCE (1).pdf, p. 34 (camada B) | CONFIRMADO |
| DRC — regra de encaminhamento ao nefrologista | acompanhamento por qualquer médico até o estágio 3A; encaminhar ao nefrologista a partir do estágio 3B | FACILITA OSCE (1).pdf, p. 34 (camada B) | CONFIRMADO |
| DRC — estadiamento por TFG (G1-G5) | G1 ≥90 · G2 60-89 · G3a 45-59 · G3b 30-44 · G4 15-29 · G5 <15 (mL/min/1,73m²) | conhecimento geral (KDIGO) — não confirmado nas fontes B, que perderam a tabela numérica na extração | conhecimento geral |
| DRC — 4 principais etiologias no Brasil | HAS, diabetes mellitus, glomerulopatias e DRPAD são citadas como as 4 principais; a ordem exata não sobreviveu à extração de texto | FACILITA OSCE (1).pdf, p. ~35-36 (camada B) | confirmar no slide |
| Síndrome urêmica — manifestações | flapping, pericardite urêmica (dor pleurítica + atrito pericárdico), elevação de ST difusa, infra de PR | FACILITA OSCE (1).pdf, p. ~39 (camada B) | CONFIRMADO |

## Pegadinhas

**Imperdoáveis:**

- Classificar como "nefrótica" ou "nefrítica" sem citar o corte de proteinúria de 24h (3,5g) que faz a diferença — o achado clínico isolado (edema, hematúria) não fecha a classificação.
- Fechar GNDA sem checar o tempo de latência entre a infecção e o início do quadro — se o intervalo for de 2-3 dias, é IgA, não GNDA.
- Reconhecer critério de diálise de urgência e ainda assim propor conduta conservadora prolongada.
- Confundir DRC com IRA num caso que já traz "3 meses de evolução" ou "achado estrutural prévio" no enunciado — o tempo de evolução é o discriminador, não só o valor de TFG isolado.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "Edema + hematúria + HAS = síndrome nefrítica, ponto" sem checar a proteinúria | os 3 achados citados batem com o "quadro clássico" decorado | narrativa acima do discriminador | síndrome nefrótica também pode ter HAS e algum grau de hematúria microscópica — o discriminador real é o valor de proteinúria de 24h, não a lista de sintomas |
| Fechar GNDA em criança com edema + urina escura pós-IVAS sem pedir complemento/FAN/anti-DNA | GNDA é a etiologia "mais comum e mais decorada" para esse quadro pediátrico | fechamento precoce | o mesmo quadro clínico serve para nefrite lúpica e nefropatia por IgA — só o painel sorológico completo (C3, FAN, anti-DNA) discrimina as três |
| Tratar hipercalemia refratária só com medidas clínicas (gluconato de cálcio, insulina-glicose) num paciente que já preenche critério de diálise de urgência | as medidas clínicas de hipercalemia são a resposta mais treinada em prova teórica | definitiva antes da inicial / fechamento precoce | quando a hipercalemia é refratária ou recorrente apesar do tratamento clínico, o critério objetivo de diálise de urgência já está preenchido — a estação pode estar testando se o aluno reconhece que "estabilizar" não substitui "indicar TRS" quando o critério bate |

## Conduta

- Inicial: classificar nefrótica × nefrítica pelo corte de proteinúria de 24h; nas suspeitas de IRA, aplicar os 3 critérios KDIGO-like.
- Definitiva: nomear a etiologia mais provável pelo tempo de latência/gatilho + painel sorológico/complemento, e só então propor conduta (na maioria dos casos primários pediátricos das fontes, é sintomática).
- Condição da conduta: presença de critério de diálise de urgência muda tudo — interrompe a investigação etiológica calma e prioriza estabilização dialítica.
- Diferencial perigoso: hipercalemia/acidose refratária e síndrome urêmica franca são emergências que não esperam o fechamento diagnóstico completo.
- O que mudaria a decisão: tempo de latência entre gatilho infeccioso e sintomas (dias vs semanas) muda a etiologia mesmo com apresentação clínica idêntica; presença de achado estrutural ou tempo de evolução >3 meses muda IRA para DRC.

## Mini-casos ativos

1. Menina, 12 anos, dor abdominal + edema há 7 dias + febre que cedeu, progressão do edema para face há 5 dias, oligúria e urina escura há 3 dias, faringite 2 semanas antes do quadro. **Pivô:** o intervalo de 2 semanas entre a faringite e o início do quadro bate com GNDA (7-21 dias); se o enunciado dissesse "2-3 dias após a faringite", a resposta certa mudaria para nefropatia por IgA mesmo com clínica idêntica.
2. Menina, 10 anos, edema de MMII, urina escura, PA aumentada, início pós-IVAS. Complemento vem baixo, FAN e anti-DNA negativos. **Pivô:** complemento baixo + FAN/anti-DNA negativos aponta GNDA, não lúpus (que teria FAN+/anti-DNA+) nem IgA (que teria complemento normal) — decida pelo painel completo, não pelo quadro clínico isolado.
3. Paciente com DM2 de longa data, TFG de 38 mL/min/1,73m² em exame de rotina, assintomático. **Pivô:** TFG de 38 já é estágio 3B — o critério de encaminhamento ao nefrologista já está preenchido mesmo sem sintomas, e a periodicidade de exames muda de anual para semestral.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Corte de proteinúria de 24h que separa nefrótica de nefrítica | 3,5 g/24h (nefrótica >3,5g, nefrítica <3,5g) | limiar |
| Tempo de latência GNDA pós-faringite × pós-impetigo | 7-21 dias (faringite) × 15-28 dias (impetigo) | valor |
| Tempo de latência da nefropatia por IgA | 2-3 dias pós-IVAS, ou durante o próprio quadro infeccioso | valor |
| A partir de qual estágio da DRC encaminha ao nefrologista? | Estágio 3B | limiar |
| 3 critérios diagnósticos de IRA (basta 1) | ΔCr ≥0,3mg/dL/48h · ↑1,5-1,9x basal/7d · débito <0,5mL/kg/h por ≥6h | sequência |
| GNDA: FAN, anti-DNA e complemento | FAN negativo, anti-DNA negativo, complemento (C3) baixo | sinal-achado |

## Revisão

- Revisar quando: antes de simular qualquer estação de glomerulopatia (o painel sorológico comparativo é o ponto que mais derruba) e ao montar a tabela de estadiamento de DRC.
- Critério de parada: quando conseguir, dado um caso de síndrome nefrítica pediátrica pós-infecciosa, decidir a etiologia certa em 3 variações de painel sorológico (GNDA/IgA/lúpus) sem consultar a fonte.
