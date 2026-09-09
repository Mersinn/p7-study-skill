# Sepse neonatal e meningite neonatal

## Metadados

- Disciplina: EISCA
- Especialidade: Neonatologia
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não
- Fontes usadas: "Sepse e meningite neonatal (1)" — anotações de aula de Letícia Burity (camada B, NATIVA, 5 pp.); "Sepse e meningite neonatal" — anotações de aula de Jéssyca Seixas, 2020.2, referenciando aula da profa. Lívia Prazim (camada B, NATIVA, 4 pp.)
- Evidência de prova/devolutiva: DEVOLUTIVA Terceira Avaliação / 3ª Avaliação Turma B 2021.1 (Q2, sepse tardia — protocolo escalonado); Devolutiva III SC 2016.1 (Q7, escore de Rodwell); Integradas — "Sepse tardia neonatal — interpretação de exame" (escore de Rodwell abaixo do limiar)
- Limitações da fonte: sem slide fotografado do professor entre as fontes de aula (tem_camada_A=false) — esta cápsula cruza DUAS anotações de aula independentes (turmas/anos diferentes) da MESMA professora (Dra. Lívia Prazim); nenhum dos dois documentos define o "escore de Rodwell" citado nas devolutivas. Revalidação clínica de 2026-08-22 adicionou SBP 2025 e NICE NG195 atualizado em 13/05/2026: janela 48/72h, amniorrexe por idade gestacional e limiar de febre materna permanecem conflitos explícitos; não usar os números como regra universal sem protocolo local.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES (segunda fonte B completou tabelas de tratamento e critérios de meningite ausentes/cortados na primeira; valores numéricos idênticos nas duas fontes onde há sobreposição)

## Contrato de recuperação

`answer_key_scope: curricular`; `clinical_validity_default: pending`. Dados
epidemiológicos, cortes, somas de critérios e esquemas B-only ficam disponíveis
para alinhamento com a aula, mas não podem ser recuperados como prática atual.
Somente claims `current` rastreáveis e fontes oficiais abertas sustentam conduta.

## Como cai

Cai como reconhecimento de risco para infecção neonatal precoce e como escolha do esquema empírico conforme a definição temporal e o protocolo local. A amniorrexe não deve ser tratada como corte universal: o contexto da idade gestacional e da diretriz importa. O erro mais perigoso é "definitiva antes da inicial" — escolher antibiótico de amplo espectro, ou tratar um RN assintomático, sem checar sinais clínicos, combinação de fatores, idade gestacional, ecologia local e protocolo institucional.

## Conceito operacional mínimo

Sepse precoce e tardia dependem da definição adotada: a cápsula usa 72h como convenção curricular, enquanto a SBP 2025 descreve sepse precoce especialmente até 48h e tardia após 48h. Não escolher antibiótico só pelo número sem declarar o protocolo. Fatores maternos e do parto devem ser combinados com idade gestacional, sinais clínicos e observação seriada; uma amniorrexe isolada não autoriza automaticamente antibiótico. Para o antibiótico empírico precoce, a referência brasileira SBP 2025 usa ampicilina ou penicilina cristalina + amicacina ou gentamicina, sempre conforme protocolo local, resistência, peso, idade gestacional, função renal e suspeita de meningite. Punção lombar não é mandatória em todo RN com sepse tardia: indicar quando houver suspeita clínica de meningite e o RN estiver estável; se não for segura, colher hemocultura antes da primeira dose e tratar com doses que cubram meningite, reavaliando depois.

## Pivô clínico

O pivô é a definição temporal explicitada pelo protocolo, não um corte universal: a aula usa 72h, a SBP 2025 usa especialmente até 48h para precoce e após 48h para tardia. Segundo pivô: risco materno/obstétrico precisa ser estratificado por idade gestacional e combinado com sinais do RN; no NICE NG195 atualizado, ROM >18h é indicador antes de parto pré-termo e >24h antes de parto a termo. Um RN assintomático não recebe antibiótico automaticamente por um único fator: aplicar a via de fatores/indicadores, observação clínica seriada ou investigação/tratamento conforme o protocolo institucional.

