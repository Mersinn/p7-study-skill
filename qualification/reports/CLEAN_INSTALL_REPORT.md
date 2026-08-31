# CLEAN_INSTALL_REPORT — P7 Study Skill 1.5.0

**Data:** 31/08/2026
**Resultado:** PASS

## Artefato verificado

- Caminho: `dist/P7-Study-Skill-1.5.0.zip`
- SHA-256: `21416ca72252856ce4d7b189b3f742a4bc1720d7f8276eec5ec31e4db92ed55f`
- Conteúdo: 253 entradas, raiz única, 0 caminhos inseguros, 0 duplicatas
  case-insensitive, 0 entradas proibidas.
- Reprodutibilidade: 2/2 construções byte a byte idênticas.

## Ambiente descartável

Extração isolada em:
`C:\Users\emers\AppData\Local\Temp\p7-clean-install-2a34d235474f487c853115c7ee6f0aaf\p7-study-skill`

- `corpus_text=False`
- `vision_png=False`
- `.p7-state=False`

Nenhum histórico da auditoria, corpus bruto ou estado do aluno foi fornecido.

## Execução reproduzida

```text
python scripts/run_tests.py
→ 54 executados = 53 PASS + 1 SKIP esperado

python scripts/reconcile_package.py --write
→ 7 artefatos determinísticos gerados; exit 0

python scripts/reconcile_package.py --check
→ 158/158 cápsulas reconciliadas; exit 0

python scripts/validate_package.py --evidence-mode standalone
→ error=0, warn=28, info=2; exit 0

python scripts/validate_package.py --release-gate --evidence-mode standalone
→ error=0, warn=28, info=2; exit 0
```

O único SKIP é a verificação do manifesto externo de fixtures comportamentais,
que deliberadamente não acompanha a instalação standalone. Os 28 warnings são
cápsulas `metadata_only` sem `source_id` resolvível no pacote portátil; não são
claims `current` silenciosamente promovidos. As duas informações registram as
camadas opcionais ausentes.

## Compatibilidade separada

Claude permanece `not_evaluated` por OAuth. Essa pendência não contaminou o
denominador Codex nem o gate de instalação standalone.
