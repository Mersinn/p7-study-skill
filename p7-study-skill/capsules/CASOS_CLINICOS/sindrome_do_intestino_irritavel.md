# Síndrome do intestino irritável

## Metadados

- Disciplina: CASOS_CLINICOS
- Especialidade: Gastroenterologia (caso clínico integrado)
- Unidade: A_DEFINIR
- Prioridade: baixa
- Risco clínico: baixo
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não (fonte MISTA aberta como imagem mostrou apenas slide de encerramento sem conteúdo; texto nativo do mesmo arquivo continha o conteúdo completo e foi usado)
- Fontes usadas: CASOS_CL_NICOS_RESUMO__249c11a613 (camada B, NATIVA, seção "Diarreia Crônica" — cita SII como causa não-infecciosa mais frequente, p.1 do docx); Abordagem_a_s_diarreias__41fb86fd8c (camada B, MISTA — slide de aula com extração de texto nativa completa e legível, seção "SII", usado por texto; p.34 aberta como imagem confirmou ser apenas slide "Obrigada" de encerramento, sem conteúdo, não usada)
- Evidência de prova/devolutiva: `cai: false` no cluster e `forca: fraca` — sem devolutiva mapeada cobrando o tema isoladamente; prioridade baixa mantida, capsula existe para fechar o diferencial de diarreia crônica funcional x orgânica (DII, celíaca) já priorizados no acervo.
- Limitações da fonte: tema sem camada A no acervo (`tem_camada_A: false`). O conteúdo direto sobre SII nas fontes B é enxuto (poucas linhas de slide em tópicos), sem critérios diagnósticos formais (ex.: Roma IV) explicitados no material — os critérios formais não estão sourced neste acervo e não são incluídos como dado de precisão para não inventar número.
- Verificação nível 1: CONFIRMADO

## Como cai

Não aparece isolado nas devolutivas mapeadas — SII entra como diagnóstico de exclusão dentro de vinhetas de dor abdominal crônica/diarreia recorrente, testando se o aluno reconhece o perfil epidemiológico típico e sabe que o diagnóstico exige antes afastar sinais de alarme e diferenciais orgânicos (DII, celíaca), não fechar por exclusão automática.

## Conceito operacional mínimo

SII é diagnóstico funcional: dor abdominal crônica e recorrente com alteração do hábito intestinal, sem base orgânica identificável. O perfil clássico é mulher, com fatores de estresse associados, entre 30-50 anos. Um discriminador prático citado na fonte é que a dor de SII não acorda o paciente à noite — sintoma noturno que desperta o sono é sinal de alarme para causa orgânica (a mesma lógica de "diarreia noturna sugere doença orgânica" vista em diarreia crônica geral) e deve afastar SII como hipótese principal.

## Pivô clínico

SII é diagnóstico de exclusão funcional, não default automático diante de qualquer dor abdominal crônica — a vinheta que descreve sintomas que mimetizam DII (sangue nas fezes, perda de peso, febre, despertar noturno) exige investigação com exames antes de fechar SII, mesmo que o perfil demográfico (mulher, meia-idade, estresse) seja compatível.

## Palavras-âncora

Dor abdominal crônica e recorrente; alteração de hábito intestinal; sem base orgânica; não acorda o paciente à noite; mulher, estresse, 30-50 anos (perfil clássico); investigar se sintomas mimetizam DII; escopolamina e bromoprida; antidepressivos (tricíclicos e ISRS).

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| diferenciar próximos | SII x DII/causa orgânica: SII não acorda o paciente à noite; sintoma noturno é sinal de alarme para causa orgânica | sinal-achado | operacional | fechamento precoce — fechar SII pelo perfil demográfico (mulher, estresse, 30-50 anos) sem checar sinais de alarme que sugerem causa orgânica | checklist de sinais de alarme (despertar noturno, sangue, perda de peso, febre) a excluir antes de fechar SII |
| melhor exame | investigação com exames só se sintomas mimetizam DII (sangue, perda de peso, febre, alteração de exames básicos) — não investigar exaustivamente todo caso compatível com perfil típico | sequência | operacional | sobre-elaboração — solicitar bateria extensa de exames (colonoscopia, calprotectina) em todo paciente com perfil clássico e sem sinais de alarme | treinar reconhecimento de quando investigação é dispensável (perfil típico, sem sinais de alarme) x obrigatória (sintomas mimetizando DII) |
| conduta inicial | tratamento inicial é sintomático/comportamental (orientação dietética, antiespasmódico) antes de escalar para antidepressivo | sequência | operacional | definitiva antes da inicial — iniciar antidepressivo tricíclico/ISRS como primeira conduta sem tentar orientação dietética e antiespasmódico primeiro | ordenar mentalmente a escada terapêutica (dieta → antiespasmódico → antidepressivo) antes de responder |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Definição | dor abdominal crônica e recorrente, com alterações de hábito intestinal, sem base orgânica | Abordagem às diarreias, linha 174-175 | CONFIRMADO |
| Discriminador de causa orgânica | SII não acorda o paciente à noite | Abordagem às diarreias, linha 176 | CONFIRMADO |
| Perfil clássico | mulher, com estresse associado, entre 30-50 anos | Abordagem às diarreias, linha 177 | CONFIRMADO |
| Indicação de exames complementares | solicitar exames se sintomas mimetizam DII | Abordagem às diarreias, linha 182 | CONFIRMADO |
| Tratamento | orientações dietéticas; escopolamina e bromoprida (sintomático); antidepressivos tricíclicos e ISRS | Abordagem às diarreias, linha 186-189 | CONFIRMADO |
| SII como causa de diarreia crônica | uma das causas não infecciosas mais frequentes de diarreia crônica em países desenvolvidos, junto com DII e síndromes de má absorção | CASOS_CL_NICOS_RESUMO, linha 148 | CONFIRMADO |
| Diarreia noturna (achado geral de diarreia crônica) | sugere doença orgânica (não funcional) | CASOS_CL_NICOS_RESUMO, linha 152 | CONFIRMADO (dado geral de diarreia crônica, consistente com o discriminador específico de SII acima) |

