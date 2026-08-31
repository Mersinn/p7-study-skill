# OSCE Pediatria — pneumonia, asma, diarreia com desidratação, aleitamento materno e assistência ao recém-nascido

## Metadados

- Disciplina: OSCE
- Especialidade: Pediatria
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não (as 3 fontes do cluster são NATIVA)
- Fontes usadas: `OSCE .pdf` (camada B, 101 páginas com marcador por slide, paginação exata: seção de Pediatria começa ~p.84; pneumonia ~p.85; assistência ao RN ~p.89; caso clínico completo de diarreia/desidratação com comandos e gabarito ~p.100); `OSCE - PEDIATRIA.pdf` (camada B, formato tabela contínua doença/sinais/exame/diagnóstico/tratamento/outros, 5 páginas pelo cluster, sem marcador de página detectável — citado como documento íntegro; único a detalhar critérios de Rocha para lactente sibilante/asma e os planos A/B/C de reidratação por extenso); `FACILITA OSCE (1).pdf` (camada B, 67 páginas com sumário próprio — assistência ao RN p.49, asma p.53, aleitamento materno p.55, diarreia p.58, pneumonia p.62)
- Evidência de prova/devolutiva: nenhuma devolutiva de prova teórica — as 3 fontes são material de revisão de colegas para o OSCE, incluindo 1 caso clínico completo com comandos numerados e gabarito comentado (diarreia aguda com desidratação grave) em `OSCE .pdf`
- Limitações da fonte: `OSCE .pdf` traz os cabeçalhos "Plano de tratamento" da diarreia repetidos 4 vezes sem o conteúdo tabular associado (provavelmente uma tabela/imagem que não sobreviveu à extração de texto) — o conteúdo dos planos A/B/C foi reconstruído a partir de `OSCE - PEDIATRIA.pdf` e `FACILITA OSCE (1).pdf`, que trazem o mesmo protocolo por extenso; nenhuma fonte tem camada A (não há slide do professor mapeado para este tema no cluster).
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Contrato de recuperação

`answer_key_scope: curricular`; `clinical_validity_default: pending`. As fontes
de OSCE são B-only. `CONFIRMADO` significa transcrição curricular, não prática
atual. Apenas linhas `CURRENT_VERIFIED` com claim rastreável podem sustentar
conduta; todos os demais cortes, volumes, esquemas e sequências ficam
`QUARANTINED` para uso clínico e não constituem checklist oficial.

## Como cai

A cabine de Pediatria concentra dois padrões: **protocolos escalonados que não podem pular etapa** (reanimação do RN, planos de reidratação A/B/C) e **aplicação de critério objetivo por idade** (frequência respiratória por faixa etária na pneumonia, dose de antibiótico por peso e idade gestacional). O caso clínico disponível (`OSCE .pdf`) treina o segundo padrão de forma direta: uma criança com sinais clássicos de desidratação grave exige que o candidato classifique formalmente o grau (não só diga "está desidratada") antes de propor a conduta, porque é a classificação que define a fase (rápida × lenta) e o volume da expansão.

## A estação

- **Tarefa:** a partir do caso clínico (lactente/criança com febre, tosse, sibilância ou diarreia — ou recém-nascido em sala de parto), reconhecer a síndrome, classificar formalmente a gravidade pelo critério objetivo correto (sinais de desidratação, sinais de gravidade respiratória, critérios de asma no lactente) e propor conduta escalonada sem pular etapa.
- **Tempo:** não informado nas fontes disponíveis.
- **Ator/paciente:** caso clínico escrito, geralmente com peso informado (para cálculo de volume/dose); pode incluir manequim de RN para simular reanimação neonatal.
- **Material:** dados vitais e de exame físico já descritos no caso (FC, FR, estado de hidratação); eventual resultado de exame de imagem (radiografia de tórax na pneumonia).
- **Rubrica sintética de treino (não oficial):** classificar gravidade, verbalizar
  segurança e calcular por peso quando pedido. Não há checklist aplicado, pesos ou
  itens eliminatórios verificáveis nas fontes.

