# Insulinoterapia no DM1 e DM2

## Metadados

- Disciplina: EISA_II
- Especialidade: Endocrinologia
- Unidade: I_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: A+B
- fonte_visual: sim (`Insulinoterapia_1___475cb4442b` pp. 13–14, 17–18, 20–26, 32–40, 43–44 — fonte ESCANEADA, TODOS os dados de precisão abaixo foram lidos direto da imagem, nunca do .txt)
- Fontes usadas: Insulinoterapia_1___475cb4442b (camada A, slide Dra. Carla Fernandes); Diabetes_3_insulinoterapia_I_unidade__6827ea5dfc (camada B, anotação de aula de Karen F.S.O.G. Agra — muito completa, usada para perfis de ação e etapas do DM2); resumed_sa_de_do_adulto_2__f8fd0b8d31 (camada B, não aberta linha a linha — redundante com Diabetes_3); APOSTILA_SA_II_P7___e43cc7bc21, Farmacoterapia_no_DM_2_parte_I_unidade__b7dabc93a3, Diabetes_mellitus_insulinoterapia__b65899b766 (camada B, citadas para rastreabilidade, não abertas — conteúdo redundante)
- Evidência de prova/devolutiva: `cai: true` no cluster; tema de altíssimo potencial de cálculo (fator de sensibilidade, RIC, divisão basal/bolus) — padrão de erro "valor/limiar trocado por proximidade numérica" e "definitiva antes da inicial" mapeados em EISA II se aplicam diretamente às contas de dose.
- Limitações da fonte: fonte A é PDF ESCANEADO (fotos de slide) — texto do OCR foi usado só como roteiro para localizar a página certa; todo valor numérico abaixo foi conferido no PNG da página antes de entrar na tabela. Duas páginas do slide (33 e 34) mostram o MESMO exemplo com idade do paciente diferente (16 anos sem cálculo, depois 18 anos com cálculo) — provável artefato de edição do professor; a versão com cálculo (18 anos) é a que vale.
- Verificação nível 1: CONFIRMADO

## Como cai

Vinheta pedindo a dose inicial de insulina basal em DM2 (10 U ou 0,1-0,2 U/kg) ou o cálculo completo de esquema basal-bolus no DM1 recém-diagnosticado (dose total por peso, divisão basal/bolus, dose de correção pelo fator de sensibilidade, RIC). Também cai como "quais insulinas podem ser misturadas" e como diferenciar efeito Somogyi de fenômeno do alvorecer diante de hiperglicemia matinal.

## Conceito operacional mínimo

Insulinoterapia reproduz o padrão fisiológico: uma insulina BASAL constante (cobre jejum/entre refeições) + picos de insulina RÁPIDA/BOLUS (cobrem cada refeição). No DM2, a insulina entra em escalonamento (basal → basal-plus → basal-plus ampliado → basal-bolus pleno). No DM1, o esquema basal-bolus pleno é a base desde o diagnóstico. Toda dose se ajusta por peso (U/kg) e por resposta glicêmica — não existe dose fixa universal.

## Pivô clínico

A variável que muda a resposta não é "qual insulina", é "qual pergunta o caso está fazendo": iniciar tratamento (dose por peso, dose fixa de 10U) x ajustar tratamento já em curso (dose de correção pelo fator de sensibilidade, ou adicionar prandial pela % da basal) x mistura/técnica (só NPH mistura com rápida) x hiperglicemia matinal (checar hipoglicemia noturna antes de mexer na dose). Confundir essas quatro pontas é o erro mais comum.

## Palavras-âncora

