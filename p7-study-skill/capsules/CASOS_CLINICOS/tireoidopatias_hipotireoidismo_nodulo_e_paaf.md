# Tireoidopatias em caso clínico — hipotireoidismo, nódulo tireoidiano e conduta de PAAF

## Metadados

- Disciplina: CASOS_CLINICOS
- Especialidade: Endocrinologia (caso clínico integrado)
- Unidade: A_DEFINIR
- Prioridade: media
- Risco clínico: medio
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não
- Fontes usadas: 2_Avaliac_a_o_Casos_Cli_nicos_TURMA_B_2021_1__7bf703af15 (camada C — questões reais de prova, Questões 1 e 3, usadas como evidência de cobrança); FACILITA_OSCE_1___6c6a714b3e (camada B, apostila de aula, seção "Doenças da tireoide", texto nativo); OSCE_ENDOCRINOLOGIA__4796d07aed (camada B, roteiro OSCE de endocrinologia, texto nativo); ANOTAC_O_ES_ca_ncer_e_no_dulo_da_tireoide__e5088007bc (camada B, anotação de aluno sobre nódulo/câncer de tireoide — corpus geral do acervo, não listada no cluster original mas aberta para checar precisão dos cortes de PAAF/Chammas/Bethesda citados na Questão 3; tratada como camada B, não como fala do professor)
- Evidência de prova/devolutiva: `cai: true` no cluster. Questão 1 (mulher, 52a, edema+constipação+queda de cabelo+bradicardia, tireoide heterogênea sem nódulo) testa reconhecer hipotireoidismo e o exame confirmatório certo. Questão 3 (Maria Alice, 32a, 2 nódulos — 0,8cm com microcalcificações e 0,5cm sem calcificação, TSH 6,5, Chammas II) testa a conduta de PAAF por corte de tamanho + característica de risco. Gabarito comentado não disponível nesta fonte (página de tentativa de quiz sem correção anexada) — a cápsula ensina o raciocínio correto a partir dos critérios da camada B, não afirma a resposta oficial do Moodle.
- Limitações da fonte: tema sem camada A no acervo (`tem_camada_A: false`). Para os cortes numéricos completos de TIRADS/Chammas/Bethesda (não usados diretamente nas duas questões-caso, mas relevantes para a lógica de PAAF), ver a cápsula `EISA_II/nodulos_tireoidianos_e_cancer_de_tireoide.md`, que tem camada A confirmada e tabela de precisão mais extensa — esta cápsula foca no raciocínio de caso clínico (extrair achado → decidir conduta), não duplica aquela tabela.
- Verificação nível 1: CONFIRMADO

## Como cai

Vinheta com quadro clínico clássico de disfunção tireoidiana (hipo ou hiper) pedindo diagnóstico + os exames certos para confirmar — testando se o aluno pede o painel completo (TSH + hormônio livre ± anticorpo ± USG) ou erra pedindo exame de menos/de mais. Vinheta com achado de USG de tireoide (tamanho do nódulo, calcificação, padrão de vascularização) e TSH levemente alterado pedindo a conduta certa: puncionar, repetir exame em X meses, ou tratar direto — testando se o aluno aplica o corte de PAAF por característica de risco em vez de decidir só pelo "tamanho parece pequeno".

## Conceito operacional mínimo

Toda vinheta de tireoide segue o mesmo esqueleto: (1) o quadro clínico aponta hipo ou hiperfunção, (2) o TSH confirma a direção (alto = hipo, baixo = hiper, salvo causa central) e o hormônio livre confirma se é clínico ou subclínico, (3) se há nódulo, a decisão de puncionar (PAAF) não depende só do tamanho absoluto — depende de características de risco (microcalcificação, vascularização central, crescimento) que podem antecipar a indicação mesmo em nódulo menor que 1cm. Errar essa hierarquia (tratar hormônio antes de decidir sobre o nódulo, ou vice-versa) é o erro mais comum do tema.

## Pivô clínico

