# Obesidade e síndrome metabólica

## Metadados

- Disciplina: EISA_II
- Especialidade: Endocrinologia
- Unidade: III_UNIDADE
- Prioridade: alta
- Risco clínico: medio
- Status: reviewed_l1
- Camada de fonte usada: B (tema sem camada A no acervo — `tem_camada_A: false`)
- fonte_visual: não
- Fontes usadas: Obesidade_e_Sind_Metabo_lica__bd2e4b03f6 (camada B, anotação de aula de Letícia Burity); Endocrino_OBESIDADE_E_SA_NDROME_METABA_LICA__79c20cd26e (camada B, anotação de aula de Edine Medeiros — traz a tabela numérica de critérios de síndrome metabólica); resumed_sa_de_do_adulto_2__f8fd0b8d31, APOSTILA_SA_II_P7___e43cc7bc21, Sd_metab_lica__8e5c3c8899 (camada B, citadas para rastreabilidade, não abertas individualmente)
- Evidência de prova/devolutiva: `cai: true` no cluster; sem devolutiva textual específica anexada. Padrão de erro "valor/limiar trocado por proximidade numérica" mapeado em EISA II se aplica diretamente aos cortes de cintura/IMC deste tema.
- Limitações da fonte: não há slide do professor no acervo para este tema (declarado no cluster: `tem_camada_A: false`) — toda a cápsula vem de anotação de aula (camada B). A tabela numérica de critérios de síndrome metabólica (Endocrino_OBESIDADE) não nomeia explicitamente qual diretriz (NCEP/IDF/OMS) ela representa; os cortes de cintura (H>94cm/M>80cm) batem com o corte IDF (etnia europoide) — inferência razoável, mas não confirmada no próprio texto, registrada como pendência.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES (ver pendência acima sobre a diretriz da tabela de síndrome metabólica)

## Como cai

Vinheta pedindo se o paciente tem indicação de farmacoterapia ou cirurgia bariátrica pelo IMC + comorbidade. Caso de ganho de peso "atípico" (súbito, sem mudança de hábito) pedindo se investiga causa secundária antes de tratar como obesidade primária. Caso com dados antropométricos e laboratoriais pedindo se fecha critério de síndrome metabólica (contagem de critérios positivos). Pergunta sobre contraindicação de fármaco antiobesidade (orlistate, sibutramina) por comorbidade do paciente.

## Conceito operacional mínimo

Obesidade = doença crônica inflamatória por acúmulo excessivo de gordura. IMC é o indicador principal mas não diferencia massa gorda de massa magra — sempre cruzar com circunferência abdominal/RCQ. Gordura visceral (central) = alto risco CV; gordura subcutânea = baixo risco CV, mesmo com IMC igual. Síndrome metabólica = obesidade central + resistência insulínica + HAS + dislipidemia, aumentando risco de DM em até 5× e de doença CV em até 3×.

## Pivô clínico

A pergunta que decide a conduta farmacológica/cirúrgica não é só "qual o IMC", é "há comorbidade associada e o paciente já falhou na MEV": IMC 27-30 SÓ autoriza medicamento SE houver comorbidade e falha de MEV; IMC 35-40 SÓ autoriza cirurgia SE houver comorbidade que ameace a vida. Sem a comorbidade, os cortes sobem (30 para medicamento; 40 para cirurgia).

## Palavras-âncora

