# Pneumonia adquirida na comunidade na infância

## Metadados

- Disciplina: EISCA
- Especialidade: Pneumologia pediátrica
- Unidade: IV
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: A
- fonte_visual: não
- Fontes usadas: PNEUMONIA COMUNITÁRIA.pdf (slide de aula, NATIVA, camada A); Pneumonia.docx.pdf (apostila, B, não aberta nesta rodada — camada A já suficiente e internamente consistente)
- Evidência de prova/devolutiva: mapa operação×movimento do banco EISCA cita explicitamente "Frequência respiratória como indicador de pneumonia" como item institucionalizado do banco (repetido quase literalmente em 5 provas/devolutivas de anos e turmas diferentes) — recomendado tratar como flashcard de resposta automática
- Limitações da fonte: nenhuma relevante — slide nativo, texto legível e completo
- Verificação nível 1: CONFIRMADO

## Contrato de recuperação

`answer_key_scope: curricular`; `clinical_validity_default: pending`. O slide
do professor ancora o que cai, mas não prova vigência clínica. Cortes, doses,
contraindicações e algoritmos só entram em resposta atual com claim `current`
rastreável ou fonte oficial aberta; fora disso permanecem `QUARANTINED`.

## Como cai

Item institucionalizado do banco: "qual a FR que classifica taquipneia/
pneumonia por faixa etária" se repete quase literalmente prova após prova.
Também cobra reconhecer os sinais de gravidade da OMS (basta 1 sinal para
classificar pela gravidade maior) e escolher o antibiótico empírico correto
por faixa etária e local de tratamento (ambulatorial x hospitalar, <2 meses x
>2 meses).

## Conceito operacional mínimo

Pneumonia é a forma mais grave das Infecções Respiratórias Agudas (IRA) — só
2-3% das IRA evoluem para pneumonia, mas é a principal causa de morte por IRA.
Diagnóstico é clínico pela estratégia AIDPI, baseado em FR e sinais de esforço
respiratório; radiografia não é obrigatória para diagnóstico ambulatorial.

## Pivô clínico

O pivô é a FR ajustada por idade como sinal MAIS sensível e mais cobrado —
não a ausculta (que pode ser normal ou inespecífica em lactentes). Um único
sinal de gravidade (não a soma) já define a classificação mais grave
(AIDPI/OMS: basta 1 sinal para "pneumonia grave"). O material também ensina
uma regra absoluta para menores de 2 meses. Essa regra fica `QUARANTINED`:
idade pequena eleva risco, mas não substitui avaliação e protocolo pediátrico
vigente.

## Palavras-âncora

FR por idade (<2m ≥60; 2m-1a ≥50; >1a ≥40); "basta 1 sinal"; SpO2 <92%;
esquemas e cortes etários do material = `QUARANTINED`; confirmar em fonte vigente.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | limiares de FR por faixa etária definem taquipneia/pneumonia: <2m ≥60 irpm; 2m-12m ≥50 irpm; >12m ≥40 irpm | limiar | factual | valor errado (trocar os cortes entre faixas etárias ou confundir com FR "normal") | card de tabela idade→FR, treinado com 5 casos variando só a idade em meses |
| priorizar emergência | basta 1 sinal de gravidade para classificar como "pneumonia grave/doença muito grave" (AIDPI) | prioridade | operacional | fechamento precoce (somar sinais/exigir múltiplos critérios antes de classificar grave) | treino de 5 vinhetas com 1 único sinal de alarme isolado, forçando classificar pela maior gravidade presente |
| reconhecer regra curricular sem promovê-la | material ensina "<2 meses = toda pneumonia grave/internar" | limiar | factual | transformar regra B-only em decisão atual absoluta | `answer_key_scope: curricular`; para prática atual, aplicar avaliação e protocolo pediátrico vigente |
| reconhecer contraindicação curricular | o slide diferencia cefotaxima e ceftriaxona no neonato | contraindicacao | factual | promover regra farmacológica do slide a prática atual | manter no painel `QUARANTINED`; consultar fonte neonatal vigente |
| reconhecer sequência curricular | o slide oferece prazo e troca antimicrobiana específicos | sequencia | factual | transformar algoritmo histórico em prática atual | treinar somente com `answer_key_scope: curricular`; para prática, reavaliar com fonte vigente |

