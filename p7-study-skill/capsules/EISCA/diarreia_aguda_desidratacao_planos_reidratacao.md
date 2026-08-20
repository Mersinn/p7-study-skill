# Diarreia aguda, desidratação e terapia de reidratação (Planos A, B e C)

## Metadados

- Disciplina: EISCA
- Especialidade: Gastroenterologia pediátrica
- Unidade: I
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: A
- fonte_visual: sim (`diarreia_e_DHE__35f8e57446` pp. 3, 4, 6, 16, 17, 19, 20, 21, 22, 23, 24)
- Fontes usadas: "Diarreias na Infância" — slide fotografado da profa. Dra. Liane Carvalho Viana (camada A, MISTA/imagem, 41 pp., incluindo tabela do MS 2023 e recomendação do Ministério da Saúde para Plano C)
- Evidência de prova/devolutiva: Devolutiva III SC 2016.1 (Q8 — ≥2 sinais de desidratação classificam como desidratado mesmo com achado tranquilizador coexistente); Integradas — "Gastro — diarreia aguda, etiologia e cronicidade"; banco EISCA lista "AIDPI — classificação de desidratação por contagem" e "Falha da TRO — indicação de via venosa" como itens dissecados
- Limitações da fonte: slide fotografado (MISTA) com 41 páginas, revisado por amostragem estratégica (~11 páginas focadas em definição, classificação, planos A/B/C e tabela de expansão) — não lido página a página; etiologia infecciosa detalhada (rotavírus, agentes bacterianos específicos) não foi revisada nesta amostra e fica fora do escopo desta cápsula
- Verificação nível 1: CONFIRMADO
- Revisão independente L2 (2026-08-20): texto integral extraído (PyMuPDF) de "Diarreia Aguda Infecciosa" (SBP, Depto. Científico de Gastroenterologia, 2022-2024), que reproduz e cita diretamente BRASIL/MS/SVSA "Manejo do paciente com diarreia" (2023); e do protocolo municipal "Doenças Diarreicas Agudas (DDA) na Criança" (Rio de Janeiro, PTC.DEA.005, 09/2025). Confirmado: definição de diarreia, cortes de duração, Plano B (50-100 mL/kg em 4-6h, falha em 6h), Plano C (30+70 mL/kg por faixa etária, RN/cardiopata grave 10 mL/kg), zinco por idade, ondansetrona por idade/peso. **Corrigido nesta revisão**: o sinal com asterisco do domínio "sede" na classificação de gravidade era descrito como "sede ausente/bebe pouco" — o documento primário registra "incapaz de ingerir líquidos/beber"; e a duração do zinco era fixa em "14 dias" — o documento primário registra intervalo "10 a 14 dias". Ver `registry/clinical_claims.jsonl` para claim_ids e locators completos.

## Como cai

Cai fortemente como classificação do grau de desidratação pela CONTAGEM de sinais (≥2 sinais = algum grau; ≥2 sinais incluindo pelo menos 1 com asterisco = grave) — não pela impressão clínica global, mesmo quando um sinal tranquilizador (ex. lágrimas presentes) coexiste com sinais de alarme. Cobra também o escalonamento estrito dos planos (nunca pular direto para C sem esgotar B) e as doses por peso/idade de SRO, zinco e expansão venosa — variáveis clássicas do tipo `valor` e `sequencia`.

## Conceito operacional mínimo

Diarreia = ≥3 evacuações amolecidas/líquidas em 24h (percepção materna é considerada confiável, mais que a frequência habitual em criança em LME). Classificação por duração (OMS): aguda ≤14 dias; disenteria = aguda com sangue; persistente >14 dias. Classificação do estado de hidratação (MS 2023) por CONTAGEM de sinais: hidratado (nenhum sinal alterado); algum grau de desidratação (≥2 sinais alterados); desidratação grave (≥2 sinais alterados, sendo pelo menos 1 marcado com asterisco — incapaz de ingerir líquidos, pulsos fracos/ausentes, sensório letárgico/comatoso). Conduta = 3 planos escalonados: A (domiciliar, prevenção), B (unidade de saúde, TRO supervisionada), C (hospitalar, reidratação venosa).

## Pivô clínico

