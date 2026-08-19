# Cirrose hepática, ascite e peritonite bacteriana espontânea

## Metadados

- Disciplina: CASOS_CLINICOS
- Especialidade: Gastro-hepatologia
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: sim (`Casos_Cli_nicos_P7_1__4f3f459b20` pp. 2–3, 18–19)
- Fontes usadas: Casos_Cli_nicos_P7_1__4f3f459b20 (B, ESCANEADA — slide fotografado, deck "Casos Clínicos P7", assinado Dr. Nomário Pedrosa Lacerda, pp. 2–3 caso BCT 60a + pp. 18–19 caso etilista + variações da PBE, com anotações manuscritas do aluno); CASOS_CL_NICOS_RESUMO__249c11a613 (B, NATIVA, resumo — seção Cirrose Hepática); 2_Avaliac_a_o_Casos_Cli_nicos_TURMA_B_2021_1__7bf703af15 (B, NATIVA — prova real, Q4 GASA e Q7 PBE)
- Evidência de prova/devolutiva: 2ª Avaliação Casos Clínicos Turma B 2021.1, Q4 (mulher 65a, ascite 1 mês, GASA 0,8 g/dL → cirrose descompensada é a resposta MENOS provável objetivamente porque GASA<1,1 aponta doença peritoneal, não hipertensão porta — item testa se o aluno aplica o corte 1,1 em vez de reconhecer o "quadro típico" de cirrose) e Q7 (homem 66a, cirrose alcoólica, confuso, líquido ascítico com 200 leucócitos/mm³ e 80% PMN → 160 PMN absoluto, que cai no limiar de variante de PBE, não PBE clássica).
- Limitações da fonte: tem_camada_A=false para o cluster — nenhuma fonte tem confirmação formal de autoria docente do professor da disciplina. Porém o deck ESCANEADO "Casos Clínicos P7" traz página de título explícita "Casos Clínicos P7 / Nomário Pedrosa Lacerda / Faculdade de Medicina Nova Esperança" nas pp. 2 e 13, o que sugere fortemente que é material de aula do próprio professor da disciplina — tratado aqui com peso alto mesmo classificado como B pelo pipeline automático. Um trecho do slide (estágios de cirrose Child-like) foi riscado pelo aluno com a nota "ver no material" — sinal de que o professor disse explicitamente para não decorar aquele quadro da tela, e por isso ele NÃO foi incluído nesta cápsula.
- Verificação nível 1: CONFIRMADO

## Como cai

Formato de Discussão de Casos Clínicos: grupos elaboram um caso (identificação, HDA, exame físico, exames complementares) e apresentam a defesa do raciocínio diante da turma e do professor. Nos dois casos-fonte usados aqui (paciente etilista com ascite recente e paciente cirrótico confuso com líquido ascítico neutrofílico), o professor pressiona sobre **por que o gradiente e a contagem de PMN definem a conduta, e não a impressão clínica geral** — a pergunta típica na arguição é "esse paciente tem estigma de hepatopatia crônica, mas o que no exame do líquido ascítico confirma ou afasta hipertensão porta como causa?" e "esse PMN de 200 com 80% neutrófilos é PBE clássica ou uma variante — qual, e muda a conduta?"

## Conceito operacional mínimo

Cirrose é o desfecho patológico comum de agressões hepáticas crônicas (fibrose extensa + nódulos regenerativos), levando a hipertensão porta e insuficiência hepatocelular. A tríade de HP relevante para a prova é ascite + esplenomegalia + circulação colateral/varizes, com encefalopatia hepática como manifestação da insuficiência hepatocelular. Ascite é a complicação mais comum de HP; sua complicação mais temida é a peritonite bacteriana espontânea (PBE) — o discriminador do líquido ascítico infectado é o PMN absoluto ≥250/mm³, não a impressão clínica de "paciente séptico".

## Pivô clínico