NPY/AgRP (orexígeno) x POMC/CART (anorexígeno); grelina (estômago, orexígena) x leptina (tecido adiposo, anorexígena); MEV; sibutramina (retirada do mercado — risco CV); orlistate (Xenical, 120mg 3×/dia, contraindicado em nefrolitíase por oxalato); liraglutida (SCALE, GLP-1); bariátrica (IMC>40 ou >35+comorbidade, >18 anos); síndrome metabólica (2 de 4 critérios + cintura/IMC>30).

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | indicação de cirurgia bariátrica: IMC>40 isoladamente OU IMC>35 SE comorbidade que ameace a vida | limiar | operacional | generalizar "IMC>35 = indica cirurgia" sem checar se há comorbidade grave associada — sem ela, o corte sobe para 40 | casos-par (IMC 36 sem comorbidade x IMC 36 com comorbidade grave) treinando reconhecer qual corte se aplica |
| aplicar critério | indicação de farmacoterapia: IMC≥30 isoladamente OU IMC 27-30 SE comorbidade + falha de MEV | limiar | operacional | negar medicamento a paciente com IMC 28 e comorbidade que já falhou MEV, achando que só IMC≥30 autoriza | tabela fixa dos 2 cortes (30 isolado; 27-30 com comorbidade+falha) treinada contra vinhetas que variam a presença de comorbidade |
| reconhecer contraindicação | orlistate contraindicado em nefrolitíase por oxalato de cálcio; sibutramina contraindicada em alto risco cardiovascular | contraindicação | factual | prescrever o fármaco errado ao paciente errado — trocar a contraindicação específica de cada droga | card fixo fármaco→contraindicação, testado contra distratores que trocam a comorbidade entre os dois fármacos |
| reconhecer diagnóstico | sinais de causa secundária de ganho de peso (súbito, sem mudança de hábito, estrias violáceas, uso de corticoide/psicotrópico) antes de rotular obesidade primária | sinal-achado | operacional | fechamento precoce em "obesidade comportamental" sem investigar causa secundária quando o enunciado já deu a pista (ganho rápido e atípico) | checklist de red flags (Cushing, hipotireoidismo, distúrbio hipotalâmico, hipoglicemia/insulinoma, SOP, fármacos) antes de tratar como obesidade primária |
| aplicar critério | síndrome metabólica: cintura ou IMC>30 + 2 DE 4 critérios adicionais (não os 4) | prioridade | operacional | exigir os 4 critérios presentes, ou usar corte de cintura de outra diretriz (102/88 em vez de 94/80) | treino de contagem explícita de critérios positivos (mínimo 2 de 4) usando sempre a mesma tabela de cortes, sem misturar diretrizes |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Classificação de IMC | abaixo do peso <18,5 · normal 18,5-24,9 · sobrepeso 25-29,9 · obesidade ≥30 (grau I 30-34,9 · grau II 35-39,9 · grau III ≥40) · superobesidade ≥50 | Obesidade e Sind. Metabólica p.1 (concorda com Endocrino_OBESIDADE) | CONFIRMADO |
| IMC de menor mortalidade | em torno de 23 kg/m² (curva em U/J — extremos são piores) | Endocrino_OBESIDADE p.2 | CONFIRMADO |
| Circunferência abdominal — corte de risco | homem <90cm / mulher <80cm (marcador qualitativo de distribuição de gordura) | Obesidade e Sind. Metabólica p.6 | CONFIRMADO |
| Relação cintura/quadril — corte de risco | homem >0,95 / mulher >0,8 | Obesidade e Sind. Metabólica p.6 | CONFIRMADO |
| Critérios de síndrome metabólica (tabela numérica) | gatilho: cintura (H>94cm/M>80cm) OU IMC>30 + 2 de 4: glicemia jejum ≥100mg/dL (fonte registra ">99") · PA sistólica ≥130 ou diastólica ≥85 (ou em tratamento) · triglicerídeos ≥150mg/dL · HDL <40mg/dL (H) / <50mg/dL (M) | Endocrino_OBESIDADE p.9 | CONFIRMADO_COM_CORREÇÕES — diretriz de origem não nomeada no texto; cortes de cintura (94/80) compatíveis com IDF etnia europoide, registrado como inferência, não confirmação |
| Síndrome metabólica — aumento de risco associado | risco de diabetes até 5× maior; risco de doença cardiovascular até 3× maior | Obesidade e Sind. Metabólica p.3 | CONFIRMADO |
| Reganho de peso pós-tratamento clínico | 50% do peso recuperado em 2 anos; 75% em 5 anos | Obesidade e Sind. Metabólica p.5 | CONFIRMADO |
| Indicação de MEV | todo sobrepeso (IMC 25-29,9) e obesidade (IMC≥30) | Obesidade e Sind. Metabólica p.5 | CONFIRMADO |
| Indicação de farmacoterapia | IMC≥30 isolado OU IMC 27-30 + comorbidade, se falha de MEV | Obesidade e Sind. Metabólica p.5 | CONFIRMADO |
| Sibutramina | inibidor de recaptação de NE/serotonina; retirada do mercado em 2010 (EMA/FDA/Health Canada) por aumento de eventos CV (IAM não fatal, AVC não fatal, morte CV, PCR ressuscitada); ANVISA (2011) permite uso cauteloso, dose 10mg/dia, máximo 15mg/dia | Obesidade e Sind. Metabólica p.6 | CONFIRMADO |
| Orlistate | 120mg, 3×/dia antes das refeições; perda de peso >11% (vs 6% placebo) no 1º ano; contraindicado em nefrolitíase por oxalato de cálcio; reduz absorção de vitaminas lipossolúveis (suplementar); efeitos GI em 15-30% (evitar refeição >30% de gordura) | Obesidade e Sind. Metabólica p.6 | CONFIRMADO |
| Liraglutida (SCALE) | dose inicial 0,6mg SC, ajuste semanal até 3mg; indicação IMC≥27 com comorbidade ou ≥30; perda de peso média 6,2% (vs 0,2% placebo); ≥5% de perda em 50,5% dos pacientes (vs 21,8%) | Obesidade e Sind. Metabólica p.7 | CONFIRMADO |
| Cirurgia bariátrica — indicação | idade >18 anos; IMC>40 kg/m² OU IMC>35 kg/m² + comorbidade que ameace a vida (lista com >21 doenças) | Obesidade e Sind. Metabólica p.8; Endocrino_OBESIDADE p.8 (concordam) | CONFIRMADO |
| Bypass em Y de Roux — complicação nutricional | risco de desnutrição: deficiência de ferro, ácido fólico, cálcio, vitamina D, vitamina B12 | Obesidade e Sind. Metabólica p.8 | CONFIRMADO |
| Hipotireoidismo como causa de ganho de peso | ganho discreto (3-4kg), por retenção hídrica/acúmulo de glicosaminoglicanos — NÃO causa obesidade isoladamente | Endocrino_OBESIDADE p.4 (concorda com a cápsula de Hipotireoidismo: "ganho de peso discreto, não causa obesidade") | CONFIRMADO |

