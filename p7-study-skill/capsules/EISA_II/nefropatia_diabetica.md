# Nefropatia Diabética / Doença Renal do Diabetes

## Metadados

- Disciplina: EISA_II
- Especialidade: Nefrologia
- Unidade: III_UNIDADE
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não
- Fontes usadas: Doenc_a_renal_do_diabetes_III_unidade__a682b8eb7b (resumo de aula, 9p, autoria Karen F. S. O. G. Agra — "imagens retiradas dos slides do professor"); Nefro_NEFROPATIA_DIABE_TICA__01f9e16a5f (resumo de aula, 11p, autoria Edine Medeiros); APOSTILA_SA_II_P7___e43cc7bc21 (B)
- Evidência de prova/devolutiva: `cai: true`, prioridade alta, risco alto — tema com múltiplas variáveis numéricas (RAC, TFG por fármaco) que se encaixam no padrão geral mapeado em EISA II de "aplicar limiar numérico fora do contexto que o valida".
- Limitações da fonte: nenhuma das 2 fontes é slide do professor — ambas são resumos de aula de colegas de turma diferentes, uma delas declarando ter copiado imagens do slide original. Os 2 resumos convergem em praticamente todos os valores numéricos citados (RAC, epidemiologia, patologia), o que eleva a confiança apesar de nenhuma ser camada A.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

Vinheta de paciente diabético com albuminúria pedindo: (1) se o exame isolado já fecha o diagnóstico ou exige confirmação; (2) se um achado atípico deveria afastar a hipótese de doença renal do diabetes (DRD) e buscar outra causa; (3) qual hipoglicemiante pode/não pode ser usado dado a TFG do paciente; (4) a sequência correta de terapia nefroprotetora (IECA/BRA → SGLT2i → antagonista mineralocorticoide).

## Conceito operacional mínimo

DRD = doença renal crônica em paciente diabético definida por albuminúria (RAC ≥30mg/g, confirmada em 2 de 3 amostras) e/ou queda da TFG, com apresentação tipicamente insidiosa e assintomática até fases avançadas. É a causa mais comum de DRC nos EUA e a 1ª/2ª causa no Brasil (atrás ou ao lado da HAS). O diagnóstico é **clínico-epidemiológico** (diabético de longa data + perda lenta e progressiva de função) — biópsia não é necessária na apresentação típica.

## Pivô clínico

Um único exame de albuminúria positivo não fecha o diagnóstico — a regra é "2 de 3" amostras em 3–6 meses (falsos positivos por esforço físico, febre, ITU são comuns). Segundo pivô: nem toda proteinúria em diabético é DRD — sinais de alarme (proteinúria com <5 anos de diagnóstico, piora rápida apesar de IECA/BRA, cilindros hemáticos/leucocitúria/acantócitos, ausência de retinopatia em DM1) obrigam a investigar outra causa antes de rotular DRD.

## Palavras-âncora

