# Diabetes mellitus gestacional

## Metadados

- Disciplina: EISA_II
- Especialidade: Endocrinologia
- Unidade: A_DEFINIR
- Prioridade: media
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B (tema sem camada A no acervo — `tem_camada_A: false`, `forca_fonte: fraca` no cluster)
- fonte_visual: não
- Fontes usadas: APOSTILA_SA_II_P7___e43cc7bc21 pp.185-186 (diagnóstico) e p.194 (insulinoterapia em gestante) — única fonte listada no cluster para este tema
- Evidência de prova/devolutiva: `cai: false` no cluster; risco clínico alto atribuído apesar da fraca cobertura de fonte — provável por ser tema de alto risco perinatal mesmo sem registro de cobrança recente.
- Limitações da fonte: esta é a única fonte do cluster para o tema, e ela é rasa neste ponto específico — cobre bem o diagnóstico e a insulinoterapia geral (com nota para gestante), mas NÃO traz na extração disponível: (1) os 3 valores de corte do TOTG 75g que definem DMG (jejum/1h/2h) — o texto menciona que o diagnóstico é fechado "quando no mínimo um dos valores a seguir está alterado" mas a tabela numérica não aparece no `.txt` (provável imagem/tabela perdida na extração); (2) metas glicêmicas específicas da gestação; (3) momento/via de parto. Os valores clássicos de IADPSG/OMS/FEBRASGO (jejum ≥92 · 1h ≥180 · 2h ≥153 mg/dL) são amplamente consolidados na literatura e foram incluídos abaixo rotulados como `conhecimento geral`, não como dado conferido nesta fonte — **confirmar no material de referência oficial da disciplina antes de usar em prova**.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES (ver pendências acima)

## Como cai

Vinheta de gestante na 1ª consulta de pré-natal com glicemia de jejum pedindo se já fecha DMG ou se precisa de TOTG entre 24-28 semanas. Caso de gestante que já preenche critério de DM franco (não DMG) na 1ª consulta, testando se o candidato troca os dois rótulos (e a implicação de risco teratogênico). Pergunta sobre qual insulina é a mais indicada/evitada na gestante e a dose inicial correta.

## Conceito operacional mínimo

DMG = diabetes com início OU diagnóstico durante o 2º/3º trimestre de gestação. Fisiopatologia: a gravidez gera resistência insulínica pela produção de lactogênio placentário. Corresponde a ~7% das gestações (até 20% por critérios HAPO). Aumenta morbimortalidade perinatal e o risco futuro de DM2 na mãe (10-63% em 5-16 anos) e nos filhos (DM2, dislipidemia, HAS) — mas, diferentemente da hiperglicemia franca na embriogênese (1º trimestre), a DMG NÃO aumenta risco de teratogênese.

## Pivô clínico

A variável que decide o fluxo diagnóstico é o valor da glicemia de jejum NA 1ª CONSULTA: se ≥92 mg/dL, o diagnóstico de DMG já está fechado, sem precisar de TOTG; só quando a GJ inicial for <92 mg/dL é que se solicita o TOTG 75g entre 24-28 semanas. E a variável que separa DMG de DM franco na gestação é a magnitude da glicemia/HbA1c na 1ª consulta — DM franco (GJ≥126, HbA1c≥6,5%, glicemia 2h≥200 no TOTG, ou aleatória≥200+sintomas) muda o rótulo e o risco (teratogênico), DMG não.

## Palavras-âncora

