# Doença Renal Crônica (DRC)

## Metadados

- Disciplina: EISA_II
- Especialidade: Nefrologia
- Unidade: II_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: A+B
- fonte_visual: sim (`DRC_2024_1_1___ca05068d36` pp. 5, 9, 10, 14, 23, 24, 26, 31, 39, 46, 48)
- Fontes usadas: DRC_2024_1_1___ca05068d36 (slide, camada A); APOSTILA_SA_II_P7___e43cc7bc21 (B); resumed_sa_de_do_adulto_2__f8fd0b8d31 (B); Nefrologia_DoenA_a_renal_crA_nica_I__3be337baf2 (B); Nefro_DOENC_A_RENAL_CRO_NICA__3429dee493 (B); DRC_Doen_a_renal_cr_nica__2da7fa9f7a (B)
- Evidência de prova/devolutiva: tema `cai: true`, prioridade alta e risco alto no cluster — sem devolutiva textual anexada a este cluster específico, mas padrão de erro geral de "limiar fora de contexto" e "definitiva antes da inicial" mapeado no banco de EISA II se aplica diretamente aos dois pivôs desta cápsula (critério temporal de DRC e indicação de TRS).
- Limitações da fonte: o slide do professor não traz a tabela clássica G1–G5/A1–A3 com os cortes numéricos completos (assume conhecimento prévio) — os cortes de TFG por estágio abaixo são rotulados "conhecimento geral" (KDIGO 2012), não extraídos do slide. Fórmula de reposição de ferro EV (slide p.24) foi omitida da tabela de precisão por ser cálculo acessório, não discriminador de prova.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

Vinheta com paciente com TFG reduzida ou alteração de exame de urina, cobrando: (1) se aquilo já fecha DRC ou exige documentação de cronicidade; (2) em que grupo de risco KDIGO o paciente cai e o que isso muda na conduta; (3) se o quadro já indica TRS ou ainda comporta tratamento conservador; (4) sequência correta de tratamento da anemia da DRC (ferro antes de EPO).

## Conceito operacional mínimo

DRC = lesão renal (estrutural/funcional) OU TFG <60 mL/min/1,73m², **persistindo por ≥3 meses**. O critério temporal é a variável que separa DRC de lesão renal aguda ou de um exame alterado isolado — sem os ≥3 meses, não se pode rotular DRC. Uma vez confirmada, o estadiamento cruza TFG (G1–G5) com albuminúria (A1–A3) num heatmap de risco (KDIGO), que determina a intensidade do seguimento — não a TFG isolada.

## Pivô clínico

Dois pivôs nesta cápsula: (1) tempo ≥3 meses é o que transforma "TFG baixa" em "DRC" — sem repetição documentada, o correto é repetir o exame, não fechar diagnóstico; (2) estágio G5 (TFG <15) não é sinônimo automático de indicação de TRS — paciente assintomático, sem perda ponderal e sem alteração clínico-laboratorial relevante pode seguir conservador mesmo com clearance de 5–10 mL/min.

## Palavras-âncora