## Pegadinhas

- Perfil demográfico compatível (mulher, meia-idade, estresse) não é suficiente para fechar SII — sinais de alarme (despertar noturno, sangue, perda de peso, febre) sempre têm que ser ativamente descartados primeiro.
- SII não é diagnóstico "por exclusão automática de tudo" — a indicação de exames é dirigida (só se sintomas mimetizam DII), não uma bateria extensa e indiscriminada em todo paciente com dor abdominal crônica.
- Tratar SII como se fosse sempre necessário antidepressivo de saída é sobre-medicalizar — a escada terapêutica começa por orientação dietética e antiespasmódico.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Mulher, 35 anos, estressada, dor abdominal crônica que a acorda à noite: fechar SII pelo perfil demográfico | perfil "bate" com o clássico de SII | fechamento precoce | despertar noturno é sinal de alarme para causa orgânica — SII classicamente não acorda o paciente; esse achado deveria reabrir a investigação, não fechar SII |
| Paciente com dor abdominal crônica típica de SII, sem sinais de alarme: solicitar colonoscopia e calprotectina fecal de rotina | parece "mais completo" investigar tudo | sobre-elaboração | sem sinais de alarme ou sintomas que mimetizem DII, a investigação extensa não é a conduta inicial recomendada nesse perfil |
| Paciente com SII recém-diagnosticada: iniciar antidepressivo tricíclico como primeira conduta | antidepressivo parece a "conduta definitiva" mais robusta | definitiva antes da inicial | a escada terapêutica começa por orientação dietética e antiespasmódico (escopolamina/bromoprida); antidepressivo entra em casos refratários ou com componente disfuncional mais marcado |

## Conduta

- Inicial: orientação dietética e uso de antiespasmódico/antiemético sintomático (escopolamina, bromoprida) no perfil típico sem sinais de alarme.
- Definitiva: antidepressivos (tricíclicos ou ISRS) reservados para casos que não respondem à abordagem inicial ou com componente disfuncional mais evidente.
- Condição da conduta: investigação com exames (colonoscopia, marcadores inflamatórios) só é indicada se os sintomas mimetizam DII (sangue, perda de peso, febre, despertar noturno).
- Diferencial perigoso: DII e outras causas orgânicas de diarreia crônica — o discriminador prático mais citado é o despertar noturno pela dor/diarreia, ausente em SII.
- O que mudaria a decisão: aparecimento de sangue nas fezes, perda de peso, febre ou despertar noturno muda a conduta de "tratamento sintomático" para "investigação ativa de causa orgânica".

## Mini-casos ativos

Mulher, 38 anos, dor abdominal crônica recorrente associada a alteração de hábito intestinal, período de maior estresse no trabalho, sem sangue nas fezes, sem perda de peso, dor não a acorda à noite → variável decisiva: perfil clássico + ausência de sinais de alarme (incluindo não despertar noturno) sustenta SII sem necessidade de investigação extensa; iniciar orientação dietética e antiespasmódico.

Mulher, 42 anos, dor abdominal crônica que a acorda à noite, com episódios de sangue nas fezes → variável decisiva: despertar noturno + sangramento são sinais de alarme que afastam SII como hipótese principal — investigar DII antes de fechar diagnóstico funcional.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Definição de SII | Dor abdominal crônica recorrente com alteração de hábito intestinal, sem base orgânica | dado |
| Discriminador de SII x causa orgânica | SII não acorda o paciente à noite | pegadinha |
| Perfil clássico de SII | Mulher, com estresse, 30-50 anos | dado |
| Quando investigar com exames em suspeita de SII | Só se sintomas mimetizam DII (sangue, perda de peso, febre) | sequência |
| Primeira linha de tratamento | Orientação dietética + antiespasmódico (escopolamina/bromoprida) | sequência |
| Quando usar antidepressivo em SII | Casos refratários à abordagem inicial | sequência |

## Revisão

- Revisar quando: antes de qualquer vinheta de dor abdominal crônica em mulher jovem/meia-idade com fator de estresse — treinar o reflexo de checar despertar noturno e demais sinais de alarme antes de fechar SII.
- Critério de parada: em 3 casos seguidos, decidir corretamente se o caso é SII (sem investigação extensa) ou exige afastar causa orgânica (com investigação), usando o despertar noturno como discriminador central.
