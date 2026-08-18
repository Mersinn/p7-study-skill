# OSCE Endocrinologia — diabetes, tireoidopatias, Cushing e hiperfunção hipofisária

## Metadados

- Disciplina: OSCE
- Especialidade: Endocrinologia
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: sim (`assuntos OSCE p7 2025.1`, p. 1 — confirma que Diabetes, Hipertireoidismo, Nódulos de tireoide e Hiperandrogenismo são as 4 estações oficiais de Endócrino em 2025.1; documento fora do array de fontes do cluster)
- Fontes usadas: `OSCE .pdf` (camada B, ~p. 56-83 — caso clínico completo de Cushing com comandos e gabarito); `OSCE - ENDOCRINOLOGIA.pdf` (camada B, ~p. 1-4, formato tabela doença/sinais/exame/diagnóstico/tratamento); `FACILITA OSCE (1).pdf` (camada B, sumário indica Diabetes p. 23 e Hiper/Hipotireoidismo p. 26 — usado aqui só para a lógica de raciocínio de obesidade/Cushing como pista associada)
- Evidência de prova/devolutiva: caso clínico com gabarito comentado (Cushing, `OSCE .pdf`)
- Limitações da fonte: **Hiperandrogenismo é estação oficial confirmada na grade 2025.1, mas nenhuma das 3 fontes mapeadas para este cluster traz conteúdo sobre o tema** — não invente aqui; trate como lacuna de cobertura e busque fonte dedicada antes da prova. O trecho de "coma mixedematoso" tem a dose de manutenção de levotiroxina cortada na extração de texto (só a dose de ataque veio completa) — marcado abaixo como pendência.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

Estação clássica de "reconhecer síndrome pela ectoscopia + confirmar com exame laboratorial + tratar". O caso descreve um quadro clínico com uma foto de achados de exame físico (ectoscopia) e pede, em sequência: hipótese → descrição dos achados visíveis → exame que confirma → conduta. Em Endócrino, o padrão-ouro citado nas fontes B nunca é "decorar o hormônio" isolado — é reconhecer o **eixo** (hipófise vs periférico) e o **sentido** da alteração (TSH alto/baixo, ACTH alto/baixo) antes de nomear a doença. **Hiperandrogenismo é estação oficial em 2025.1 mas está fora da cobertura das fontes disponíveis — ver Limitações acima.**

## A estação

- **Tarefa:** a partir do caso clínico e da ectoscopia/exame físico descritos ou visíveis na cabine, reconhecer a síndrome endócrina, descrever os achados de exame físico esperados, indicar o exame que confirma e propor a conduta (2 opções costuma ser aceito quando o comando pede "cite duas opções").
- **Tempo:** não informado nas fontes.
- **Ator/paciente:** caso clínico com descrição de ectoscopia (ex.: fácies cushingoide, estrias violáceas) — o achado pode vir descrito no texto ou colado como imagem/figura na cabine.
- **Material:** exames laboratoriais já com resultado disponível na cabine (ex.: PSA, USGTR, TSH/T4L, PAAF), conforme o caso.
- **Critério do checklist (inferido):** nomear a hipótese, descrever cada achado de ectoscopia visível (não só citar o diagnóstico), indicar o exame confirmatório correto (não qualquer exame de tireoide/hipófise genérico) e listar a(s) opção(ões) terapêutica(s) pedida(s).

## Pivô clínico

O pivô é a **direção do eixo hormonal**: cortisol alto + ACTH alto = hipófise; cortisol alto + ACTH baixo/normal = adrenal. TSH baixo + T4L alto = hipertireoidismo primário; TSH alto + T4L alto = hipersecreção hipofisária de TSH (raro, mas é a pegadinha clássica de trocar "TSH alto" por "sempre hipotireoidismo"). Errar a direção da seta derruba a hipótese inteira mesmo sabendo o nome da doença.

## Palavras-âncora

