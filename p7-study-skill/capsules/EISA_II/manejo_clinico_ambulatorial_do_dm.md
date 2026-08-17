# Manejo clínico ambulatorial do DM (avaliação inicial, seguimento, anamnese endócrina)

## Metadados

- Disciplina: EISA_II
- Especialidade: Endocrinologia
- Unidade: I_UNIDADE
- Prioridade: media
- Risco clínico: medio
- Status: reviewed_l1
- Camada de fonte usada: A+B
- fonte_visual: sim (`Oficina_Manejo_Cli_nico_do_DM__48bca328b6` — texto nativo bem extraído da MISTA, conferido por consistência interna; conteúdo numérico do caso clínico e das tabelas de metas foi conferido contra a estrutura do texto, sem necessidade de abrir imagem porque não havia tabela apenas-imagem nas páginas usadas)
- Fontes usadas: Oficina_Manejo_Cli_nico_do_DM__48bca328b6 (camada A, oficina da Profa. Narriane Chaves — caso clínico completo com evolução em 6 meses); ROTEIRO_DE_ANAMNESE_ENDO_CRINO__21b691b7d9 (camada B, roteiro de anamnese da Profa. Mirna de Sá — estrutura de 1ª consulta x retorno, itens específicos por patologia); Casos_cli_nicos_Prof_Narriane_Chaves__f0a6616ad6 (camada B, banco de casos de avaliação prática — usado apenas como referência de formato de caso, não extraído em detalhe)
- Evidência de prova/devolutiva: `cai: true` no cluster. Tema processual (fluxo de consulta) — o erro mais provável é operacional (pular etapa da anamnese ou aplicar o intervalo de seguimento errado), não de conteúdo farmacológico isolado (que pertence à cápsula de "metas de tratamento e terapia não insulínica").
- Limitações da fonte: a Oficina é rica em farmacologia comparada (metformina, sulfonilureias, incretinas, SGLT2, pioglitazona) — este conteúdo NÃO foi duplicado aqui em profundidade por pertencer a outro tema do cluster ("Diabetes: metas de tratamento e terapia não insulínica"); esta cápsula foca no PROCESSO ambulatorial (anamnese, frequência de seguimento, inércia terapêutica, metas por domínio, ajuste por situação especial).
- Verificação nível 1: CONFIRMADO

## Como cai

Caso clínico completo de paciente com DM2 mal controlado, pedindo a sequência de avaliação inicial (exame físico + laboratório) e a frequência de retorno até atingir metas. Pergunta sobre qual item da anamnese é obrigatório perguntar ao diabético (mapa glicêmico, dieta detalhada, data do último fundo de olho) e não foi perguntado no caso. Vinheta pedindo a meta pressórica/lipídica certa por perfil de risco (com/sem DAC, idoso, albuminúria). Caso com contraindicação específica (hepatopatia, DRC, idoso) pedindo qual fármaco evitar.

## Conceito operacional mínimo

Manejo ambulatorial do DM é um PROCESSO cíclico, não um evento único: avaliação inicial estruturada (exame físico + laboratório completo) → definição de metas por domínio (glicemia, PA, lipídios, peso) → tratamento → seguimento em intervalo definido pela distância à meta → reavaliação e intensificação SEM demora se fora da meta. A "inércia terapêutica" (esperar para intensificar) tem custo cardiovascular mensurável, não é conduta neutra.

## Pivô clínico

A variável que decide o intervalo de retorno não é "o paciente está confortável", é "o paciente está na meta": fora da meta glicêmica/lipídica/pressórica/de peso → retorno em 3 meses ou menos; estável e nas metas → 4-6 meses. E a variável que muda a escolha do fármaco quase sempre é a situação especial do enunciado (função renal, função hepática, idade, gestação) — não a eficácia "geral" da droga mais popular.

## Palavras-âncora

