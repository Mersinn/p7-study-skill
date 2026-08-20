# qualification/ — evidência da qualificação da v1.0.0

Este diretório fica **fora** de `p7-study-skill/` de propósito: é evidência de
processo, não parte do pacote distribuído. Mantê-lo fora preserva
`PACKAGE_MANIFEST.json` e o gate de reprodutibilidade do pacote.

- `tools/` — ferramentas determinísticas de varredura e execução.
- `reports/` — relatórios e CSVs gerados; reproduzíveis pelos comandos citados
  em cada relatório.

Nenhum arquivo aqui fecha gate por si só. `p7-study-skill/registry/release_gates.json`
continua sendo a fonte de verdade do estado dos gates.