Lactogênio placentário; GJ≥92 na 1ª consulta = DMG fechado; TOTG 75g entre 24-28 semanas se GJ<92; DM franco x DMG (risco teratogênico só no franco/1º trimestre); Detemir (1ª escolha de basal na gestante); dose reduzida 0,2-0,3 UI/kg/dia na gestante.

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | GJ na 1ª consulta: ≥92 mg/dL já fecha DMG (sem TOTG); <92 mg/dL → TOTG 24-28 semanas | limiar | operacional | pedir TOTG em toda gestante independente da GJ inicial, ignorando que GJ≥92 já fecha o diagnóstico sozinha | fluxo de decisão fixo (GJ<92 → TOTG 24-28 sem; GJ≥92 → DMG fechado) treinado contra vinhetas com GJ variando ao redor de 92 |
| reconhecer diagnóstico | DM franco na 1ª consulta (GJ≥126, HbA1c≥6,5%, TOTG 2h≥200, aleatória≥200+sintomas) é rotulado "DM prévio/diagnosticado na gestação", NÃO "DMG" | valor | operacional | rotular qualquer diabetes identificado na gestação como "DMG", perdendo a distinção de risco teratogênico | card fixo contrastando os dois rótulos e a implicação (DM franco/1º tri = risco teratogênico; DMG/2º-3º tri = não aumenta teratogênese) |
| reconhecer contraindicação | insulinas com uso descrito em gestantes nesta fonte: Detemir (1ª escolha), NPH, Regular, Lispro, Aspart — Glargina e Glulisina não constam nessa lista | contraindicação | factual | escolher glargina como basal "padrão" na gestante por ser a mais usada na população geral | card fixo "gestante: Detemir 1ª escolha; NPH/Regular/Lispro/Aspart alternativas descritas" |
| aplicar critério / calcular | dose inicial de insulina reduzida na gestante (0,2-0,3 UI/kg/dia) x dose padrão do adulto (0,3-0,5 UI/kg/dia) | valor | operacional | aplicar a dose padrão do adulto à gestante, gerando dose inicial excessiva e risco de hipoglicemia | card de exceção "gestante/renal/puberdade/IMC baixo = dose menor (0,2-0,3), não a dose padrão" |
| priorizar / reconhecer risco | DMG aumenta risco de macrossomia e morbimortalidade perinatal, mas NÃO aumenta risco de malformação congênita (teratogênese) | fato | factual | aplicar o mesmo risco de malformação da hiperglicemia franca no 1º trimestre à DMG (2º/3º trimestre) | card de contraste DMG x DM pré-gestacional descompensado quanto ao risco teratogênico |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Definição de DMG | diabetes com início ou diagnóstico no 2º/3º trimestre de gestação | APOSTILA p.185 | CONFIRMADO |
| Prevalência | 7% de todas as gestações (critérios HAPO: até 20%) | APOSTILA p.185 | CONFIRMADO |
| Risco de DM2 futuro (mãe) | 10-63% em 5 a 16 anos após o parto | APOSTILA p.185 | CONFIRMADO |
| Risco teratogênico | DMG NÃO aumenta risco de teratogênese (diferente de hiperglicemia franca na embriogênese) | APOSTILA p.185 | CONFIRMADO |
| Rastreio na 1ª consulta | dosar GJ em todas as gestantes; DM franco se GJ≥126, TOTG 2h≥200, HbA1c≥6,5% ou glicemia aleatória≥200+sintomas (confirmar por repetição, exceto o critério de sintomas) | APOSTILA p.185 | CONFIRMADO |
| GJ≥92 na 1ª consulta (sem critério de DM franco) | diagnóstico de DMG fechado diretamente, sem necessidade de TOTG | APOSTILA p.185-186 | CONFIRMADO |
| GJ<92 na 1ª consulta | TOTG 75g de glicose anidra entre 24-28 semanas de gestação | APOSTILA p.186 | CONFIRMADO |
| Valores de corte do TOTG 75g para DMG (jejum/1h/2h) | jejum ≥92 · 1h ≥180 · 2h ≥153 mg/dL — 1 valor alterado já fecha diagnóstico | não encontrado no trecho extraído da apostila (tabela/imagem provavelmente perdida na extração) | AUSENTE_NA_FONTE — conhecimento geral (IADPSG/OMS/FEBRASGO); confirmar no material oficial antes de usar como dado decisivo em prova |
| Insulinas com uso descrito em gestante | Detemir (1ª escolha), NPH, Regular, Lispro, Aspart | APOSTILA p.194 | CONFIRMADO |
| Dose inicial de insulina em gestante | 0,2-0,3 UI/kg/dia (menor que a dose padrão do adulto, 0,3-0,5 UI/kg/dia) | APOSTILA p.194 | CONFIRMADO |
| Divisão da dose de NPH | 2/3 pela manhã + 1/3 à noite (bed time) | APOSTILA p.194 | CONFIRMADO |

## Pegadinhas

