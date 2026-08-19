# Crescimento e desenvolvimento (curvas OMS, escore z, marcos do DNPM, idade corrigida)

## Metadados

- Disciplina: EISCA
- Especialidade: Pediatria geral / Puericultura
- Unidade: A_DEFINIR
- Prioridade: media
- Risco clínico: medio
- Status: reviewed_l1
- Camada de fonte usada: A+B
- fonte_visual: sim (`semio_PED__c241597932` p.3 — gráfico "Curvas de Crescimento" OMS weight-for-age; p.21 — slide "Microcefalia e Macrocefalia - OMS" com limiares de escore Z do professor)
- Fontes usadas: semio_PED__c241597932 (A, ESCANEADA, slide do professor — confirma o uso das curvas OMS e o limiar de escore Z especificamente para perímetro cefálico); Crescimento_e_desenvolvimento__03a4aa93bc (B, NATIVA, resumo de aluno — Bianca G. B. Santos, 4 páginas, único material do acervo com a tabela completa de escores Z por curva e os marcos/sinais de alarme do DNPM)
- Evidência de prova/devolutiva: MAPA_OPERACAO_MOVIMENTO regista "Curvas de crescimento — faixa de normalidade" (aplicar critério, variável decisiva = normalidade entre -2 e +2 escores Z, não -3/+3, cruzado com PC medido) no banco de itens dissecados do bloco EISCA.
- Limitações da fonte: a fonte A (slide do professor, `semio_PED`) confirma o uso de curvas OMS e o limiar de escore Z **especificamente para perímetro cefálico** (microcefalia/macrocefalia), mas é um slide de semiologia geral — não contém marcos do DNPM por idade nem a tabela completa de escore Z para peso/estatura/IMC, nem a fórmula de idade corrigida. Esses dados vêm só da fonte B (resumo de aluno), sem cruzamento com uma segunda fonte independente — tratados como CONFIRMADO por ser fonte única, mas sem verificação cruzada. Marcos de DNPM detalhados por semana/mês (ex.: sorrio social a X semanas, sentar sem apoio a Y meses) **não constam** nas fontes disponíveis além dos sinais de alarme listados; se a prova cobrar marco isolado fora dessa lista, é conhecimento geral de puericultura, não confirmado nestas fontes.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

O discriminador clássico é o **limiar de normalidade do escore Z**: a prova troca -2/+2 (correto, é o limiar de normalidade da OMS para peso/estatura/PC) por -3/+3 (limiar de gravidade, não de normalidade) — quem decora "a curva normal é entre -3 e +3" erra por regra mal-aprendida/valor trocado. O segundo padrão é cobrar **sinal de alarme do desenvolvimento por idade específica** (3, 6, 9, 12 meses) e trocar a idade esperada do marco, ou pedir cálculo de **idade corrigida** em prematuro e esquecer de aplicá-la até os 2 anos.

## Conceito operacional mínimo

Crescimento = ganho mensurável de peso/estatura/perímetros, avaliado por curvas OMS em escore Z (não em percentil isolado, embora ambos meçam a mesma posição relativa). Desenvolvimento = aquisição de função (motora, cognitiva, social), avaliado por marcos esperados por idade e por sinais de alarme quando um marco falha. Em pré-termo, o crescimento e o desenvolvimento só devem ser comparados à curva/marco cronológico usando a **idade corrigida** (idade cronológica menos as semanas que faltaram para completar 40 semanas), aplicada até os 2 anos de vida.

## Pivô clínico

O que decide "normal" ou "alterado" na curva de crescimento é o **escore Z entre -2 e +2** (não -3/+3, que já é a faixa de gravidade) — esse é o limiar que a prova mais testa. Para o desenvolvimento, o pivô é a **falha em atingir o marco esperado para a idade** (não a "impressão geral" de atraso) associada a sinal de alarme específico daquela idade (3, 6, 9 ou 12 meses) — presença de sinal de alarme antecipa a consulta seguinte; persistência por mais de 2 consultas indica encaminhamento a especialista.

## Palavras-âncora

