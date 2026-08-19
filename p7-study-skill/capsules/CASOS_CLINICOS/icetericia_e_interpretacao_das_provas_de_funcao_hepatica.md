# Icterícia e interpretação das provas de função hepática

## Metadados

- Disciplina: CASOS_CLINICOS
- Especialidade: Gastroenterologia/Hepatologia (caso clínico integrado)
- Unidade: A_DEFINIR
- Prioridade: media
- Risco clínico: medio
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não
- Fontes usadas: CASOS_CL_NICOS_RESUMO__249c11a613 (camada B, NATIVA, seção "Cirrose Hepática" — exames laboratoriais, p.1 do docx); Casos_Cli_nicos_P7_1__4f3f459b20 (camada B, ESCANEADA, p.19 aberta como imagem — mostrou conteúdo de "Variações da PBE/ascite", sem relação direta com interpretação de icterícia; não usada como fonte de dado numérico deste tema)
- Evidência de prova/devolutiva: `cai: false` no cluster e `forca: fraca` — nenhuma devolutiva mapeada cobra este tema isoladamente. A cápsula existe porque interpretação de provas hepáticas é pré-requisito transversal para os casos de cirrose/ascite/PBE já priorizados no acervo, mas deve ser tratada como apoio, não como tema de alta probabilidade de cair sozinho.
- Limitações da fonte: tema sem camada A no acervo (`tem_camada_A: false`) e sem fonte B dedicada a "icterícia" como síndrome — o único material direto disponível é a seção de exames laboratoriais da cápsula de cirrose hepática do resumo de casos clínicos, que cobre o padrão de bilirrubina/transaminases mas não discute a classificação clássica pré-hepática/hepática/pós-hepática nem GGT/fosfatase alcalina. Essa classificação está incluída abaixo rotulada como conhecimento geral (não sourced neste acervo) e deve ser tratada com confiança mais baixa que os dados marcados CONFIRMADO.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES (dados numéricos confirmados; classificação sindrômica geral rotulada à parte)

## Como cai

Não aparece isolado nas devolutivas mapeadas — icterícia entra como achado dentro de vinhetas de cirrose, hepatite ou obstrução biliar, testando se o aluno usa o padrão de bilirrubina (direta x indireta) e a razão AST/ALT para localizar a lesão (pré-hepática, hepatocelular ou colestática/pós-hepática) antes de propor conduta.

## Conceito operacional mínimo

Icterícia é sinal (bilirrubina acumulada na pele/mucosas), e a prova cobra localizar a causa antes de tratar: bilirrubina indireta isolada aponta para produção aumentada ou conjugação deficiente (hemólise, síndrome de Gilbert) sem lesão hepatocelular; bilirrubina direta elevada aponta para colestase (intra ou extra-hepática); elevação de transaminases (AST/ALT) aponta para lesão hepatocelular. A razão AST/ALT ajuda a sugerir etiologia dentro do padrão hepatocelular — não é um exame isolado que "fecha" diagnóstico sozinho, mas orienta a hipótese mais provável.

## Pivô clínico

Separar bilirrubina direta de indireta é o primeiro corte que qualquer vinheta de icterícia exige — indireta isolada não precisa de investigação de vias biliares (não é obstrutiva), enquanto direta elevada obriga a pensar em colestase e eventualmente em exame de imagem para excluir obstrução mecânica. Dentro do padrão hepatocelular, a razão AST/ALT >2 com AST<300 sugere lesão alcoólica, enquanto AST/ALT>1000 (ambas muito elevadas) sugere necrose grave (hepatite viral aguda, toxina, isquemia) — são raciocínios diferentes que a vinheta pode testar separadamente.

## Palavras-âncora

