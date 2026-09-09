# Amostra manual de identidade documental

VERIFICADO em 2026-09-08T13:59:14.204178+00:00. Commit de origem DOCUMENTADO: `b0a9f23091e0cb92e97829e4d9d30fc05f51cf48`; HEAD medido indisponível. Código SHA-256 `2a3c748c9e6466fc1f8617c72fe1b6dae6a4cb7f44d7133e619d0e713f07b00c`. Manifesto SHA-256 `3b5fd6c8d9933e6e42fe2d2f0859b60e0cd3cb88a6c0d9b6e08c68305f00b641`.

Revisor: `agent:/root/final_verifier`. Revisão lexical individual, sem leitura de páginas originais e sem assinatura clínica humana.

VERIFICADO: 20/20 vínculos amostrados lexicalmente compatíveis: 5 controles exact existentes + 10 novos stem + 0 folded + 5 novos placeholder. As 5 linhas placeholder referem-se a um único DOCX em duas cápsulas.

PENDÊNCIA: critério original de 5 amostras reais por nível NÃO ATENDIDO. Não há linhas resolved:folded no conjunto reparado. Fixtures sintéticas L2 estão nos testes adversariais e não integram esta amostra. L0 foi preservado, portanto seus controles não são novos matches.

Limite: resolved identifica a melhor candidata documental da célula, não completude de todas as citações, nem confirmação clínica. Em células com várias citações, as demais menções podem continuar sem vínculo. Nenhum PDF/PPTX/DOCX original foi lido nesta revisão.

## 01 — resolved:exact

Cápsula `capsules/EISCA/cardiopatias_congenitas.md`, linha de seção `4`.

Célula/linha literal: Incidência de cardiopatia congênita | 8 a cada 1.000 nascidos vivos | AtualizeA5N6__cd97472180 p.4 | CONFIRMADO

Manifesto:

- `AtualizeA5N6__cd97472180` → `EISCA - Ensino Integrado em Saúde da Criança e Adolescente\Slides Aulas\AtualizeA5N6.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** ID completo AtualizeA5N6__cd97472180 literal; o manifesto aponta AtualizeA5N6.pdf em Slides Aulas/EISCA. Controle legado exato; p.4 não lida.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 02 — resolved:exact

Cápsula `capsules/EISCA/neuroblastoma.md`, linha de seção `4`.

Célula/linha literal: % das neoplasias malignas pediátricas | 8–10% | Neuroblastoma__c984597fac p.4 | CONFIRMADO

Manifesto:

- `Neuroblastoma__c984597fac` → `EISCA - Ensino Integrado em Saúde da Criança e Adolescente\Slides Aulas\Slides Segunda Prova \Neuroblastoma.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** ID completo Neuroblastoma__c984597fac literal identifica o slide EISCA/Slides Segunda Prova, não o resumo homônimo. Controle legado; p.4 não lida.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 03 — resolved:exact

Cápsula `capsules/EISCA/neuroblastoma.md`, linha de seção `15`.

Célula/linha literal: Estadiamento (INSS) — estádio 1/2/3/4/4S | 15% / 5% / 29% / 46% / 5% | Neuroblastoma__c984597fac p.21; Neuroblastoma__97ea516ab3 p.3 | CONFIRMADO (cruzado A×B, valores idênticos)

Manifesto:

- `Neuroblastoma__97ea516ab3` → `EISA II - Ensino Integrado em Saúde do Adulto II\NEUROLOGIA\Resumos\Neuroblastoma.pdf`

