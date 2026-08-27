# Baseline da P7 Study Skill v1.5.0

**Data:** 2026-08-27 (America/Fortaleza)  
**Branch de origem:** `qualification/v1.0.0-codex`  
**Branch de trabalho:** `release/v1.5.0`  
**HEAD/tree confirmados:** `6fc906fdc2522c340a8d4f4c67a942f5c62433bb` / `ec5b387c72470d05eca505d4350e16049c3d9932`  
**Remoto após push:** `origin/qualification/v1.0.0-codex` em `6fc906f`; `release/v1.5.0` criada no mesmo snapshot.  
**Decisão:** `HOLD`.

## Baseline reproduzido antes da migração

- `python p7-study-skill/scripts/run_tests.py`: 28/28 PASS;
- `python p7-study-skill/scripts/reconcile_package.py --check`: 158 cápsulas;
- `python p7-study-skill/scripts/validate_package.py`: `error=0`, `warn=28`, `info=2`;
- release gate legado: exit 0, demonstrando que a verificação antiga aceitava
  caminhos narrados sem provar existência, hash ou snapshot;
- registry: 52 = 35 `current` + 16 `quarantined` + 1 `conflict`;
- detector: 3.602 ocorrências primárias, 3.516 sem resolução; alto risco
  2.817, com 2.731 sem resolução;
- camadas opcionais `corpus_text` e `vision_png` ausentes; fallback declarado
  `metadata_only`;
- ZIP anterior: 10 entradas `__pycache__`/`.pyc`.

## Delta semântico do Marco A

O pacote passa a `1.5.0-rc.1`; a decisão volta a `HOLD`; gates clínicos,
evidenciais, de instalação e de snapshot final foram reabertos. Evidência válida
foi preservada em seus artefatos originais. A migração detalhada está em
`p7-study-skill/registry/GATE_MIGRATIONS.md`.
