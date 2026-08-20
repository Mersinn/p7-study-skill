# Colite pseudomembranosa por Clostridioides difficile

## Metadados

- Disciplina: CASOS_CLINICOS
- Especialidade: Gastroenterologia / Infectologia
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B (fisiopatologia/quadro/diagnóstico) + conhecimento geral atualizado (esquema antibiótico de 1ª linha)
- fonte_visual: sim (`Abordagem_a_s_diarreias__41fb86fd8c`, pp. 24-27 — slide fotografado/renderizado, lido como imagem; a numeração de página foi conferida diretamente nos arquivos `p024.png`-`p027.png`, não extraída do `.txt` da fonte, que é MISTA)
- Fontes usadas: `Abordagem às diarreias.pdf` (camada B, tipo MISTA, pp.24-27 — quadro "COLITE PSEUDOMEMBRANOSA" com definição, quadro clínico, diagnóstico e tratamento, incluindo 1 imagem de colonoscopia com pseudomembranas)
- Evidência de prova/devolutiva: nenhuma disponível neste cluster — o tema foi sinalizado como pendente pelo próprio levantamento de faltantes do aluno (`19_FALTA_CLUSTERS.json`), sem prova/devolutiva mapeada
- Limitações da fonte: a única fonte do cluster é um resumo de colega (camada B), sem camada A (slide do professor) mapeada para este tema. O esquema de tratamento antibiótico do slide trata vancomicina VO e metronidazol VO como opções equivalentes de 1ª linha — isso está **desatualizado** frente à diretriz de referência atual (IDSA/SHEA 2021), que reclassificou vancomicina VO (ou fidaxomicina) como 1ª linha e relegou o metronidazol a alternativa de segunda escolha. A fonte também não menciona o teste de GDH (glutamato desidrogenase) nem a contraindicação explícita a antiperistálticos — ambos os pontos abaixo estão rotulados como conhecimento geral, não como conteúdo da fonte B, exatamente porque o enunciado da tarefa identificou esses dois pontos como os mais cobrados neste tema (gatilho antibiótico, diagnóstico por toxina/GDH e conduta com vancomicina oral, nunca antiperistáltico) e a fonte disponível não os cobre por completo.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

O caso clássico é um paciente **idoso, hospitalizado ou recentemente hospitalizado, com uso de antibiótico (atual ou recente, mesmo já suspenso)**, que desenvolve diarreia aquosa associada a dor abdominal e febre. A operação central que a prova cobra não é "reconhecer diarreia infecciosa" — é reconhecer o **gatilho antibiótico** como pivô diagnóstico (o antibiótico pode já ter sido suspenso há semanas), pedir o exame que realmente confirma o diagnóstico (pesquisa de toxina/GDH, não coprocultura isolada) e, na conduta, aplicar duas regras de alto risco: vancomicina **oral** é a base do tratamento (não parenteral, porque o alvo é luminal) e antiperistálticos são **proibidos** por risco de precipitar megacólon tóxico. Casos Clínicos avalia por simulação em grupo (ver `formato_avaliacao_discussao_casos_clinicos.md`), então o candidato deve estar pronto para **defender** cada uma dessas escolhas perante a turma, não só recitá-las.

## Conceito operacional mínimo