KDIGO 2012; TFG <60 ≥3 meses; albuminúria; heatmap de risco; grupo amarelo/laranja/vermelho; G1–G5; A1–A3; TRS; hipervolemia refratária; pericardite urêmica; EPO; estoque de ferro; fístula arteriovenosa; HAS e DM como causas principais.

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | persistência ≥3 meses do achado (TFG<60 ou marcador de lesão) | limiar | factual/operacional | premissa não checada — fechar DRC com um único exame alterado, ignorando o tempo de evolução do enunciado | checklist fixo: "este achado está documentado há ≥3 meses?" antes de rotular DRC |
| aplicar critério / priorizar emergência | par TFG × albuminúria no heatmap (grupo amarelo/laranja/vermelho) | prioridade | operacional | analogia sem validação funcional — julgar gravidade só pela TFG, ignorando a albuminúria (ex.: G3a sem albuminúria é amarelo, mas G3a **com** albuminúria já é vermelho) | treinar o heatmap como tabela ativa, cruzando as duas variáveis em cada caso, nunca uma isolada |
| conduta definitiva | sintomas urêmicos refratários (hipervolemia, hipercalemia/acidose, pericardite/sangramento/encefalopatia) presentes ou ausentes | sinal-achado | operacional | definitiva antes da inicial — indicar TRS só pelo estágio G5, sem checar se o paciente está sintomático; ou o inverso, manter conservador em paciente já com sintoma refratário | checklist de sintomas obrigatório antes de decidir conservador x TRS, independente do estágio numérico |
| conduta / sequência | correção do estoque de ferro antes de iniciar EPO | sequência | operacional | perder a sequência — prescrever EPO diante de anemia da DRC sem checar ferritina/estoque de ferro primeiro | fixar o script "ferro → depois EPO" e treinar casos que dão ferritina baixa como distrator para pular a etapa |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Critério 1 de DRC | Lesão renal (anormalidade estrutural/funcional, patológica ou por marcador) por período ≥3 meses, com ou sem queda de TFG | DRC_2024_1_1 p.9 (KDIGO 2012) | CONFIRMADO |
| Critério 2 de DRC | TFG <60 mL/min/1,73m² por período ≥3 meses, com ou sem lesão renal | DRC_2024_1 p.9 (KDIGO 2012) | CONFIRMADO |
| Marcadores de dano parenquimatoso | Albuminúria; hematúria de origem glomerular; alterações eletrolíticas/tubulares; achado histológico em biópsia | DRC_2024_1 p.10 | CONFIRMADO |
| Marcadores por imagem | Rins policísticos; hidronefrose; cicatrizes corticais; doença infiltrativa; estenose de artéria renal | DRC_2024_1 p.10 | CONFIRMADO |
| Principais causas de DRC no Brasil | HAS 34% > DM 31% > GNC 9% ≈ "Outras" 11% ≈ Indeterminadas 11% > rins policísticos 4% | DRC_2024_1 p.14 (SBN CENSO 2018) | CONFIRMADO |
| Grupo Amarelo (KDIGO) | TFG >60 com albuminúria 30–300 mg/g (G1/G2 + A2) OU TFG 45–60 sem albuminúria (G3a + A1) — monitoramento anual, controle de fatores de progressão | DRC_2024_1 p.46 (UNASUS 2016) | CONFIRMADO |
| Grupo Vermelho (KDIGO) | G4/G5 com qualquer grau de albuminúria OU G3a/G3b com albuminúria — encaminhar ao nefrologista, monitorização 1–3 meses, preparar TRS | DRC_2024_1 p.48 (UNASUS 2016) | CONFIRMADO |
| Estadiamento por TFG (G1–G5) | G1 ≥90; G2 60–89; G3a 45–59; G3b 30–44; G4 15–29; G5 <15 mL/min/1,73m² | conhecimento geral (KDIGO 2012) — não explícito no slide | conhecimento geral |
| Categorias de albuminúria (A1–A3) | A1 <30 mg/g; A2 30–300 mg/g; A3 >300 mg/g | conhecimento geral (KDIGO 2012) — não explícito no slide | conhecimento geral |
| Indicações de TRS em DRC G V | Ao menos 1 de: hipervolemia refratária a restrição de sódio/água e diuréticos; anorexia/náuseas/vômitos; hipercalemia/acidose refratária; pericardite, sangramento ou encefalopatia urêmica | DRC_2024_1 p.31 | CONFIRMADO |
| Limite para manter tratamento conservador | Ccr 5–10 mL/min/1,73m², desde que assintomático, sem perda ponderal e sem alteração clínico-laboratorial relevante | DRC_2024_1 p.31 | CONFIRMADO |
| Sequência do tratamento da anemia | Iniciar EPO somente após corrigir o estoque de ferro | DRC_2024_1 p.23 | CONFIRMADO |
| Alvo de Hb no tratamento da anemia da DRC | 11–12 g/dL (dose de EPO SC 50–100 U/kg, 1–3x/semana) | DRC_2024_1 p.23 | CONFIRMADO |
| Fósforo e PTH alvo por estágio | G3: fósforo 3,0–4,6 / PTH 35–70; G4: fósforo 3,0–4,6 / PTH 70–110; G5: fósforo 3,5–5,5 / PTH 150–300 | DRC_2024_1 p.26 (UNASUS 2016) | CONFIRMADO |
| Antecedência da confecção de fístula arteriovenosa | 1–4 meses antes da necessidade de uso (para maturação) | DRC_2024_1 p.48 | CONFIRMADO |
| Prevenção de nefropatia por contraste em DRC | Evitar contraste hiperosmolar; menor dose possível; evitar outro nefrotóxico peri-procedimento; hidratação salina antes/depois; checar TFG em 48–96h | DRC_2024_1 p.39 (UNASUS 2016) | CONFIRMADO |

## Pegadinhas

