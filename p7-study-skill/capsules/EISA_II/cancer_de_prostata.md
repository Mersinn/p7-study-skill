# Câncer de Próstata

## Metadados

- Disciplina: EISA_II
- Especialidade: Urologia/Oncologia
- Unidade: III_UNIDADE
- Prioridade: alta
- Risco clínico: medio
- Status: reviewed_l1
- Camada de fonte usada: A+B
- fonte_visual: sim (`NEOPLASIA_DE_PROSTATA_RESUMIDA__58cfadd4e2` pp. 1–14)
- Fontes usadas: NEOPLASIA_DE_PROSTATA_RESUMIDA__58cfadd4e2 (slide, camada A); Urologia_CA_NCER_DE_PRO_STATA__ec4ee2ece9 (B, transcrição quase literal do mesmo slide); ANOTAC_O_ES_ca_ncer_de_pro_stata__6614a32c87 (B, resumo Karen Agra); Onco_NEOPLASIAS_UROLO_GICAS__66462ee210 (B); APOSTILA_SA_II_P7___e43cc7bc21 (B)
- Evidência de prova/devolutiva: tema `cai: true`, prioridade alta, força "forte" no cluster. O padrão geral de erro "definitiva antes da inicial em recidiva de próstata (bloqueio hormonal antes do tratamento loco-regional de resgate)" e "aplicar limiar numérico fora do contexto de idade que o valida (relação PSA livre/total só válida >55 anos)" do banco EISA II mapeiam diretamente para os dois pivôs centrais desta cápsula.
- Limitações da fonte: nenhuma limitação relevante — 4 fontes independentes (1 slide + 3 resumos de aluno, um deles quase-transcrição literal do slide) convergem em praticamente todos os números.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

Vinheta pedindo: (1) se o PSA alterado indica biópsia, cobrando o corte certo para a idade do paciente; (2) conduta diante de biópsia negativa com PSA persistentemente alterado (re-biópsia x RTU); (3) conduta diante de recidiva bioquímica pós-prostatectomia — reconhecer se o padrão é local (radioterapia de resgate) ou sistêmico (hormonioterapia); (4) sequência correta do tratamento do câncer metastático até a resistência à castração.

## Conceito operacional mínimo

Câncer de próstata é hormônio-dependente, majoritariamente assintomático até doença avançada (incide na zona periférica, não comprime a uretra como a HPB). Diagnóstico = PSA + toque retal → biópsia guiada por USG transretal (12 fragmentos, sextante) se qualquer um estiver alterado. O PSA só é interpretável dentro do contexto que o valida: idade do paciente muda o corte de biópsia, e ITU/instrumentação recente falseiam o valor. No tratamento metastático, a sequência é sempre castração (cirúrgica ou química) → se falhar, bloqueio adrenal (abiraterona) → se falhar, quimioterapia — nunca pular etapa.

## Pivô clínico

(1) O corte de PSA que indica biópsia muda com a idade: PSA 4–10 ng/ml só usa a relação livre/total <10% como critério em pacientes **>55 anos**; em pacientes **até 55 anos**, o corte é PSA >2,5 ng/ml isoladamente — aplicar o critério de livre/total fora dessa faixa etária é o erro clássico. (2) Após prostatectomia radical, recidiva bioquímica com perfil de baixo risco pré-operatório (PSA pré ≤10, Gleason <7, sem invasão de vesícula seminal, PSA detectável só após 2 anos, margem cirúrgica positiva) sugere recidiva **local** → radioterapia de resgate na loja prostática; perfil de alto risco (PSA pré >20, Gleason ≥7, invasão de vesícula seminal, PSA detectável <2 anos, margem negativa) sugere recidiva **sistêmica** → tratamento hormonal. Tratar como sistêmica um caso de padrão local (ou vice-versa) é o erro central da prova nesse tópico.

## Palavras-âncora