## Dados de precisão

### Painel curricular histórico

`answer_key_scope: curricular`. Cortes e esquemas abaixo reproduzem o slide da
faculdade. `CONFIRMADO` aqui significa alinhamento curricular, não vigência
clínica. Em prática atual, não recuperar número, combinação ou regra absoluta
sem claim `current` rastreável ou fonte oficial aberta.

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| % das IRA que evoluem para pneumonia | 2-3% | PNEUMONIA COMUNITÁRIA.pdf, Introdução | CONFIRMADO |
| FR de taquipneia — <2 meses | ≥60 irpm | PNEUMONIA COMUNITÁRIA.pdf, Diagnóstico clínico | QUARANTINED — alinhamento curricular; vigência não verificada |
| FR de taquipneia — 2 a 12 meses | ≥50 irpm | PNEUMONIA COMUNITÁRIA.pdf, Diagnóstico clínico | QUARANTINED — alinhamento curricular; vigência não verificada |
| FR de taquipneia — >12 meses | ≥40 irpm | PNEUMONIA COMUNITÁRIA.pdf, Diagnóstico clínico | QUARANTINED — alinhamento curricular; vigência não verificada |
| Critério de internação por hipoxemia — <2 meses | SpO2 <92%, FR ≥70 irpm, cianose, apneia, gemido, incapacidade de se alimentar | PNEUMONIA COMUNITÁRIA.pdf, Classificação por faixa etária | QUARANTINED — alinhamento curricular; vigência não verificada |
| Critério de internação por hipoxemia — 2m a 5a | SpO2 <92%, FR ≥50 irpm, cianose, gemido, sinais de desidratação | PNEUMONIA COMUNITÁRIA.pdf, Classificação por faixa etária | QUARANTINED — alinhamento curricular; vigência não verificada |
| Indicação de UTI | SpO2 <92% com FiO2 >60%, hipotensão, falência respiratória, apneia recorrente | PNEUMONIA COMUNITÁRIA.pdf, Indicações de UTI | QUARANTINED — alinhamento curricular; vigência não verificada |
| Regime ambulatorial ensinado no material | amoxicilina 50 mg/kg/dia em 3 doses (ou 90 mg/kg/dia em 2 doses) | PNEUMONIA COMUNITÁRIA.pdf, Tratamento ambulatorial | QUARANTINED — confirmação curricular; vigência/dose não verificadas |
| Prazo para reavaliar falha terapêutica ambulatorial | febre persistente ou piora após 72h | PNEUMONIA COMUNITÁRIA.pdf, Tratamento ambulatorial | QUARANTINED — alinhamento curricular; vigência não verificada |
| Esquema hospitalar <2 meses | penicilina cristalina/ampicilina + amicacina/gentamicina, ou ampicilina + cefalosporina de 3ª geração | PNEUMONIA COMUNITÁRIA.pdf, Tratamento medicamentoso | QUARANTINED — alinhamento curricular; vigência não verificada |
| RN <28 dias — cefalosporina preferida | cefotaxima (não ceftriaxona, risco de deslocar bilirrubina/kernicterus) | PNEUMONIA COMUNITÁRIA.pdf, Tratamento medicamentoso | QUARANTINED — alinhamento curricular; vigência não verificada |
| Esquema hospitalar >2 meses, casos muito graves | oxacilina + cloranfenicol ou ceftriaxona (cobertura p/ S. aureus/H. influenzae) | PNEUMONIA COMUNITÁRIA.pdf, Tratamento medicamentoso | QUARANTINED — alinhamento curricular; vigência não verificada |
| SpO2 alvo com O2 suplementar hospitalar | manter entre 92% e 94%; suspender quando estável >92% em ar ambiente | PNEUMONIA COMUNITÁRIA.pdf, Conduta no hospital | QUARANTINED — alinhamento curricular; vigência não verificada |

## Pegadinhas

- A ausculta pulmonar pode estar **normal** ou inespecífica em lactentes com
  pneumonia — não descartar pelo exame físico pulmonar isolado; a FR é o
  sinal mais sensível.
- Hemograma/PCR/procalcitonina são marcadores **inespecíficos**; não devem
  ser usados rotineiramente para decidir tratamento ambulatorial.