Inércia terapêutica (atraso de 6 meses → +6% risco de IM); metas por domínio (glicêmica/PA/lipídios/peso); retorno 3m (fora da meta) x 4-6m (estável); ClCr<30 (evitar metformina/glibenclamida/glimepirida/liraglutida); ClCr<45 (evitar SGLT2i); idoso (evitar sulfonilureia, sobretudo glibenclamida); mapa glicêmico por horário; roteiro de anamnese (1ª consulta x retorno).

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| priorizar / conduta definitiva | inércia terapêutica: atraso de 6 meses na intensificação aumenta risco de doença CV/IM (20%→26% em 5 anos) | prioridade | operacional | aguardar "mais uma consulta" para intensificar terapia em paciente fora da meta, tratando a espera como neutra | regra fixa: "HbA1c/PA/lipídio fora da meta = intensificar já, não esperar o próximo retorno" |
| aplicar critério | frequência de retorno: a cada 3 meses ou menos se fora das metas; a cada 4-6 meses se estável nas metas | sequência | operacional | aplicar intervalo de 6 meses a paciente ainda fora de meta, ou trazer paciente estável de volta a cada 3 meses sem necessidade | card de bifurcação fixo (fora da meta → ≤3m; estável e na meta → 4-6m) treinado contra vinhetas que trocam o status do paciente |
| reconhecer contraindicação | situação especial muda o fármaco a evitar: hepatopatia grave (evitar metformina); ClCr<30 (evitar metformina/glibenclamida/glimepirida/liraglutida); ClCr<45 (evitar SGLT2i); idoso (evitar sulfonilureia, sobretudo glibenclamida) | contraindicação | factual | manter metformina/sulfonilureia "padrão" em paciente com a contraindicação específica do enunciado, por serem a 1ª linha da população geral | tabela fixa comorbidade→fármaco a evitar, testada contra distratores que mantêm o fármaco padrão apesar da contraindicação |
| aplicar critério | meta pressórica por perfil: sem DAC <130/80 · com DAC não reduzir <120/70 · idoso >80 anos até <150 · com albuminúria <130/80 | limiar | operacional | aplicar a meta padrão (<130/80) a idoso >80 anos ou a coronariopata, ignorando a exceção que muda o alvo | tabela de metas por perfil treinada contra casos que trocam o perfil (idade, DAC, albuminúria) |
| reconhecer diagnóstico / estrutura | anamnese do diabético tem itens obrigatórios além do genérico: tempo de doença, sintomas de descompensação, hipoglicemia recente, neuropatia periférica, data do último fundo de olho, dieta detalhada por refeição, mapa glicêmico por horário | sequência | operacional | fazer anamnese genérica sem os itens específicos do diabético (esquecer hipoglicemia ou data do fundo de olho) | checklist fixo da anamnese específica do diabético, conferido item a item antes de fechar a consulta |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Exame físico inicial do diabético | peso, altura, IMC, circunferência abdominal, PA, fundo de olho, pele, acantose nigricans, local de aplicação de insulina, exame dos pés | Oficina p.2 | CONFIRMADO |
| Avaliação laboratorial inicial e seguimento | EAS+sedimentoscopia, creatinina, colesterol total+HDL, triglicérides, ECG (anual), avaliação oftalmológica (anual, exceto DM1 só a partir de 3 anos de diagnóstico) | Oficina p.3 | CONFIRMADO |
| Frequência de retorno | a cada 3 meses ou menos até atingir metas glicêmicas/lipídicas/de peso/PA; a cada 4-6 meses se estável nesses parâmetros | Oficina p.3 (SBD 2019) | CONFIRMADO |
| Inércia terapêutica — impacto CV | atraso de 6 meses na intensificação (vs imediata) aumenta risco de doença CV/IM de 20% para 26% em 5 anos (n=110.543) | Oficina p.6 (Paul S, et al. Diabetologia 2013) | CONFIRMADO |
| Meta pressórica | sem DAC: PAS<130/PAD<80 · com DAC: não reduzir <120/70 · idosos >80 anos: até PAS<150 · com albuminúria (>30mg/g): PAS<130/PAD<80 | Oficina p.15 (Bertoluci et al. 2017) | CONFIRMADO |
| Estratificação de risco CV no DM | idade >49 (H) ou >56 (M); DM>10 anos; DAC familiar prematura; síndrome metabólica (IDF); HAS tratada/não tratada; tabagismo atual; TFG<60 ou albuminúria>30mg/g; neuropatia autonômica cardíaca; retinopatia diabética | Oficina p.15 | CONFIRMADO |
| Antiagregação plaquetária | prevenção primária sem doença aterosclerótica: geralmente NÃO recomendada; alto risco + >65 anos + baixo risco de sangramento: pode ser útil; risco muito alto (doença aterosclerótica estabelecida/evento CV prévio): indicada | Oficina p.16 | CONFIRMADO |
| Situação especial — disfunção hepática | evitar metformina; se etilismo importante, evitar também sulfonilureia (risco de hipoglicemia grave/acidose lática) | Oficina p.17 | CONFIRMADO |
| Situação especial — gestação/lactação | preferir insulinoterapia; metformina antes da insulina é incerto (marcado com interrogação na fonte) | Oficina p.17 | CONFIRMADO |
| Situação especial — disfunção renal | evitar metformina, liraglutida, glibenclamida, glimepirida se ClCr<30 mL/min/1,73m²; ajustar dose de inibidores de DPP-4 (exceto linagliptina) se ClCr<30; evitar inibidor de SGLT-2 se ClCr<45 | Oficina p.17 | CONFIRMADO |
| Situação especial — idoso | evitar sulfonilureia, principalmente glibenclamida (maior risco de hipoglicemia); se necessário, preferir glimepirida ou gliclazida | Oficina p.17 | CONFIRMADO |
| Caso clínico — evolução em 6 meses | GJ 245→113 mg/dL; HbA1c 9,6%→6,9%; creatinina 1,5→1,2; TFGe 53→70; CT 203→164; LDL 110→68; TG 250→168; peso 99,8→93kg (-6,8kg); PA 160x88→120x80 | Oficina p.18-19 | CONFIRMADO |
| Anamnese — estrutura da 1ª consulta (roteiro Mirna de Sá) | identificação, QP, HDA (foco endócrino), medicações em uso (com posologia/horário), antecedentes pessoais (mulheres: menarca, GxPxAx, menopausa), antecedentes familiares (obesidade, doença tireoideana), exame físico (incluindo tireoide sempre), exames com data, hipóteses diagnósticas, conduta | ROTEIRO_ANAMNESE p.1 | CONFIRMADO |
| Anamnese — estrutura do retorno | hipóteses diagnósticas prévias, medicações em uso, evolução (melhora, queixa nova, adesão), exame físico, exames, conduta | ROTEIRO_ANAMNESE p.1 | CONFIRMADO |
| Anamnese específica — diabetes | tempo de doença, sintomas de descompensação (poliúria/polifagia/polidipsia/perda de peso), hipoglicemia recente, sintomas de neuropatia periférica, data do último fundo de olho, atividade física, dieta detalhada por refeição, mapa glicêmico por horário; exame dos pés com teste de sensibilidade na 1ª consulta e anual/semestralmente | ROTEIRO_ANAMNESE p.2 | CONFIRMADO |
| Anamnese específica — obesidade/sobrepeso | tempo/ritmo de ganho de peso, uso prévio de medicação para emagrecer, uso de corticoide prolongado, padrão alimentar (ansiedade/compulsão/beliscador/hiperfágico), circunferência abdominal, estigmas de Cushing | ROTEIRO_ANAMNESE p.2 | CONFIRMADO |
| Anamnese específica — tireoide | sintomas de hipo E hipertireoidismo, nódulos (já fez PAAF?), adesão e uso correto da levotiroxina (jejum, aguardar 30-40min), USG com descrição completa do nódulo (não só a conclusão) | ROTEIRO_ANAMNESE p.2 | CONFIRMADO |
| Anamnese específica — rastreio de osteoporose | mulheres >65 anos ou menopausa precoce, homens >70 anos, ou uso prolongado de corticoide → perguntar densitometria prévia, ingesta de cálcio, fratura prévia; anotar aparelho e T-score/Z-score de coluna lombar, colo do fêmur e fêmur total | ROTEIRO_ANAMNESE p.2 | CONFIRMADO |