## Pivô clínico

O pivô mais recorrente nas 3 fontes é o **peso/idade como filtro que muda toda a conduta**: a mesma queixa (febre + tosse, ou diarreia) tem protocolo de antibiótico e de reidratação completamente diferentes conforme a criança tenha menos ou mais de 2 meses de vida, e conforme o peso corporal informado no caso — o candidato que "sabe o protocolo" mas esquece de aplicar o filtro de idade/peso erra a estação mesmo acertando o diagnóstico.

## Palavras-âncora

Frequência respiratória por faixa etária · sinais de gravidade (tiragem subcostal, batimento de asa de nariz, cianose central) · APGAR (1º e 5º minuto) · hora de ouro · minuto de ouro · VPP · massagem cardíaca 3:1 · critérios maiores/menores de asma no lactente · sinal da prega · plano A/B/C · SRO · regra dos 10 passos do aleitamento materno.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | classificação do grau de desidratação (hidratado / leve / grave) pela contagem de sinais objetivos (estado de alerta, olhos, lágrimas, boca/língua, sede, sinal da prega, pulso, enchimento capilar) | limiar | operacional | fechamento precoce — dizer "criança desidratada" sem nomear o grau formal, ou contar só 1-2 sinais isolados em vez do conjunto | treinar contagem explícita de sinais positivos por categoria (hidratado/leve/grave) antes de classificar, com casos que têm sinais "mistos" de categorias diferentes |
| aplicar critério / sequenciar conduta | plano de reidratação (A domiciliar / B na unidade / C internação) definido pelo grau de desidratação, não pela vontade do médico | sequência | operacional | pular direto para plano C (hidratação venosa) em criança com desidratação leve, ou manter plano B numa criança já classificada como grave | fixar a régua "grau de desidratação → plano correspondente" e treinar 3 casos que só variam o grau |
| calcular dose/volume por peso | idade e peso mudam o cálculo no material | valor | factual | recuperar fórmula B-only como vigente ou usar faixa etária errada | treinar aritmética curricular, mas abrir protocolo atual antes de uma resposta clínica |
| reconhecer contraindicação / aplicar critério curricular | idade muda o gabarito de pneumonia na aula | limiar | operacional | promover esquema antigo a prática atual | reconhecer o filtro de idade e consultar protocolo vigente; nenhum antimicrobiano B-only é liberado |
| priorizar emergência / sequenciar conduta | SBP 2026: respiração/choro + tônus definem vitalidade; IG seleciona algoritmo; VPP se apneia/irregular ou FC<100 após passos iniciais | sequência | operacional | misturar algoritmo antigo e atual | treinar a cápsula clínica SBP 2026 |
| aplicar critério curricular | a aula usa limiares de FR por idade | limiar | factual | usar corte antigo como critério clínico isolado | treinar reconhecimento de faixa etária e abrir fonte vigente para uso real |

## Dados de precisão

### Painel curricular histórico, salvo indicação `CURRENT_VERIFIED`