- Radiografia não deve ser solicitada para "controle de cura" — baixa
  sensibilidade etiológica e dissociação clínico-radiológica é comum.
- Eosinofilia em pneumonia afebril sugere Chlamydia trachomatis — pista
  etiológica específica, não achado inespecífico de rotina.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "Ausculta normal descarta pneumonia" | reflexo de valorizar o exame físico pulmonar como principal | premissa não checada | em lactentes a semiologia pulmonar pode ser pobre; FR é o sinal mais sensível, não a ausculta |
| "Somar 2-3 sinais de gravidade para classificar pneumonia grave" | hábito de "quanto mais sinais, mais grave" de outros escores | fechamento precoce/regra mal-aprendida | AIDPI: 1 único sinal já define a classificação de maior gravidade |
| "Iniciar ceftriaxona em RN segundo a regra do slide" | parece uma regra farmacológica pronta | contraindicação ignorada | a distinção farmacológica do material é curricular `QUARANTINED`; prática atual exige fonte neonatal vigente |
| "Trocar antibiótico cedo por falta de melhora" | ansiedade por resposta clínica rápida | definitiva antes da inicial | o prazo e a troca do slide são curriculares `QUARANTINED`; reavaliar clinicamente com protocolo vigente |

## Conduta

- Inicial: classificar gravidade pela FR, oxigenação, esforço, capacidade de
  alimentação e sinais de perigo. Os esquemas/doses do material ficam em painel
  curricular `QUARANTINED`; não prescrever como prática atual sem fonte pediátrica
  vigente e contexto de idade, gravidade, resistência e protocolo local.
- Definitiva curricular: esquemas de troca, combinação e duração permanecem
  somente no painel histórico `QUARANTINED`. Não os repetir como algoritmo de
  prática atual sem overlay pediátrico vigente.
- Condição da conduta: idade pequena aumenta risco, mas internação depende da
  avaliação clínica e do protocolo pediátrico vigente; não usar regra absoluta B-only.
- Diferencial perigoso: derrame pleural, pneumatocele, abscesso — sinais
  radiológicos de complicação que indicam internação obrigatória mesmo sem
  outros critérios clínicos de gravidade.
- O que mudaria a decisão: piora de oxigenação, esforço, alimentação, hidratação
  ou estado geral aumenta urgência. Cortes exatos do slide ficam no painel
  curricular e não são promovidos a decisão atual sem fonte vigente.

## Mini-casos ativos

1. **Item curricular:** lactente de 4 meses, tosse e FR medida em 54 irpm.
   Aplicar o corte ensinado no slide somente com `answer_key_scope: curricular`;
   não tratá-lo como diagnóstico clínico atual sem fonte oficial vigente.
2. Recém-nascido com suspeita de pneumonia e sinal de gravidade. Variável
   decisiva: reconhecer alto risco e aplicar protocolo neonatal vigente; não
   escolher cefalosporina pela regra curricular isolada.
3. Criança em tratamento, ainda febril. Variável decisiva: reavaliar gravidade,
   adesão, complicação e diagnóstico antes de trocar antimicrobiano; o algoritmo
   temporal/farmacológico do slide é `QUARANTINED`.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Segundo o slide, quais os cortes de FR por idade? | <2m ≥60; 2m-12m ≥50; >12m ≥40 irpm — `answer_key_scope: curricular` | limiar curricular |
| Segundo o slide, quantos sinais de gravidade bastam? | 1 sinal — resposta curricular; vigência clínica depende de fonte atual | limiar curricular |
| A regra "<2 meses = sempre internar" pode ser aplicada como prática atual? | Não; é curricular `QUARANTINED`. Aplicar avaliação e protocolo vigente | limite de fonte |
| Esquemas, contraindicações e prazo de troca do slide entram em prática atual? | Não sem claim `current` rastreável ou fonte oficial aberta | limite de fonte |

## Revisão

- Revisar quando: junto com BVA e asma — os três compartilham banco de itens
  sobre taquipneia/desconforto respiratório em lactente e são fonte comum de
  troca de conduta entre si.
- Critério de parada: recitar de memória os 3 limiares de FR por idade e
  aplicá-los corretamente em 4 vinhetas variando apenas a idade em meses.