Basal-bolus; fator de sensibilidade (1800/DTD); RIC — relação insulina-carboidrato (400/DTD); dose de correção; insulinização oportuna; efeito Somogyi (hipoglicemia → rebote, reduzir dose noturna); fenômeno do alvorecer (5h-8h, resistência fisiológica, trocar horário/aumentar basal); IDegLira/IGlarLixi; DUAL V.

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | indicação de insulina em DM2 — "recomendada" (sintomático, HbA1c>9% ou GJ≥250) x "considerar" (diagnóstico recente, assintomático, sem DCV/renal) | limiar | operacional | generalizar critério de bolso — tratar todo DM2 novo como indicação formal de insulina, ignorando que o diagnóstico recente assintomático é só "considerar", não "recomendar" | tabela dos 3 cenários de indicação (recente assintomático / falha de terapia dupla-tripla / sintomático com HbA1c>9%-GJ≥250) com o verbo exato de cada um, treinada contra vinhetas embaralhadas |
| aplicar critério / calcular | divisão da dose total diária no DM1 novo: 0,5 U/kg/dia total → ~40-50% basal + 50-60% bolus dividido nas refeições | valor | operacional | sobre-elaboração ou fechamento precoce — calcular só a dose total (U/kg) e esquecer de dividir entre basal e bolus por refeição | repetir o cálculo em 3 passos fixos (dose total → basal → bolus ÷ nº de refeições) em casos variando o peso, sem pular etapa |
| aplicar critério / calcular | fator de sensibilidade (1800/dose total diária) x RIC — relação insulina-carboidrato (400/dose total diária) — fórmulas parecidas, usos diferentes | valor | operacional | valor errado — trocar a fórmula do FS pela do RIC (ou vice-versa) por proximidade estrutural (ambas são "número mágico" ÷ DTD) | treinar as duas fórmulas lado a lado no mesmo caso, sempre nomeando qual pergunta cada uma responde (FS = quanto corrige a glicemia atual; RIC = quanto cobre o carboidrato da refeição) antes de aplicar |
| interpretar laboratório / priorizar | hiperglicemia matinal: hipoglicemia de madrugada documentada (Somogyi) x ausência dela com resistência fisiológica 5h-8h (alvorecer) | sinal-achado | operacional | inverter a direção da conduta — aumentar a dose noturna diante de hiperglicemia matinal sem checar se há hipoglicemia prévia às 3h (que pediria REDUZIR a dose, não aumentar) | checklist fixo: antes de mexer na dose noturna por hiperglicemia matinal, checar glicemia de madrugada; card de pares opostos Somogyi (diminuir NPH da noite) x alvorecer (trocar horário/aumentar basal) |
| reconhecer contraindicação | só a insulina NPH pode ser misturada na mesma seringa com insulina rápida/ultrarrápida; aspirar a rápida primeiro | contraindicação | factual | valor errado — assumir que qualquer insulina basal (glargina, detemir, degludeca) pode ser misturada com rápida, ou inverter a ordem de aspiração | card fixo "só NPH mistura; rápida é aspirada primeiro", testado contra distratores com as outras 4 basais |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Indicação de insulina — DM2 recém-diagnosticado, assintomático, sem DCV/renal | terapia dupla (metformina+insulina) deve ser CONSIDERADA | Insulinoterapia (1) p.13, conferido visualmente | CONFIRMADO |
| Indicação de insulina — DM2 sintomático (poliúria/perda de peso) com HbA1c>9% ou GJ≥250 mg/dl | terapia à base de insulina é RECOMENDADA, mesmo que transitória | Insulinoterapia (1) p.14, conferido visualmente | CONFIRMADO |
| Indicação de insulina — falha de terapia dupla/tripla | HbA1c acima do alvo mesmo após dupla/tripla terapia com GLP1-RA ou GLP1-RA+GIP → insulina | Insulinoterapia (1) p.11-12 (roteiro OCR, conteúdo simples e concordante com resumed) | CONFIRMADO |
| Como iniciar insulinoterapia (qualquer indicação) | escolher basal longa/ultralonga; iniciar 10U ou 0,1-0,2 U/kg; objetivo = controle da glicemia de jejum; aumentar 2U a cada 3 dias até meta | Insulinoterapia (1) p.18, conferido visualmente | CONFIRMADO |
| DM2 — 1ª etapa (basal) | 10 U/dia ou 0,1-0,2 U/kg/dia, ao dormir + metformina; ajustar por glicemia de jejum | Diabetes_3_insulinoterapia p.5 (camada B, concorda com slide A) | CONFIRMADO |
| DM2 — 2ª/3ª etapa (basal-plus) | adicionar 4U ou 0,1 U/kg ou 10% da dose basal por refeição, começando na refeição de pior glicemia pós-prandial; aumentar 1-2U 2x/semana | Insulinoterapia (1) p.26 (ADA 2023), conferido visualmente; Diabetes_3 p.5 (concordam) | CONFIRMADO |
| Sinais de que a basal não é mais suficiente | dose basal >0,5 U/kg/dia · hipoglicemias frequentes/grande variabilidade · descontrole pós-prandial importante · diferença bed-time × jejum de 50-55 mg/dl | Insulinoterapia (1) p.25, conferido visualmente | CONFIRMADO |
| DM2 — 4ª etapa (basal-bolus pleno) | 1-2 doses basal + 3 doses prandiais (antes de cada refeição principal) | Diabetes_3 p.5-6 | CONFIRMADO |
| IDegLira (degludeca+liraglutida) — dose inicial | 10U se virgem de insulina; 16U se uso prévio de insulina ou GLP1-RA; dose máxima 50U da combinação | Insulinoterapia (1) p.20 e 22, conferido visualmente (2 páginas concordantes) | CONFIRMADO |
| Estudo DUAL V — IDegLira x IGlar U100 (ambos + metformina) | ΔHbA1c: -1,81 x -1,13 (p<0,001) · Δpeso: -1,4kg x +1,8kg (p<0,001) · hipoglicemia: 2,23 x 5,05 eventos/paciente-ano (p<0,001) · HbA1c final: 6,6% x 7,1% | Insulinoterapia (1) p.22-23, conferido visualmente | CONFIRMADO |
| DM1 — dose total diária ao diagnóstico | ~0,5 U/kg/dia (exemplo: 60kg → 30U/dia) | Insulinoterapia (1) p.35, conferido visualmente | CONFIRMADO |
| DM1 — divisão basal/bolus | esquema simples: 40-50% basal + 50-60% bolus fixa, dividida nas refeições (ex.: 15U basal + 15U bolus = 5U antes de cada refeição) | Insulinoterapia (1) p.32 e 35, conferido visualmente | CONFIRMADO |
| Fator de sensibilidade (FS) | 1800 ÷ dose total diária de insulina (ex.: 1800/30 = 60 → 1U baixa 60mg/dl) | Insulinoterapia (1) p.38, conferido visualmente | CONFIRMADO |
| Dose de correção | (glicemia atual − meta) ÷ FS (ex.: alvo 100, glicemia 300, FS 60 → (300-100)/60 = 3,3 ≈ 3U) | Insulinoterapia (1) p.38, conferido visualmente | CONFIRMADO |
| RIC — relação insulina-carboidrato | 400 ÷ dose total diária de insulina (ex.: 400/30 = 13,3 → RIC 1:13, ou seja 1U cobre ~13g de carboidrato) | Insulinoterapia (1) p.39, conferido visualmente | CONFIRMADO |
| Dose total pré-refeição (correção + carboidrato) | soma das duas doses calculadas separadamente (ex.: 3U correção + 5U carboidrato = 8U pré-almoço) | Insulinoterapia (1) p.40, conferido visualmente | CONFIRMADO |
| Perfil de ação — insulinas rápidas | Regular: início 30min-1h, duração 10-16h, maior risco de hipoglicemia · Aspart/Lispro/Glulisina (ultrarrápidas): início 5-15min, duração 3-5h, menor risco | Diabetes_3 p.4 (camada B; concorda com o gráfico da camada A p.17) | CONFIRMADO |
| Perfil de ação — insulinas basais | NPH: início 30min-1h/dura 10-16h (maior risco hipo) · Detemir: 1-3h/18-22h · Glargina U100: 2-4h/20-24h · Glargina U300: 6h/36h · Degludeca: 21-41min/42h (menor risco, "a melhor") | Diabetes_3 p.4-5; Insulinoterapia (1) p.17 (gráfico, concordam) | CONFIRMADO |
| Ordem de risco de hipoglicemia entre basais | NPH > Detemir > Glargina U100 > Glargina U300 = Degludeca | Diabetes_3 p.5 | CONFIRMADO (não presente na camada A — rotulado como B) |
| Mistura de insulinas na mesma seringa | somente NPH pode ser misturada com rápida/ultrarrápida; aspirar a rápida primeiro | Insulinoterapia (1) p.27, conferido visualmente | CONFIRMADO |
| Efeito Somogyi | hiperglicemia de rebote por hipoglicemia noturna → hormônios contrarreguladores; tratamento: DIMINUIR a dose de NPH/lenta da noite | Diabetes_3 p.7 (definição e tratamento; camada A traz só a definição, sem o tratamento, na p.44) | CONFIRMADO |
| Fenômeno do alvorecer | resistência tissular à insulina entre 5h-8h (pico de cortisol); tratamento: trocar horário da NPH para a hora de deitar, ou aumentar basal via bomba nesse intervalo | Diabetes_3 p.7; Insulinoterapia (1) p.44 (definição, concordam) | CONFIRMADO |
| Metas glicêmicas individualizadas | DM1/DM2 padrão: HbA1c<7,0, GJ/pré-prandial 80-130, pós-prandial<180 · idoso saudável: HbA1c<7,5 · idoso comprometido: HbA1c<8,0 · idoso muito comprometido: evitar sintomas de hiper/hipo · criança/adolescente: HbA1c<7,0, GJ 70-130 | Insulinoterapia (1) p.24, conferido visualmente | CONFIRMADO |