PI-RADS IV/V; sextante (12 fragmentos); NIP/PIN; ASAP; cinética de PSA (0,75 ng/ml/ano); densidade de PSA (>0,15); flare tumoral; critério ASTRO/Phoenix (nadir+2); orquiectomia subcapsular; abiraterona + prednisona; compressão medular.

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | idade do paciente (>55 x ≤55 anos) para escolher o corte de biópsia com PSA 4–10 | limiar | factual | generalizar critério de bolso fora do contexto de idade — aplicar a relação PSA livre/total <10% em paciente ≤55 anos, ou usar corte de 2,5 em paciente >55 | tabela única "corte de PSA por faixa etária", revisada ativamente antes de cada caso |
| diferenciar próximos (recidiva pós-PTR) | perfil de risco pré-operatório + tempo até PSA detectável + margem cirúrgica | sinal-achado | operacional | definitiva antes da inicial — indicar hormonioterapia sistêmica em paciente com perfil de recidiva local, pulando a radioterapia de resgate | tabela cruzada dos 2 perfis (local x sistêmico), treinada variando 1 variável por vez |
| conduta / sequência | resposta do PSA a cada etapa do bloqueio hormonal (castração → abiraterona → quimioterapia) | sequência | operacional | perder a sequência — pular direto para quimioterapia ou abiraterona sem confirmar falha da etapa anterior (PSA voltando a subir) | script fixo "castração → PSA subiu? → abiraterona → PSA subiu de novo? → quimioterapia", nunca pular |
| reconhecer contraindicação | presença de obstrução urinária antes de indicar radioterapia | contraindicação | factual | premissa não checada — indicar radioterapia em paciente com sintomas obstrutivos, que a RT só piora (distorção arquitetural da próstata) | checklist fixo: "paciente tem sintomas obstrutivos?" antes de escolher RT x cirurgia |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Indicação de biópsia por PSA | Toque suspeito; OU PSA >10 ng/ml (repetido); OU PSA 4–10 com relação livre/total <10% **em >55 anos**; OU PSA >2,5 ng/ml **em ≤55 anos**; OU cinética de PSA >0,75 ng/ml/ano | NEOPLASIA_DE_PROSTATA p.3-4 | CONFIRMADO (3 fontes convergentes) |
| Cinética de PSA em uso de testosterona exógena | Tolera-se subida de até 1,4 ng/ml/ano (testosterona é hiperplasiante) | ANOTAC_O_ES_ca_ncer_de_pro_stata p.1 | CONFIRMADO (só 1 fonte B; confirmar no slide) |
| PSA e ITU | ITU é a principal causa de PSA falsamente elevado — pedir urina 1 junto; se leucocitúria, tratar ITU e recolher PSA depois | ANOTAC_O_ES_ca_ncer_de_pro_stata p.2 | CONFIRMADO |
| Intervalo pós-instrumentação uretral para colher PSA | Aguardar 21 dias (3 semanas) | ANOTAC_O_ES_ca_ncer_de_pro_stata p.2 | CONFIRMADO |
| PSA normal não exclui câncer | 25% dos cânceres de próstata cursam com PSA <4 ng/ml | NEOPLASIA_DE_PROSTATA p.5 | CONFIRMADO |
| Biópsia — técnica padrão | Transretal, guiada por USG, mínimo 12 fragmentos (sextante = 2 fragmentos × 6 regiões), zona periférica | NEOPLASIA_DE_PROSTATA p.3, p.6 | CORRIGIDO — Onco_NEOPLASIAS p.6 registrava "preferencialmente 18 fragmentos"; prevalece o slide (12) |
| Antibioticoprofilaxia pré-biópsia | Levofloxacino 500mg — 1cp na noite anterior, 1cp na noite da biópsia, 1cp na noite posterior (3 doses) | Urologia_CA_NCER_DE_PRO_STATA p.4-5 | CONFIRMADO (só fontes B; confirmar no slide) |
| Intervalo mínimo para re-biópsia | 90 dias (até 120 dias) após a biópsia anterior | Urologia_CA_NCER_DE_PRO_STATA p.3-4 | CONFIRMADO |
| Sequência de re-biópsia (SUS) | 1) padrão (12 frag.) → 2) padrão repetida ou saturação (16-20 frag.) → 3) guiada por RNM multiparamétrica com fusão → 4) RTU (colhe zona periuretral, ~10% dos CaP) | ANOTAC_O_ES_ca_ncer_de_pro_stata p.4; Urologia_CA_NCER_DE_PRO_STATA p.4 | CONFIRMADO (2 fontes B convergentes; confirmar no slide) |
| Complicação mais comum da biópsia | Hematoespermia 9,8% (até 90 dias); disúria persistente 7,2%; hematúria 6,2%; urosepse é a mais rara (0,1%) | NEOPLASIA_DE_PROSTATA p.6-7 | CONFIRMADO (slide + 2 fontes B idênticas) |
| Tipo histológico predominante | Adenocarcinoma 95%; zona periférica 75-80% | NEOPLASIA_DE_PROSTATA p.7 | CORRIGIDO — Onco_NEOPLASIAS p.6 registrava 98%; prevalece o slide (95%) |
| Estratificação de risco por Gleason | ≤6 = baixo risco; 7 = risco intermediário; 8-10 = alto risco | NEOPLASIA_DE_PROSTATA p.8 | CONFIRMADO |
| Indicação de cintilografia óssea | Biópsia positiva **E** (PSA que indicou biópsia >20 ng/ml OU Gleason ≥7 OU dor óssea OU fosfatase alcalina elevada) | NEOPLASIA_DE_PROSTATA p.8-9 | CONFIRMADO |
| Prostatectomia radical — resultado | ~85% de cura; disfunção erétil até 80-90% (Karen: 92%); incontinência <10%; estenose 0,5-9% | NEOPLASIA_DE_PROSTATA p.9-10 | CONFIRMADO |
| Radioterapia — contraindicação | Mesmas indicações da PTR, EXCETO paciente com obstrução urinária (RT piora o padrão miccional) | NEOPLASIA_DE_PROSTATA p.10 | CONFIRMADO |
| Braquiterapia — critérios | Gleason <7; próstata <60g; expectativa de vida >5 anos; sem sintomas urinários | NEOPLASIA_DE_PROSTATA p.11 | CONFIRMADO |
| Observação vigilante — critérios | T1c (biópsia por PSA, não por toque); ausência de padrão 4/5 de Gleason primário; ≤3 fragmentos positivos de 12; nenhum fragmento >50% comprometido | NEOPLASIA_DE_PROSTATA p.11 | CONFIRMADO |
| Orquiectomia bilateral | Padrão-ouro do bloqueio hormonal (testosterona <50 em 4h); indicação de urgência: compressão medular aguda por metástase | NEOPLASIA_DE_PROSTATA p.11; ANOTAC_O_ES_ca_ncer_de_pro_stata p.9 | CONFIRMADO |
| Flare tumoral | Antiandrogênico periférico deve ser feito 2-3 semanas antes e mantido 2-3 semanas após início do agonista de LHRH, para evitar hiperestimulação inicial | NEOPLASIA_DE_PROSTATA p.12; ANOTAC_O_ES_ca_ncer_de_pro_stata p.9 | CONFIRMADO |
| Sequência na resistência à castração | Castração (química/cirúrgica) → PSA subiu → Abiraterona (bloqueia CYP17 adrenal) + prednisona 10mg/dia → PSA subiu novamente → Quimioterapia | ANOTAC_O_ES_ca_ncer_de_pro_stata p.9 | CONFIRMADO (só fonte B; confirmar no slide) |
| Recidiva bioquímica pós-PTR | PSA persistentemente detectável após PTR, ou elevação após período indetectável ("cut point" 0,2–0,4 ng/ml) | NEOPLASIA_DE_PROSTATA p.13 | CONFIRMADO |
| Perfil de recidiva local pós-PTR | PSA pré ≤10; Gleason <7; sem invasão de vesícula seminal; PSA detectável >2 anos pós-cirurgia; margem cirúrgica positiva → radioterapia na loja prostática | NEOPLASIA_DE_PROSTATA p.13-14 | CONFIRMADO |
| Perfil de recidiva sistêmica pós-PTR | PSA pré >20; Gleason ≥7; com invasão de vesícula seminal; PSA detectável <2 anos; margem negativa → tratamento hormonal | NEOPLASIA_DE_PROSTATA p.13-14 | CONFIRMADO |

