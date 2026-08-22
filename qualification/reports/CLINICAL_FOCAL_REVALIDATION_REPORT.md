# CLINICAL_FOCAL_REVALIDATION_REPORT — P7 / sepse neonatal

**Marco:** D — revalidação clínica focal de alto risco  
**Data:** 2026-08-22  
**Branch:** `qualification/v1.0.0-codex`  
**Base de auditoria:** `origin/qualification/v1.0.0-claude` @ `0a9f558a9727e3bb6aa1fb7e9b967517b53128bb`  
**Estado de release:** `HOLD`

## Escopo e método

Foi reaberta somente a cápsula priorizada `capsule:eisca:sepse_e_meningite_neonatal`, preservando os registros anteriores. A comparação foi feita contra:

- [SBP — Diretrizes para uso racional de antibióticos em unidades neonatais, 2025](https://www.sbp.com.br/fileadmin/user_upload/sbp/2025/marco/17/24815f-Diretrizes_para_uso_racional_antibioticos_em_Unid_Neonatal.pdf), PDF p.5–6: janela temporal operacional e esquemas empíricos.
- [NICE NG195 — Neonatal infection](https://www.nice.org.uk/guidance/NG195), atualização vigente em 13/05/2026: fatores de risco por idade gestacional, indicadores maternos e tratamento/investigação precoce.
- SPRS 2012 já registrada em `source-version:sprs.boletim.sepse-neonatal.2012-v1n1`, como evidência histórica quase-primária.

Nenhuma divergência foi convertida em `current` por média ou por plausibilidade curricular.

## Adjudicação dos quatro claims canônicos

| Claim | Estado | Resultado |
|---|---|---|
| `janela-precoce-tardia` | `conflict` | A cápsula/aula usa 72h; a SBP 2025 descreve precoce especialmente até 48h e tardia após 48h; a SPRS 2012 descreve faixa 48–72h. A cápsula passou a exigir declaração do protocolo. |
| `amniorrexe-fator-risco-maior` | `conflict` | >18h é confirmado na SPRS, mas o NICE atual separa >18h antes de parto pré-termo e >24h antes de parto a termo. O “risco 4x” não foi confirmado. O corte deixou de ser universalizado. |
| `esquema-empirico-precoce` | `current` com contexto | SBP 2025 confirma ampicilina ou penicilina cristalina + amicacina ou gentamicina. A cápsula agora explicita dependência de protocolo, resistência, peso, idade gestacional, rim e meningite; NICE usa benzilpenicilina + gentamicina em seu contexto. |
| `febre-materna-limiar` | `conflict` | >38°C na cápsula, >37,5°C na SPRS e atualização NICE 2026 enfatizando sepse materna/chorioamnionite. Nenhum limiar universal foi promovido. |

## Correções de segurança aplicadas

- Amniorrexe foi contextualizada por idade gestacional e diretriz.
- RN assintomático não é tratado automaticamente por um fator isolado; a via de indicadores/observação/protocolo precisa ser aplicada.
- Punção lombar deixou de ser descrita como mandatória em toda sepse tardia; a indicação depende de suspeita de meningite e estabilidade.
- Esquema tardio foi alinhado à SBP 2025: oxacilina + amicacina como primeira opção; vancomicina + cefotaxima/cefepime como segunda, conforme flora e resistência.
- A coleta de hemocultura antes da primeira dose foi preservada e reforçada.

## Artefatos e comandos reproduzíveis

Registros atualizados: `registry/clinical_claims.jsonl`, `registry/sources.jsonl`, `registry/source_versions.jsonl`, `registry/reviewers.json`, cápsula EISCA, `CLAIM_ADJUDICATION_LOG.md` e `CLINICAL_SWEEP_REPORT.md`.

Comandos executados:

```text
python scripts/run_tests.py                         # 20/20 PASS
python scripts/reconcile_package.py --write         # 6 artefatos determinísticos
python qualification/tools/build_canonical_coverage.py
python scripts/reconcile_package.py --check         # 158 cápsulas reconciliadas
python scripts/validate_package.py                  # error=2, warn=36, info=2
python scripts/validate_package.py --release-gate   # exit 1, como esperado em HOLD
```

Estado canônico: 52 claims — 41 `current`, 8 `quarantined`, 3 `conflict`; todos os 52 com FK de source-version e locator completos. Os dois conflitos de alto risco permanecem bloqueadores objetivos.

Este marco não fecha nenhum gate global. Jornadas comportamentais continuam sem novo resultado válido: a tentativa T10 foi registrada como `INCONCLUSIVE` por `ConnectionRefused`, sem inferência sobre o produto.