Escore Z -2 a +2 = adequado; -3 a -2 = baixo/magreza; <-3 = muito baixo/magreza acentuada; >+2 = elevado; IMC tem faixa extra (+2 a +3 sobrepeso, >+3 obesidade); PC = Altura/2 + 10; idade corrigida = idade cronológica − semanas que faltavam para 40 semanas; catch-up: PC primeiro, depois estatura, depois peso; estirão: meninas 11 anos, meninos 13 anos; sinais de alarme aos 3/6/9/12 meses; consultas de puericultura: 7 no 1º ano, 2 no 2º ano, 1/ano do 3º ao 6º ano.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | faixa de normalidade do escore Z nas curvas de peso/estatura/PC: entre -2 e +2 (não -3/+3) | limiar | factual | valor errado — trocar -2/+2 (normalidade) por -3/+3 (gravidade) | card de limiar fixo + 5 casos com escore Z variando entre -3,5 e +3,5, classificando cada um |
| aplicar critério | faixa de IMC tem cortes extras: obesidade >+3; sobrepeso +2 a +3; risco de sobrepeso +1 a +2; adequado +1 a -2; magreza -2 a -3; magreza acentuada <-3 | limiar | factual | regra mal-aprendida — aplicar a mesma faixa -2/+2 do peso/estatura ao IMC sem ajustar os cortes intermediários | tabela comparativa lado a lado peso/estatura/PC x IMC, treinada com casos que só variam a curva usada |
| interpretar imagem/ecg/laboratório | ordem de recuperação do catch-up growth em pré-termo: PC recupera primeiro, depois estatura, depois peso | sequência | operacional | erro de leitura/sequência — inverter a ordem (achar que peso recupera primeiro) | flashcard de sequência fixa PC→estatura→peso, treinado com 3 casos de acompanhamento seriado |
| aplicar critério | idade corrigida = idade cronológica (semanas) − semanas que faltavam para completar 40 semanas de IG; usar até 2 anos | valor | operacional | premissa não checada — comparar prematuro à curva/marco pela idade cronológica sem corrigir, ou parar de corrigir antes dos 2 anos | 5 casos de cálculo de idade corrigida variando IG ao nascer e idade cronológica atual |
| reconhecer diagnóstico | sinal de alarme do desenvolvimento específico por idade: 3m (não sustenta cabeça/não abre mãos/não sorri), 6m (rigidez de membros/não controla cabeça/não dá risada), 9m (não senta sem apoio/mãos fechadas sem pinça/não localiza som/não balbucia), 12m (parada/inerte, não ajuda com as mãos, não brinca de esconde-achou, não responde ao nome) | fato | factual | troca de comando — atribuir o sinal de alarme à idade errada | tabela fixa idade→sinal de alarme, treinada com casos que trocam a idade do lactente |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Uso de curvas de crescimento OMS confirmado em aula | gráfico "Curvas de Crescimento" (weight-for-age) exibido no slide de medidas antropométricas | semio_PED p.3 (A) | CONFIRMADO |
| Limiar de escore Z para perímetro cefálico (microcefalia) | PC < -2 DP da média específica para sexo/IG = microcefalia; < -3 DP = microcefalia grave | semio_PED p.21 (A) | CONFIRMADO |
| Limiar de escore Z para perímetro cefálico (macrocefalia) | PC > +2 DP da média = macrocefalia (escore Z +2) | semio_PED p.21 (A) | CONFIRMADO |
| Momento da medida de PC para classificação de micro/macrocefalia | ≥24h após o nascimento e dentro da 1ª semana de vida (até 6 dias e 23h) | semio_PED p.21 (A) | CONFIRMADO |
| Interpretação de escore Z — peso e estatura | >+2 = elevado; entre -2 e +2 = adequado; entre -3 e -2 = baixo; <-3 = muito baixo | B p.2 | CONFIRMADO |
| Interpretação de escore Z — perímetro cefálico | >+2 = acima do esperado; entre -2 e +2 = adequado; <-2 = abaixo do esperado | B p.2 | CONFIRMADO |
| Interpretação de escore Z — IMC | +3 = obesidade; entre +2 e +3 = sobrepeso; entre +1 e +2 = risco de sobrepeso; entre +1 e -2 = adequado; entre -2 e -3 = magreza; <-3 = magreza acentuada | B p.2 | CONFIRMADO |
| Fórmula do perímetro cefálico estimado | PC = Altura/2 + 10 | B p.1 | CONFIRMADO |
| Classificação de peso ao nascer (pré-termo) | Baixo peso (BP) 1500–2499g; Muito baixo peso (MBP) 1000–1499g; Extremo baixo peso (EBP) <1000g | B p.1 | CONFIRMADO |
| Fórmula de idade corrigida | idade cronológica (semanas) − semanas que faltavam para completar 40 semanas de IG | B p.1 | CONFIRMADO |
| Exemplo de idade corrigida na fonte | bebê de 6 meses nascido com 30 semanas (faltavam 10 semanas ≈ 2 meses) → crescimento esperado de criança de 4 meses | B p.1 | CONFIRMADO |
| Ordem do catch-up growth (recuperação) | PC recupera a curva normal primeiro, depois estatura, depois peso | B p.1–2 | CONFIRMADO |
| Ganho de peso esperado por trimestre no 1º ano | 1º tri: 750g/mês (2.250g); 2º tri: 600g/mês (1.800g); 3º tri: 500g/mês (1.500g); 4º tri: 400g/mês (1.200g) | B p.2 | CONFIRMADO |
| Ganho de peso total esperado no 1º ano | 6.750g + peso de nascimento | B p.2 | CONFIRMADO |
| Velocidade de crescimento estatural pós-natal | elevada nos 2 primeiros anos; declínio dos 2–5 anos; constante a partir dos 5 anos (5–6 cm/ano) | B p.1 | CONFIRMADO |
| Estirão puberal — idade típica | meninas 11 anos; meninos 13 anos | B p.1 | CONFIRMADO |
| Calendário de consultas de puericultura | 1º ano: 7 consultas (15 dias/1/2/4/6/9/12 meses); 2º ano: 2 consultas (18/24 meses); 3º–6º ano: 1 consulta/ano | B p.1 | CONFIRMADO |
| Sinais de alarme do desenvolvimento aos 3 meses | não levanta a cabeça; não abre as mãos; não sorri | B p.3 | CONFIRMADO |
| Sinais de alarme do desenvolvimento aos 6 meses | rigidez dos membros; não controla a cabeça; não dá risada | B p.3 | CONFIRMADO |
| Sinais de alarme do desenvolvimento aos 9 meses | não senta sem apoio; pernas rígidas ou moles; mãos fechadas/sem preensão em pinça; não localiza som/não vira a cabeça; não balbucia/sorriso social pobre | B p.3 | CONFIRMADO |
| Sinais de alarme do desenvolvimento aos 12 meses | criança parada/inerte, colocada de pé não ajuda com as mãos, não brinca de esconde-achou, não responde ao nome | B p.3 | CONFIRMADO |
| Conduta diante de falha em marco do desenvolvimento | antecipar a consulta seguinte e investigar contexto ambiental/vínculo/estímulos | B p.3 | CONFIRMADO |
| Conduta diante de atraso persistente | persistência do atraso por >2 consultas (ou ausência do marco no último quadro sombreado) → encaminhar a especialista | B p.3 | CONFIRMADO |
| Direção do desenvolvimento motor | craniocaudal | B p.3 | CONFIRMADO |
| Fatores de risco para morbidade no SNC do desenvolvimento | HPIV, LPV, infarto hemorrágico, dilatação pós-hemorrágica, meningite neonatal — principalmente em pré-termo | B p.3 | CONFIRMADO |

