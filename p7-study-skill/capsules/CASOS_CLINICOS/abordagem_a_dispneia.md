# Abordagem à dispneia — causas, sinais de alerta e investigação

## Metadados

- Disciplina: CASOS_CLINICOS
- Especialidade: Clínica Médica (sintoma-guarda-chuva cardiorrespiratório)
- Unidade: A_DEFINIR
- Prioridade: media
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não
- Fontes usadas: CASOS_CL_NICOS_RESUMO__249c11a613 (camada B, NATIVA, seção "DISPNEIA", p.1 do docx); Casos_Cli_nicos_P7_1__4f3f459b20 (camada B, ESCANEADA, p.19 aberta como imagem — mostrou conteúdo de "Variações da PBE/ascite", sem relação com dispneia; citação do cluster não corresponde ao tema, descartada)
- Evidência de prova/devolutiva: `cai: false` no cluster — sem evidência direta de cobrança isolada nas devolutivas mapeadas. Tema entra como sintoma transversal que atravessa casos cardíacos, pulmonares, anêmicos e tromboembólicos da prova de Casos Clínicos, e por isso mantém prioridade média mesmo sem devolutiva própria.
- Limitações da fonte: tema sem camada A no acervo (`tem_camada_A: false`). A única fonte com conteúdo real é um resumo compilado estilo livro-texto/UpToDate, sem indicação de autoria docente — não é possível afirmar "o professor ensinou X" a partir dela. A segunda fonte que o cluster apontou (Casos_Clínicos_P7_1, p.19) não tinha relação com o tema quando aberta como imagem; não foi usada, e isso é registrado aqui em vez de forçar uma citação falsa.
- Verificação nível 1: CONFIRMADO

## Como cai

Não aparece como questão isolada nas devolutivas mapeadas — dispneia entra embutida em vinhetas de ICC, TEP, DPOC/asma, pneumonia, anemia grave e derrame pleural, exigindo que o aluno reconheça o mecanismo (obstrutivo x restritivo x cardíaco x vascular x metabólico) a partir da ausculta e da história, e priorize a causa que ameaça a vida antes de fechar a mais "familiar".

## Conceito operacional mínimo

Dispneia é sintoma, não diagnóstico — o primeiro corte é temporal (aguda: minutos a poucos dias; crônica: semanas a meses) e o segundo é mecanístico (obstrução de via aérea alta/baixa, doença do parênquima pulmonar, falência de bomba cardíaca, doença vascular pulmonar, causa extrapulmonar como anemia ou acidose metabólica). A gravidade não se mede pela etiologia, mas pelo trabalho respiratório e pelo nível de consciência — um paciente "calmo" com dispneia intensa e confusão mental está mais grave do que um ansioso taquipneico e lúcido.

## Pivô clínico

O achado da ausculta muda o diagnóstico mais provável, mas nenhum achado isolado fecha o caso: sibilos sugerem asma/DPOC, mas insuficiência cardíaca também pode sibilar ("asma cardíaca") em paciente idoso com cardiopatia prévia; crepitação sugere IC esquerda ou doença intersticial, mas também aparece em pneumonia — o discriminador é o contexto (febre + tosse produtiva = infeccioso; ortopneia + DPN + edema = cardíaco). Sinais de alerta (dispneia em repouso, confusão/agitação, uso de musculatura acessória, dor torácica) mudam a conduta de "investigar ambulatorialmente" para "estabilizar agora".

## Palavras-âncora