O gradiente de albumina soro-ascite (GASA) — não a etiologia "óbvia" pela história — decide se a ascite é por hipertensão porta ou por doença peritoneal: GASA ≥1,1 = transudato = hipertensão porta; GASA <1,1 = exsudato = doença peritoneal (neoplasia, TB peritoneal, pancreática). Dentro de cada grupo, a proteína do líquido ascítico refina a causa: GASA≥1,1 + proteína ≥2,5 = ascite cardiogênica; GASA≥1,1 + proteína <2,5 = ascite por cirrose; GASA<1,1 + proteína ≥2,5 = neoplasia/TB/pancreática; GASA<1,1 + proteína <2,5 = síndrome nefrótica. Um paciente com estigma óbvio de hepatopatia crônica ainda pode ter GASA<1,1 (outra causa concomitante) — a prova testa exatamente esse ponto (Q4 da 2ª Avaliação).

## Palavras-âncora

GASA ≥1,1 transudato/HP; GASA <1,1 exsudato; PMN ≥250/mm³ = PBE; PMN<250 + cultura+ = bacterascite; PMN>250 + cultura− = ascite neutrofílica; cultura monobacteriana (PBE) x polimicrobiana (secundária); paracentese em QIE; ceftriaxona 3ª geração; norfloxacino profilaxia; restrição de sódio 2g/dia; espironolactona:furosemida 100:40.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| interpretar imagem/laboratório | GASA ≥1,1 vs <1,1 aplicado ao valor numérico do caso, não à impressão clínica geral | limiar | operacional | narrativa acima do discriminador — fechar em "cirrose descompensada" pela história típica sem calcular o gradiente | treino de "calcule antes de fechar": dado GASA numérico + história sugestiva, forçar o aluno a citar o valor e classificar antes de nomear a causa |
| aplicar critério | PMN absoluto ≥250/mm³ no líquido ascítico define PBE; variantes por combinação de PMN e cultura | limiar | factual | valor errado — confundir contagem total de leucócitos (200) com PMN absoluto, ou tratar 80% de PMN sem calcular o valor absoluto | card de cálculo: dado leucócitos totais + %PMN, calcular PMN absoluto e classificar (PBE / bacterascite / ascite neutrofílica) em 5 casos |
| diferenciar próximos | PBE (monobacteriana) vs peritonite bacteriana secundária (polimicrobiana, cirurgia/perfuração) vs bacterascite vs ascite neutrofílica | sinal-achado | factual | troca de rótulo — usar "peritonite bacteriana secundária" quando o enunciado já dá cultura monobacteriana | tabela-par das 4 entidades com PMN + cultura + conduta lado a lado, treinada por reconhecimento rápido |
| conduta definitiva | esquema diurético escalonado (espironolactona+furosemida 100:40, dose máx 400/160) e meta de perda de peso 0,5–1kg/dia | sequência | operacional | definitiva antes da inicial — pular direto para dose máxima ou diurético isolado sem checar se restrição de sódio isolada já é suficiente | script fixo: sódio 2g/dia primeiro → se insuficiente, iniciar espironolactona+furosemida na proporção 100:40 → escalonar a cada 3-5 dias |
| reconhecer contraindicação | profilaxia 1ª de PBE (Cr≥1,2 ou ureia>53,5 ou Na≤130, OU Child-Pugh≥9 + bilirrubina≥3) x indicação de profilaxia 2ª (após qualquer episódio de PBE) | contraindicacao | operacional | premissa não checada — indicar norfloxacino de rotina em todo cirrótico com ascite sem checar se preenche o critério laboratorial da profilaxia 1ª | checklist escrito dos critérios antes de indicar profilaxia primária vs. indicação automática de secundária |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| GASA transudato (hipertensão porta) | ≥1,1 g/dL | Casos_Clinicos_P7_1 p.3; CASOS_CLINICOS_RESUMO | CONFIRMADO |
| GASA exsudato (doença peritoneal) | <1,1 g/dL | Casos_Clinicos_P7_1 p.3 | CONFIRMADO |
| Refinamento por proteína do líquido ascítico | ≥2,5 g/dL + GASA≥1,1 = cardiogênica; <2,5 + GASA≥1,1 = cirrose; ≥2,5 + GASA<1,1 = neoplasia/TB/pancreática; <2,5 + GASA<1,1 = síndrome nefrótica | Casos_Clinicos_P7_1 p.18 | CONFIRMADO |
| PBE — critério diagnóstico | PMN ≥250/mm³ no líquido ascítico, cultura monobacteriana | Casos_Clinicos_P7_1 p.3, p.18; CASOS_CLINICOS_RESUMO | CONFIRMADO |
| Bacterascite (variante) | PMN <250/mm³ + cultura positiva; costuma resolver espontaneamente, sem ATB se assintomático | Casos_Clinicos_P7_1 p.19 | CONFIRMADO |
| Ascite neutrofílica (variante) | PMN >250/mm³ + cultura negativa; tratar como PBE (culturas negativas não isentam o tratamento) | Casos_Clinicos_P7_1 p.19 | CONFIRMADO |
| Tratamento da PBE | cefalosporina de 3ª geração (ceftriaxona) ou amoxicilina+clavulanato | Casos_Clinicos_P7_1 p.18 | CONFIRMADO |
| Profilaxia primária da PBE | Cr≥1,2 mg/dL (ou ureia>53,5) ou Na≤130 mEq/L; OU Child-Pugh≥9 pontos + bilirrubina total≥3 mg/dL; droga de escolha norfloxacino | Casos_Clinicos_P7_1 p.18 | CONFIRMADO |
| Profilaxia secundária da PBE | indicada após todo episódio de PBE | Casos_Clinicos_P7_1 p.18 | CONFIRMADO |
| Local de escolha da paracentese | quadrante inferior esquerdo (QIE) — menor risco por sigmoide mais móvel que ceco | Casos_Clinicos_P7_1 p.18 | CONFIRMADO |
| Reposição de albumina em paracentese de alto volume | 6–8g de albumina por litro de ascite retirado quando volume >5L | Casos_Clinicos_P7_1 p.18 | CONFIRMADO |
| Esquema diurético clássico | espironolactona 100mg + furosemida 40mg dose única matinal, escalonar a cada 3-5 dias mantendo proporção 100:40, dose máx 400mg/160mg | Casos_Clinicos_P7_1 p.3, p.18 | CONFIRMADO |
| Meta de perda de peso com diurético | 0,5 a 1 kg/dia | Casos_Clinicos_P7_1 p.3, p.18 | CONFIRMADO |
| Estadiamento de gravidade da cirrose (compensada/descompensada, mortalidade por estágio) | conteúdo do slide riscado pelo aluno, com nota "ver no material" | Casos_Clinicos_P7_1 p.2 | confirmar no slide (professor indicou não decorar dessa tela; conferir material complementar) |

