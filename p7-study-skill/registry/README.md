# Registros canônicos

Este diretório contém aliases e, nas próximas etapas de revisão clínica, os
registros JSONL conformes aos schemas versionados. Arquivos pessoais de estudo
não pertencem aqui: o ledger do aluno fica em `.p7-state/`, ignorado pelo Git.

`aliases.json` resolve nomes para joins e declara cobertura `partial` ou
`complete`. As duas lacunas recuperadas nesta RC apontam agora para cápsulas
autônomas e estão `complete`; quarentenas internas continuam visíveis e não são
apagadas por esse estado. Um alias nunca cria uma cápsula fictícia.
