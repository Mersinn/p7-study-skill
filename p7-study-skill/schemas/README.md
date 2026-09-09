# Modelo de dados canônico

`schemas/v1/` contém contratos JSON Schema 2020-12 para oito entidades do
projeto, proveniência de revisão e avaliação auditável de prioridade. A versão do schema é
independente da versão da skill: todos os registros atuais usam
`schema_version: "1.0.0"`.

Os campos de estado são ortogonais. `transcription`, `curricular_alignment`,
`clinical_validity` e `independent_review` não podem ser colapsados em um único
`status`. Uma transcrição fiel de um slide antigo pode estar `confirmed` e, ao
mesmo tempo, ter validade clínica `historical_only`.

## Identidade e joins

- IDs são estáveis, minúsculos e com prefixo de entidade.
- Texto exibido ao aluno nunca é chave de join.
- Variações legadas são resolvidas por `config/normalization.json` e
  `registry/aliases.json`.
- `I`, `I_UNIDADE` e equivalentes tornam-se `UNIT_1`; `media` e `média`
  tornam-se `medium`. O valor original permanece em `legacy_metadata` nos
  artefatos reconciliados para auditoria.

## Migração

As cápsulas Markdown continuam preservadas. `scripts/reconcile_package.py`
materializa uma visão canônica delas sem reescrever o conteúdo. Claims clínicos
novos devem ser registrados como JSONL conforme `clinical-claim.schema.json`.
Quando faltar evidência, use `pending` ou `quarantined`; nunca preencha campos
com inferências silenciosas.
