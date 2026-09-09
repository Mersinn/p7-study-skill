# Reparo P7 — resultado e limites

Data: 2026-09-08T14:13:01.264755+00:00. Candidato `1.5.1-rc.1`. **Estado final de liberação: HOLD.**

**VERIFICADO:** matcher e consumidores reparados, com revisão adversarial independente e preservação do conteúdo clínico. **PENDÊNCIA:** os critérios de liberação integral não foram atendidos; o candidato não equivale à v1.5.1 final aprovada.

## Resultado de proveniência — 2.392 linhas em ambos os snapshots

| Estado | Baseline 06/09/2026 | Candidato 08/09/2026 |
|---|---:|---:|
| `resolved:exact` | 75 | 75 |
| `resolved:stem` | 0 | 245 |
| `resolved:folded` | 0 | 0 |
| `resolved:placeholder` | 0 | 5 |
| `declared_no_source` | 0 | 24 |
| `ambiguous` | 0 | 33 |
| `unresolved_source_reference` | 2317 | 2010 |

No baseline, os 75 exact eram registrados como `resolved`. **250/2.392 novos vínculos**: 245 stem + 5 placeholder. A queda de unresolved em 307 linhas inclui 24 ausências legítimas e 33 ambiguidades; essas 57 linhas não são novas resoluções.

**VERIFICADO:** 75/75 vínculos exatos preservados, incluindo 8/8 linhas com múltiplos IDs explícitos. 2.392/2.392 identidades e enunciados de linha preservados. 201/201 arquivos protegidos comparados permaneceram idênticos, incluindo cápsulas, contratos de runtime e dados clínicos abrangidos pela verificação. Nenhum claim foi promovido.

## Verificação executada

- Suíte principal: **53/54 aprovados, 1/54 ignorado, 0 falhas**, igual ao baseline. O teste ignorado exige a fixture original externa ao ZIP; não foi removido nem substituído.
- Testes adversariais independentes: **33/33**. Incluem conflitos de ID, precedência, ausência, limites do placeholder e preservação dos registros. Não são os 17 gates históricos.
- Amostra manual: **20/20 compatíveis lexicalmente** — 5 controles exact, 10 novos stem e 5 novos placeholder. Zero páginas primárias lidas; isso não comprova suporte clínico.
- Reconciliação: passou; **158/158 cápsulas** reconciliadas.
- Empacotamento preliminar: **2/2 construções idênticas** e **1/1 instalação limpa estrutural aprovada**. Verificação do pacote congelado é registrada em FINAL_VERIFICATION.json.

## Gate de liberação — universo fixo 17

Os 17/17 PASS herdados continuam documentados na história v1.5.0. No candidato, 8/17 admitem rechecagem mecânica local e 9/17 permanecem pending porque suas entradas originais não acompanham o ZIP. Nenhuma pendência de qualificação foi descrita como falha clínica observada.

| Gate | v1.5.0 documentado | Candidato | Natureza |
|---|---|---|---|
| `version_integrity` | passed | passed | Rechecagem estrutural local |
| `evidence_integrity` | passed | passed | Rechecagem estrutural local |
| `critical_inventory_complete` | passed | pending | Qualificação original ausente; não reexecutado |
| `high_risk_accounted` | passed | pending | Qualificação original ausente; não reexecutado |
| `p0_exposed_zero` | passed | pending | Qualificação original ausente; não reexecutado |
| `p1_high_risk_exposed_zero` | passed | pending | Qualificação original ausente; não reexecutado |
| `current_claim_traceability` | passed | passed | Rechecagem estrutural local |
| `behavioral_regression` | passed | pending | Qualificação original ausente; não reexecutado |
| `p6_parity` | passed | pending | Qualificação original ausente; não reexecutado |
| `longitudinal_resume` | passed | pending | Qualificação original ausente; não reexecutado |
| `package_hygiene` | passed | passed | Rechecagem estrutural local |
| `clean_install` | passed | passed | Rechecagem estrutural local |
| `report_consistency` | passed | passed | Rechecagem estrutural local |
| `red_team` | passed | pending | Qualificação original ausente; não reexecutado |
| `runtime_context` | passed | pending | Qualificação original ausente; não reexecutado |
| `structured_provenance` | passed | passed | Rechecagem estrutural local |
| `narrative_consistency` | passed | passed | Rechecagem estrutural local |

