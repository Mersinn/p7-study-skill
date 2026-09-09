# BASELINE_DELTA_REPORT — Marco A

**Data:** 22/08/2026 (America/Fortaleza)  
**Branch:** `qualification/v1.0.0-codex`  
**Base confirmada:** `origin/qualification/v1.0.0-claude` em
`0a9f558a9727e3bb6aa1fb7e9b967517b53128bb`  
**Decisão:** HOLD preservado.

## Escopo

Este marco estabiliza o estado recebido. Não reabre a auditoria, não altera a
fixture comportamental, não executa novo ciclo do detector e não fecha gate por
ausência de erro observado.

## Execução reproduzida

Executado em `p7-study-skill/`:

```text
python scripts/run_tests.py                         → 20/20 PASS
python scripts/reconcile_package.py --write         → 6 artefatos regenerados
python scripts/reconcile_package.py --check         → 158 cápsulas reconciliadas
python scripts/validate_package.py                 → error=0, warn=36, info=2
python scripts/validate_package.py --release-gate   → HOLD; 8 gates abertos
python qualification/tools/build_canonical_coverage.py
                                                     → 52 claims; 52/52 evidence locators completos
```

Os 36 warnings são 28 cápsulas sem `source_id` resolvível e os oito gates
intencionalmente pendentes. Os dois `INFO` são as camadas opcionais
`corpus_text`/`vision_png` ausentes, com fallback `metadata_only` honesto.

## Estado recebido confirmado

| Evidência | Resultado vigente |
|---|---:|
| Cápsulas | 158 |
| Cápsulas de alto risco | 105 |
| Claims canônicos | 52 = 43 `current`, 8 `quarantined`, 1 `conflict` |
| Sources / source_versions | 24 / 24 |
| Precision rows | 2.391 |
| Detector | v1.4.0 congelado |
| Behavioral evidence herdada | T05 FAIL; T08 PASS; T09 PASS |
| Reconcile / validate | PASS / `error=0` |
| Release | HOLD; 8 gates abertos |

## Delta aplicado

- artefatos determinísticos do pacote foram regenerados pelo reconciler; não
  foram editados manualmente;
- `AGENTS.md` e `README_INSTALL.md` deixaram de descrever um piloto humano como
  gate vigente; a qualificação é por jornadas sintéticas reproduzíveis;
- relatórios do detector e da varredura clínica agora apontam explicitamente
  para v1.4.0 e separam snapshots históricos v1.1–v1.3 do estado atual;
- criada a view claim-level `CANONICAL_CLAIM_COVERAGE.csv`, com resumo JSON,
  separando estado/evidência do registry de linkage lexical do detector. A view
  marca o caso temporal da sepse como limitação conhecida, em vez de converter
  `0%` lexical em ausência de claim.

Nenhuma cápsula, claim, fixture, gate ou resultado comportamental foi alterado
neste marco.