- TFG 55 mL/min em exame único, sem documentação prévia = não é DRC ainda — falta o critério de cronicidade (≥3 meses); a conduta correta é repetir o exame, não rotular.
- Estágio G5 (TFG <15) não obriga diálise imediata: se assintomático, sem perda ponderal e sem alteração clínico-laboratorial relevante, o paciente pode seguir conservador mesmo com clearance de 5–10 mL/min.
- Grupo Amarelo do heatmap NÃO é "sem risco" — ainda exige investigação de causas tratáveis e monitoramento anual; não confundir com "alta do seguimento".
- G3a isolado (TFG 45–59) sem albuminúria é grupo Amarelo (risco moderado); o mesmo G3a **com** albuminúria já salta para o grupo Vermelho (risco muito alto) — a albuminúria muda a cor, não só a TFG.
- Corrigir anemia da DRC com EPO antes de checar/corrigir o estoque de ferro é conduta errada mesmo que a Hb esteja baixa — a sequência importa.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "TFG de 52 mL/min em exame de rotina único → iniciar investigação e tratamento de DRC estágio G3a" | Valor numérico já está abaixo de 60, parece objetivamente DRC | premissa não checada | Falta a persistência ≥3 meses — sem repetição documentada, ainda não é DRC pelos critérios KDIGO |
| "DRC estágio G5 (TFG 12), paciente estável e sem queixas → indicar TRS imediatamente pelo estágio" | G5 = "falência renal" no nome, parece indicação automática | definitiva antes da inicial | Estágio isolado não indica TRS; sem sintoma refratário e sem perda ponderal, pode manter conservador |
| "Paciente DRC com Hb 9, ferritina 40 (baixa) → iniciar EPO em altas doses para corrigir rápido" | Anemia da DRC "se trata com EPO" é a associação automática | fechamento precoce | Ferritina baixa indica estoque de ferro deficiente — corrigir ferro primeiro, só depois iniciar EPO |
| "TFG 50 sem albuminúria (G3a A1) → grupo Vermelho, encaminhar já ao nefrologista" | G3a soa "avançado", junta-se à ideia de alto risco | analogia sem validação funcional | G3a **sem** albuminúria (A1) é grupo Amarelo — é a albuminúria associada que definiria Vermelho, não a TFG isolada |

## Conduta

- Inicial: confirmar cronicidade (≥3 meses) antes de rotular DRC; classificar por TFG × albuminúria (heatmap KDIGO); investigar causas tratáveis nos grupos de menor risco; controlar HAS/DM/dislipidemia e evitar nefrotóxicos em todos os estágios.
- Definitiva: nos grupos Laranja/Vermelho — encaminhar ao nefrologista, corrigir distúrbio mineral-ósseo (fósforo/PTH por estágio) e anemia (ferro → EPO), preparar acesso para TRS (fístula AV com 1–4 meses de antecedência) e ofertar as três modalidades (hemodiálise, diálise peritoneal, transplante preemptivo).
- Condição da conduta: indicar TRS apenas diante de sintoma urêmico refratário (hipervolemia, hipercalemia/acidose, pericardite/sangramento/encefalopatia) OU DRC G V — não pelo número de TFG isoladamente quando o paciente está estável.
- Diferencial perigoso: lesão renal aguda sobreposta à DRC (queda aguda adicional de função) — checar histórico de TFG basal antes de atribuir toda a queda à cronicidade.
- O que mudaria a decisão: presença de albuminúria muda o grupo de risco mesmo com TFG preservada; aparecimento de sintoma urêmico refratário muda de conservador para TRS independentemente do estágio numérico isolado.

## Mini-casos ativos

Paciente, exame de rotina, Cr sugerindo TFG 55, sem exame prévio disponível. Variável decisiva: ausência de documentação de persistência ≥3 meses → conduta é repetir a TFG em 3 meses, não fechar DRC.

Paciente DRC G5 (TFG 12), assintomático, peso estável, sem alterações laboratoriais agudas. Variável decisiva: ausência de sintoma refratário → pode manter tratamento conservador apesar do estágio avançado.

Paciente DRC G3a, TFG 50, albuminúria 80 mg/g. Variável decisiva: a albuminúria (A2) associada à TFG classifica o paciente em risco mais alto do que sugeriria a TFG isolada — checar a tabela cruzada, não só o número da TFG.

Paciente DRC estágio 4 vai realizar angiotomografia com contraste eletiva. Variável decisiva: risco de nefropatia por contraste → hidratação salina peri-procedimento, menor dose de contraste, TFG de controle em 48–96h.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Critério temporal de DRC | Achado (lesão renal ou TFG<60) persistindo ≥3 meses | dado |
| TFG<60 em exame único, sem repetição | Não fecha DRC — repetir em 3 meses | pegadinha |
| Sequência do tratamento da anemia da DRC | Corrigir estoque de ferro → só depois iniciar EPO | sequência |
| Alvo de Hb no tratamento com EPO | 11–12 g/dL | dado |
| O que define o Grupo Vermelho do heatmap | G4/G5 com qualquer albuminúria OU G3a/G3b **com** albuminúria | dado |
| DRC G5 assintomático e estável | Pode seguir conservador até Ccr 5–10 mL/min | pegadinha |
| Causas mais comuns de DRC no Brasil | HAS (34%) > DM (31%) | dado |
| Antecedência para confecção de FAV | 1–4 meses antes da necessidade dialítica | sequência |
| Indicações de TRS na DRC GV | Hipervolemia refratária, hipercalemia/acidose refratária, sintomas GI refratários, pericardite/sangramento/encefalopatia urêmica | dado |

## Revisão

- Revisar quando: antes de qualquer questão que dê TFG isolada em vinheta sem histórico, ou que peça "conduta" em paciente DRC avançado.
- Critério de parada: aplicar corretamente o critério temporal (≥3 meses) e o heatmap TFG×albuminúria em 3 casos seguidos, sem confundir estágio numérico com indicação automática de TRS.
