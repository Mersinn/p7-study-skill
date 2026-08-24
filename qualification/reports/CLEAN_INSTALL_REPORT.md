# CLEAN_INSTALL_REPORT — instalação descartável

**Data:** 24/08/2026
**Fonte:** `qualification/v1.0.0-codex` @ `48d0e44`
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

A invocação da skill numa superfície de modelo headless não foi concluída: a
tentativa histórica T10 terminou com `ConnectionRefused` e a tentativa
autorizada de 24/08 terminou antes da inferência com `401 OAuth access token has
expired`. Portanto este relatório comprova instalação e runtime determinístico,
mas não fecha o gate `clean_install` nem `scripted_user_journeys`; o pacote
também preserva os dois conflitos clínicos de alto risco, por isso o release
gate permanece vermelho mesmo com a instalação determinística aprovada.