`answer_key_scope: curricular`. Doses, volumes, cortes, antimicrobianos e
sequências marcados apenas `CONFIRMADO` permanecem `QUARANTINED` para prática
atual. O status confirma a transcrição da aula, não vigência clínica.

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Frequência respiratória-limiar de taquipneia por faixa etária | <2 meses: >60 irpm · 2-11 meses: >50 · 12-59 meses: >40 · 5-8 anos: >35 · >8 anos: >20 | `OSCE - PEDIATRIA.pdf` (doc. íntegro) | CONFIRMADO |
| Pneumonia — sinais de gravidade | tiragem subcostal; dificuldade para ingerir líquidos; sinais de dificuldade respiratória mais grave (movimentos involuntários da cabeça, batimento de asa do nariz); cianose central | `OSCE .pdf`, ~p.85 | CONFIRMADO |
| Pneumonia — padrão radiológico | lobar: opacificação homogênea, obedece a segmento pulmonar, broncograma aéreo (pneumococo, lactentes >6 meses) · intersticial: bilateral e difusa, infiltrado discreto, hiperinsuflação (vírus/micoplasma) · broncopneumonia: não respeita segmentação, limites irregulares (S. aureus) | `OSCE .pdf`, ~p.85 / `OSCE - PEDIATRIA.pdf` | CONFIRMADO |
| Pneumonia — tratamento por idade | <2 meses: internação obrigatória — <1 semana ampicilina + gentamicina; >1 semana ampicilina + ceftriaxona · ≥2 meses ambulatorial: amoxicilina ou penicilina G procaína, sem melhora em 48h → amoxicilina + clavulanato (ou cefalosporina de 2ª geração) · internação grave: penicilina cristalina ou ampicilina · muito grave: oxacilina + cloranfenicol ou oxacilina + ceftriaxona; sem melhora em 48-72h ou piora: vancomicina + ceftriaxona | `OSCE .pdf`, ~p.85 / `OSCE - PEDIATRIA.pdf` | CONFIRMADO |
| Asma — critérios diagnósticos no lactente | alto risco de asma: 2 critérios maiores (obrigatoriamente 1 dos 2 primeiros) OU 2 maiores + 2 menores. Maiores: hospitalização por sibilância grave; ≥3 episódios de sibilância em 6 meses; história de asma nos pais; dermatite atópica. Menores: rinorreia não associada a resfriado; sibilância não associada a resfriado; eosinofilia >5%; sexo masculino | `OSCE - PEDIATRIA.pdf` (doc. íntegro) / `FACILITA OSCE (1).pdf`, p.53 | CONFIRMADO |
| Asma — espirometria | só realizável em crianças ≥6 anos que obedecem comando; VEF1 aumenta >10% pós-broncodilatador confirma diagnóstico; relação VEF1/CVF >0,7 | `OSCE - PEDIATRIA.pdf` / `FACILITA OSCE (1).pdf`, p.53 | CONFIRMADO |
| Crise asmática 6–11 anos — prática atual | SABA + O2 quando indicado + corticoide sistêmico precoce; ipratrópio em grave. Quando O2 é indicado, alvo 92–95%; SpO2 <92% sugere O2, mas 92% não é corte absoluto para negar diante de outros critérios de gravidade. SpO2 isolada não indica VNI/IOT | GINA 2026, Box 9-4 e Box 9-6 | CURRENT_VERIFIED |
| Crise asmática — antibiótico | não é rotina (80% das exacerbações são virais); só na forte suspeita de infecção bacteriana (febre, escarro purulento, consolidação radiográfica) | `FACILITA OSCE (1).pdf`, p.53 | CONFIRMADO |
| Magnésio na asma | não rotineiro; considerar após falha inicial em grave | GINA 2026 | CURRENT_VERIFIED |
| Diarreia — definição | ≥3 evacuações amolecidas/líquidas em 24h | `OSCE .pdf`, ~p.100 / `FACILITA OSCE (1).pdf`, p.58 | CONFIRMADO |
| Diarreia — sinais de desidratação por grau | hidratado: alerta, olhos/lágrimas normais, boca/língua úmidas, sede/diurese preservadas, pulso cheio, enchimento capilar <3s, prega rápida · leve: irritado, olhos fundos sem lágrimas, boca/língua seca, sede aumentada, diurese diminuída, prega lenta, pulso rápido e débil, enchimento capilar 3-5s · grave: comatoso/letárgico, incapaz de beber ou bebe mal, olhos muito fundos sem lágrimas, boca/língua muito seca, diurese ausente, prega >2s para desaparecer, pulso muito débil/ausente, enchimento capilar >5s | `OSCE - PEDIATRIA.pdf` (doc. íntegro) | CONFIRMADO |
| Plano A (domiciliar) | manter alimentação habitual; oferecer líquidos/SRO após cada evacuação: <2 anos 50-100mL; 2-10 anos 100-200mL; >10 anos o que aceitar; suplementar zinco em <5 anos por 14 dias | `OSCE - PEDIATRIA.pdf` / `FACILITA OSCE (1).pdf`, p.58 | CONFIRMADO |
| Plano B (unidade de saúde) | SRO 50-100 mL/kg em 4-6h na unidade; suspender alimentação exceto o aleitamento materno (mantido); vômitos ocasionais não contraindicam (reduzir volume, aumentar intervalo, considerar ondansetrona); vômitos persistentes → gastróclise (SNG) | `OSCE - PEDIATRIA.pdf` / `FACILITA OSCE (1).pdf`, p.58 | CONFIRMADO |
| Plano C (internação) — fase de expansão rápida | <5 anos: 20 mL/kg de SF a cada 30 min, repetir até hidratar · ≥5 anos: 30 mL/kg de SF em 30 min + 70 mL/kg de ringer lactato em 2h30 · RN ou cardiopata grave: expansões de 10 mL/kg a cada 30 min | `OSCE - PEDIATRIA.pdf` (doc. íntegro) | CONFIRMADO |
| Plano C — fase de manutenção/reposição | manutenção: SG5% + SF na proporção 4:1 pela regra de Holliday-Segar + KCl 10% (2mL/100mL) em 24h · reposição: SG5% + SF partes iguais, iniciar 50 mL/kg/dia, reavaliar pelas perdas | `OSCE .pdf`, ~p.100 / `OSCE - PEDIATRIA.pdf` | CONFIRMADO |
| Diarreia — antibiótico | não é rotina (vírus são a principal causa); indicado se comprometimento do estado geral, disenteria ou cólera grave; opções: azitromicina, ceftriaxona ou ciprofloxacino (adolescente/>30kg) | `FACILITA OSCE (1).pdf`, p.58 | CONFIRMADO |
| Diarreia — "bônus" de tratamento | antiemético: ondansetrona; zinco 10mg/dia (<6 meses) ou 20mg/dia (6 meses-5 anos) por 10-14 dias; evitar antidiarreicos | `FACILITA OSCE (1).pdf`, p.58 | CONFIRMADO |
| APGAR | avaliado no 1º e 5º minuto de vida; repetido a cada 5 min se <7 no 5º minuto | `OSCE .pdf`, ~p.89 / `FACILITA OSCE (1).pdf`, p.49 | CONFIRMADO |
| Reanimação neonatal — vitalidade | respira/chora + tônus flexor; IG seleciona algoritmo. APGAR não deve atrasar VPP | SBP 2026 ≥34 | CURRENT_VERIFIED |
| Reanimação neonatal — se resposta "não" | estímulo tátil no dorso (até 2x) → se não funcionar, clampear cordão e iniciar passos iniciais (calor radiante, secar, posicionar vias aéreas, aspirar se necessário) → reavaliar FC e ritmo respiratório | `FACILITA OSCE (1).pdf`, p.49 | CONFIRMADO |
| Reanimação neonatal — VPP | se FC <100 ou ritmo respiratório irregular após os passos iniciais: iniciar VPP com balão autoinflável (ambu) + máscara, "aperta-solta-solta" por 30s; minuto de ouro = iniciar VPP antes do 1º minuto de vida; reavaliar a cada 30s | `FACILITA OSCE (1).pdf`, p.49 | CONFIRMADO |
| Reanimação neonatal — massagem cardíaca | indicada se FC <60 após VPP correta por 30s; técnica dos 2 polegares (2 médicos) é preferida — maior pico de pressão sistólica, melhor perfusão coronariana, menos cansativa; proporção 3:1 (3 compressões : 1 ventilação), ciclos de 60s antes de reavaliar | `OSCE .pdf`, ~p.89 / `FACILITA OSCE (1).pdf`, p.49 | CONFIRMADO |
| Reanimação neonatal — droga de escolha | adrenalina (vasoconstrição periférica, aumenta perfusão coronariana/débito cardíaco), via endovenosa por cateter umbilical (via endotraqueal só uma vez, absorção lenta/imprevisível); SF 0,9% como expansor se não houver resposta à adrenalina ou houver sinais de hipovolemia | `FACILITA OSCE (1).pdf`, p.49 | CONFIRMADO |
| Reanimação neonatal — regra antiga de interrupção | considerar interrupção após 10 min de assistolia sem resposta | `FACILITA OSCE (1).pdf`, p.49 | QUARANTINED — não usar; decisão exige diretriz neonatal vigente e contexto individual |
| Aleitamento materno — 10 passos (versão resumida) | norma escrita e equipe treinada; informar gestantes; ajudar a iniciar amamentação na 1ª meia hora pós-parto; ensinar a amamentar e manter lactação; não dar outro alimento sem indicação médica; alojamento conjunto 24h; livre demanda; não dar bicos/chupetas; encorajar grupos de apoio pós-alta | `FACILITA OSCE (1).pdf`, p.55 | CONFIRMADO |
| Aleitamento — recomendação de tempo | exclusivo até os 6 meses; complementado até os 2 anos ou mais | `FACILITA OSCE (1).pdf`, p.55 | CONFIRMADO |
| Aleitamento — mastite | não contraindica a amamentação; tratamento com ibuprofeno e, se quadro significativo, antibiótico (amoxicilina + clavulanato por 10-14 dias) | `FACILITA OSCE (1).pdf`, p.55 | CONFIRMADO |
| Aleitamento — colostro × leite maduro | colostro: último trimestre até a 1ª semana pós-parto, rico em proteína e IgA, pobre em gordura/carboidrato, efeito laxante · leite de transição: 7º-14º dia · leite maduro: a partir da 2ª semana | `FACILITA OSCE (1).pdf`, p.55 | CONFIRMADO |