O pivô é a CONTAGEM OBJETIVA de sinais segundo o critério do MS, não a impressão clínica global — a presença de um sinal tranquilizador (ex. lágrimas presentes) NÃO neutraliza a contagem de sinais de alarme já presentes. Segundo pivô: cada plano tem critério de ENTRADA e de FALHA próprios — Plano C não é escolhido pela "gravidade que parece", mas por critérios objetivos (perda >10% do peso, contraindicação de TRO, choque, vômitos biliosos/incontroláveis, falha comprovada da TRO).

## Palavras-âncora

3+ evacuações amolecidas/líquidas em 24h · disenteria = diarreia com sangue · desidratação grave = ≥2 sinais com 1 asterisco (incapaz de beber, pulsos fracos, sensório alterado) · Plano A domiciliar · Plano B unidade de saúde (50-100 mL/kg em 4-6h) · Plano C hospitalar (expansão 30 mL/kg + 70 mL/kg) · zinco 10-14 dias · ondansetrona por peso/idade · sinais de alarme (sangue nas fezes, recusa alimentar, oligúria).

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | classificação de desidratação por CONTAGEM de ≥2 sinais (grave = ≥2 com 1 asterisco) | limiar | operacional | narrativa acima do discriminador (neutraliza sinais de alarme com achado tranquilizador coexistente) | treinar contagem explícita de sinais positivos/negativos segundo a tabela MS antes de julgar gravidade global |
| conduta definitiva | plano C: perda de peso >10%, contraindicação de TRO, choque, vômitos biliosos/incontroláveis, ou falha da TRO | limiar | operacional | definitiva antes da inicial (pula para EV sem esgotar TRO supervisionada) | checklist das 5 indicações de Plano C, treinado com casos-par (falha documentada × ainda dentro do prazo de B) |
| conduta definitiva | Plano C: expansão 30 mL/kg + 70 mL/kg, tempo dobrado em <1 ano vs ≥1 ano | sequencia | operacional | valor errado (troca volume ou tempo entre as faixas etárias) | tabela fixa idade → volume → tempo, treinada com 4 casos variando só a idade |
| conduta inicial | SRO após cada evacuação: 50-100 mL (<1 ano), 100-200 mL (1-10 anos), livre demanda (>10 anos) | valor | factual | valor errado (troca as faixas etárias) | flashcard de 3 faixas etárias × volume de SRO |
| priorizar emergência | falha da TRO após 6h ou sinais de piora = evolução para hospital/Plano C | limiar | operacional | fechamento precoce (insiste em manter Plano B além do prazo definido) | regra fixa: reavaliar em 4-6h; se sem melhora, escalar — não prolongar TRO indefinidamente |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Definição de diarreia | ≥3 evacuações amolecidas ou líquidas em 24h | Diarreias na Infância (slide Liane Viana), p.3 | CONFIRMADO |
| Diarreia aguda — duração | até 14 dias | Diarreias na Infância (slide Liane Viana), p.6 | CONFIRMADO |
| Diarreia persistente — duração | superior a 14 dias | Diarreias na Infância (slide Liane Viana), p.6 | CONFIRMADO |
| Desidratação grave — déficit de peso | acima de 10% | Diarreias na Infância (slide Liane Viana), p.17 (tabela MS 2023) | CONFIRMADO |
| Algum grau de desidratação — déficit de peso | até 10% | Diarreias na Infância (slide Liane Viana), p.17 | CONFIRMADO |
| Critério de desidratação grave | ≥2 sinais alterados, incluindo ao menos 1 sinal com asterisco (incapaz de ingerir líquidos, pulsos fracos/ausentes, sensório letárgico/comatoso/inconsciente) | Diarreias na Infância (slide Liane Viana), p.17 (tabela MS 2023) | CONFIRMADO |
| Plano A — SRO por evacuação, <1 ano | 50-100 mL | Diarreias na Infância (slide Liane Viana), p.20 | CONFIRMADO |
| Plano A — SRO por evacuação, 1-10 anos | 100-200 mL | Diarreias na Infância (slide Liane Viana), p.20 | CONFIRMADO |
| Plano A — suplementação de zinco, <6 meses | 10 mg/dia (2,5 mL) por 10-14 dias | Diarreias na Infância (slide Liane Viana), p.20 | CONFIRMADO |
| Plano A — suplementação de zinco, ≥6 meses | 20 mg/dia (5 mL) por 10-14 dias | Diarreias na Infância (slide Liane Viana), p.20 | CONFIRMADO |
| Plano B — volume orientação inicial | 50-100 mL/kg administrado entre 4-6h | Diarreias na Infância (slide Liane Viana), p.22 | CONFIRMADO |
| Plano B — SOG se vômitos persistentes | 20 mL/kg/h | Diarreias na Infância (slide Liane Viana), p.22 | CONFIRMADO |
| Plano B — ondansetrona, 6-24 meses | 2 mg (0,2-0,4 mg/kg) | Diarreias na Infância (slide Liane Viana), p.22 | CONFIRMADO |
| Plano B — ondansetrona, 2-10 anos | 4 mg | Diarreias na Infância (slide Liane Viana), p.22 | CONFIRMADO |
| Plano B — ondansetrona, >10 anos | 8 mg | Diarreias na Infância (slide Liane Viana), p.22 | CONFIRMADO |
| Plano B — reavaliação de falha | sem melhora após 6h → encaminhar para internação | Diarreias na Infância (slide Liane Viana), p.22 | CONFIRMADO |
| Plano C — expansão <1 ano | 30 mL/kg em 1h + 70 mL/kg em 5h (SF 0,9% ou Ringer lactato) | Diarreias na Infância (slide Liane Viana), p.24 (recomendação MS) | CONFIRMADO |
| Plano C — expansão ≥1 ano | 30 mL/kg em 30 min + 70 mL/kg em 2h30 (SF 0,9% ou Ringer lactato) | Diarreias na Infância (slide Liane Viana), p.24 (recomendação MS) | CONFIRMADO |
| Plano C — RN e cardiopata grave | expansão com 10 mL/kg em 30 min | Diarreias na Infância (slide Liane Viana), p.24 | CONFIRMADO |
| Plano C — indicações | perda de peso >10%, contraindicação de TRO (íleo paralítico, abdome agudo, alteração de consciência/convulsões), choque hipovolêmico, vômitos biliosos ou de difícil controle, falha da TRO | Diarreias na Infância (slide Liane Viana), p.23 | CONFIRMADO |
| Osmolaridade SRO OMS 2002 | 245 mOsm/L (Na 75 mmol/L) | Diarreias na Infância (slide Liane Viana), p.21 | CONFIRMADO |
| Osmolaridade do plasma (referência) | 291 mOsm/L | Diarreias na Infância (slide Liane Viana), p.21 | CONFIRMADO |
| Exames laboratoriais — indicação | não são rotina; solicitar em evolução atípica/arrastada/grave, imunodeprimidos, sangue nas fezes, lactentes <4 meses | Diarreias na Infância (slide Liane Viana), p.16 | CONFIRMADO |