## Pegadinhas

- "Considerar" ≠ "recomendar": DM2 recém-diagnosticado assintomático sem DCV/renal é só CONSIDERAR insulina associada à metformina — não é indicação formal automática como no sintomático com HbA1c>9%.
- Fator de sensibilidade (1800/DTD) e RIC (400/DTD) têm a MESMA estrutura de fórmula (número fixo ÷ dose total diária) e respondem perguntas DIFERENTES — FS corrige a glicemia atual, RIC cobre o carboidrato da próxima refeição. A prova troca as duas.
- Hiperglicemia matinal não é sempre "aumentar a dose noturna" — se houver hipoglicemia de madrugada (Somogyi), a conduta é DIMINUIR a dose, o oposto do reflexo.
- Só NPH mistura com insulina rápida na mesma seringa — glargina, detemir e degludeca NUNCA são misturadas com rápida (perdem seu perfil de ação prolongado).
- Degludeca tem a maior duração (42h) e o menor risco de hipoglicemia entre as basais — mas isso não significa que ela substitui bolus; ainda cobre só o basal.
- O exemplo do slide A tem uma inconsistência de edição (paciente de "16 anos" na página anterior à versão com cálculo, que usa "18 anos") — ao estudar, usar sempre a versão com o cálculo completo (18 anos, 60kg, 30U/dia).

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| DM2 recém-diagnosticado, assintomático, HbA1c 8%, sem DCV/renal → iniciar insulina de imediato como terapia formal | "diabetes novo = trata logo" é o reflexo | generalizar critério de bolso | Aqui insulina é só "considerada" em associação com metformina — não é a recomendação formal (que exige sintoma + HbA1c>9% ou GJ≥250) |
| Paciente 60kg com DM1 novo: iniciar com 30U de insulina basal (Glargina) 1x/dia, sem bolus | "dose total = tudo em uma injeção só" simplifica | fechamento precoce / lacuna de sequência | A dose total (30U) deve ser dividida ~40-50% basal + 50-60% bolus fracionado nas refeições — basal isolada não cobre o pico pós-prandial |
| Calcular a dose de correção usando RIC (400/DTD) em vez do fator de sensibilidade (1800/DTD) | as duas fórmulas têm a mesma estrutura visual | valor errado por proximidade estrutural | RIC cobre carboidrato da refeição; fator de sensibilidade corrige a glicemia atual — usar a fórmula errada troca o valor final da dose |
| Paciente com hiperglicemia matinal recorrente → aumentar a dose de NPH noturna sem checar glicemia de madrugada | hiperglicemia "pede" mais insulina, reflexo intuitivo | inverter a direção do achado / não checar premissa | Se houver hipoglicemia às 3h (efeito Somogyi), a conduta correta é DIMINUIR a dose noturna — aumentar pioraria o quadro |
| Misturar insulina glargina com insulina rápida na mesma seringa para reduzir o número de aplicações | parece prático e "economiza picada" | premissa não checada / regra mal-aprendida | Somente NPH pode ser misturada com rápida — misturar glargina destrói o perfil de liberação prolongada da basal |