## Pegadinhas

- Fora da meta glicêmica/pressórica/lipídica/de peso → retorno em 3 meses OU MENOS, não em 6 meses "para dar tempo de ver resultado" — a inércia terapêutica tem custo CV mensurável.
- ClCr<30 contraindica metformina, mas o corte para evitar SGLT2i é diferente (ClCr<45) — não usar o mesmo corte para as duas classes.
- Meta pressórica NÃO é uma única faixa para todo diabético — coronariopata tem piso (não reduzir <120/70), idoso >80 anos tem meta mais frouxa (até <150), e paciente com albuminúria volta à meta padrão (<130/80).
- Anamnese do diabético exige perguntar especificamente sobre hipoglicemia recente e data do último fundo de olho — não é suficiente perguntar só sobre sintomas de hiperglicemia (poliúria/polidipsia/polifagia).
- Idoso com necessidade de sulfonilureia: evitar glibenclamida (maior risco de hipoglicemia) — se precisar da classe, preferir glimepirida ou gliclazida, não a mais barata/mais usada.
- Prevenção primária com AAS não é para todo diabético — só em alto risco (>65 anos, baixo risco de sangramento) ou risco muito alto (doença aterosclerótica já estabelecida).

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Paciente com HbA1c 8,5% (fora da meta), medicação otimizada na última consulta → agendar retorno em 6 meses "para dar tempo" | esperar parece prudente para avaliar resposta | inércia terapêutica disfarçada de cautela | Fora da meta = retorno em 3 meses ou menos; esperar 6 meses prolonga a exposição a hiperglicemia e aumenta risco CV mensurável |
| Paciente com DRC (ClCr 40) e DM2 mal controlado → manter metformina por ser "primeira linha padrão" | metformina é a droga mais lembrada como 1ª linha universal | manter regra geral sem checar a exceção nomeada | ClCr<30 contraindica metformina — no caso (ClCr 40) ainda não está contraindicada, mas o aluno deve saber o corte exato, não "achar que está próximo o suficiente" para evitar por precaução indevida ou manter por displicência |
| Diabético coronariopata com PA 118x68 → intensificar anti-hipertensivo para chegar a <130/80 "para ficar dentro da meta padrão" | meta padrão (<130/80) é a mais memorizada | aplicar regra geral sem checar a exceção do perfil | Em diabético com DAC, a meta tem piso — não reduzir <120/70; intensificar mais pode ser prejudicial |
| Anamnese de retorno do diabético → repetir toda a dieta detalhada por refeição como na 1ª consulta | "padronizar" a anamnese parece mais seguro | sobre-elaboração / repetir etapa já feita | No retorno, só anotar as MUDANÇAS na dieta, não repetir tudo de novo |