## Palavras-âncora

Streptococcus grupo B (GBS) · amniorrexe = limiar dependente de idade gestacional/protocolo · cultura sem atraso material do antibiótico indicado · punção lombar conforme suspeita e estabilidade · sinais de choque · CIVD · critérios laboratoriais curriculares `QUARANTINED` · esquema precoce brasileiro SBP rastreado · esquema tardio dependente de protocolo e flora local.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| identificar complicação | amniorrexe é fator de risco contextual: NICE usa >18h antes de parto pré-termo e >24h antes de parto a termo; combinar com os demais indicadores e o protocolo local | limiar | operacional | valor universalizado (troca 18h por outro corte, ou trata uma amniorrexe isolada como indicação automática) | card comparativo idade gestacional × limiar × conduta, com treino de combinação de fatores |
| conduta definitiva | esquema empírico depende da definição temporal adotada: precoce (penicilina/ampicilina + aminoglicosídeo) × tardia (cobertura hospitalar conforme flora/resistência) | sequencia | operacional | definitiva antes da inicial (aplica esquema tardio hospitalar em quadro precoce ou vice-versa) | casos pareados com o protocolo declarado e horários próximos de 48/72h |
| priorizar emergência | RN assintomático de risco não recebe ATB automaticamente por um único fator; aplicar via de indicadores, observação seriada ou investigação/tratamento conforme protocolo | prioridade | operacional | fechamento precoce (trata sem critério) ou atraso indevido (aguarda cultura quando a via já indica ATB) | árvore risco/indicador × sinais clínicos × observação/ATB, sem transformar um fator isolado em regra |
| exame inicial | hemocultura antes do antibiótico quando isso não causar atraso material; líquor conforme suspeita e estabilidade | sequencia | operacional | atrasar ATB indicado para completar coleta, ou puncionar RN instável | checklist de coleta sem atraso + indicação/segurança de PL |
| aplicar critério curricular | material B cita 3+ sinais OU 2 sinais + 1 fator de risco | limiar | operacional | promover corte curricular a regra atual | `QUARANTINED`; treinar avaliação clínica/protocolo vigente |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Sepse precoce — janela de início | 72h é convenção curricular desta cápsula; SBP 2025 descreve sepse precoce especialmente até 48h e tardia após 48h | aulas Burity/Seixas; SBP 2025, p.5 | CONFLITO — declarar protocolo |
| Sepse precoce — etiologia curricular | 62% Gram+ (43% Strep. grupo B); 37% Gram- (29% E. coli) | Sepse e meningite neonatal (Burity), p.1; (Seixas), p.1 | QUARANTINED — percentuais B-only, não epidemiologia atual |
| Sepse tardia — etiologia curricular | 79% Gram+ (57% S. epidermidis, 12% S. aureus); 19% Gram- multirresistente; 6% fungos | Sepse e meningite neonatal (Burity), p.1; (Seixas), p.1 | QUARANTINED — percentuais B-only, não epidemiologia atual |
| GBS — mortalidade curricular | 20-30% | Sepse e meningite neonatal (Burity), p.2; (Seixas), p.1 | QUARANTINED — prognóstico B-only |
| GBS — sequelas neurológicas curriculares | 15-30% dos sobreviventes | Sepse e meningite neonatal (Burity), p.2; (Seixas), p.1 | QUARANTINED — prognóstico B-only |
| Fator de risco — amniorrexe | limiar depende da idade gestacional e do protocolo; NICE: >18h antes de parto pré-termo, >24h antes de parto a termo | SPRS 2012, p.2; NICE NG195, atualização 13/05/2026 | CONFLITO — não universalizar; risco 4x não verificado |
| Febre materna intraparto | cápsula usa >38°C; SPRS 2012 usa >37,5°C; NICE 2026 enfatiza sepse materna/chorioamnionite no eixo de risco | SPRS 2012, p.2; NICE NG195, rationale, atualização 13/05/2026 | CONFLITO — limiar não universal |
| Sepse presumível — critério de soma curricular | 1 fator maior + 2 fatores menores (ou 2 maiores, conforme Seixas) | Sepse e meningite neonatal (Burity), p.2; (Seixas), p.2 — pequena divergência de redação entre as 2 fontes B, mesma professora | QUARANTINED — divergência B-only; não escolher uma variante por coerência aparente |
| Sepse clínica tardia — corte citado na aula | 3+ sinais clínicos OU 2 sinais + 1 fator de risco | fontes B | QUARANTINED — não usar como critério atual isolado |
| Choque séptico — limiares citados no material | FC>160bpm; FR>60ipm; PAM<30mmHg; TEC>2s; diurese <1 mL/kg/h | Sepse e meningite neonatal (Seixas), p.3 | QUARANTINED — B-only; não usar cortes isolados como critério atual |
| Hemocultura — sensibilidade e ordem citadas na aula | 80%; colher antes do ATB quando não houver atraso material | fontes B | QUARANTINED — não usar sensibilidade nem regra absoluta como prática atual |
| Meningite associada a sepse | material orienta líquor/cobertura conforme clínica e estabilidade | fontes B | QUARANTINED — prática atual exige protocolo neonatal vigente |
| Hemograma infeccioso | 3 ou mais dos 7 aspectos avaliados positivos | fontes B | QUARANTINED — corte curricular |
| PCR — VPN e cinética | VPN 99%; positiva após 24h; alterada se >6-10 mg/L | fonte B | QUARANTINED — cortes curriculares |
| Esquema sepse precoce | ampicilina ou penicilina cristalina + amicacina ou gentamicina; seguir protocolo, resistência, idade gestacional, peso, rim e suspeita de meningite | SBP 2025, p.5; NICE NG195 para contexto britânico | REVALIDADO COM CONTEXTO |
| Esquema sepse tardia | tabela cita opções dependentes de flora hospitalar e resistência | SBP 2025, p.5 | QUARANTINED — não há claim current exato no registry |
| Sepse fúngica | material traz frequência, agente e antifúngicos específicos | fontes B | QUARANTINED — não usar como conduta atual |
| Meta de hematócrito no suporte | manter Ht > 40% | fonte B | QUARANTINED — meta curricular |