## Pegadinhas

- O limiar de normalidade nas curvas OMS de peso/estatura/PC é **-2 a +2** escores Z — não -3/+3. -3/+3 já é a faixa de gravidade (muito baixo peso / magreza acentuada), não o corte de "anormal".
- A curva de IMC **não segue a mesma faixa** de peso/estatura: ela tem degraus extras (risco de sobrepeso entre +1 e +2, sobrepeso entre +2 e +3, obesidade >+3) — aplicar o corte simples -2/+2 ao IMC é regra mal-aprendida.
- Idade corrigida se aplica **até os 2 anos** de vida do pré-termo — usar idade cronológica pura (sem correção) num prematuro de 8 meses avaliado por curva/marco é premissa não checada.
- A ordem de recuperação do catch-up growth é PC → estatura → peso — não o inverso; PC ser o "primeiro a normalizar" é contraintuitivo e por isso testável.
- Sinal de alarme do desenvolvimento é específico da idade (3, 6, 9, 12 meses) — usar um sinal de uma idade para julgar outra faixa etária é troca de comando.
- Falha em um marco não indica automaticamente encaminhamento a especialista — a conduta correta é antecipar a próxima consulta e investigar contexto; só a persistência por mais de 2 consultas justifica encaminhamento.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Lactente com escore Z de peso = -2,5 → "peso normal, dentro da faixa aceitável de -3 a +3" | -3/+3 soa como "faixa ampla e seguro", número redondo fácil de decorar errado | valor errado / regra mal-aprendida | -2,5 já está fora da faixa de normalidade (-2 a +2); classifica-se como baixo peso para a idade |
| Criança com IMC escore Z +2,2 → "classificar como obesidade, pois passou de +2" | reflexo de aplicar o mesmo corte +2 usado para peso/estatura | superextrapolação | para IMC, +2 a +3 é sobrepeso, não obesidade; só acima de +3 é obesidade |
| Prematuro de 32 semanas, hoje com 18 meses de idade cronológica → "comparar diretamente com a curva de 18 meses, já que passou de 1 ano" | crença de que a correção só vale no primeiro ano de vida | premissa não checada | a idade corrigida deve ser aplicada até os 2 anos, não só até 1 ano |
| Lactente de 9 meses que ainda não senta sem apoio, mas sorri e balbucia bem → "sem sinal de alarme, pois a maioria dos marcos está presente" | contar marcos presentes e "empatar" com os ausentes, em vez de aplicar o critério objetivo | neutralizar sinal de alerta com sinal tranquilizador coexistente | não sentar sem apoio aos 9 meses já é, isoladamente, sinal de alarme listado para essa idade — não precisa de outros marcos ausentes para configurar alerta |
| RN pré-termo em acompanhamento seriado → "esperar que o peso normalize primeiro, como sinal de boa recuperação" | peso é o parâmetro mais lembrado/mais fácil de medir em casa | erro de leitura de sequência | a ordem correta de recuperação é PC primeiro, depois estatura, e o peso é o último a normalizar |