RAC (relação albumina/creatinina); regra "2 de 3"; Kimmelstiel-Wilson (nodular); glomeruloesclerose difusa; hiperfiltração; declínio de 12mL/min/ano; TFG e fármaco (metformina <30; SGLT2 não iniciar <20 mas pode manter); dose máxima tolerada de IECA/BRA antes do SGLT2i; nunca IECA+BRA juntos; finerenona.

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | confirmação da albuminúria em 2 de 3 amostras (3–6 meses de intervalo) | limiar | operacional | fechamento precoce — fechar diagnóstico de DRD com 1 único exame de albuminúria positivo, sem repetir | script fixo "melhor de 3": 1º positivo não fecha nada; 2 positivos fecham sem precisar do 3º; 2 negativos encerram investigação |
| reconhecer diagnóstico | sinais de alarme que sugerem causa não-diabética apesar do DM (proteinúria precoce, piora rápida com IECA, cilindros hemáticos/leucocitúria/acantócitos, ausência de retinopatia em DM1) | sinal-achado | operacional | premissa não checada — assumir DRD só pela presença de diabetes, sem checar os sinais de alarme que apontam outra etiologia | checklist "quando suspeitar que NÃO é DRD" obrigatório antes de fechar o diagnóstico em qualquer vinheta de proteinúria + diabetes |
| aplicar critério | TFG como limiar de início x de manutenção de cada hipoglicemiante (ex.: SGLT2i não inicia se TFG<20, mas pode manter até a diálise se já em uso) | limiar | factual | valor errado — tratar o limiar de início e o de manutenção como se fossem o mesmo corte de TFG | tabela de duas colunas por fármaco (TFG mínima para iniciar x TFG mínima para manter), treinada separadamente |
| conduta / sequência | pré-requisito de dose máxima tolerada de IECA/BRA antes de iniciar SGLT2i; nunca associar IECA+BRA | sequência | operacional | perder a sequência — iniciar SGLT2i sem antes otimizar o IECA/BRA, ou empilhar IECA+BRA buscando duplo bloqueio do SRAA | script fixo da sequência terapêutica (IECA/BRA em dose máxima → SGLT2i → antagonista mineralocorticoide não esteroide) + regra fixa "nunca IECA+BRA" |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Posição epidemiológica da DRD | 1ª causa de DRC nos EUA; 1ª ou 2ª causa no Brasil (junto/atrás da HAS); >70% dos pacientes em diálise no Brasil são HAS+DM | Doenc_a_renal_do_diabetes p.1; Nefro_NEFROPATIA_DIABE p.1 | CONFIRMADO (2 fontes) |
| Prevalência de albuminúria aumentada | 34% dos pacientes com DM1 e 37% com DM2 | Doenc_a_renal_do_diabetes p.1; Nefro_NEFROPATIA_DIABE p.1 | CONFIRMADO (2 fontes, valores idênticos) |
| Categorias de RAC (ADA/KDIGO) | <30mg/g: normal; 30–300mg/g: aumentada (ex-"microalbuminúria"); >300mg/g: muito aumentada (ex-"macroalbuminúria") | Doenc_a_renal_do_diabetes p.1; Nefro_NEFROPATIA_DIABE p.1 | CONFIRMADO (2 fontes, valores idênticos) |
| Regra de confirmação da albuminúria | 2 de 3 amostras positivas (intervalo 3–6 meses); 1 exame isolado positivo não fecha diagnóstico | Doenc_a_renal_do_diabetes p.2 | CONFIRMADO |
| Início do rastreio | DM2: no momento do diagnóstico; DM1: 5 anos após o diagnóstico (ou antes, se descompensação); depois, anual | Doenc_a_renal_do_diabetes p.2 | CONFIRMADO |
| Achado histológico mais comum (menos específico) | Glomeruloesclerose difusa (expansão mesangial difusa) | Doenc_a_renal_do_diabetes p.2; Nefro_NEFROPATIA_DIABE p.2 | CONFIRMADO (2 fontes) |
| Achado histológico mais específico (menos comum) | Lesão de Kimmelstiel-Wilson (glomeruloesclerose nodular) — também vista em amiloidose (Congo+) e doença de depósito de cadeia leve (Congo-) | Doenc_a_renal_do_diabetes p.2; Nefro_NEFROPATIA_DIABE p.2 | CONFIRMADO (2 fontes) |
| Sinais de alarme contra DRD | Proteinúria com <5 anos de diagnóstico de DM; piora rápida de função apesar de IECA; cilindros hemáticos, leucocitúria, acantócitos no sumário de urina; ausência de retinopatia (não exclui, mas levanta suspeita, principalmente em DM1) | Doenc_a_renal_do_diabetes p.4 | CONFIRMADO |
| Proteinúria em DM2 por outra causa | 10–20% dos pacientes com DM2 e proteinúria têm lesão renal por outra patologia, não o diabetes | Doenc_a_renal_do_diabetes p.4; Nefro_NEFROPATIA_DIABE p.2 | CONFIRMADO (2 fontes) |
| Velocidade de progressão | Declínio fisiológico pós-40 anos: ~1mL/min/ano; na DRD: ~12mL/min/ano | Doenc_a_renal_do_diabetes p.4 | CONFIRMADO |
| Meta de HbA1c | <7% | Doenc_a_renal_do_diabetes p.5 | CONFIRMADO |
| Restrição proteica | 0,8–1g/kg/dia; evitar >1,3g/kg/dia (associado a mais albuminúria, queda mais rápida da TFG e maior mortalidade CV) | Doenc_a_renal_do_diabetes p.5 | CONFIRMADO |
| Restrição de sódio | ADA: <1.500mg Na/dia (3,75g sal); KDIGO: <2.000mg Na/dia (5g sal); evitar "sal light" (KCl) pelo risco de hipercalemia | Doenc_a_renal_do_diabetes p.6 | CONFIRMADO |
| Metformina por TFG | TFG >45: pode usar; 30–44: avaliar caso a caso; <30: não usar (risco de acidose lática) | Doenc_a_renal_do_diabetes p.6 | CONFIRMADO |
| SGLT2i (dapa/empaglifozina) por TFG | Iniciar só se TFG ≥20; se já em uso e TFG cair <20, pode manter até a diálise (nefroproteção é de longo prazo, não se inicia "tarde demais") | Doenc_a_renal_do_diabetes p.8 | CONFIRMADO |
| Pré-requisito para iniciar SGLT2i | Paciente já deve estar em dose máxima tolerada de IECA/BRA | Doenc_a_renal_do_diabetes p.8 | CONFIRMADO |
| Duplo bloqueio SRAA (IECA+BRA) | Não deve ser feito — não reduz proteinúria adicionalmente, aumenta efeitos colaterais e mortalidade | Doenc_a_renal_do_diabetes p.9 | CONFIRMADO |
| Indicação de IECA/BRA mesmo sem HAS | Diabético com PA normal (ex.: 120x80) e albuminúria confirmada (>30mg/g em 2 amostras) já deve receber IECA/BRA em dose máxima tolerada | Doenc_a_renal_do_diabetes p.9 | CONFIRMADO |
| Finerenona | Antagonista do receptor mineralocorticoide não esteroide; indicada em DM2 com albuminúria e alto risco CV; pode ser usada com TFG <25 e K <4,8 | Doenc_a_renal_do_diabetes p.9 | CONFIRMADO |
| Meta pressórica (ADA) | PA <140x90mmHg (geral); <130x80mmHg em jovens ou alto risco de AVC/DCV/proteinúria elevada | Doenc_a_renal_do_diabetes p.9 | CONFIRMADO |