Ectoscopia · TSH/T4L · ACTH · cortisol pós-dexametasona · PAAF · TIRADS · Bethesda-like (critérios de PAAF) · IGF-1 · agonista dopaminérgico · cirurgia transesfenoidal (CTE).

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | indicação de PAAF: nódulo sólido/misto ≥1cm OU calcificação OU Chammas IV/V OU crescimento ≥50% do volume/≥20% em 2 dimensões em 1 ano; nódulo ≥4cm vai direto para lobectomia sem PAAF | limiar | operacional | valor errado — aplicar "PAAF sempre" sem checar se o nódulo já ultrapassou o limiar que pula a PAAF (≥4cm) | casos pareados: nódulo de 0,8cm TIRADS alto vs nódulo de 4,5cm — decidir PAAF ou cirurgia direta antes de olhar a resposta |
| interpretar imagem/ecg/laboratório | sentido do TSH e do T4L define primário vs central vs subclínico (hiper e hipotireoidismo) | função | factual | inverter a leitura da dupla TSH/T4L (achar que TSH baixo é sempre hipotireoidismo) | tabela comparativa das 6 combinações possíveis (TSH×T4L, hiper e hipo) treinada como flashcard de associação direta, não frase corrida |
| conduta definitiva | sequência de tratamento do Cushing: cirurgia (CTE) é 1ª escolha; medicamentoso (cetoconazol) para casos graves/sem remissão; radioterapia só se insucesso cirúrgico | sequência | operacional | inverter a ordem — oferecer cetoconazol como resposta única "porque é mais simples", sem citar a cirurgia como 1ª escolha | flashcard de sequência terapêutica por doença hipofisária (Cushing, acromegalia, prolactinoma), sempre nomeando a 1ª e a 2ª linha separadamente |
| reconhecer contraindicação | combinações fármaco × comorbidade no DM2 (DII evita acarbose/metformina; HPB evita iSGLT2; IC prefere iSGLT2; idoso frágil prefere iDPP4) | contraindicação | factual | aplicar a combinação "padrão" de DM2 (metformina + o que for) sem checar a comorbidade citada no caso | tabela fixa comorbidade → fármaco a evitar/preferir, treinada com 5 casos que variam só a comorbidade associada |
| priorizar emergência | coma mixedematoso (hipoglicemia + RNC + hipotensão/bradicardia + hipotermia + hiponatremia) é emergência que exige levotiroxina IV em altas doses, não a dose de reposição ambulatorial | sinal-achado | operacional | tratar hipotireoidismo descompensado com a dose de reposição padrão (1,6 mcg/kg/dia VO) em vez de reconhecer a emergência e escalonar a dose/via | treinar reconhecimento do padrão de descompensação aguda de doença hormonal crônica como gatilho de mudança de dose/via, não só de diagnóstico |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Diagnóstico de DM (2 testes se assintomático; 1 se sintomas clássicos) | Glicemia jejum ≥126 mg/dL · HbA1c ≥6,5% · TOTG 2h ≥200 mg/dL · glicemia aleatória ≥200 mg/dL + sintomas clássicos (basta 1 teste) | OSCE .pdf, p. ~58 (camada B) | CONFIRMADO |
| Escalonamento terapêutico do DM2 por HbA1c | HbA1c <7,5% = monoterapia (metformina) · 7,5-9% = terapia dupla · >9% = terapia tripla · >9% + sintomas ou HGT >300 = insulinização | OSCE .pdf, p. ~59 (camada B) | CONFIRMADO |
| Esquema clássico de insulinização | NPH + regular, dose 0,3-1 UI/kg/dia, 2/3 pela manhã e 1/3 à noite | OSCE .pdf, p. ~59 (camada B) | CONFIRMADO |
| Indicação de PAAF em nódulo de tireoide | sólido/misto ≥1cm OU calcificação OU Chammas IV/V OU crescimento ≥50% do volume ou ≥20% em 2 dimensões em 1 ano; nódulo ≥4cm vai direto para lobectomia | OSCE .pdf, p. ~65 (camada B) | CONFIRMADO |
| Diagnóstico de hipertireoidismo | TSH reduzido + T4L aumentado (clínico); TSH reduzido + T4L normal (subclínico); TSH e T4L aumentados (central, sugere adenoma hipofisário produtor de TSH) | OSCE .pdf, p. ~68 (camada B) | CONFIRMADO |
| Tratamento do hipertireoidismo | metimazol (1ª linha, inibe conversão T4→T3) · propiltiouracil (gravidez) · radioablação por iodo (recidiva) · cirurgia (bócio volumoso/malignidade na PAAF) · propranolol 40-120mg/dia (controle sintomático, ~4 semanas) | OSCE .pdf, p. ~70 (camada B) | CONFIRMADO |
| Quando tratar hipotireoidismo | TSH >10 OU sintomático OU doença cardíaca OU jovem OU grávida | OSCE - ENDOCRINOLOGIA.pdf, p. ~4 (camada B, tabela) | CONFIRMADO |
| Reposição de levotiroxina | 1,6 mcg/kg/dia, dose única, manhã, em jejum; dose de supressão 2,2 mcg/kg/dia; reavaliar TSH em 4-6 semanas | OSCE - ENDOCRINOLOGIA.pdf, p. ~4 (camada B, tabela) | CONFIRMADO |
| Coma mixedematoso — achados | hipoglicemia, rebaixamento do nível de consciência, depressão respiratória, hipotensão + bradicardia, hipotermia, hiponatremia | OSCE - ENDOCRINOLOGIA.pdf, p. ~4 (camada B, tabela) | CONFIRMADO |
| Coma mixedematoso — dose de ataque de levotiroxina | 500-800 mcg (dose de ataque) | OSCE - ENDOCRINOLOGIA.pdf, p. ~4 (camada B, tabela) | CONFIRMADO |
| Coma mixedematoso — dose de manutenção | valor cortado na extração de texto (só restou o fragmento "100") | OSCE - ENDOCRINOLOGIA.pdf, p. ~4 (camada B, tabela) | confirmar no slide |
| Confirmação de hipercortisolismo (Cushing) | 2 de 3 alterados: cortisol pós 1mg dexametasona ≥1,8 mcg/dL · cortisol urinário livre 3-4x LSN · cortisol salivar da meia-noite ≥2x LSN | OSCE .pdf, p. ~76 (camada B) | CONFIRMADO |
| Etiologia do Cushing pela dupla ACTH/cortisol | cortisol alto + ACTH alto = origem hipofisária (Doença de Cushing) · cortisol alto + ACTH baixo/normal = origem adrenal (adenoma) | OSCE .pdf, p. ~77 (camada B) | CONFIRMADO |
| Tratamento do Cushing | cirurgia (CTE, adenomectomia transesfenoidal) = 1ª escolha, melhora em 2-12 meses · cetoconazol = medicamentoso, casos graves/sem remissão · radioterapia = insucesso cirúrgico | OSCE .pdf, p. ~78 (camada B) | CONFIRMADO |
| Diagnóstico de acromegalia | IGF-1 normal + GH <0,4 exclui; IGF-1 ≥1,3x LSN confirma; padrão-ouro é GH pós-TOTG (dosar a cada 30min por 2h após 75g dextrosol) — normal suprime <0,4, acromegalia não suprime (>0,4) | OSCE .pdf, p. ~80 (camada B) | CONFIRMADO |
| Hiperprolactinemia — valores de corte | causas fisiológicas: prolactina <50 ng/mL (exceto gravidez); adenoma produtor: prolactina >100 ng/mL | OSCE .pdf, p. ~72 (camada B) | CONFIRMADO |