## Pegadinhas

**Erros curriculares de treino (não itens oficiais nem regras clínicas atuais):**

- Não classificar formalmente o grau de desidratação (dizer só "está desidratado") antes de propor o plano de reidratação — a estação cobra o grau nomeado, que é o que define o plano.
- Pular etapa da reanimação neonatal (ex.: ir direto para massagem cardíaca sem ter feito e reavaliado a VPP por 30s).
- Escolher antimicrobiano sem declarar idade, gravidade e fonte vigente; os esquemas B-only não são recuperáveis como prática atual.
- Suspender o aleitamento materno durante o plano B de reidratação — a fonte é explícita que só os outros alimentos são suspensos, o leite materno é mantido.
- Não calcular o volume de expansão do plano C pelo peso informado no caso, respondendo só com a fórmula genérica sem aplicar o número.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "Criança com febre e tosse = pneumonia, iniciar amoxicilina" sem checar idade/gravidade | amoxicilina é lembrada primeiro | premissa não checada | não fecha diagnóstico nem esquema; a fonte B-only não autoriza prescrição atual |
| Classificar uma criança com "olhos fundos e prega lenta" como desidratação grave só por esses 2 sinais | são achados que "soam graves" | superextrapolação | esses 2 sinais isolados descrevem desidratação **leve** — desidratação grave exige o conjunto mais extenso (comatoso/letárgico, incapaz de beber, prega >2s, pulso muito débil) |
| Esperar uma hora de falha do SABA para dar corticoide | reproduz a escada antiga | sequência perdida | no GINA 2026, corticoide é precoce, exceto nas crises mais leves |
| Suspender toda alimentação, incluindo o peito, durante a terapia de reidratação oral (plano B) | "suspender alimentação" é a instrução mais lembrada do plano B | regra mal-aprendida | a suspensão vale para outros alimentos; o aleitamento materno é mantido porque funciona como líquido reidratante |

