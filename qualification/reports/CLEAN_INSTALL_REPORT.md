# CLEAN_INSTALL_REPORT — instalação descartável

**Data:** 25/08/2026 (snapshot histórico anterior preservado abaixo)
**Fonte vigente:** `qualification/v1.0.0-codex` @ `39ed34e`
**Ambiente:** cópia descartável em `work/clean_install_20260822_v2`, fora do clone
versionado; nenhum corpus bruto foi copiado.

## Procedimento reproduzido

1. Copiada a pasta completa `p7-study-skill/` para
   `.codex/skills/p7-study-skill/` em diretório descartável.
2. Confirmadas as camadas opcionais ausentes: `corpus_text=False`,
   `vision_png=False`.
3. Executados os comandos documentados pelo pacote:

```text
python scripts/run_tests.py                         → 20/20 PASS
python scripts/reconcile_package.py --write         → EXIT_CODE=0
python scripts/reconcile_package.py --check         → 158 cápsulas reconciliadas, EXIT_CODE=0
python scripts/validate_package.py                 → error=2, warn=36, info=2, EXIT_CODE=1 (2 conflitos clínicos de alto risco)
python scripts/validate_package.py --release-gate   → EXIT_CODE=1, HOLD
```

O fallback sem corpus/vision foi observado como `metadata_only`; não houve
alegação de inspeção de fonte bruta. As dependências são apenas biblioteca
padrão Python.

## Revalidação após a reconstrução estrutural — 24/08/2026

Uma terceira cópia descartável (`qualification/clean_install_20260824_structural`)
foi criada a partir do commit local `16b492f`, incluindo as duas views novas de
entrega ativa. Resultado reproduzível:

```text
python scripts/run_tests.py                         → 20/20 PASS
python scripts/reconcile_package.py --write         → EXIT_CODE=0
python scripts/reconcile_package.py --check         → 158 cápsulas reconciliadas, EXIT_CODE=0
python scripts/validate_package.py                 → error=2, warn=36, info=2, EXIT_CODE=1
python scripts/validate_package.py --release-gate   → EXIT_CODE=1, HOLD
```

A instalação e os artefatos permanecem determinísticos. Os dois erros são os
conflitos clínicos de alto risco já registrados; não foram mascarados pela
mudança estrutural.

## Limitação

As tentativas Claude de T10 continuam registradas como compatibilidade e não
afetam este gate de instalação. Elas permanecem relevantes para
`scripted_user_journeys`, não para `clean_install`.

## Revalidação vigente — instalação descartável v4

Foi copiada a skill atual para
`qualification/headless_test_env/clean_install_20260825/p7-study-skill`, sem
corpus bruto nem estado do aluno. Na cópia descartável, os comandos produziram:

```text
python scripts/run_tests.py                 → 20/20 PASS
python scripts/reconcile_package.py --write → EXIT_CODE=0
python scripts/reconcile_package.py --check → 158 cápsulas reconciliadas, EXIT_CODE=0
python scripts/validate_package.py          → error=0, warn=36, info=2
```

O gate `clean_install` está **PASS** com esta evidência. Isso não fecha a
release: `critical_claim_sweep`, `p0_zero`, `p1_high_risk_zero`, os gates
comportamentais, o E2E longitudinal e as jornadas continuam independentes e
mantêm a decisão global em `HOLD`.