Colite pseudomembranosa é uma colite mediada por **toxinas** (A e B) do *Clostridium difficile*/*Clostridioides difficile*, desencadeada pela disrupção da flora intestinal normal por antibioticoterapia — o organismo prolifera e produz toxina, que causa inflamação da mucosa colônica e formação de pseudomembranas (placas amarelo-esbranquiçadas visíveis à colonoscopia). O diagnóstico depende de demonstrar a toxina (ou o antígeno GDH associado a ela), não apenas a presença da bactéria. O tratamento é antibiótico específico (vancomicina oral ou fidaxomicina), nunca terapia sintomática com antiperistáltico.

## Pivô clínico

O pivô é duplo: (1) **o gatilho antibiótico não precisa estar em uso no momento da consulta** — a colite pode surgir até 8-10 semanas após a suspensão do antibiótico, e um candidato que só pergunta "está tomando algum remédio?" sem perguntar especificamente sobre uso **recente** (mesmo já suspenso) perde o dado decisivo; (2) **a gravidade muda o esquema** — leucocitose importante (>15.000) e elevação da creatinina (≥1,5× o basal), ou sinais de colite fulminante (hipotensão, íleo, distensão abdominal com megacólon), tiram o caso do esquema padrão de vancomicina VO isolada e podem exigir associação parenteral e avaliação cirúrgica.

## Palavras-âncora

Colite pseudomembranosa · *Clostridium difficile*/*Clostridioides difficile* · gatilho antibiótico (clindamicina, fluoroquinolona, cefalosporina) · toxina A e B · GDH · pseudomembranas amarelo-esbranquiçadas · vancomicina oral · nunca antiperistáltico · megacólon tóxico · fidaxomicina · transplante de microbiota fecal.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| reconhecer diagnóstico | tríade diarreia + uso de antibiótico nas últimas 8-10 semanas (mesmo já suspenso) + fator de risco (idade, hospitalização, cirurgia abdominal prévia, uso de SNE) | fato | operacional | lacuna — perguntar só sobre uso **atual** de medicação, sem checar antibioticoterapia recente já suspensa, perdendo o gatilho | checklist obrigatório "uso de antibiótico nas últimas 8-10 semanas" em todo caso de diarreia aguda em idoso ou paciente hospitalizado |
| melhor exame | diagnóstico depende de detectar a toxina (ELISA/PCR) ou o antígeno GDH — a coprocultura isolada não confirma o diagnóstico (pode ser positiva para cepa não-toxigênica) | sequência | operacional | troca de comando — solicitar só coprocultura achando que ela fecha o diagnóstico, como em outras diarreias bacterianas | fixar que coprocultura NÃO é o exame confirmatório de colite por *C. difficile*; o exame-alvo é a pesquisa de toxina/GDH (ou NAAT/PCR) |
| reconhecer contraindicação | antiperistáltico (ex. loperamida) é contraindicado — pode precipitar megacólon tóxico | contraindicação | factual | prescrever antidiarreico "para aliviar o sintoma" sem checar a etiologia infecciosa/inflamatória subjacente | fixar antiperistáltico como contraindicação absoluta em diarreia infecciosa/inflamatória, usando *C. difficile* como o exemplo mais cobrado |
| conduta definitiva | vancomicina VO (ou fidaxomicina) é a 1ª linha atual — não metronidazol isolado | regra atualizada | factual | regra mal-aprendida/desatualizada — responder metronidazol como 1ª linha por ser o esquema "clássico" mais decorado em fontes antigas | fixar a atualização: vancomicina VO 125mg 6/6h por 10 dias (ou fidaxomicina) é a base do tratamento; metronidazol é alternativa, não equivalente |
| priorizar emergência | sinais de gravidade (leucocitose >15.000, creatinina ≥1,5× basal) ou de colite fulminante (hipotensão, íleo, megacólon) mudam o esquema e podem exigir avaliação cirúrgica | limiar | operacional | aplicar o mesmo esquema padrão de vancomicina VO isolada a um caso que já preenche critério de gravidade/fulminância | checklist de gravidade (leucometria, creatinina, sinais de choque/íleo/distensão) antes de fechar o esquema terapêutico |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Definição e agente etiológico | diarreia causada por toxinas bacterianas; agente = *Clostridium difficile* ou *Clostridioides difficile* | `Abordagem às diarreias.pdf`, p.24 (imagem) | CONFIRMADO |
| Quadro clínico | diarreia, febre, dor abdominal, colite | `Abordagem às diarreias.pdf`, p.25 (imagem) | CONFIRMADO |
| Paciente clássico | idoso, uso recente de antibiótico, cirurgia abdominal prévia, uso de sonda nasoenteral (SNE) | `Abordagem às diarreias.pdf`, p.25 (imagem) | CONFIRMADO |
| Antibióticos classicamente gatilho ("CFC") | clindamicina (principal), fluoroquinolonas e cefalosporinas — qualquer antibiótico pode desencadear o quadro, mas esses três são os classicamente mais associados | `Abordagem às diarreias.pdf`, p.25 (imagem) | CONFIRMADO |
| Diagnóstico laboratorial/endoscópico | pesquisa de toxina A e B (ELISA e PCR); coprocultura; colonoscopia mostrando pseudomembranas amarelo-esbranquiçadas | `Abordagem às diarreias.pdf`, p.26 (imagem, inclui foto de colonoscopia) | CONFIRMADO |
| GDH (glutamato desidrogenase) | usado como teste de triagem em algoritmo diagnóstico de 2 etapas (GDH de alta sensibilidade + toxina/NAAT confirmatório de alta especificidade) — não citado na fonte B disponível | conhecimento geral (ausente da fonte) | conhecimento geral |
| Janela de risco pós-antibiótico | o quadro pode surgir até 8-10 semanas após a suspensão do antibiótico gatilho, mesmo sem uso atual | conhecimento geral (ausente da fonte) | conhecimento geral |
| Tratamento conforme a fonte B (desatualizado) | vancomicina VO 125mg 6/6h; metronidazol VO 500mg 8/8h listado como opção equivalente; fidaxomicina se recorrência; se grave/septicemia: vancomicina VO + metronidazol EV; transplante de microbiota fecal para casos recorrentes | `Abordagem às diarreias.pdf`, p.27 (imagem) | CORRIGIDO — ver linha abaixo |
| Tratamento atualizado (1ª linha atual, conhecimento geral equivalente a A') | vancomicina VO 125mg 6/6h por 10 dias OU fidaxomicina 200mg 12/12h por 10 dias para episódio inicial (não-grave e grave); metronidazol reservado a casos não-graves quando as duas opções acima estão indisponíveis, ou associado por via EV à vancomicina VO em quadro fulminante/complicado; recorrência: fidaxomicina preferencial ou vancomicina em esquema prolongado/pulsado; recorrências múltiplas: transplante de microbiota fecal | conhecimento geral (diretriz IDSA/SHEA 2021) — diverge da fonte B, que trata metronidazol como 1ª linha equivalente | CORRIGIDO |
| Antiperistáltico | contraindicado — risco de precipitar megacólon tóxico; não citado explicitamente na fonte B disponível, incluído por ser ponto de altíssima cobrança e de segurança clínica | conhecimento geral (ausente da fonte) | conhecimento geral |

## Pegadinhas

**Imperdoáveis (ponto explicitamente sinalizado como de alto risco para este tema):**

- Prescrever antiperistáltico/antidiarreico (ex. loperamida) para "aliviar a diarreia" — pode precipitar megacólon tóxico.
- Responder metronidazol como 1ª linha isolada de tratamento — a diretriz atual coloca vancomicina VO (ou fidaxomicina) como base do esquema.
- Pedir só coprocultura e considerar isso suficiente para fechar o diagnóstico — o exame-alvo é a pesquisa de toxina/GDH.
- Descartar o diagnóstico porque o paciente "não está tomando antibiótico no momento" — a janela de risco vai até 8-10 semanas após a suspensão.
- Prescrever vancomicina por via **parenteral** (a via oral é a que atinge concentração luminal eficaz no cólon; vancomicina EV não trata a colite por *C. difficile*).

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "Diarreia pós-ATB — manter conduta conservadora com antidiarreico e observar" | parece uma conduta cautelosa e de baixo risco | fechamento precoce / subestimação de risco | antiperistáltico é contraindicado nessa etiologia — retarda o trânsito de um cólon já inflamado e aumenta o risco de megacólon tóxico |
| "Metronidazol VO é a escolha, é o mais usado e mais barato" | é o antibiótico mais lembrado de fontes/provas mais antigas sobre o tema | regra mal-aprendida / desatualizada | a diretriz de referência atual (2021) reclassificou vancomicina VO (ou fidaxomicina) como 1ª linha; metronidazol passou a alternativa, não escolha equivalente |
| "Coprocultura positiva já confirma o diagnóstico" | coprocultura é o exame "padrão" lembrado para a maioria das diarreias infecciosas bacterianas | troca de comando / pivô perdido | a coprocultura pode ser positiva para cepas não-toxigênicas de *C. difficile*; o diagnóstico depende de demonstrar a toxina (ou GDH/NAAT), não a bactéria isoladamente |
| "Paciente não está em uso de nenhum medicamento, então não pode ser colite por *C. difficile*" | raciocínio temporal simplista — "causa" deveria estar presente no momento do efeito | premissa não checada | o quadro pode surgir semanas após a suspensão do antibiótico gatilho; a pergunta certa é sobre uso **recente**, não uso **atual** |

## Conduta

- Inicial: suspender o antibiótico gatilho, se ainda em uso e clinicamente possível; solicitar pesquisa de toxina A/B (e GDH/NAAT quando disponível); hidratação; **nunca** prescrever antiperistáltico.
- Definitiva: vancomicina VO 125mg 6/6h por 10 dias OU fidaxomicina 200mg 12/12h por 10 dias como 1ª linha atual; metronidazol reservado a casos não-graves sem acesso às opções acima, ou associado por via EV à vancomicina VO em quadro fulminante/complicado; recorrência → fidaxomicina ou vancomicina em esquema prolongado/pulsado; recorrências múltiplas → transplante de microbiota fecal.
- Condição da conduta: gravidade laboratorial (leucometria >15.000, creatinina ≥1,5× basal) e clínica (hipotensão, íleo, distensão abdominal) mudam o esquema — quadro fulminante pode exigir associação parenteral e avaliação cirúrgica além do esquema oral padrão.
- Diferencial perigoso: megacólon tóxico — distensão abdominal importante, parada de eliminação de fezes e gases, toxemia/taquicardia, risco de perfuração; é favorecido justamente pelo uso indevido de antiperistáltico.
- O que mudaria a decisão: gravidade laboratorial/clínica do quadro, primeiro episódio × recorrência, disponibilidade local de vancomicina VO/fidaxomicina.

## Mini-casos ativos

1. Mulher, 78 anos, internada há 12 dias por pneumonia tratada com clindamicina, hoje com diarreia aquosa 6×/dia, febre de 38,5°C e dor abdominal difusa, sem sangue nas fezes. **Pivô:** o uso recente de clindamicina somado à idade e à hospitalização já aponta para colite por *C. difficile* — solicitar pesquisa de toxina (não só coprocultura), garantir que nenhum antiperistáltico seja prescrito, e iniciar vancomicina VO.
2. Homem, 65 anos, diarreia iniciada 3 semanas após alta hospitalar onde recebeu ceftriaxona por 7 dias (já suspensa há 3 semanas). Leucocitose de 18.000/mm³, creatinina 1,8 mg/dL (basal 1,0 mg/dL). **Pivô:** o antibiótico já foi suspenso há 3 semanas, mas ainda está dentro da janela de risco (até 8-10 semanas); a leucocitose >15.000 associada à creatinina ≥1,5× o basal já caracteriza gravidade — o esquema deixa de ser "vancomicina VO isolada e reavaliar" e passa a exigir vigilância mais próxima de evolução para quadro fulminante.
3. Paciente em tratamento para colite por *C. difficile* há 2 dias, evolui com distensão abdominal importante, parada de eliminação de fezes e gases, e taquicardia. **Pivô:** reconhecer sinais de megacólon tóxico — suspender imediatamente qualquer antiperistáltico em uso, solicitar imagem abdominal (radiografia/TC) e acionar avaliação cirúrgica, pois o quadro caminha para risco iminente de perfuração.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Diarreia associada a ATB em idoso hospitalizado — qual exame fecha o diagnóstico? | Pesquisa de toxina A/B (ELISA/PCR) ou GDH — não a coprocultura isolada | fato |
| 1ª linha de tratamento atual para colite por *C. difficile* | Vancomicina VO 125mg 6/6h por 10 dias (ou fidaxomicina) — não metronidazol isolado | regra |
| Antiperistáltico está indicado na colite por *C. difficile*? | Não, nunca — risco de precipitar megacólon tóxico | contraindicação |
| Até quando após suspender o antibiótico gatilho pode surgir o quadro? | Até 8-10 semanas | valor |
| Achado colonoscópico característico | Pseudomembranas amarelo-esbranquiçadas | sinal-achado |
| Antibióticos classicamente gatilho ("CFC") | Clindamicina (principal), fluoroquinolonas, cefalosporinas | fato |

## Revisão

- Revisar quando: antes de qualquer simulação de caso de diarreia em paciente idoso ou hospitalizado, e sempre que a conduta antibiótica memorizada citar metronidazol como 1ª linha isolada.
- Critério de parada: quando, dado um caso de diarreia pós-antibiótico, conseguir nomear o exame correto (toxina/GDH), recusar antiperistáltico, e prescrever vancomicina VO como 1ª linha sem hesitar, em 3 variações de gravidade do caso.