## Pegadinhas

- IMC 27-30 SÓ autoriza medicamento SE houver comorbidade associada E falha de MEV — sem essas duas condições, o corte para medicamento é 30.
- IMC 35-40 SÓ autoriza cirurgia bariátrica SE houver comorbidade que ameace a vida — sem ela, o corte é 40.
- Hipotireoidismo causa ganho de peso discreto (3-4kg por retenção hídrica), NÃO obesidade — tratar hipotireoidismo em paciente obeso não vai "curar" a obesidade.
- Síndrome metabólica exige 2 DE 4 critérios adicionais (além do gatilho de cintura/IMC), não os 4 — contar mal os critérios é o erro mais comum.
- Sibutramina foi retirada do mercado por risco CV, mas ainda pode ser prescrita no Brasil com cautela (dose máxima 15mg/dia) — não é uma droga banida por completo, é uso restrito.
- IMC isolado pode enganar: atleta com massa muscular alta pode ter IMC de sobrepeso/obesidade sem excesso real de gordura — sempre cruzar com circunferência abdominal ou métodos de composição corporal antes de rotular.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Paciente com IMC 28, hipertensão associada, já tentou MEV sem sucesso → negar farmacoterapia porque "IMC não chega a 30" | corte de 30 é o mais memorizado | generalizar critério de bolso desatualizado | IMC 27-30 + comorbidade + falha de MEV já autoriza medicamento — não precisa esperar IMC≥30 |
| Paciente com IMC 36, sem nenhuma comorbidade relevante → indicar cirurgia bariátrica | "IMC>35 = bariátrica" é a meia-regra mais lembrada | superextrapolação sem checar a exceção | Sem comorbidade que ameace a vida, o corte para cirurgia é IMC>40, não 35 |
| Paciente obeso com TSH elevado → tratar o hipotireoidismo e esperar reversão completa da obesidade | "tireoide desregulada = culpa do peso" é intuitivo | analogia sem validação funcional | Hipotireoidismo causa só 3-4kg de ganho por retenção hídrica — não explica obesidade franca; tratar a tireoide não resolve a obesidade de base |
| Paciente com nefrolitíase por oxalato de cálcio, obeso, deseja perda de peso rápida → prescrever orlistate | orlistate é o fármaco "mais simples e mais estudado" | premissa não checada / contraindicação ignorada | Orlistate é CONTRAINDICADO em nefrolitíase por oxalato de cálcio — a informação do enunciado muda a escolha do fármaco |
| Paciente com cintura aumentada + glicemia de jejum alterada apenas → já fechar diagnóstico de síndrome metabólica | 2 achados "positivos" parecem suficientes | não validar contagem completa de critérios | O gatilho (cintura/IMC>30) conta à parte — são necessários mais 2 dos 4 critérios adicionais (só glicemia não fecha o diagnóstico) |

