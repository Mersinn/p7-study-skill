# CLEAN_INSTALL_REPORT — instalação descartável

**Data:** 22/08/2026  
**Fonte:** `qualification/v1.0.0-codex` @ `f56a1e5`  
**Ambiente:** cópia descartável em `work/clean_install_20260822`, fora do clone
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
python scripts/validate_package.py                 → error=0, warn=36, info=2, EXIT_CODE=0
python scripts/validate_package.py --release-gate   → EXIT_CODE=1, HOLD
```

O fallback sem corpus/vision foi observado como `metadata_only`; não houve
alegação de inspeção de fonte bruta. As dependências são apenas biblioteca
padrão Python.

## Limitação

A invocação da skill numa superfície de modelo headless não foi concluída: a
tentativa T10 terminou com `ConnectionRefused`, e uma repetição fora do sandbox
exigiria autorização explícita para exportar o pacote/fixtures a uma API
externa. Portanto este relatório comprova instalação e runtime determinístico,
mas não fecha o gate `clean_install` nem `scripted_user_journeys`.