Em nódulo tireoidiano, o "tamanho ≥1cm" não é o único gatilho de PAAF — a presença de microcalcificação ou vascularização predominantemente central (Chammas IV/V) antecipa a indicação mesmo abaixo de 1cm. É exatamente essa nuance que separa o nódulo de 0,8cm com microcalcificação (indicação de PAAF) do nódulo de 0,5cm sem calcificação e vascularização só periférica (Chammas II, sem indicação) na Questão 3 da prova real mapeada — dois nódulos no mesmo paciente, condutas diferentes.

## Palavras-âncora

TSH alto + T4L baixo = hipotireoidismo primário; TSH baixo + T4L/T3 altos = hipertireoidismo; hipotireoidismo subclínico (TSH alto, T4L normal — repetir em 3 meses antes de tratar, salvo gestante/sintomático/anti-TPO+); PAAF indicada se ≥1cm OU microcalcificação OU vascularização central (Chammas IV/V) OU crescimento ≥50% do volume em 1 ano; Chammas I-V (padrão de vascularização); Bethesda I-VI (resultado citológico).

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| melhor exame | painel completo para hipotireoidismo com achado sugestivo de causa autoimune: TSH + T3 total + T4 livre + anti-TPO + USG com doppler, não só TSH+T3+T4 | fato | factual | lacuna — pedir só o painel hormonal básico e esquecer anti-TPO quando a vinheta já sugere etiologia autoimune (bócio heterogêneo, mulher, sintomas clássicos) | checklist "hipofunção com pista de autoimunidade → sempre incluir anti-TPO" |
| aplicar critério | indicação de PAAF por característica de risco (microcalcificação, Chammas IV/V, crescimento), não só por corte absoluto de tamanho | limiar | operacional | valor errado — decidir só pelo tamanho ("0,8cm é pequeno, não precisa puncionar") ignorando a microcalcificação que antecipa a indicação | treino de pares de nódulos no mesmo caso (um com risco, outro sem) forçando decisão diferenciada para cada um |
| conduta inicial x definitiva | TSH levemente elevado (6,5) com nódulo de risco: puncionar o nódulo suspeito E repetir função tireoidiana em 3 meses — não tratar hipotireoidismo subclínico de imediato nem ignorar o nódulo | sequência | operacional | definitiva antes da inicial — iniciar levotiroxina de imediato num TSH levemente elevado sem antes reavaliar em 3 meses (salvo critério de tratamento imediato) | card fixo "TSH 4–10 sem critério de tratamento imediato → repetir em 3 meses antes de tratar" |
| reconhecer contraindicação | tratar hipertireoidismo com PTU fora das indicações específicas (1º trimestre de gestação, crise tireotóxica) em vez de metimazol (1ª linha) | contraindicação | factual | regra mal-aprendida — usar PTU como 1ª linha padrão em vez de metimazol | par fixo "metimazol = 1ª linha geral; PTU = só gestante 1º tri ou crise tireotóxica" |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Diagnóstico laboratorial do hipotireoidismo | T3 e T4 baixos, TSH alto (mecanismo de retroalimentação do eixo hipotálamo-hipófise) | FACILITA_OSCE p.749-751 | CONFIRMADO |
| Hipotireoidismo subclínico | TSH alto com T3/T4 normais; conduta padrão é repetir TSH em 3 meses antes de tratar, exceto se gestante, sintomático, ou outras condições que autorizam tratar de imediato | FACILITA_OSCE p.752-757 | CONFIRMADO |
| Tratamento do hipotireoidismo | Levotiroxina (T4 sintético), tomada pela manhã em jejum, 30 min antes do café | FACILITA_OSCE p.762-766 | CONFIRMADO |
| Hipotireoidismo na gestante | TSH >4 já indica tratar; TSH 2,5–4 → solicitar anti-TPO: se positivo, trata; se negativo, só acompanha | FACILITA_OSCE p.766-769 | CONFIRMADO |
| Tratamento do hipertireoidismo | Metimazol (MMI) é 1ª escolha; PTU reservado para 1º trimestre de gestação (menor teratogenicidade) e crise tireotóxica (bloqueia conversão periférica T4→T3); betabloqueador (propranolol) para sintomas adrenérgicos | FACILITA_OSCE p.770-776 | CONFIRMADO |
| Caso real — hipotireoidismo (Questão 1) | Mulher 52a, edema de MMII, dificuldade para perder peso, constipação, insônia, queda de cabelo, pele ressecada/unhas quebradiças, obesidade central (IMC 33), PA 130x90, FC 52bpm, tireoide heterogênea sem nódulo — alternativas de diagnóstico incluem hipotireoidismo x tireoidite de Hashimoto x hipertireoidismo, com diferentes painéis de exame | 2_Avaliação p.1 (Questão 1) | CONFIRMADO (achados clínicos batem com hipofunção: bradicardia, constipação, pele seca, queda de cabelo — não com hiperfunção) |
| Caso real — nódulos tireoidianos (Questão 3) | Maria Alice, 32a, 2 nódulos: 0,8cm com microcalcificações (Chammas II) e 0,5cm sem calcificação (Chammas II); TSH 6,5, T4L 0,92, T3 total 105, anti-TPO 22 | 2_Avaliação p.2-3 (Questão 3) | CONFIRMADO |
| Indicação de PAAF (nódulo sólido/misto) | ≥1cm OU microcalcificação OU vascularização mais central que periférica (Chammas IV/V) OU crescimento ≥50% do volume ou ≥20% em ≥2 dimensões em 1 ano; também indicado se TIRADS 3/4/5 | ANOTAÇÕES nódulo/câncer de tireoide, linhas 54-61 | confirmar no slide (fonte é anotação de aluno, camada B; cruzar com camada A da cápsula EISA_II antes de citar como número fechado em prova) |
| Seguimento por Bethesda | Bethesda I: repetir PAAF em ~4 meses · II: USG anual + TSH/T4L 6/6 meses · III/IV: teste genético, lobectomia ou acompanhar · V/VI: tireoidectomia total | ANOTAÇÕES nódulo/câncer de tireoide, linhas 113-124 | confirmar no slide (mesma ressalva acima) |