## Pegadinhas

- Lágrimas presentes ou outro sinal isoladamente tranquilizador NÃO neutraliza a contagem de ≥2 sinais de alarme já presentes — o critério do MS é contagem objetiva, não balanço subjetivo entre sinais bons e ruins.
- O tempo de expansão do Plano C MUDA conforme a idade (<1 ano: 1h+5h; ≥1 ano: 30min+2h30) — não é um tempo único fixo para todas as idades.
- SRO por evacuação NÃO é dose única para toda criança — varia por faixa etária (50-100 mL, 100-200 mL, ou livre demanda >10 anos).
- Exames laboratoriais NÃO são rotina em diarreia aguda — só se justificam em evolução atípica, grave, imunodeprimido, sangue nas fezes ou lactente <4 meses.
- Diarreia persistente (>14 dias) é definida SÓ pela duração, mas já sinaliza risco de desnutrição/desidratação — não confundir com "crônica" (não usado nesta classificação da OMS apresentada).

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "Criança com prega cutânea lentificada mas ainda com lágrimas presentes não está desidratada" | um sinal normal parece neutralizar a gravidade | narrativa acima do discriminador | a classificação usa contagem objetiva de sinais alterados — se ≥2 sinais estão alterados, é desidratação, independente de outro sinal estar normal |
| "Toda criança desidratada deve começar direto na hidratação venosa para ser mais rápido" | parece a via mais eficiente e definitiva | definitiva antes da inicial | Plano C só é indicado por critérios objetivos (choque, perda>10%, contraindicação de TRO, falha comprovada de TRO) — a TRO/Plano B é sempre a primeira tentativa quando não há essas indicações |
| "Solicitar coprocultura e hemograma de rotina em toda diarreia aguda para não perder o diagnóstico etiológico" | parece investigação completa e cautelosa | sobre-elaboração | exames não são rotina — só em evolução atípica, grave, imunodeprimido, sangue nas fezes ou lactente <4 meses |
| "O volume e o tempo de expansão do Plano C são os mesmos para lactente e escolar" | simplifica a memorização de um único protocolo | valor errado | o tempo de infusão é DIFERENTE por faixa etária (<1 ano é mais lento: 1h+5h; ≥1 ano é mais rápido: 30min+2h30) |