- `Neuroblastoma__c984597fac` → `EISCA - Ensino Integrado em Saúde da Criança e Adolescente\Slides Aulas\Slides Segunda Prova \Neuroblastoma.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** Dois IDs completos distintos aparecem separados por ponto e vírgula: c984597fac é o slide pediátrico, 97ea516ab3 é o resumo em EISA II/NEUROLOGIA. Ambos preservados; p.21 e p.3 não lidas.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 04 — resolved:exact

Cápsula `capsules/EISCA/neuroblastoma.md`, linha de seção `16`.

Célula/linha literal: Estádio 4S — definição do corte de MO | disseminação limitada a fígado, pele e/ou MO em criança <1 ano, com MO comprometida ATÉ 10%; acima disso já é estádio 4 | Neuroblastoma__97ea516ab3 p.3 | CONFIRMADO

Manifesto:

- `Neuroblastoma__97ea516ab3` → `EISA II - Ensino Integrado em Saúde do Adulto II\NEUROLOGIA\Resumos\Neuroblastoma.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** ID completo Neuroblastoma__97ea516ab3 identifica exclusivamente o resumo EISA II/NEUROLOGIA, apesar do título compartilhado com o slide. Controle legado; p.3 não lida.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 05 — resolved:exact

Cápsula `capsules/EISCA/osteossarcoma.md`, linha de seção `4`.

Célula/linha literal: Pico de incidência | 13–16 anos (2 fontes convergem em "13 a 16" e "14 e 16"; tratado como faixa de adolescência, estirão de crescimento) | osteossarcoma__ad984b30b6 p.1; 1_Osteossarcoma__da1747531d p.1 | CONFIRMADO_COM_CORREÇÕES (pequena divergência de 1 ano no limite inferior entre as 2 fontes B — sem A para arbitrar; registrada)

Manifesto:

- `1_Osteossarcoma__da1747531d` → `EISCA - Ensino Integrado em Saúde da Criança e Adolescente\Resumos\1-Osteossarcoma.pdf`

- `osteossarcoma__ad984b30b6` → `EISCA - Ensino Integrado em Saúde da Criança e Adolescente\Resumos\osteossarcoma.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** Dois IDs completos identificam dois PDFs de resumo distintos: 1-Osteossarcoma.pdf e osteossarcoma.pdf. Citações explícitas múltiplas preservadas; divergência já textual não arbitrada.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 06 — resolved:stem

Cápsula `capsules/CASOS_CLINICOS/abordagem_a_dispneia.md`, linha de seção `4`.

Célula/linha literal: Causas de dispneia aguda | asma brônquica; inalação de corpo estranho; pneumotórax; embolia pulmonar; isquemia/IAM; ICC descompensada; TAG (crise de ansiedade); paralisia diafragmática | CASOS_CL_NICOS_RESUMO p.1 | CONFIRMADO

Manifesto:

- `CASOS_CL_NICOS_RESUMO__249c11a613` → `CASOS CLÍNICOS\CASOS CLÍNICOS RESUMO.docx`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** CASOS_CL_NICOS_RESUMO coincide literalmente com o stem do ID e o manifesto o liga a CASOS CLÍNICOS RESUMO.docx. A corrupção já está nos dois textos; L1 é suficiente. p.1 não lida.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 07 — resolved:stem

Cápsula `capsules/CASOS_CLINICOS/abordagem_diarreia_aguda_cronica.md`, linha de seção `4`.

Célula/linha literal: Definição de diarreia | frequência aumentada ou fezes amolecidas, massa >200g/dia | CASOS_CLINICOS_RESUMO; Casos_Clinicos_P7_1 p.5; Abordagem_a_s_diarreias p.1 | CONFIRMADO

Manifesto:

- `Abordagem_a_s_diarreias__41fb86fd8c` → `CASOS CLÍNICOS\Slides Aulas \Abordagem às diarreias.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** Abordagem_a_s_diarreias é stem literal do PDF Abordagem às diarreias.pdf. As outras duas menções não foram consideradas confirmação: prevalece apenas a candidata mais exata; vínculo parcial declarado.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 08 — resolved:stem

Cápsula `capsules/CASOS_CLINICOS/hemorragia_subaracnoide_hipertensao_intracraniana.md`, linha de seção `8`.