## Pegadinhas

- Nódulo pequeno (<1cm) não é automaticamente "sem indicação de PAAF" — microcalcificação ou vascularização central antecipam a indicação independentemente do corte de 1cm, como no nódulo de 0,8cm da Questão 3.
- TSH levemente elevado (ex.: 6,5) não autoriza tratar hipotireoidismo de imediato — é a faixa de subclínico que pede repetição em 3 meses, salvo critério específico de tratamento imediato (gestante, sintomático, TSH≥10).
- PTU não é 1ª linha geral do hipertireoidismo — é reservado para 1º trimestre de gestação e crise tireotóxica; usar PTU como resposta padrão fora desses contextos é erro de regra mal-aprendida.
- Tireoide heterogênea à palpação, sem nódulo evidente, não afasta doença autoimune (Hashimoto/Graves) — a textura heterogênea por si só já é achado sugestivo e deve levar a pedir anti-TPO/anti-TG, não só TSH/T3/T4.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Nódulo de 0,8cm com microcalcificações: não puncionar por ser menor que 1cm | o corte "clássico" de 1cm é o mais lembrado | valor errado / regra mal-aprendida | microcalcificação é característica de risco que antecipa a indicação de PAAF mesmo abaixo de 1cm — o nódulo de 0,5cm sem calcificação é que não tem indicação |
| Puncionar os dois nódulos de uma vez (0,8cm e 0,5cm) | parece mais "completo" investigar tudo | sobre-elaboração | o nódulo de 0,5cm sem calcificação e com vascularização só periférica (Chammas II) não preenche critério de PAAF — puncionar sem indicação é conduta desnecessária |
| TSH 6,5 com sintomas leves: iniciar levotiroxina imediatamente | tratar logo parece mais resolutivo | definitiva antes da inicial | hipotireoidismo subclínico sem critério de tratamento imediato deve ter o TSH repetido em 3 meses antes de iniciar reposição hormonal |
| Hipertireoidismo em paciente não gestante: iniciar com PTU por ser "o antitireoidiano clássico" | PTU é o nome mais associado popularmente a "remédio para tireoide" | regra mal-aprendida | metimazol é a 1ª linha fora da gestação (1º trimestre) e da crise tireotóxica — PTU tem maior risco de hepatotoxicidade e é reservado a contextos específicos |