Bilirrubina direta (colestase) x indireta (produção/conjugação: hemólise, Gilbert); razão AST/ALT >2 com AST<300 (lesão alcoólica); AST/ALT >1000 (necrose hepática grave: viral, tóxica, isquêmica); albumina (meia-vida 28 dias, marcador de função crônica); tempo de protrombina prolongado (função de síntese aguda); icterícia pré-hepática x hepática x pós-hepática (classificação clássica, ver limitação de fonte).

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| interpretar imagem/laboratório | padrão de bilirrubina: direta (colestase) x indireta isolada (hemólise/Gilbert, sem lesão hepatocelular) | fato | factual | lacuna — não diferenciar bilirrubina direta de indireta e investigar vias biliares num paciente com hiperbilirrubinemia indireta isolada | card fixo "indireta isolada = não pensar em obstrução; direta elevada = pensar em colestase" |
| interpretar imagem/laboratório | razão AST/ALT >2 (AST<300) sugere etiologia alcoólica; AST/ALT muito elevadas (>1000) sugerem necrose grave | valor | factual | regra mal-aprendida — tratar qualquer elevação de transaminases como "hepatite" genérica sem aplicar a razão para direcionar etiologia | treino de casos comparando razões diferentes com o mesmo nível absoluto de transaminase |
| aplicar critério | albumina <3mg/dL sustentada sugere hepatopatia crônica; TP prolongado >3 segundos sugere disfunção de síntese | limiar | factual | não diferenciar marcador de função crônica (albumina) de marcador agudo (TP) | par fixo albumina=crônico / TP=agudo, testado com casos que variam tempo de evolução |
| reconhecer diagnóstico | elevação isolada de bilirrubina indireta com demais provas normais sugere síndrome de Gilbert ou hemólise, não hepatopatia estrutural | fato | factual | sobre-elaboração — investigar hepatopatia extensa (biópsia, imagem) num quadro que é elevação isolada e benigna de bilirrubina indireta | checklist "bilirrubina indireta isolada + demais exames normais = pensar primeiro em Gilbert/hemólise antes de investigação extensa" |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Aminotransferases | elevação indica lesão hepatocelular | CASOS_CL_NICOS_RESUMO p.1 (seção Cirrose) | CONFIRMADO |
| Razão AST/ALT sugestiva de lesão alcoólica | AST/ALT >2 e AST <300 UI/L | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Transaminases em necrose severa | AST e ALT >1000 (hepatites virais, toxinas, isquemia) | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Bilirrubina direta elevada | sugere colestase | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Bilirrubina indireta isolada | sugere síndrome de Gilbert ou hemólise | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Albumina | meia-vida de 28 dias; redução sustentada <3 mg/dL sugere hepatopatia | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Tempo de protrombina | prolongamento >3 segundos sugere hepatopatia | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Exames de imagem de 1ª linha | USG (rápida, não invasiva, sem contraste, avalia parênquima e rastreia neoplasia); TC; RM; CPRE conforme indicação | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO |
| Classificação clássica de icterícia (pré-hepática/hepática/pós-hepática) | pré-hepática: hemólise/produção aumentada, predomina indireta; hepática: lesão hepatocelular, mista; pós-hepática/obstrutiva: colestase mecânica, predomina direta | não localizado no acervo mapeado para este tema | conhecimento geral — confirmar no slide se camada A for localizada futuramente |

## Pegadinhas

- Elevação isolada de transaminases sem colestase não significa obstrução biliar — o padrão bilirrubina direta é que aponta para colestase, não a elevação de AST/ALT isolada.
- AST elevada não é específica de fígado — pode vir de músculo cardíaco/esquelético; ALT é mais específica de lesão hepatocelular. Vinheta que usa só "transaminases elevadas" sem discriminar qual está mais alta pode estar testando essa diferença.
- Albumina baixa em quadro agudo (poucos dias) não indica necessariamente hepatopatia crônica — pela meia-vida longa (28 dias), queda rápida de albumina pode refletir outras causas (perda proteica, desnutrição aguda, inflamação sistêmica), não só disfunção hepática crônica.
- Icterícia com bilirrubina indireta isolada e demais provas normais não deve ser tratada como emergência hepática — geralmente é achado benigno (Gilbert) e não exige investigação invasiva.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Paciente ictérico com bilirrubina indireta isolada elevada: solicitar USG de vias biliares para investigar obstrução | icterícia "sempre" remete a obstrução biliar na memória do aluno | analogia sem validação funcional | bilirrubina indireta isolada não é padrão obstrutivo — o exame de imagem de vias biliares tem baixo rendimento nesse cenário; a investigação deveria ser de hemólise/Gilbert |
| AST e ALT elevadas: fechar hepatite viral aguda sem calcular a razão AST/ALT | "transaminases altas = hepatite" é associação automática | fechamento precoce | AST/ALT >2 com AST<300 sugere etiologia alcoólica, não viral — a razão muda a hipótese etiológica mais provável |
| Albumina baixa em paciente internado há 3 dias: fechar cirrose hepática de base | albumina baixa "parece" sempre hepatopatia crônica | premissa não checada | pela meia-vida de 28 dias, queda de albumina em poucos dias não reflete necessariamente hepatopatia crônica — outras causas agudas devem ser consideradas |