## Conduta

- Inicial (DM2, insulina virgem): escolher basal longa/ultralonga; iniciar 10U ou 0,1-0,2 U/kg/dia; ajustar 2U a cada 3 dias até meta de jejum.
- Definitiva (escalonamento DM2): basal → basal-plus (4U/0,1U/kg/10% da basal na refeição de pior pós-prandial) → basal-plus ampliado → basal-bolus pleno (1-2 basal + 3 prandial).
- Definitiva (DM1 ao diagnóstico): basal-bolus pleno desde o início — 0,5 U/kg/dia total, 40-50% basal + 50-60% bolus dividido nas refeições; ajustar por fator de sensibilidade (correção) e RIC (carboidrato).
- Condição da conduta: se basal >0,5 U/kg/dia OU hipoglicemias frequentes OU descontrole pós-prandial OU diferença bed-time × jejum de 50-55 mg/dl → basal isolada não é mais suficiente, avançar de etapa.
- Diferencial perigoso: hiperglicemia matinal sem checar glicemia de madrugada — pode ser Somogyi (hipoglicemia prévia, reduzir dose) em vez de alvorecer (resistência fisiológica, trocar horário/aumentar).
- O que mudaria a decisão: uso prévio de insulina ou GLP1-RA muda a dose inicial de IDegLira (10U → 16U); presença de hipoglicemia às 3h muda a direção do ajuste da dose noturna (aumentar → diminuir).