## Pegadinhas

**Imperdoáveis:**

- Nomear "hipertireoidismo" ou "hipotireoidismo" só pelo quadro clínico sem citar o par TSH/T4L que confirma — a hipótese sem o exame que a sustenta não fecha a estação.
- Esquecer de descartar corticoide exógeno antes de investigar Cushing endógeno (é o passo 1 do protocolo, antes até de confirmar hipercortisolismo).
- Trocar a ordem do tratamento do Cushing/prolactinoma/acromegalia — oferecer só o medicamentoso quando a cirurgia é 1ª escolha.
- Aplicar a combinação de fármacos "padrão" do DM2 (metformina + qualquer coisa) sem checar a comorbidade citada no caso (DII, HPB, IC, idoso frágil).

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "TSH alto = hipotireoidismo, sempre" | é a regra mais decorada de toda a endocrinologia básica | superextrapolação / regra mal-aprendida | existe hipertireoidismo central (TSH e T4L ambos altos) por adenoma hipofisário secretor de TSH — regra geral tem exceção que muda a resposta |
| Responder Cushing com "cortisol basal baixo" como achado tranquilizador | cortisol é secretado de forma pulsátil, então intuitivamente pareceria fazer sentido medir o basal | premissa não checada | o cortisol basal isolado NÃO serve para diagnóstico justamente pela secreção pulsátil — é por isso que se usam os 3 testes dinâmicos (dexa, urinário 24h, salivar da meia-noite) |
| Escolher metformina de primeira linha em paciente com DII descrita no caso | metformina é o fármaco mais "automático" para DM2 em qualquer contexto | premissa não checada / contraindicação ignorada | metformina (e acarbose) devem ser evitadas em doença inflamatória intestinal — o caso citou a comorbidade de propósito para mudar a resposta padrão |
| Achar que hiperprolactinemia leve (50-99 ng/mL) já fecha diagnóstico de prolactinoma | o valor está "alto" e o aluno já quer fechar a hipótese estrutural | fechamento precoce | a faixa entre causas fisiológicas (<50) e adenoma (>100) é uma zona cinzenta que exige RNM de sela túrcica antes de fechar prolactinoma, não decisão só pelo número |