## Conduta

- Inicial: anamnese estruturada (roteiro 1ª consulta) + exame físico completo (peso/IMC/CA/PA/fundo de olho/pele/pés) + laboratório completo (EAS, creatinina, lipidograma, ECG anual, oftalmológico anual).
- Definitiva: metas por domínio (glicemia, PA por perfil, lipídios, peso) com intensificação SEM demora se fora da meta.
- Condição da conduta: escolha do fármaco ajustada por situação especial (função renal, hepática, idade, gestação) — nunca a droga "padrão" sem checar a exceção do enunciado.
- Diferencial perigoso: inércia terapêutica — manter o mesmo esquema por "mais uma consulta" em paciente fora da meta tem custo CV mensurável, não é conduta neutra.
- O que mudaria a decisão: perfil de risco CV (DAC, idade, albuminúria) muda a meta pressórica; função renal/hepática/idade mudam o fármaco de escolha; estar ou não na meta muda o intervalo de retorno.

## Mini-casos ativos

Paciente DM2, HbA1c 8,2% na consulta atual (meta <7%), sem ajuste de medicação nesta consulta → variável decisiva: fora da meta → retorno em 3 meses ou menos, não 6 meses.

Paciente DM2 com ClCr 25 mL/min/1,73m², em uso de metformina → variável decisiva: ClCr<30 → contraindicação a metformina, trocar o esquema.

Paciente DM2 de 84 anos, PA 145x85, sem outras comorbidades relevantes → variável decisiva: idade>80 anos → meta pressórica mais frouxa (até PAS<150), não intensificar para <130/80.

Consulta de retorno de diabético, sem queixas novas, mesma dieta da consulta anterior exceto suspensão do cuscuz → variável decisiva: é retorno, não 1ª consulta → anotar só a mudança (suspendeu cuscuz), não repetir a dieta inteira.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Retorno se fora da meta | 3 meses ou menos | dado |
| Retorno se estável na meta | 4-6 meses | dado |
| Atraso de 6 meses na intensificação | Aumenta risco de IM (20%→26% em 5 anos) | pegadinha |
| Meta de PA em diabético com DAC | Não reduzir <120/70 (tem piso) | pegadinha |
| Meta de PA em idoso >80 anos | Até PAS<150 (mais frouxa) | pegadinha |
| ClCr que contraindica metformina | <30 mL/min/1,73m² | dado |
| ClCr que contraindica SGLT2i | <45 mL/min/1,73m² | pegadinha |
| Sulfonilureia a evitar no idoso | Glibenclamida (maior risco de hipoglicemia) | pegadinha |
| Itens obrigatórios na anamnese do diabético | Hipoglicemia recente, data do último fundo de olho, mapa glicêmico por horário, dieta detalhada | dado |
| Anamnese de retorno vs 1ª consulta (dieta) | Retorno só anota as mudanças, não repete tudo | pegadinha |

## Revisão

- Revisar quando: antes de caso clínico completo de DM pedindo conduta + intervalo de retorno, e antes de vinheta com situação especial (renal/hepática/idoso/gestante) pedindo qual fármaco evitar.
- Critério de parada: aplicar corretamente o intervalo de retorno (3m x 4-6m) e a meta pressórica por perfil em 3 casos seguidos, e listar os itens obrigatórios da anamnese específica do diabético sem esquecer nenhum.