**PENDÊNCIA:** não houve reexecução integral de 17/17. Os denominadores históricos e as limitações individuais estão em GATE_DELTA.json e RELEASE_AUDIT.md. A geração de hashes não substitui jornadas, inventário ou avaliação comportamental. O comando de release deve retornar bloqueio pelos gates pending; esse bloqueio não foi afrouxado.

## Quarentena e revisão humana

**DOCUMENTADO:** registry preservado em **34/52 current, 17/52 quarantined, 1/52 conflict**. Isto descreve o estado herdado, não 34 validações clínicas novas. **VERIFICADO:** **0/17 promoções**, **17/17 itens triados** e **17/17 na fila humana**.

Triagem operacional desta rodada: **A 3/17**, **B 10/17**, **C 3/17**, **D 1/17**. A–D não veio definido no handoff; as definições e a justificativa por claim estão em QUARANTINE_TRIAGE.md. A prioridade formal de estudo permanece `unscored`; a ordem da fila usa risco e dependências, sem inventar incidência em provas.

**PENDÊNCIA:** 26 documentos curriculares únicos mapeados, mais imagem avulsa e instrumento oficial OSCE. Os nomes exatos e as páginas disponíveis estão em SOURCE_REQUESTS.md. Página ausente não foi inventada. A busca dos títulos nos arquivos disponíveis não localizou as fontes P7. W1 não foi iniciado sem a ingestão exigida; W2 registra source_unavailable nesta revisão; W3 não recebeu provas originais para medir incidência.

**DECISÃO HUMANA NECESSÁRIA:** ler e assinar a evidência de cada futura promoção. Autorização de implementação não é assinatura clínica. O conflito de febre materna intraparto permanece intocado.

## Conflitos registrados

- O ZIP não contém `.git`. Commit de origem **DOCUMENTADO**, nunca apresentado como HEAD medido: `b0a9f23091e0cb92e97829e4d9d30fc05f51cf48`. Identidade verificável do ZIP: `21416ca72252856ce4d7b189b3f742a4bc1720d7f8276eec5ec31e4db92ed55f`.
- A nota literal metadata-only/supersessão aparece em **4/17** quarentenas, não 8/17. Mais **1/17** registra extrapolação cruzada. O matcher curricular não resolve disponibilidade ou supersessão de EXTRIP/ASAM.
- `Casos_Cli_nicos_P7_1__4f3f459b20` contém underscore adicional; o coringa de exatamente um caractere não pode apagá-lo para casar `Casos_Clinicos_P7_1`. A regra não foi afrouxada.
- Não existem novos L0 preservando o comportamento antigo, nem cinco casos reais L2 neste conjunto. **O requisito de cinco por nível não foi atendido.**

## Continuidade e autoria

Quatro subagentes foram iniciados antes da interrupção em 06/09; os arquivos salvos foram recuperados. O quinto e último subagente realizou a revisão independente final em 08/09. O orquestrador completou o código interrompido, integrou os resultados e preparou o candidato. Nenhum laudo foi atribuído ao agente interrompido que não chegou a entregá-lo.

O baseline BASELINE.json permanece imutável, SHA-256 `ed2bf614d30a4b16ed0a599e2788314a4c896e179a3c70b7f3584ef99fd33e3b`. Código revisado: `2a3c748c9e6466fc1f8617c72fe1b6dae6a4cb7f44d7133e619d0e713f07b00c`. As evidências por linha, comandos, amostra e fila acompanham o pacote de revisão.

## Critério de aceite

**Não atendidos:** 54/54 aprovações sem skip; 17/17 gates reexecutados; cinco amostras reais por nível; ingestão das fontes e verificação humana das quarentenas. **Atendidos:** status explícito para todas as linhas, preservação dos vínculos exatos, 20 verificações lexicais reais, triagem e fila completas, zero promoção automática e delta integral.

**Resultado:** reparo técnico revisável concluído; liberação final e etapas clínicas mantidas em HOLD. Não instalar o candidato como substituto silencioso de uma release já qualificada.