## Conduta

- Inicial: em disfunção tireoidiana suspeita, solicitar TSH + hormônio livre (T4L) ± anticorpo (anti-TPO) conforme suspeita etiológica; em nódulo palpável ou achado incidental, USG com doppler para caracterizar (tamanho, calcificação, vascularização) + função tireoidiana.
- Definitiva: hipotireoidismo clínico → levotiroxina; hipertireoidismo → metimazol (ou PTU se gestante 1º trimestre/crise tireotóxica) ± betabloqueador sintomático; nódulo com critério de risco → PAAF, seguida de conduta por Bethesda.
- Condição da conduta: hipotireoidismo subclínico só trata de imediato se gestante, sintomático, TSH≥10, ou doença cardiovascular associada — caso contrário, repetir TSH em 3 meses.
- Diferencial perigoso: nódulo com característica de risco (microcalcificação, vascularização central, crescimento rápido) não pode ser "observado" só porque é menor que 1cm — atraso na PAAF atrasa diagnóstico de malignidade.
- O que mudaria a decisão: gestação muda a escolha do antitireoidiano (PTU no 1º trimestre) e antecipa o limiar de tratamento do hipotireoidismo (TSH>4 já trata); anti-TPO positivo muda a conduta em TSH limítrofe de gestante (2,5–4) de "observar" para "tratar".

## Mini-casos ativos

Mulher, 52 anos, edema de MMII, dificuldade para emagrecer, constipação, insônia, queda de cabelo, pele ressecada, unhas quebradiças, obesidade central, PA 130x90, FC 52bpm, tireoide heterogênea sem nódulo palpável → variável decisiva: conjunto de achados aponta hipofunção (bradicardia, constipação, pele seca), não hiperfunção — o painel de exames deve incluir anti-TPO e USG com doppler pela textura heterogênea, testando etiologia autoimune (Hashimoto).

Mulher, 32 anos, aumento de volume cervical há 20 dias, USG com 2 nódulos sólidos (0,8cm com microcalcificações e 0,5cm sem calcificação, ambos Chammas II), TSH 6,5, T4L normal, anti-TPO negativo → variável decisiva: só o nódulo de 0,8cm tem característica de risco (microcalcificação) que indica PAAF; o TSH levemente elevado sem outros critérios pede repetição em 3 meses, não tratamento imediato.

Gestante, 1º trimestre, hipertireoidismo confirmado (TSH suprimido, T4L alto) → variável decisiva: PTU é a escolha nesse contexto específico (menor risco teratogênico), não metimazol, que é 1ª linha fora da gestação inicial.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| TSH alto + T4L baixo | Hipotireoidismo primário | dado |
| TSH baixo + T4L/T3 altos | Hipertireoidismo | dado |
| Hipotireoidismo subclínico sem critério de tratamento imediato | Repetir TSH em 3 meses antes de tratar | sequência |
| Antitireoidiano de 1ª linha (fora de gestação inicial/crise) | Metimazol | dado |
| PTU é indicado quando? | 1º trimestre de gestação ou crise tireotóxica | pegadinha |
| Nódulo <1cm indica PAAF quando... | Há microcalcificação, vascularização central (Chammas IV/V) ou crescimento rápido | pegadinha |
| Gestante com TSH 2,5–4: próximo passo | Solicitar anti-TPO antes de decidir tratar | sequência |

## Revisão

- Revisar quando: antes de qualquer vinheta que combine sintomas de disfunção tireoidiana com achado de nódulo — o aluno precisa separar as duas decisões (tratar a função x puncionar o nódulo) em vez de misturá-las em uma resposta só.
- Critério de parada: em 3 casos seguidos, identificar corretamente a direção da disfunção (hipo/hiper), decidir tratar ou repetir exame, e aplicar o critério de risco correto para indicar ou não PAAF.