Célula/linha literal: Apresentação clássica de HSA | cefaleia thunderclap ("pior dor da vida"), síncope, vômito "em jato", rigidez de nuca, ausência de febre, rebaixamento do nível de consciência | FACILITA_OSCE l.166-175; OSCE_NEUROLOGIA l.360-368 | CONFIRMADO

Manifesto:

- `OSCE_NEUROLOGIA__2cfa60427a` → `OSCE P7\OSCE - NEUROLOGIA.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** OSCE_NEUROLOGIA é stem literal de OSCE - NEUROLOGIA.pdf, no segundo segmento da fonte. FACILITA_OSCE não foi resolvido. Localizador textual l.360-368 não foi verificado no PDF.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 09 — resolved:stem

Cápsula `capsules/EISA_II/avaliacao_laboratorial_em_nefrologia.md`, linha de seção `4`.

Célula/linha literal: Fases da urinálise | Exame físico/visual → químico → microscópico (sedimento) | DIAG_SIND_DIAG_LAB_2024_2 p.45 região; slide 6 (2021.2) | CONFIRMADO

Manifesto:

- `DIAG_SIND_DIAG_LAB_2024_2__048561d4fc` → `EISA II - Ensino Integrado em Saúde do Adulto II\NEFROLOGIA\Slides Aulas\Slides Primeira Prova \DIAG SIND + DIAG LAB 2024.2.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** DIAG_SIND_DIAG_LAB_2024_2 é stem literal do arquivo DIAG SIND + DIAG LAB 2024.2.pdf. Versão 2024.2 integra o nome; a menção adicional a 2021.2 não foi promovida a outra fonte.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 10 — resolved:stem

Cápsula `capsules/EISA_II/avaliacao_laboratorial_em_nefrologia.md`, linha de seção `11`.

Célula/linha literal: Divergência de densidade | Slide de 2021.2 (mesma professora) traz 1,003–1,030; resumo B cita faixa "típica" 1,015–1,025 com hiperdiluição <1,003 e glicosúria >1,032 | AVALIAC_A_O_LABORATORIAL_EM_NEFROLOGIA slide 11 (2021.2); resumo Elvis | registrado — prevalece a versão A mais recente (2024.2); se a questão citar literalmente o slide antigo, considerar 1,003–1,030

Manifesto:

- `AVALIAC_A_O_LABORATORIAL_EM_NEFROLOGIA__4419b29eb0` → `EISA II - Ensino Integrado em Saúde do Adulto II\NEFROLOGIA\Slides Aulas\Slides Primeira Prova \AVALIAÇÃO LABORATORIAL EM NEFROLOGIA.pptx`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** AVALIAC_A_O_LABORATORIAL_EM_NEFROLOGIA corresponde literalmente ao stem do PPTX AVALIAÇÃO LABORATORIAL EM NEFROLOGIA.pptx. Slide11 é apenas localizador herdado; resumo Elvis segue sem vínculo.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 11 — resolved:stem

Cápsula `capsules/EISA_II/bexiga_neurogenica.md`, linha de seção `4`.

Célula/linha literal: Inervação vesical | Parassimpático (plexo pélvico, M3, acetilcolina) = contração/esvaziamento; Simpático (plexo hipogástrico, alfa=contrai colo, beta=relaxa corpo) = armazenamento; Esfíncter = somática, n. pudendo | slide p.1-2; Bexiga_neuroge_nica p.1 | CONFIRMADO

Manifesto:

- `Bexiga_neuroge_nica__d255c01ebc` → `EISA II - Ensino Integrado em Saúde do Adulto II\UROLOGIA\Resumos\Bexiga neurogênica.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** Bexiga_neuroge_nica é stem literal de Bexiga neurogênica.pdf em UROLOGIA/Resumos. O prefixo genérico slide p.1-2 não conta como identificação documental.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 12 — resolved:stem

Cápsula `capsules/EISA_II/bexiga_neurogenica.md`, linha de seção `6`.

Célula/linha literal: Causas mais citadas | AVC isquêmico, TRM, disrafismo oculto (na criança: meningomielocele é a mais comum), Alzheimer, tumor craniano, metástase óssea | slide p.3; Uro_BEXIGA_NEUROGA_NICA p.1; APOSTILA p.153 | CONFIRMADO

Manifesto:

- `Uro_BEXIGA_NEUROGA_NICA__6bd4d01ade` → `EISA II - Ensino Integrado em Saúde do Adulto II\UROLOGIA\Resumos\Uro - BEXIGA NEUROGÃ_NICA.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** Uro_BEXIGA_NEUROGA_NICA é stem literal de Uro - BEXIGA NEUROGÃ_NICA.pdf no manifesto. Mantida a grafia peculiar do arquivo; não confundido com Bexiga neurogênica.pdf. APOSTILA não foi vinculada.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 13 — resolved:stem

Cápsula `capsules/EISA_II/cancer_de_prostata.md`, linha de seção `5`.

Célula/linha literal: Cinética de PSA em uso de testosterona exógena | Tolera-se subida de até 1,4 ng/ml/ano (testosterona é hiperplasiante) | ANOTAC_O_ES_ca_ncer_de_pro_stata p.1 | CONFIRMADO (só 1 fonte B; confirmar no slide)

Manifesto:

- `ANOTAC_O_ES_ca_ncer_de_pro_stata__6614a32c87` → `Resumos das Unidades \SAÚDE DO ADULTO II\III UNIDADE\Urologia\ANOTAÇÕES - câncer de próstata.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** ANOTAC_O_ES_ca_ncer_de_pro_stata é stem literal do PDF ANOTAÇÕES - câncer de próstata.pdf em Resumos das Unidades. Registro não confirma o valor clínico nem a página1.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 14 — resolved:stem

Cápsula `capsules/EISA_II/cancer_de_prostata.md`, linha de seção `10`.

Célula/linha literal: Antibioticoprofilaxia pré-biópsia | Levofloxacino 500mg — 1cp na noite anterior, 1cp na noite da biópsia, 1cp na noite posterior (3 doses) | Urologia_CA_NCER_DE_PRO_STATA p.4-5 | CONFIRMADO (só fontes B; confirmar no slide)

Manifesto:

- `Urologia_CA_NCER_DE_PRO_STATA__ec4ee2ece9` → `EISA II - Ensino Integrado em Saúde do Adulto II\UROLOGIA\Resumos\Urologia - CÂNCER DE PRÓSTATA.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** Urologia_CA_NCER_DE_PRO_STATA é stem literal de Urologia - CÂNCER DE PRÓSTATA.pdf, distinto do resumo ANOTAÇÕES. O vínculo lexical não valida o regime terapêutico transcrito.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 15 — resolved:stem

Cápsula `capsules/EISA_II/cancer_de_testiculo.md`, linha de seção `5`.

Célula/linha literal: Tipos histológicos | 90-95% são tumores de células germinativas (seminomas e não seminomas); seminoma é o mais comum (50%) | Urologia_CA_NCER_DE_TESTI_CULO p.1; Onco_NEOPLASIAS p.4 | CONFIRMADO

Manifesto:

- `Urologia_CA_NCER_DE_TESTI_CULO__2d3b7d9fc1` → `EISA II - Ensino Integrado em Saúde do Adulto II\UROLOGIA\Resumos\Urologia - CÂNCER DE TESTÍCULO.pdf`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** Urologia_CA_NCER_DE_TESTI_CULO é stem literal de Urologia - CÂNCER DE TESTÍCULO.pdf. Onco_NEOPLASIAS não foi resolvido; vínculo parcial explícito, sem confirmação da histologia.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 16 — resolved:placeholder

Cápsula `capsules/CASOS_CLINICOS/abordagem_diarreia_aguda_cronica.md`, linha de seção `5`.

Célula/linha literal: Diarreia aguda | duração <14 dias | CASOS_CLINICOS_RESUMO; Casos_Clinicos_P7_1 p.5 | CONFIRMADO

Manifesto:

- `CASOS_CL_NICOS_RESUMO__249c11a613` → `CASOS CLÍNICOS\CASOS CLÍNICOS RESUMO.docx`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** CASOS_CLINICOS_RESUMO difere de CASOS_CL_NICOS_RESUMO em uma posição (I versus _). O manifesto aponta CASOS CLÍNICOS RESUMO.docx; compatibilidade lexical L3. Casos_Clinicos_P7_1 não foi resolvido.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 17 — resolved:placeholder

Cápsula `capsules/CASOS_CLINICOS/abordagem_diarreia_aguda_cronica.md`, linha de seção `15`.

Célula/linha literal: Indicação de exames na diarreia aguda | diarreia sanguinolenta, febre>38,5°C, >6 dejeções/dia, duração>48h, dor abdominal severa, idosos/imunodeprimidos | CASOS_CLINICOS_RESUMO | CONFIRMADO

Manifesto:

- `CASOS_CL_NICOS_RESUMO__249c11a613` → `CASOS CLÍNICOS\CASOS CLÍNICOS RESUMO.docx`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** CASOS_CLINICOS_RESUMO isolado preenche exatamente um placeholder em CL_NICOS; demais caracteres coincidem. Mesmo DOCX do manifesto, sem concorrente L3 observado. Critérios clínicos não verificados.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 18 — resolved:placeholder

Cápsula `capsules/CASOS_CLINICOS/abordagem_diarreia_aguda_cronica.md`, linha de seção `16`.

Célula/linha literal: ATB empírico na diarreia aguda | quinolona oral (ciprofloxacino 500mg 12/12h ou levofloxacino 500mg/dia) 3-5 dias, só nos casos graves | CASOS_CLINICOS_RESUMO | CONFIRMADO

Manifesto:

- `CASOS_CL_NICOS_RESUMO__249c11a613` → `CASOS CLÍNICOS\CASOS CLÍNICOS RESUMO.docx`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** CASOS_CLINICOS_RESUMO isolado possui o mesmo alinhamento de um caractere que a amostra anterior; a dose no enunciado não participa do matching. Validade terapêutica permanece não avaliada.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 19 — resolved:placeholder

Cápsula `capsules/CASOS_CLINICOS/cirrose_hepatica_ascite_pbe.md`, linha de seção `4`.

Célula/linha literal: GASA transudato (hipertensão porta) | ≥1,1 g/dL | Casos_Clinicos_P7_1 p.3; CASOS_CLINICOS_RESUMO | CONFIRMADO

Manifesto:

- `CASOS_CL_NICOS_RESUMO__249c11a613` → `CASOS CLÍNICOS\CASOS CLÍNICOS RESUMO.docx`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** No segundo segmento, CASOS_CLINICOS_RESUMO preenche I no placeholder de CL_NICOS. Casos_Clinicos_P7_1 p.3 fica sem vínculo. Documento escolhido é DOCX, não um PDF presumido.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.

## 20 — resolved:placeholder

Cápsula `capsules/CASOS_CLINICOS/cirrose_hepatica_ascite_pbe.md`, linha de seção `7`.

Célula/linha literal: PBE — critério diagnóstico | PMN ≥250/mm³ no líquido ascítico, cultura monobacteriana | Casos_Clinicos_P7_1 p.3, p.18; CASOS_CLINICOS_RESUMO | CONFIRMADO

Manifesto:

- `CASOS_CL_NICOS_RESUMO__249c11a613` → `CASOS CLÍNICOS\CASOS CLÍNICOS RESUMO.docx`

**VERIFICADO — PASS_LEXICAL_IDENTITY_ONLY:** CASOS_CLINICOS_RESUMO no segundo segmento corresponde pelo mesmo placeholder; Casos_Clinicos_P7_1 p.3,p.18 não foi vinculado. Esta quinta linha L3 repete documento e mecanismo, não amplia diversidade documental.

**PENDÊNCIA:** sustentação clínica pela página não avaliada; fonte primária indisponível.