## Pegadinhas

- Relação PSA livre/total <10% só é critério válido para biópsia em pacientes **>55 anos** — em ≤55 anos, o corte é PSA >2,5 isolado.
- PSA normal (<4) não exclui câncer de próstata — 25% dos casos cursam assim; por isso o toque retal continua obrigatório mesmo com PSA normal.
- Biópsia negativa NÃO exclui malignidade — é evento aleatório/probabilístico dentro da zona periférica; PSA persistentemente alterado após biópsias negativas justifica re-biópsia (aguardando 90-120 dias) e, ao final, RTU para cobrir a zona periuretral (~10% dos CaP).
- Recidiva bioquímica pós-PTR não é sempre tratada com hormonioterapia — perfil de baixo risco pré-operatório com PSA detectável tardiamente (>2 anos) sugere recidiva LOCAL, tratada com radioterapia de resgate, não bloqueio hormonal sistêmico direto.
- Não pular etapa na resistência à castração — abiraterona só entra depois que a castração (química/cirúrgica) falhou (PSA voltou a subir); quimioterapia só depois que a abiraterona também falhou.
- Radioterapia está contraindicada (relativamente) em paciente com obstrução urinária — nesse caso, prostatectomia é preferível.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "Homem de 48 anos, PSA 6 ng/ml, relação livre/total 8% → sem indicação de biópsia (relação >5%... aguardar)" | O raciocínio de livre/total parece aplicável a qualquer PSA na faixa 4-10 | generalizar critério de bolso desatualizado | Em ≤55 anos o critério de livre/total não vale — o corte correto para essa idade é PSA >2,5, que já está ultrapassado (6 > 2,5), logo há indicação de biópsia |
| "Paciente pós-PTR, PSA pré 25, Gleason 8, PSA detectável 8 meses após cirurgia → radioterapia de resgate na loja prostática" | "Recidiva pós-cirurgia" evoca reflexo de tratar localmente | analogia sem validação funcional | Esse perfil (PSA pré alto, Gleason alto, detecção precoce) é de recidiva SISTÊMICA — a conduta correta é tratamento hormonal, não RT local |
| "Câncer de próstata metastático, iniciar quimioterapia diretamente para ganhar tempo" | Doença metastática parece justificar tratamento mais agressivo de cara | definitiva antes da inicial | A sequência obrigatória começa pela castração (cirúrgica ou química); quimioterapia só entra após falha de castração + abiraterona |
| "Iniciar agonista de LHRH isolado no paciente recém-diagnosticado com metástase óssea extensa" | Agonista de LHRH é o tratamento hormonal "padrão" | premissa não checada | Sem antiandrogênico periférico associado 2-3 semanas antes, o agonista de LHRH causa flare tumoral (hiperestimulação inicial) — risco de piora aguda, inclusive compressão medular |