Ortopneia; dispneia paroxística noturna; sibilos (asma/DPOC) x estridor (obstrução extratorácica de via aérea) x crepitação (IC esquerda/doença intersticial/pneumonia); turgência jugular e edema pré-sacral (IC); dispneia súbita + dor pleurítica + fator de risco para TVP (TEP); oximetria, RX de tórax, ECG, gasometria arterial, angioTC.

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| diferenciar próximos | mecanismo obstrutivo x restritivo x cardíaco x vascular a partir do padrão temporal + ausculta + sintomas associados | sequência | operacional | analogia sem validação — fechar em asma pela sibilância sem checar história cardíaca (idoso, cardiopatia prévia = "asma cardíaca") | pares de comparação lado a lado: sibilos de causa pulmonar x sibilos de causa cardíaca, com a mesma vinheta variando só a história prévia |
| priorizar emergência | sinais de alerta: dispneia em repouso, confusão/agitação, uso de musculatura acessória, dor torácica, sudorese noturna, perda ponderal | sinal-achado | operacional | narrativa acima do discriminador — investigar a causa "mais provável" antes de reconhecer que o paciente já está em sinal de alarme e precisa de estabilização imediata | checklist fixo de sinais de alerta a aplicar antes de qualquer hipótese diagnóstica em vinheta de dispneia |
| interpretar achado de exame físico | crepitação pode ser IC esquerda, doença intersticial ou pneumonia — o discriminador é febre/tosse produtiva (infeccioso) x ortopneia/DPN/edema (cardíaco) | fato | factual | fechamento precoce no primeiro diagnóstico associado ao achado semiológico, sem checar o contexto que discrimina | treino de casos que trocam só o contexto (febre x edema de MMII) mantendo o mesmo achado de ausculta |
| exame inicial | escolha entre oximetria/RX/ECG/gasometria conforme a hipótese perseguida — ECG não pode ser pulado em paciente com fator de risco cardiovascular mesmo se a hipótese inicial for pulmonar | sequência | operacional | lacuna — pedir só RX de tórax e não pedir ECG em paciente com fator de risco cardiovascular, perdendo isquemia silenciosa como causa | checklist "todo paciente com dispneia e fator de risco CV recebe ECG", independente da hipótese inicial |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Causas de dispneia aguda | asma brônquica; inalação de corpo estranho; pneumotórax; embolia pulmonar; isquemia/IAM; ICC descompensada; TAG (crise de ansiedade); paralisia diafragmática | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Causas de dispneia crônica | doença pulmonar intersticial; doença pulmonar obstrutiva; derrame pleural; doença pulmonar restritiva; ICC; hipertensão pulmonar; angina; anemia; descondicionamento físico | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Sinais de alerta ("sinais de alarme") | dispneia em repouso durante o exame; diminuição do nível de consciência ou agitação/confusão mental; uso de musculatura acessória e excursão do ar reduzida; dor torácica; crepitações; perda ponderal; sudorese noturna; palpitações | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Interpretação de achados de ausculta | sibilos: asma/DPOC; estridor: obstrução extratorácica de vias respiratórias; crepitação: IC esquerda, doença pulmonar intersticial, ou pneumonia (se acompanhada de sinais de consolidação) | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Achados de exame físico direcionadores | turgência jugular e edema pré-sacral/de MMII sugerem IC; bulhas extras/abafadas/sopros; palidez conjuntival (anemia); linfadenopatia cervical/supraclavicular/inguinal | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Fatores de risco a investigar na HDA | imobilização/cirurgia recente, viagem longa, câncer, história pessoal/familiar de coagulopatia, gestação, ACO, dor em panturrilha, edema de MMII e TVP conhecida — todos apontando para TEP | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Exames de primeira linha | oximetria de pulso; RX de tórax; ECG; gasometria arterial; angioTC (se suspeita de TEP) | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |

## Pegadinhas

- Sibilância não é sinônimo de asma — em paciente idoso com cardiopatia conhecida, sibilos podem representar "asma cardíaca" (congestão pulmonar), e tratar como crise asmática sem investigar IC atrasa a conduta correta.
- Crepitação isolada não fecha pneumonia — sem febre e tosse produtiva, o achado é mais compatível com IC esquerda ou doença intersticial; o contexto clínico é o discriminador, não o achado semiológico isolado.
- Estridor (obstrução alta) é diferente de sibilo (obstrução baixa) — confundir os dois muda completamente a conduta (corpo estranho/obstrução de via aérea superior é emergência de via aérea, não broncodilatador).
- Dispneia "leve" em paciente ansioso pode mascarar TAG verdadeiro, mas não se deve fechar ansiedade sem antes descartar causas orgânicas graves (TEP, IAM) quando há fator de risco presente na história.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Paciente idoso, dispneico, com sibilos difusos: tratar como crise de asma com broncodilatador | sibilos são o achado clássico de asma na maioria dos casos de prova | analogia sem validação funcional | sem checar história cardíaca (cardiopatia prévia, edema, ortopneia) o quadro pode ser IC descompensada ("asma cardíaca") — broncodilatador isolado não trata a causa |
| Paciente com dispneia e crepitação bibasal: fechar pneumonia e pedir só RX de tórax | crepitação + achado radiológico parecem suficientes para infecção | fechamento precoce sem checar sinais de alarme cardíacos | sem febre/tosse produtiva e com edema de MMII/ortopneia, a hipótese mais provável é IC esquerda, não pneumonia — ECG e BNP mudariam a conduta |
| Paciente jovem, ansioso, com dispneia leve recorrente: fechar transtorno de ansiedade generalizada (TAG) sem investigar mais | ansiedade é diagnóstico de exclusão "fácil" e comum nessa faixa etária | fechamento precoce / premissa não checada | se há fator de risco para TEP (uso de ACO, imobilização, viagem longa) presente na história, ansiedade não pode ser fechada antes de excluir causa orgânica grave |