## Conduta

- Inicial: anamnese completa (história ponderal, fator desencadeante, comorbidades, antecedentes familiares) + exame físico (IMC, circunferência abdominal, RCQ, sinais de causa secundária).
- Definitiva: MEV para todo sobrepeso/obesidade; farmacoterapia se IMC≥30 ou (27-30 + comorbidade + falha de MEV); cirurgia bariátrica se IMC>40 ou (35-40 + comorbidade que ameace a vida), idade >18.
- Condição da conduta: escolha do fármaco depende de contraindicação individual (orlistate x nefrolitíase por oxalato; sibutramina x risco CV alto).
- Diferencial perigoso: ganho de peso súbito/atípico sem mudança de hábito → investigar causa secundária (Cushing, distúrbio hipotalâmico, hipoglicemia/insulinoma, SOP, fármacos) antes de tratar como obesidade primária.
- O que mudaria a decisão: presença de comorbidade muda os cortes de IMC para medicamento e cirurgia; histórico de nefrolitíase por oxalato muda a escolha farmacológica.

## Mini-casos ativos

Paciente IMC 28, DM2 mal controlado, já tentou MEV por 6 meses sem sucesso → variável decisiva: comorbidade + falha de MEV → farmacoterapia já indicada, mesmo com IMC<30.

Paciente IMC 36, hígido, sem comorbidades → variável decisiva: ausência de comorbidade grave → NÃO indicar cirurgia bariátrica ainda (corte sem comorbidade é 40).

Paciente obeso com cintura aumentada, PA 135/90, TG 160, glicemia de jejum 95 (normal), HDL normal → variável decisiva: contar os critérios positivos (cintura + PA + TG = gatilho + 2 de 4) → fecha síndrome metabólica mesmo com glicemia normal.

Paciente com litíase renal por oxalato de cálcio prévia, deseja tratamento farmacológico para obesidade → variável decisiva: contraindicação específica → evitar orlistate, considerar outra opção (ex.: liraglutida, sem essa contraindicação).

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| IMC para farmacoterapia sem comorbidade | ≥30 | dado |
| IMC para farmacoterapia com comorbidade + falha MEV | 27-30 | pegadinha |
| IMC para cirurgia bariátrica sem comorbidade | >40 | dado |
| IMC para cirurgia bariátrica com comorbidade grave | >35 | pegadinha |
| Orlistate — contraindicação | Nefrolitíase por oxalato de cálcio | pegadinha |
| Sibutramina — por que foi retirada do mercado | Aumento de eventos cardiovasculares (estudo com 9800 pacientes) | dado |
| Síndrome metabólica — quantos critérios além do gatilho | 2 de 4 (não os 4) | pegadinha |
| Hipotireoidismo e obesidade | Só 3-4kg de ganho — não causa obesidade franca | pegadinha |
| Gordura visceral x subcutânea | Visceral = alto risco CV; subcutânea = baixo risco CV, mesmo IMC igual | conceito |

## Revisão

- Revisar quando: antes de vinheta pedindo indicação de farmacoterapia/cirurgia bariátrica, e antes de caso com dados antropométricos+laboratoriais pedindo síndrome metabólica.
- Critério de parada: aplicar corretamente os cortes de IMC (com e sem comorbidade) para medicamento e cirurgia em 3 casos seguidos, e contar certo os critérios de síndrome metabólica (gatilho + 2 de 4) sem exigir os 4.
