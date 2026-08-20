# Manifesto do pacote

O inventário estável vive em `artifacts/PACKAGE_MANIFEST.json` e é gerado por:

```text
python scripts/reconcile_package.py --write
```

Validação sem escrita:

```text
python scripts/reconcile_package.py --check
```

O manifesto exclui `artifacts/` — inclusive ele próprio —, `.git/`, caches e `.p7-state/`. Essa estratégia elimina o hash autorreferente e torna duas execuções consecutivas idênticas quando as entradas não mudam. Não edite o JSON manualmente.