## Conduta

- Inicial: nomear a síndrome (não o fármaco) a partir do quadro clínico + ectoscopia.
- Definitiva: confirmar com o exame laboratorial/dinâmico correto (não qualquer exame de tireoide/hipófise) e só então tratar.
- Condição da conduta: eixo hipofisário vs periférico decide qual exame confirma — nunca tratar antes de saber a direção do eixo.
- Diferencial perigoso: coma mixedematoso e crise adrenal são as descompensações agudas de doença hormonal crônica — reconhecer sinais de RNC/hipotensão/hipotermia num paciente com quadro tireoidiano/adrenal muda a via e a dose do tratamento.
- O que mudaria a decisão: comorbidade citada no caso (DII, HPB, IC, gravidez, idade) muda o fármaco de escolha mesmo mantendo o mesmo diagnóstico.

## Mini-casos ativos

1. Mulher, 29 anos, ganho de peso progressivo (20kg/2anos), fraqueza muscular, aborto espontâneo há 1 ano com piora do quadro, amenorreia, lesões avermelhadas no abdome, HAS e DM de início recente. **Pivô:** ectoscopia (fácies cushingoide, estrias violáceas, giba de búfalo) + descartar corticoide exógeno antes de pedir cortisol pós-dexa/urinário/salivar — não pule direto para "Cushing, trata com cetoconazol".
2. Paciente com bócio difuso, taquicardia, tremor, exoftalmia e TSH pedido no caso vem **aumentado**, com T4L também aumentado. **Pivô:** não é hipotireoidismo (apesar do TSH "alto" que o aluno decorou como sinal de hipo) — é hipertireoidismo central, e o próximo passo é investigar adenoma hipofisário secretor de TSH.
3. Homem, 58 anos, DM2 há 10 anos, insuficiência cardíaca com fração de ejeção reduzida, procurando ajuste de terapia. **Pivô:** a IC no enunciado não é pano de fundo — ela indica metformina + iSGLT2 (dapagliflozina), não a combinação genérica de DM2.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| ACTH alto + cortisol alto = origem? | Hipofisária (Doença de Cushing) | fato |
| ACTH baixo/normal + cortisol alto = origem? | Adrenal (adenoma) | fato |
| Nódulo de tireoide ≥4cm — pula a PAAF? | Sim, vai direto para lobectomia | limiar |
| Quando tratar hipotireoidismo com TSH entre 5 e 10? | Se sintomático, doença cardíaca, jovem ou grávida — senão, só reavaliar | regra |
| 1ª escolha de tratamento em Cushing, prolactinoma e acromegalia hipofisários | Cirurgia transesfenoidal (CTE) | fato |
| DM2 + DII — quais fármacos evitar? | Metformina e acarbose | contraindicação |

## Revisão

- Revisar quando: antes de simular qualquer estação hipofisária (Cushing, acromegalia, prolactinoma) ou de tireoide, e ao montar a tabela comorbidade × fármaco do DM2.
- Critério de parada: quando conseguir, sem consultar a fonte, nomear a síndrome, o exame confirmatório correto e a 1ª linha de tratamento para os 5 quadros (DM, nódulo, hiper/hipotireoidismo, Cushing, acromegalia) em menos de 30 segundos cada. Hiperandrogenismo fica de fora deste critério até a lacuna de fonte ser fechada.
