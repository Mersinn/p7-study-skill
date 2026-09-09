# Triagem das 17 quarentenas

Data: 2026-09-06T18:45:40.171398+00:00. Commit local medido: indisponível (ZIP sem Git). Commit de origem DOCUMENTADO: `b0a9f23091e0cb92e97829e4d9d30fc05f51cf48`. ZIP SHA-256: `21416ca72252856ce4d7b189b3f742a4bc1720d7f8276eec5ec31e4db92ed55f`. Registry SHA-256: `df3f7ed4f07e2e2cc91dd804fce9336db1c9721c1eab237b5ea80f0d6ae3d337`.

**DOCUMENTADO:** universo 17/52 claims do registry distribuídas em 10 cápsulas. **VERIFICADO:** nenhuma claim ou cápsula editada por este workstream.

**INFERIDO — decisão operacional desta rodada, não herdada:** A–D não foi definido no handoff disponível. A taxonomia abaixo serve à fila, não à validade nem à promoção.

| Bucket | Critério | Quantidade |
|---|---|---|
| A | Lacuna documental sem divergência explícita registrada | 3/17 |
| B | Divergência/conflito contextual documentado | 10/17 |
| C | Evidência parcial, composta ou extrapolação | 3/17 |
| D | Instrumento curricular/oficial indisponível (OSCE) | 1/17 |

Precedência da triagem: D (instrumento oficial) → C (cobertura/extrapolação) → B (divergência expressa) → A (lacuna residual). A não significa “o matcher libera”; B não altera `clinical_validity` para `conflict` automaticamente.

| Claim | Bucket | Impedimento específico | Próximo passo |
|---|---|---|---|
| `claim:asth.under5-doses` | B | A própria cápsula e o contexto registram tabelas/doses divergentes para ≤5 anos; conteúdo exato precisa do slide. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:li.ectr-recommended` | B | Contexto registra cortes antigos do slide versus overlay EXTRIP; a nota metadata-only não esgota a divergência curricular. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:li.charcoal` | A | Ausência curricular explicitamente declarada; overlay EXTRIP metadata-only e supersessão não verificada. A não implica reparável pelo matcher. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:thi.prophylaxis` | B | Contexto registra doses curriculares divergentes; obter documentos e separar profilaxia de Wernicke suspeita. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:thi.glucose-order` | B | Material diz sempre antes; overlay admite outra ordem; divergência contextual expressa. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:thi.wernicke-high-dose` | B | Fontes curriculares divergem em doses e não há regime universal fechado no registry. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:clo.anc-us` | B | Quinzenal indefinido no currículo versus calendário FDA; jurisdição Brasil pendente. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:clo.thresholds-us` | B | Limiar FDA ligado à população EUA, enquanto currículo não diferencia jurisdição. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:clo.rems-us` | B | Currículo anterior ao fim do REMS; regra EUA não transposta ao Brasil. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:bf.hiv-htlv` | C | Evidência vinculada não cobre integralmente a claim composta HIV/HTLV. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:bf.medicines` | A | Lista antiga e orientação geral; nenhum confronto fármaco-específico fechado. Necessita documento/lista exata e fontes por fármaco. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:sem.vitals` | A | Tabelas curriculares não disponíveis e faixas atuais não validadas; divergência específica ainda não documentada. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:osce.synthetic-rubric` | D | Orientações de colegas e lista de temas não substituem instrumento aplicado, pesos ou rubricagem oficial. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:thi.glucose-order-coma` | C | ASAM para abstinência foi extrapolada para coma; nota registra extrapolação cruzada não verificada. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:diarreia-planos.osmolaridade-sro` | C | Fonte clínica vinculada cobre Na 75 versus 90, mas não todo o conjunto 245/291 mOsm/L. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:sepse-neonatal.janela-precoce-tardia` | B | Registry documenta 72h curricular versus SBP 2025/48h e SPRS 2012/faixa 48–72h. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |
| `claim:sepse-neonatal.amniorrexe-fator-risco-maior` | B | Registry documenta >18h sem estratificar versus cortes por idade gestacional no NICE; multiplicador 4x sem confirmação. | Consultar mapeamento exato em SOURCE_REQUESTS; ingerir fonte, comparar contexto e aguardar assinatura humana. |

**PENDÊNCIA:** `transcription_this_review: source_unavailable` e `curricular_alignment_this_review: source_unavailable` para 17/17. Os 17/17 estados herdados `confirmed` não são revalidação atual.

**CONFLITO:** 4/17 têm a nota literal de metadata-only/supersessão; mais 1/17 tem metadata-only/extrapolação. O vínculo causal com matching L1/L3 não está demonstrado para overlays EXTRIP/ASAM.

**DECISÃO HUMANA NECESSÁRIA:** 0/17 promoções. O conflito preexistente de febre materna intraparto está fora destes 17 itens e permanece intocado; nenhum vencedor foi escolhido.