## Pegadinhas

- Estigma clínico clássico de hepatopatia (telangiectasias, eritema palmar, ginecomastia) NÃO substitui o cálculo do GASA — a prova cobrou exatamente esse ponto (Q4: mulher com quadro sugestivo, mas GASA 0,8 aponta para causa peritoneal, não cirrose).
- 200 leucócitos/mm³ com 80% de PMN não é "quase PBE por estar perto de 250" — o PMN absoluto é 160/mm³ (200×0,80), abaixo do limiar de 250; é preciso calcular, não estimar.
- Bacterascite assintomática não trata com antibiótico de rotina — a conduta é repunção e reavaliação, ao contrário da ascite neutrofílica (PMN>250 com cultura negativa), que trata como PBE mesmo sem confirmação microbiológica.
- Cultura POLImicrobiana em líquido ascítico não é variante de PBE — é sinal de peritonite bacteriana secundária (perfuração/cirurgia), e muda a conduta para investigação cirúrgica, não só antibioticoterapia.
- Profilaxia com norfloxacino não é automática para todo cirrótico ascítico — depende de critério laboratorial objetivo (função renal/sódio) ou de episódio prévio de PBE.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "Cirrose descompensada" numa paciente com estigma sugestivo mas GASA 0,8 g/dL | a narrativa clínica (idade, ascite, perda de peso) soa como cirrose | narrativa acima do discriminador | GASA<1,1 aponta doença peritoneal (ex.: carcinomatose), não hipertensão porta — o dado laboratorial deveria vencer a impressão clínica |
| Classificar líquido com 200 leucócitos/80% PMN como "não PBE porque o total é <250" | confunde o corte de leucócitos totais com o corte de PMN absoluto | valor errado | o critério é PMN absoluto (160, calculado), que também não fecha PBE aqui — mas o erro do aluno é aplicar o corte na variável errada, não perceber que precisa calcular |
| Iniciar norfloxacino em todo paciente cirrótico com ascite "para prevenir PBE" | parece prudência preventiva | premissa não checada | profilaxia 1ª exige critério laboratorial objetivo (Cr/Na ou Child-Pugh+bilirrubina) — não é indicação automática por ter ascite |
| Tratar bacterascite assintomática com ceftriaxona imediatamente | soa mais seguro tratar toda cultura positiva | sobre-elaboração | bacterascite costuma resolver espontaneamente; a conduta preferida é repunção/reavaliação, não ATB de largada |

