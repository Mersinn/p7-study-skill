# qualification/ — evidência da qualificação da v1.0.0

Este diretório fica **fora** de `p7-study-skill/` de propósito: é evidência de
processo, não parte do pacote distribuído. Mantê-lo fora preserva
`PACKAGE_MANIFEST.json` e o gate de reprodutibilidade do pacote.

- `tools/` — ferramentas determinísticas de varredura e execução.
- `reports/` — relatórios e CSVs gerados; reproduzíveis pelos comandos citados
  em cada relatório.

A view `reports/CANONICAL_CLAIM_COVERAGE.csv` é gerada por
`python qualification/tools/build_canonical_coverage.py`. Ela conta claims
canônicos uma vez, separa estado clínico/evidência de linkage lexical do
detector e marca explicitamente limitações conhecidas de claims temporais. Ela
não substitui `CRITICAL_CLAIM_COVERAGE.csv` nem descongela o detector.

Nenhum arquivo aqui fecha gate por si só. `p7-study-skill/registry/release_gates.json`
continua sendo a fonte de verdade do estado dos gates.