## Conduta

- Inicial: classificar formalmente a gravidade (grau de desidratação, sinais de gravidade respiratória, critérios de asma no lactente) antes de qualquer prescrição; em RN, responder as 3 perguntas de reanimação antes de decidir entre contato pele a pele e passos iniciais.
- Definitiva: pneumonia e reidratação exigem protocolo pediátrico vigente; asma
  6–11 anos segue o núcleo `CURRENT_VERIFIED` (broncodilatador, corticoide
  sistêmico precoce e O2 quando indicado), sem recuperar a escada antiga.
- Condição da conduta: idade, peso e gravidade mudam protocolos; em asma 6–11,
  não postergar corticoide até falha de uma hora, exceto crise muito leve.
- Diferencial perigoso: sinais de gravidade respiratória (tiragem, batimento de asa de nariz, cianose central) e vômitos persistentes/incapacidade de beber (que indicam gastróclise ou plano C) não esperam reavaliação prolongada.
- O que mudaria a decisão: idade, peso, gravidade, resposta clínica e protocolo
  vigente. Não postergar automaticamente corticoide até falha em uma hora.

## Mini-casos ativos

1. J.K.M., 3 anos, 8kg, com diarreia, letargia, incapacidade de beber, prega muito lenta e pulso fraco. **Pivô curricular:** reconhecer desidratação grave e necessidade de resposta urgente. Volume, solução e velocidade devem vir de protocolo pediátrico vigente; a fórmula antiga não é recuperada desta cápsula.
2. RN a termo, nasce chorando, bom tônus, mãe sem intercorrências. **Pivô:** respondeu "sim" às 3 perguntas — a conduta é contato pele a pele e clampeamento tardio do cordão, não avaliação de APGAR antes de decidir (o APGAR não entra nessa decisão inicial).
3. Lactente com sibilância recorrente, internação e história familiar de asma. **Pivô curricular:** reconhecer fatores de risco; a soma e os cortes da aula estão `QUARANTINED` e não fecham diagnóstico atual.
4. Puérpera com mama direita quente, pesada, dolorosa, sem hiperemia, no 4º dia pós-parto. **Pivô:** esse quadro descreve ingurgitamento mamário fisiológico (apojadura), não mastite — orientar a manter a amamentação e o esvaziamento completo de cada mama, sem suspender o aleitamento.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| A cápsula fornece idade/esquema atual de pneumonia? | Não. Os cortes e antimicrobianos B-only estão `QUARANTINED`; usar protocolo vigente | segurança |
| Como responder a desidratação grave em prática atual? | Reconhecer emergência e abrir protocolo pediátrico vigente; a fórmula B-only não é liberada | segurança |
| A cápsula fornece volume atual do plano C? | Não. O cálculo B-only é curricular; confirmar protocolo vigente por idade, peso e contexto | segurança |
| O aleitamento materno é suspenso no plano B? | Não — só os outros alimentos são suspensos; o leite materno é mantido | regra |
| A soma curricular de critérios fecha asma no lactente hoje? | Não. Está `QUARANTINED`; diagnóstico atual exige avaliação e fonte vigente | segurança |
| Núcleo atual da crise asmática 6–11 anos | broncodilatador, corticoide sistêmico precoce e O2 quando indicado, alvo 92–95%; não usar 92% como corte absoluto de não tratamento | sequência atual |
| A regra B-only de repetição do APGAR é protocolo atual? | Não nesta cápsula; confirmar na diretriz neonatal vigente | segurança |
| Como recuperar técnica/proporção de compressões neonatais? | Usar algoritmo neonatal vigente; não inferir apenas do material B-only | segurança |

## Revisão

- Revisar quando: antes de qualquer simulação de estação de pediatria, e sempre que o caso trouxer peso corporal ou idade em meses explícitos — são os dois dados que mais mudam a conduta nesta especialidade.
- Critério de parada: quando conseguir, dado um caso de diarreia ou de pneumonia pediátrica, classificar a gravidade formalmente e aplicar o esquema correto de conduta variando só a idade/peso em 3 casos seguidos, sem consultar a fonte.