## Conduta

- Inicial: avaliar gravidade (nível de consciência, trabalho respiratório, oximetria), oxigenoterapia se necessário, e direcionar a investigação (RX de tórax, ECG, gasometria) pela hipótese sindrômica levantada na história e no exame físico.
- Definitiva: tratar a causa de base identificada — broncodilatador/corticoide em obstrutivo, diurético/vasodilatador em IC descompensada, anticoagulação/trombólise em TEP conforme gravidade, antibioticoterapia em pneumonia, transfusão/investigação etiológica em anemia sintomática.
- Condição da conduta: todo paciente com dispneia e fator de risco cardiovascular relevante deve receber ECG, independentemente de qual hipótese estiver sendo perseguida primeiro.
- Diferencial perigoso: TEP, pneumotórax hipertensivo, edema agudo de pulmão e obstrução de via aérea superior — todos podem se apresentar como "só dispneia" sem sinais floridos no início.
- O que mudaria a decisão: presença de dor pleurítica + fator de risco para TVP eleva a suspeita de TEP e muda o exame de escolha para angioTC; sinais de choque com desvio de traqueia (pneumotórax hipertensivo) exige descompressão imediata, sem esperar RX.

## Mini-casos ativos

Paciente de 68 anos, cardiopata, dispneico há 3 dias, com sibilos difusos à ausculta, edema de MMII e ortopneia → variável decisiva: sibilos em paciente com história cardíaca positiva e sinais congestivos apontam para IC descompensada ("asma cardíaca"), não asma — pedir ECG/BNP/RX antes de broncodilatador isolado.

Paciente de 30 anos, em uso de anticoncepcional oral, dispneia súbita há 2 horas associada a dor pleurítica e taquicardia, sem história pulmonar prévia → variável decisiva: fator de risco para TVP + dispneia súbita + dor pleurítica é a tríade que aciona suspeita de TEP — próximo passo é angioTC, não RX de tórax isolado.

Paciente jovem, sem comorbidades, com dispneia leve recorrente associada a ansiedade situacional, sem fatores de risco para TEP ou doença cardiopulmonar na história → variável decisiva: ausência de sinais de alarme e de fatores de risco orgânicos permite investigar TAG como hipótese, mas só depois de descartar ativamente causa orgânica pela história.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Crepitação bibasal + febre + tosse produtiva | Sugere pneumonia (infeccioso) | dado |
| Crepitação bibasal + ortopneia + edema de MMII | Sugere IC esquerda descompensada | pegadinha |
| Sibilos em idoso cardiopata | Pensar em "asma cardíaca" antes de asma primária | pegadinha |
| Estridor x sibilo | Estridor = obstrução alta; sibilo = obstrução baixa | dado |
| Tríade de suspeita de TEP | Dispneia súbita + dor pleurítica + fator de risco para TVP | dado |
| Exame que não pode faltar em dispneia + fator de risco CV | ECG, independentemente da hipótese inicial | sequência |

## Revisão

- Revisar quando: antes de qualquer caso clínico que abra com "dispneia" como queixa principal, especialmente se a vinheta tiver história cardíaca, uso de ACO/imobilização, ou febre — são as três bifurcações que decidem o caminho diagnóstico.
- Critério de parada: em 3 vinhetas seguidas, identificar corretamente o mecanismo (obstrutivo/restritivo/cardíaco/vascular) e citar o exame inicial correto sem pular o ECG em paciente de risco cardiovascular.