## Pegadinhas

- Um exame de albuminúria positivo isolado não fecha DRD — falsos positivos ocorrem por esforço físico intenso, febre e ITU; é preciso confirmar 2 de 3 amostras.
- Diabetes de longa data não exclui investigar outra causa de proteinúria — 10–20% dos DM2 com proteinúria têm lesão renal por outra doença.
- Ausência de retinopatia diabética NÃO exclui DRD (embora deva levantar suspeita, sobretudo em DM1) — não é critério de exclusão absoluto.
- O corte de TFG para **iniciar** um SGLT2i (≥20) é diferente do corte para **manter** a droga (pode continuar mesmo com TFG<20, até a TRS) — tratar os dois como o mesmo valor é erro comum.
- IECA/BRA em diabético com albuminúria confirmada é indicado mesmo com PA normal — a indicação aqui é pela albuminúria, não pela hipertensão.
- Duplo bloqueio do SRAA (IECA+BRA) não é "mais proteção" — é conduta contraindicada, sem benefício adicional e com mais efeitos adversos.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Diabético com 1 exame de RAC = 45mg/g → já fechar diagnóstico de DRD e iniciar tratamento | Valor acima de 30 já parece "positivo" | fechamento precoce | Precisa de confirmação em 2 de 3 amostras antes de fechar o diagnóstico — 1 exame isolado pode ser falso positivo |
| Diabético há 20 anos, com proteinúria nova e cilindros hemáticos no sumário de urina → assumir progressão natural da DRD | Tempo longo de diabetes "explica" a proteinúria | premissa não checada | Cilindros hemáticos são sinal de alarme para OUTRA causa (ex.: glomerulonefrite) — não é o padrão esperado da DRD |
| Paciente com TFG 18mL/min, sem uso prévio de SGLT2i → iniciar dapaglifozina agora, já que "é nefroprotetor" | SGLT2i é lembrado como sempre benéfico na DRD | valor errado | Abaixo de TFG 20, SGLT2i não deve ser **iniciado** (só mantido se já em uso) — iniciar tarde demais não traz o benefício esperado |
| Diabético com albuminúria confirmada e função renal em franca queda apesar do IECA em dose máxima → associar um BRA para reforçar o bloqueio do SRAA | "Reforçar o mesmo mecanismo" parece lógico para mais proteção | perder a sequência | Duplo bloqueio IECA+BRA é contraindicado — não reduz mais a proteinúria e aumenta risco (hipercalemia, mortalidade) |