## Conduta

- Inicial: paracentese diagnóstica em toda ascite de início recente (ambulatorial ou internado) — contagem celular, diferencial, proteína total e albumina do líquido, calcular GASA.
- Definitiva: restrição de sódio (2g/dia) + diuréticos orais escalonados (espironolactona+furosemida 100:40) se restrição isolada insuficiente; PBE confirmada → ceftriaxona (ou amoxi-clavulanato) empírica, sem aguardar cultura.
- Condição da conduta: profilaxia com norfloxacino só se critério laboratorial (Cr≥1,2/ureia>53,5/Na≤130 ou Child-Pugh≥9+bilirrubina≥3) presente, OU após qualquer episódio prévio de PBE (secundária).
- Diferencial perigoso: peritonite bacteriana secundária (cultura polimicrobiana, sinais de abdome cirúrgico) — não responde a só antibiótico, precisa de investigação de foco perfurativo/cirúrgico.
- O que mudaria a decisão: GASA muda a hipótese etiológica inteira (porta x peritoneal); PMN absoluto (não %PMN nem leucócitos totais) muda entre observar e tratar; cultura mono x polimicrobiana muda entre PBE e peritonite secundária.

## Mini-casos ativos

Paciente cirrótico, ascite volumosa, GASA 1,3 g/dL, proteína do líquido ascítico 1,8 g/dL. Pergunta de defesa: "por que você classifica essa ascite como por cirrose e não cardiogênica, se ambas têm GASA≥1,1?" Variável decisiva: proteína do líquido ascítico <2,5 g/dL aponta cirrose; ≥2,5 apontaria causa cardiogênica — refinar o GASA com a proteína antes de fechar a etiologia.

Paciente cirrótico internado, ascite, líquido ascítico com 300 leucócitos/mm³, 90% PMN, cultura negativa. Pergunta de defesa: "essa cultura negativa exclui infecção e dispensa antibiótico?" Variável decisiva: PMN absoluto 270/mm³ (>250) com cultura negativa = ascite neutrofílica, que se trata como PBE apesar da cultura negativa — cultura negativa não descarta tratamento quando o PMN já fecha o critério.

Paciente com ascite recente, sem estigma de hepatopatia, dor abdominal, GASA 0,6 g/dL, proteína do líquido ascítico 3,2 g/dL. Pergunta de defesa: "por que você não trata como PBE mesmo tendo alteração inflamatória no líquido?" Variável decisiva: GASA<1,1 + proteína≥2,5 aponta causa peritoneal (neoplasia/TB), não hipertensão porta/PBE — a investigação deve seguir para etiologia peritoneal, não para tratamento empírico de PBE sem confirmar PMN≥250.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| GASA ≥1,1 significa | transudato / hipertensão porta | dado |
| GASA <1,1 significa | exsudato / doença peritoneal | dado |
| Critério diagnóstico de PBE | PMN ≥250/mm³ + cultura monobacteriana | dado |
| PMN<250 + cultura positiva = | bacterascite (costuma resolver espontâneo) | pegadinha |
| PMN>250 + cultura negativa = | ascite neutrofílica (trata como PBE) | pegadinha |
| Tratamento empírico da PBE | ceftriaxona (3ª geração) ou amoxicilina+clavulanato | dado |
| Local preferido de paracentese | quadrante inferior esquerdo | dado |
| Esquema diurético clássico | espironolactona 100mg + furosemida 40mg, escalonar 100:40 | dado |
| Critério de profilaxia primária de PBE | Cr≥1,2/ureia>53,5/Na≤130 OU Child-Pugh≥9+bilirrubina≥3 | pegadinha |

## Revisão

- Revisar quando: antes de qualquer vinheta com ascite + valores de GASA/proteína/PMN no líquido ascítico, ou caso de cirrótico confuso/febril com dado laboratorial do líquido.
- Critério de parada: resolver 5 casos-par variando GASA e proteína do líquido, mais 3 casos variando PMN absoluto e cultura, sem confundir os limiares.