## Conduta

- Inicial: diante de icterícia, separar bilirrubina direta de indireta e solicitar transaminases, albumina e tempo de protrombina para localizar o padrão (colestático x hepatocelular x pré-hepático).
- Definitiva: depende inteiramente da causa identificada pelo padrão laboratorial — não há conduta única para "icterícia"; o próximo passo (imagem de vias biliares, sorologia viral, investigação hemolítica) é ditado pelo padrão de bilirrubina e transaminases.
- Condição da conduta: bilirrubina direta elevada + achado de dilatação de vias biliares na USG direciona para investigação/tratamento de causa obstrutiva (CPRE); bilirrubina indireta isolada com demais provas normais não exige a mesma investigação.
- Diferencial perigoso: icterícia colestática associada a febre e dor em hipocôndrio direito (tríade de Charcot) sugere colangite aguda, quadro de emergência que não pode ser tratado como hepatopatia crônica estável.
- O que mudaria a decisão: presença de dilatação de vias biliares na USG muda a investigação de "hepatopatia difusa" para "causa obstrutiva mecânica", exigindo exame de imagem mais dirigido (colangio-RM/CPRE) em vez de só seguimento clínico.

## Mini-casos ativos

Paciente com icterícia leve, bilirrubina total elevada às custas de indireta, transaminases e demais provas normais, sem outros sintomas → variável decisiva: padrão de indireta isolada com exames normais aponta para síndrome de Gilbert (achado benigno) — não indicar investigação invasiva de imediato.

Paciente etilista, icterícia, AST 250, ALT 90 (razão AST/ALT >2), albumina 2,8 mg/dL há semanas de evolução, TP prolongado → variável decisiva: razão AST/ALT>2 com AST<300 sugere lesão alcoólica; albumina baixa sustentada + TP prolongado reforçam hepatopatia crônica descompensada, não lesão aguda isolada.

Paciente com icterícia, febre e dor em hipocôndrio direito, bilirrubina direta elevada, USG com dilatação de vias biliares → variável decisiva: tríade sugestiva de colangite aguda — conduta muda de investigação ambulatorial para estabilização e desobstrução urgente (CPRE), não seguimento eletivo.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Bilirrubina direta elevada sugere | Colestase | dado |
| Bilirrubina indireta isolada sugere | Hemólise ou síndrome de Gilbert | dado |
| Razão AST/ALT >2 com AST<300 | Sugere etiologia alcoólica | dado |
| AST e ALT >1000 | Sugere necrose hepática grave (viral, tóxica, isquêmica) | dado |
| Marcador de função hepática crônica (meia-vida longa) | Albumina (28 dias) | dado |
| Marcador de disfunção hepática aguda | Tempo de protrombina prolongado | dado |
| Icterícia indireta isolada + exames normais → investigação invasiva? | Não, geralmente achado benigno (Gilbert) | pegadinha |

## Revisão

- Revisar quando: antes de qualquer caso de cirrose, ascite/PBE ou hepatite — icterícia e o painel hepático são pré-requisito para interpretar esses casos maiores, então revisar este tema junto com eles.
- Critério de parada: em 3 casos seguidos, separar corretamente o padrão de bilirrubina (direta x indireta), aplicar a razão AST/ALT para sugerir etiologia, e não confundir marcador agudo (TP) com marcador crônico (albumina).