## Mini-casos ativos

Paciente com DM2 recém-diagnosticado, assintomático, HbA1c 7,8%, sem doença cardiovascular ou renal → variável decisiva: ausência de sintomas e de HbA1c>9%/GJ≥250 → insulina associada à metformina é apenas CONSIDERADA, não a conduta obrigatória.

Paciente 60kg, DM1 diagnosticado há 2 dias, sem tratamento prévio → variável decisiva: peso (0,5 U/kg/dia = 30U/dia) → 15U basal (Glargina) + 15U bolus (Lispro), 5U antes de cada refeição.

Mesmo paciente, em uso de 15U Glargina, HGT pré-almoço 300 (alvo 100), refeição com 60g de carboidrato, FS=1:60, RIC=1:13 → variável decisiva: dose de correção (3U) + dose por carboidrato (5U) somadas → 8U pré-almoço.

Paciente em uso de NPH à noite, glicemia matinal elevada — variável decisiva: resultado da glicemia de madrugada (3h): se baixa (hipoglicemia) = Somogyi → diminuir a NPH noturna; se normal/alta = alvorecer → trocar horário da NPH para a hora de deitar ou aumentar a basal.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Dose inicial de insulina basal (DM2, insulina virgem) | 10U ou 0,1-0,2 U/kg/dia; ajustar 2U a cada 3 dias | dado |
| DM2 recém-diagnosticado assintomático, sem DCV/renal | insulina é "considerada", não recomendação formal | pegadinha |
| DM2 sintomático + HbA1c>9% ou GJ≥250 | insulina é RECOMENDADA, mesmo que transitória | dado |
| Fator de sensibilidade (FS) | 1800 ÷ dose total diária → corrige a glicemia atual | dado |
| RIC (relação insulina-carboidrato) | 400 ÷ dose total diária → cobre carboidrato da refeição | dado |
| DM1 novo — divisão da dose total | 40-50% basal + 50-60% bolus dividido nas refeições | dado |
| Insulinas que podem ser misturadas na seringa | somente NPH + rápida/ultrarrápida; aspirar a rápida primeiro | pegadinha |
| Ordem de risco de hipoglicemia (basais) | NPH > Detemir > Glargina U100 > Glargina U300 = Degludeca | dado |
| Hiperglicemia matinal + hipoglicemia às 3h | efeito Somogyi → DIMINUIR a dose noturna | pegadinha |
| Hiperglicemia matinal sem hipoglicemia prévia | fenômeno do alvorecer → trocar horário/aumentar basal 5h-8h | conceito |
| IDegLira — dose inicial | 10U (virgem de insulina) / 16U (uso prévio de insulina ou GLP1-RA) | dado |

## Revisão

- Revisar quando: antes de qualquer vinheta com cálculo de dose de insulina (DM1 novo, correção, contagem de carboidratos) e antes de vinheta de hiperglicemia matinal.
- Critério de parada: executar corretamente o cálculo completo (dose total → basal/bolus → FS → RIC → dose de correção somada à de carboidrato) em 3 casos variando peso/glicemia sem consultar a fórmula, e diferenciar Somogyi de alvorecer em 3 vinhetas seguidas checando sempre a glicemia de madrugada primeiro.