## Conduta

- Inicial: classificar a duração (aguda/persistente) e o grau de hidratação pela contagem objetiva de sinais (tabela MS 2023); iniciar Plano A se hidratado, Plano B se algum grau de desidratação.
- Definitiva: Plano B com SRO 50-100 mL/kg em 4-6h na unidade de saúde, reavaliando o estado de hidratação continuamente; se vômitos persistentes, SOG 20 mL/kg/h; ondansetrona por peso/idade se necessário; se sem melhora em 6h, encaminhar para hospital.
- Condição da conduta: Plano C reservado para perda de peso >10%, contraindicação de TRO (íleo paralítico, abdome agudo, alteração de consciência/convulsões), choque hipovolêmico, vômitos biliosos/incontroláveis ou falha comprovada da TRO — expansão por faixa etária (30+70 mL/kg, tempo variando conforme <1 ano ou ≥1 ano; RN/cardiopata grave: 10 mL/kg em 30 min).
- Diferencial perigoso: sinais de alarme (não melhorar em 2 dias, aumento de frequência/volume, vômitos frequentes, sangue nas fezes, recusa alimentar, diminuição da diurese, muita sede) indicam reavaliação/escalonamento mesmo em Plano A.
- O que mudaria a decisão: contraindicação de TRO (alteração de consciência, convulsão, abdome agudo, íleo paralítico) muda diretamente para Plano C, independente do grau de desidratação calculado pela tabela.

## Mini-casos ativos

1. Lactente de 8 meses, prega cutânea desaparece lentamente, mucosa oral seca, mas ainda apresenta lágrimas presentes e pulsos cheios. Classificação: 2 sinais alterados (turgor + mucosa), sem nenhum sinal com asterisco → "algum grau de desidratação" → Plano B, não desidratação grave. Variável decisiva: contagem de sinais + ausência de sinal com asterisco.
2. Criança de 3 anos, letárgica, pulsos fracos, mucosa muito seca, déficit de peso estimado em 12%. Classificação: ≥2 sinais alterados incluindo 2 com asterisco (sensório + pulsos) → desidratação grave → Plano C, expansão 30 mL/kg em 30 min + 70 mL/kg em 2h30 (SF 0,9% ou Ringer). Variável decisiva: presença de sinal com asterisco define gravidade, não só a contagem total.
3. Lactente de 5 meses em Plano B há 6 horas, sem melhora dos sinais de desidratação, mantendo recusa alimentar e diurese diminuída. Conduta: falha da TRO → encaminhar para internação/Plano C. Variável decisiva: limiar de reavaliação em 6h, não prolongar TRO indefinidamente.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Critério de desidratação grave (MS 2023) | ≥2 sinais alterados, incluindo ao menos 1 com asterisco (incapaz de beber, pulsos fracos, sensório alterado) | Limiar |
| Um sinal tranquilizador neutraliza sinais de alarme? | Não — a classificação é por contagem objetiva, não por balanço subjetivo | Pegadinha |
| Plano C — volume e tempo de expansão <1 ano | 30 mL/kg em 1h + 70 mL/kg em 5h | Valor |
| Plano C — volume e tempo de expansão ≥1 ano | 30 mL/kg em 30min + 70 mL/kg em 2h30 | Valor |
| Zinco no Plano A — dose por idade | <6 meses: 10 mg/dia; ≥6 meses: 20 mg/dia, por 10-14 dias | Valor |
| Indicações de Plano C | Perda de peso >10%, contraindicação de TRO, choque, vômitos biliosos/incontroláveis, falha da TRO | Conduta |
| Exames laboratoriais na diarreia aguda | Não são rotina — só em evolução atípica/grave, imunodeprimido, sangue nas fezes, <4 meses | Pegadinha |

## Revisão

- Revisar quando: antes de qualquer simulado de I unidade (Gastroenterologia pediátrica) e sempre que houver questão combinando AIDPI/classificação de desidratação.
- Critério de parada: classificar corretamente o grau de desidratação pela tabela de contagem de sinais e aplicar o plano correspondente (incluindo volume/tempo por faixa etária) em 4/4 mini-casos, sem se deixar levar por impressão clínica global.