- GJ≥92 mg/dL na 1ª consulta JÁ fecha DMG — não é preciso esperar o TOTG de 24-28 semanas; o TOTG só é para quem tem GJ<92 inicial.
- DM identificado na 1ª consulta com critério de DM franco (GJ≥126, HbA1c≥6,5%) NÃO é "DMG" — é DM prévio/diagnosticado na gestação, com implicação de risco teratogênico diferente.
- DMG aumenta risco de macrossomia e morbimortalidade perinatal, mas NÃO aumenta risco de malformação congênita — essa é uma característica do DM pré-gestacional/franco descompensado no período de embriogênese (1º trimestre), não da DMG.
- Dose de insulina na gestante é MENOR que a dose padrão do adulto (0,2-0,3 x 0,3-0,5 UI/kg/dia) — usar a dose padrão pode gerar hipoglicemia.
- Detemir é a insulina basal de escolha citada especificamente para gestantes nesta fonte — não assumir que a basal "mais popular" (glargina) é automaticamente a preferida na gravidez.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Gestante com GJ 98 mg/dL na 1ª consulta → aguardar TOTG entre 24-28 semanas para fechar diagnóstico | TOTG "parece" sempre necessário para confirmar DM na gestação | fechamento tardio / pular etapa já resolvida | GJ≥92 na 1ª consulta já fecha DMG diretamente — não é preciso esperar o TOTG |
| Gestante com GJ 130 mg/dL na 1ª consulta → rotular como "DMG leve" | qualquer hiperglicemia na gravidez "parece" DMG | analogia sem validação funcional | GJ≥126 é critério de DM franco, não DMG — muda o rótulo e implica risco teratogênico (se a hiperglicemia já estava presente na embriogênese) |
| Gestante iniciando insulina → calcular a dose pela fórmula padrão do adulto (0,3-0,5 UI/kg/dia) | é a dose "geral" mais lembrada | valor errado por não checar a população especial | Gestante é situação especial com dose menor (0,2-0,3 UI/kg/dia) — dose padrão do adulto pode causar hipoglicemia |
| DMG diagnosticada no 2º trimestre → contar a mãe e a família que há risco aumentado de malformação fetal | "diabetes na gravidez = risco de malformação" é o reflexo mais comum | superextrapolação sem checar o momento da hiperglicemia | DMG (2º/3º trimestre, pós-embriogênese) não aumenta teratogênese — esse risco é do DM franco/pré-gestacional mal controlado no 1º trimestre |

## Conduta

- Inicial: dosar GJ em toda gestante na 1ª consulta de pré-natal; se critério de DM franco presente, rotular como DM prévio/diagnosticado na gestação (não DMG); se GJ≥92 sem critério de DM franco, fechar DMG diretamente.
- Se GJ<92 na 1ª consulta: TOTG 75g entre 24-28 semanas; DMG se algum valor alterado (ver pendência de valores de corte acima).
- Definitiva: MEV como base; insulina se necessário — Detemir como basal de escolha citada, NPH/Regular/Lispro/Aspart como alternativas descritas na fonte; dose inicial reduzida (0,2-0,3 UI/kg/dia).
- Condição da conduta: distinguir DMG de DM franco muda a orientação de risco teratogênico dada à paciente.
- O que mudaria a decisão: valor da GJ na 1ª consulta (abaixo/acima de 92 e de 126) muda todo o fluxo diagnóstico subsequente.

## Mini-casos ativos

Gestante de 10 semanas, GJ na 1ª consulta = 95 mg/dL, sem outros critérios de DM franco → variável decisiva: GJ≥92 → DMG fechado diretamente, sem necessidade de TOTG.

Gestante de 8 semanas, GJ na 1ª consulta = 128 mg/dL → variável decisiva: GJ≥126 → critério de DM franco, não DMG — rotular como DM prévio/diagnosticado na gestação, com implicação de risco teratogênico (hiperglicemia já presente na embriogênese).

Gestante de 26 semanas, GJ inicial havia sido 85 mg/dL (< 92), agora com TOTG 75g solicitado → variável decisiva: momento correto do exame (24-28 semanas, pela GJ inicial <92) → conduta already alinhada ao protocolo.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| GJ≥92 na 1ª consulta de pré-natal | DMG fechado, sem necessidade de TOTG | dado |
| GJ<92 na 1ª consulta | TOTG 75g entre 24-28 semanas | dado |
| GJ≥126 ou HbA1c≥6,5% na 1ª consulta | DM franco/prévio, NÃO DMG | pegadinha |
| DMG e risco teratogênico | DMG NÃO aumenta — só DM franco/1º trimestre aumenta | pegadinha |
| Insulina basal de escolha na gestante | Detemir | dado |
| Dose inicial de insulina na gestante | 0,2-0,3 UI/kg/dia (menor que a do adulto padrão) | pegadinha |

## Revisão

- Revisar quando: antes de vinheta com GJ na 1ª consulta de pré-natal, e antes de caso pedindo insulinização em gestante.
- Critério de parada: aplicar corretamente o fluxo GJ<92→TOTG / GJ≥92→DMG fechado / GJ≥126→DM franco em 3 casos seguidos sem confundir os rótulos.

## Pendência a confirmar

Os 3 valores de corte do TOTG 75g (jejum/1h/2h) que definem DMG entre 24-28 semanas não estão presentes no trecho extraído da única fonte deste tema. Antes de usar esse dado como decisivo em treino de questão, confirmar no material de referência oficial da disciplina (slide do professor, se existir, ou diretriz FEBRASGO/SBD citada em aula).