## Pegadinhas

- Duas fontes B da mesma professora divergem levemente na redação do critério de "sepse presumível" (uma diz "1 maior + 2 menores", a compilação de risco cita também "2 maiores") — a prova provavelmente cobra a combinação mais frequente citada nas devolutivas (1 maior + 2 menores); tratar como pendência a confirmar no slide, não como certeza absoluta.
- RN assintomático não recebe antibiótico automaticamente por um único fator: aplicar a via de indicadores, combinação de fatores, observação seriada ou investigação/tratamento conforme o protocolo institucional. Quando a via indicar ATB, colher hemocultura antes e não esperar a cultura positivar.
- Colher hemocultura antes da primeira dose quando isso não causar atraso material; antibiótico indicado não deve ser adiado para completar coleta.
- Punção lombar não é obrigatória em todo RN com sepse tardia: indicá-la quando houver suspeita de meningite e estabilidade; se não for segura, colher hemocultura e usar cobertura/dose para meningite, reavaliando a punção após estabilização.
- Leucocitose isolada da mãe (fator menor) não fecha sepse presumível sozinha — precisa de mais um fator (maior ou menor) associado.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "RN com sintomas após 96h de vida deve receber automaticamente o esquema de penicilina + aminoglicosídeo" | esquema precoce decorado como "o" tratamento de sepse neonatal | definitiva antes da inicial / valor errado | após o corte definido pelo protocolo, reavaliar como sepse tardia e cobrir flora hospitalar conforme SBP/local; não transportar o esquema precoce sem checar a janela |
| "Aguardar hemocultura positiva antes de iniciar antibiótico em RN cuja via de indicadores já exige tratamento" | parece prudente não tratar sem confirmação | fechamento precoce (invertido: atraso indevido) | quando o protocolo indica ATB, colher hemocultura antes e iniciar sem aguardar positividade; quando há apenas um fator isolado, não inventar indicação automática |
| "Aguardar coleta completa antes de iniciar ATB indicado" | parece maximizar rendimento diagnóstico | atraso indevido | colher antes quando viável, mas não atrasar tratamento indicado |
| "Meningite neonatal é uma complicação rara e principalmente ligada à sepse precoce" | meningite soa como evento raro e desconectado | pivô perdido | meningite está mais associada à sepse TARDIA, e 25% dos neonatos com sepse têm meningite — não é achado raro |