## Conduta

- Inicial: rastrear com RAC (DM2 ao diagnóstico; DM1 aos 5 anos) + creatinina/TFG anualmente; confirmar albuminúria em 2 de 3 amostras antes de rotular DRD; checar sinais de alarme para outra etiologia.
- Definitiva: IECA/BRA em dose máxima tolerada (mesmo sem HAS, se albuminúria confirmada) → associar SGLT2i (se TFG≥20 para iniciar) → associar finerenona se albuminúria persistente e alto risco CV (TFG≥25, K<4,8); controle glicêmico intensificado (HbA1c<7%) com ajuste de hipoglicemiante pela TFG; restrição proteica moderada (0,8–1g/kg/dia) e de sódio.
- Condição da conduta: TFG muda a escolha do hipoglicemiante (metformina até 30; SGLT2i até 20 para iniciar, sem limite inferior para manter); nunca associar IECA+BRA.
- Diferencial perigoso: sinais de alarme (proteinúria precoce, cilindros hemáticos, piora rápida com IECA) obrigam investigação de causa não-diabética, inclusive biópsia se necessário.
- O que mudaria a decisão: confirmação em 2ª amostra muda de "observar" para "tratar"; queda de TFG<20 muda a estratégia de SGLT2i de "pode iniciar" para "só mantém se já em uso".

## Mini-casos ativos

Diabético tipo 2, RAC de 55mg/g em amostra única, sem exame prévio. Variável decisiva: exame único → repetir em 3–6 meses antes de fechar DRD, não iniciar tratamento definitivo ainda.

Diabético tipo 1 há 8 anos, proteinúria nova, cilindros hemáticos e leucocitúria no sumário de urina. Variável decisiva: sinais de alarme presentes → investigar outra causa (ex.: glomerulonefrite), não assumir DRD.

Diabético tipo 2, TFG 22mL/min, ainda não usa SGLT2i, IECA em dose máxima tolerada. Variável decisiva: TFG≥20 → pode iniciar SGLT2i agora, respeitando o pré-requisito do IECA já otimizado.

Mesmo paciente 1 ano depois, já em uso de SGLT2i, TFG caiu para 15mL/min. Variável decisiva: droga já em uso → manter até a diálise, não suspender por TFG baixa.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Regra de confirmação da albuminúria | 2 de 3 amostras positivas, 3–6 meses de intervalo | sequência |
| Achado histológico mais específico da DRD | Lesão de Kimmelstiel-Wilson (nodular) | dado |
| Sinais de alarme contra DRD | Proteinúria <5 anos de DM, piora rápida com IECA, cilindros hemáticos/leucocitúria/acantócitos | pegadinha |
| Metformina — limite de TFG | Não usar se TFG <30 | limiar |
| SGLT2i — iniciar x manter | Iniciar só se TFG≥20; manter mesmo com TFG<20 até a diálise | pegadinha |
| Pré-requisito para SGLT2i | Dose máxima tolerada de IECA/BRA já em uso | sequência |
| IECA+BRA associados | Contraindicado — sem benefício extra, mais efeito adverso | pegadinha |
| Indicação de IECA/BRA sem HAS | Albuminúria confirmada >30mg/g em 2 amostras já indica, mesmo com PA normal | dado |
| Velocidade de declínio da TFG na DRD | ~12mL/min/ano (vs. ~1mL/min/ano fisiológico pós-40a) | dado |

## Revisão

- Revisar quando: antes de vinheta com diabético e albuminúria/proteinúria, ou pedindo ajuste de hipoglicemiante pela função renal.
- Critério de parada: aplicar corretamente a regra "2 de 3" e reconhecer 3 sinais de alarme contra DRD em casos seguidos, sem confundir o corte de início x manutenção do SGLT2i.