## Conduta

- Inicial: em toda consulta de puericultura, plotar peso/estatura/PC (e IMC quando aplicável) na curva OMS correspondente à idade e sexo, calculando o escore Z; em pré-termo, usar idade corrigida até os 2 anos.
- Definitiva: se escore Z fora de -2/+2 (ou fora dos cortes específicos do IMC) ou sinal de alarme do desenvolvimento presente, antecipar a consulta seguinte e investigar contexto (alimentação, doença de base, estímulo/vínculo, ambiente); manter vigilância ativa.
- Condição da conduta: encaminhamento a especialista só se o atraso persistir por mais de 2 consultas consecutivas, ou se o marco continuar ausente no último quadro sombreado da caderneta.
- Diferencial perigoso: escore Z <-3 (muito baixo peso/magreza acentuada) ou >+3 (IMC obesidade) exige investigação mais agressiva de causa orgânica, não só reforço de orientação alimentar.
- O que mudaria a decisão: idade gestacional ao nascer (define se e até quando corrigir a idade); presença de fator de risco neurológico (HPIV, LPV, meningite neonatal) reforça necessidade de seguimento mais próximo do desenvolvimento, mesmo com marcos aparentemente presentes.

## Mini-casos ativos

Lactente de 4 meses de idade cronológica, nascido pré-termo de 32 semanas (faltaram 8 semanas ≈ 2 meses para 40 semanas). Variável decisiva: idade corrigida = 4 − 2 = 2 meses; os marcos e a curva de crescimento devem ser avaliados como se a criança tivesse 2 meses, não 4 — cobrar sinal de alarme de 3 meses nessa criança seria prematuro.

Criança de 8 meses com escore Z de peso -2,4 e escore Z de estatura -1,0, sem sinais de alarme do desenvolvimento. Variável decisiva: peso fora da faixa de normalidade (-2 a +2) já classifica baixo peso para a idade, mesmo com estatura normal — investigar causa nutricional/orgânica, sem esperar "impressão geral" de desnutrição.

Lactente de 9 meses que não senta sem apoio, mas sorri, balbucia e localiza som normalmente. Variável decisiva: o sinal de alarme "não sentar sem apoio aos 9 meses" já configura, isoladamente, indicação de antecipar a consulta seguinte e investigar — não é necessário que outros marcos também estejam ausentes.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Faixa de normalidade do escore Z (peso/estatura/PC) | entre -2 e +2 (não -3/+3) | pegadinha |
| Cortes de IMC por escore Z | magreza acentuada <-3; magreza -3 a -2; adequado -2 a +1; risco sobrepeso +1 a +2; sobrepeso +2 a +3; obesidade >+3 | pegadinha |
| Fórmula de PC estimado | PC = Altura/2 + 10 | dado |
| Fórmula de idade corrigida | idade cronológica (semanas) − semanas que faltavam p/ 40 semanas de IG; usar até 2 anos | dado |
| Ordem do catch-up growth | PC → estatura → peso | pegadinha |
| Ganho de peso 1º ano | 6.750g + peso de nascimento (750/600/500/400 g por mês nos 4 trimestres) | dado |
| Sinal de alarme aos 3 / 6 / 9 / 12 meses | 3m: não sustenta cabeça/não sorri; 6m: rigidez/não dá risada; 9m: não senta sem apoio/sem pinça; 12m: inerte/não brinca esconde-achou | dado |
| Conduta diante de falha em marco | antecipar consulta seguinte; encaminhar a especialista só se persistir >2 consultas | pegadinha |
| Classificação de peso ao nascer | BP 1500–2499g; MBP 1000–1499g; EBP <1000g | dado |

## Revisão

- Revisar quando: antes de qualquer questão com escore Z numérico, gráfico de curva OMS, cálculo de idade corrigida em pré-termo, ou vinheta de lactente com marco do desenvolvimento ausente.
- Critério de parada: classificar corretamente 6 casos variando escore Z (peso, estatura, PC, IMC) entre -3,5 e +3,5, calcular idade corrigida em 3 cenários de IG diferentes, e identificar o sinal de alarme certo para a idade em 4 vinhetas sem trocar a faixa etária.
