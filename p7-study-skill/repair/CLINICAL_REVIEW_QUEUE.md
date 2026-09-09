# Fila de revisão humana — P7

Data: 2026-09-08T14:02:14.834393+00:00. Snapshot de origem: commit DOCUMENTADO `b0a9f23091e0cb92e97829e4d9d30fc05f51cf48`; ZIP `21416ca72252856ce4d7b189b3f742a4bc1720d7f8276eec5ec31e4db92ed55f`.

**VERIFICADO:** 17/17 quarentenas incluídas; 0/17 promoções. Registry original preservado. **PENDÊNCIA:** fonte primária curricular ausente em 17/17; nenhuma revisão clínica foi assinada nesta rodada.

**INFERIDO:** a ordem abaixo é operacional, por criticidade documentada, consequência de erro e dependências. Não é frequência de prova nem o score oficial de estudo. A prioridade calculada permanece `unscored`, pois faltam incidência, iminência e dados individuais necessários à fórmula existente.

| Ordem | Claim | Tipo / criticidade | Bucket | Impedimento |
|---|---|---|---|---|
| 1 | `claim:li.ectr-recommended` | threshold / high | B | Contexto registra cortes antigos do slide versus overlay EXTRIP; a nota metadata-only não esgota a divergência curricular. |
| 2 | `claim:thi.prophylaxis` | dose / high | B | Contexto registra doses curriculares divergentes; obter documentos e separar profilaxia de Wernicke suspeita. |
| 3 | `claim:thi.glucose-order-coma` | treatment_sequence / high | C | ASAM para abstinência foi extrapolada para coma; nota registra extrapolação cruzada não verificada. |
| 4 | `claim:thi.glucose-order` | treatment_sequence / high | B | Material diz sempre antes; overlay admite outra ordem; divergência contextual expressa. |
| 5 | `claim:thi.wernicke-high-dose` | dose / high | B | Fontes curriculares divergem em doses e não há regime universal fechado no registry. |
| 6 | `claim:li.charcoal` | contraindication / high | A | Ausência curricular explicitamente declarada; overlay EXTRIP metadata-only e supersessão não verificada. A não implica reparável pelo matcher. |
| 7 | `claim:clo.thresholds-us` | threshold / high | B | Limiar FDA ligado à população EUA, enquanto currículo não diferencia jurisdição. |
| 8 | `claim:asth.under5-doses` | dose / high | B | A própria cápsula e o contexto registram tabelas/doses divergentes para ≤5 anos; conteúdo exato precisa do slide. |
| 9 | `claim:sepse-neonatal.amniorrexe-fator-risco-maior` | threshold / high | B | Registry documenta >18h sem estratificar versus cortes por idade gestacional no NICE; multiplicador 4x sem confirmação. |
| 10 | `claim:sepse-neonatal.janela-precoce-tardia` | time_window / high | B | Registry documenta 72h curricular versus SBP 2025/48h e SPRS 2012/faixa 48–72h. |
| 11 | `claim:clo.anc-us` | guideline_dependent / high | B | Quinzenal indefinido no currículo versus calendário FDA; jurisdição Brasil pendente. |
| 12 | `claim:clo.rems-us` | guideline_dependent / high | B | Currículo anterior ao fim do REMS; regra EUA não transposta ao Brasil. |
| 13 | `claim:bf.hiv-htlv` | contraindication / high | C | Evidência vinculada não cobre integralmente a claim composta HIV/HTLV. |
| 14 | `claim:bf.medicines` | contraindication / high | A | Lista antiga e orientação geral; nenhum confronto fármaco-específico fechado. Necessita documento/lista exata e fontes por fármaco. |
| 15 | `claim:sem.vitals` | threshold / high | A | Tabelas curriculares não disponíveis e faixas atuais não validadas; divergência específica ainda não documentada. |
| 16 | `claim:diarreia-planos.osmolaridade-sro` | concentration / medium | C | Fonte clínica vinculada cobre Na 75 versus 90, mas não todo o conjunto 245/291 mOsm/L. |
| 17 | `claim:osce.synthetic-rubric` | other / high | D | Orientações de colegas e lista de temas não substituem instrumento aplicado, pesos ou rubricagem oficial. |

## Trabalho para cada item

1. Obter os arquivos e localizadores de `SOURCE_REQUESTS.md`. Página contextual não fecha a transcrição da claim.
2. W2: ler diretamente a página e registrar trecho, edição, hash e `confirmed`, `divergent` ou `source_unavailable` nesta ficha. Os valores de trabalho não são gravados automaticamente no schema canônico.
3. W1: após a ingestão prevista no contrato, localizar fonte oficial brasileira da especialidade/Ministério da Saúde; fonte internacional é complemento com jurisdição explícita. Registrar valor, fonte primária, ano, população, cenário e concordância/divergência.
4. W3: usar apenas provas/devolutivas originais para incidência e formato; não usar frequência como validade clínica.
5. Adjudicar aula × diretriz. Não atribuir CONVERGENTE, DIVERGENTE ou ÓRFÃ enquanto faltarem as duas saídas necessárias.
6. Colher verificação humana identificada antes de promover qualquer quarentena. Campo de assinatura vazio nesta ficha significa pendência, não assinatura genérica.
7. Somente depois atualizar o registry canônico, reconciliar sua view CSV e repetir os gates aplicáveis.

## Campos obrigatórios de assinatura

Para cada claim: documento curricular + página + trecho; diretriz primária + ano + jurisdição + localizador; população/contexto; resultado de cada eixo; identidade real de L1; identidade humana da revisão independente; data; decisão e justificativa. O JSON acompanhante contém todos os itens para preenchimento.

**DOCUMENTADO:** a classificação A–D foi definida operacionalmente nesta rodada; não é taxonomia herdada nem juízo de validade.

**DECISÃO HUMANA NECESSÁRIA:** o conflito preexistente de febre materna intraparto permanece intocado, fora desta fila de 17. Autorização técnica não constitui confirmação de nenhum enunciado médico.

**PENDÊNCIA:** W1 não iniciado por falta da ingestão primária exigida. Não foi feita busca clínica externa nem alegada vigência médica atual.