## Conduta

- Inicial: aplicar a via institucional de fatores/indicadores, idade gestacional e sinais do RN. Quando houver indicação, colher hemocultura antes da primeira dose se isso não atrasar materialmente o antibiótico; considerar líquor conforme suspeita e estabilidade.
- Definitiva: o claim `current` rastreável sustenta o núcleo penicilínico + aminoglicosídeo para sepse precoce no contexto declarado. Esquemas tardios, antifúngicos e doses da aula permanecem `QUARANTINED`; usar protocolo institucional vigente.
- Condição da conduta: se o estado clínico não permitir punção lombar, tratar empiricamente com doses adequadas para meningite (não subdosar assumindo apenas sepse sem SNC).
- Diferencial perigoso: deterioração de perfusão, consciência, respiração e diurese exige resposta urgente, sem aguardar cultura. Os cortes numéricos B-only acima estão `QUARANTINED` e não funcionam isoladamente como regra atual.
- O que mudaria a decisão: combinação de fatores/indicadores que fecha a via institucional, qualquer sinal clínico de deterioração, idade gestacional, suspeita de meningite e estabilidade para punção; um fator isolado não deve ser promovido a indicação universal.

## Mini-casos ativos

1. RN termo, mãe com amniorrexe de 20h e febre intraparto de 38,5°C, nasce assintomático. Conduta: não fechar automaticamente só pela frase "2 fatores maiores"; declarar a diretriz, verificar idade gestacional/indicadores, iniciar observação ou ATB conforme a via institucional e, se indicar ATB, colher hemocultura antes. Variável decisiva: protocolo + combinação de fatores, não um número isolado.
2. RN de 10 dias em UTI neonatal desenvolve recusa alimentar, apneia e distermia. Conduta de treino: reconhecer contexto tardio/hospitalar, colher culturas sem atrasar tratamento indicado e usar protocolo institucional vigente; a combinação farmacológica da aula está `QUARANTINED`.
3. RN com sepse tardia confirmada e hemocultura positiva para germe Gram-negativo hospitalar; estado clínico grave impede punção lombar imediata. Conduta: tratar empiricamente com antibiótico em dose suficiente para cobrir meningite, mesmo sem confirmação liquórica, e reavaliar a punção quando estabilizar. Variável decisiva: impossibilidade de PL não dispensa cobertura para SNC.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Janela que separa sepse precoce de tardia | declarar a definição do protocolo (cápsula: 72h; SBP 2025: especialmente até 48h/ após 48h) | Limiar |
| Agente destacado pela aula na sepse precoce | Streptococcus do grupo B (GBS); percentuais e mortalidade da aula estão `QUARANTINED` | fato curricular |
| Ordem hemocultura × antibiótico | colher antes quando viável, sem atrasar ATB indicado | Sequência |
| Esquema empírico sepse precoce | Penicilina/ampicilina + aminoglicosídeo (gentamicina/amicacina) | Conduta |
| Esquema empírico sepse tardia | protocolo institucional vigente; combinações da aula `QUARANTINED` | Limite de fonte |
| Corte curricular para sepse tardia | 3+ sinais OU 2 sinais + 1 fator — `QUARANTINED` | Histórico |
| RN assintomático com fatores de risco — conduta | Aplicar via institucional de indicadores/observação; se ATB indicado, colher cultura antes e não esperar positividade | Pegadinha |

## Revisão

- Revisar quando: antes de qualquer simulado que combine emergências neonatais e antes da unidade que cobrir Neonatologia (unidade ainda não definida nas fontes consultadas — confirmar no cronograma do professor).
- Critério de parada: acertar 4/4 mini-casos distinguindo precoce×tardia pelo tempo de início e aplicando o esquema antibiótico correspondente sem trocar os dois esquemas.