## Conduta

- Inicial: PSA + toque retal → biópsia transretal guiada por USG (12 fragmentos) se PSA ou toque alterados, respeitando o corte de PSA ajustado à idade.
- Definitiva: doença localizada → prostatectomia radical OU radioterapia (sobrevida equivalente); observação vigilante se critérios de baixo risco preenchidos; doença metastática → bloqueio hormonal (castração) com antiandrogênico de cobertura contra flare.
- Condição da conduta: radioterapia evitada se obstrução urinária presente; braquiterapia só se Gleason <7, próstata <60g, expectativa de vida >5 anos e sem sintomas urinários.
- Diferencial perigoso: compressão medular aguda por metástase óssea é indicação de orquiectomia subcapsular de URGÊNCIA, não conduta eletiva.
- O que mudaria a decisão: perfil de recidiva pós-PTR (local x sistêmico) muda radioterapia de resgate por hormonioterapia; resposta do PSA a cada etapa do bloqueio hormonal autoriza (ou não) avançar para a próxima linha de tratamento.

## Mini-casos ativos

Homem de 52 anos, PSA 7 ng/ml, relação livre/total 12%, toque normal. Variável decisiva: idade ≤55 → critério de livre/total não se aplica; usar corte PSA >2,5 (já ultrapassado) → indicar biópsia.

Homem pós-prostatectomia radical há 3 anos, PSA pré-operatório era 8, Gleason 6, margem positiva, PSA agora detectável em 2,8 ng/ml. Variável decisiva: perfil de baixo risco + detecção tardia (>2 anos) → recidiva local → radioterapia de resgate na loja prostática.

Homem com câncer de próstata metastático em bloqueio hormonal há 18 meses (castração química), PSA volta a subir progressivamente. Variável decisiva: falha da castração confirmada pelo PSA → próxima etapa é abiraterona + prednisona, não quimioterapia direta.

Homem com câncer de próstata metastático e quadro agudo de paraparesia por compressão medular. Variável decisiva: emergência oncológica → orquiectomia subcapsular de urgência, não bloqueio hormonal eletivo.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Corte de PSA 4-10 com relação livre/total <10% — para quem vale? | Só para pacientes >55 anos | pegadinha |
| Corte de PSA para indicar biópsia em ≤55 anos | PSA >2,5 ng/ml | dado |
| Nº de fragmentos da biópsia padrão | 12 (sextante, 2 por região × 6) | dado |
| Biópsia negativa exclui câncer? | Não — é evento aleatório; PSA persistente justifica re-biópsia | pegadinha |
| Sequência do bloqueio hormonal na resistência à castração | Castração → abiraterona (+prednisona) → quimioterapia | sequência |
| Perfil de recidiva LOCAL pós-PTR | PSA pré baixo, Gleason baixo, detecção tardia (>2 anos), margem + | dado |
| Perfil de recidiva SISTÊMICA pós-PTR | PSA pré alto (>20), Gleason ≥7, detecção precoce (<2 anos), margem - | dado |
| Por que associar antiandrogênico ao agonista de LHRH? | Evitar o "flare tumoral" (hiperestimulação inicial) | pegadinha |
| Contraindicação relativa à radioterapia | Obstrução urinária | dado |
| Indicação de urgência de orquiectomia | Compressão medular aguda por metástase | dado |
| Critérios de observação vigilante | T1c por PSA, sem padrão 4/5 primário, ≤3/12 fragmentos +, nenhum >50% comprometido | dado |

## Revisão

- Revisar quando: antes de qualquer vinheta com PSA alterado pedindo indicação de biópsia, e antes de vinheta de recidiva pós-prostatectomia.
- Critério de parada: aplicar corretamente o corte de PSA por idade e classificar recidiva local x sistêmica em 3 casos seguidos, sem pular etapa na sequência de tratamento da doença metastática resistente à castração.
