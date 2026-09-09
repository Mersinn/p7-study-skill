# F-LEDGER — entrada congelada para duas sessões Codex limpas

## Sessão A — entrada do usuário

> Quero retomar meu estudo de indicações de Plano C. Faça uma revisão ativa,
> registre minha confiança antes da resposta e, depois que eu responder,
> registre o resultado no ledger local.

## Sessão B — entrada do usuário

> Voltei em 16/09/2026 para revisar. O que está pendente pra mim hoje?

## Arquivos permitidos

- a skill instalada em `p7-study-skill/SKILL.md`;
- o protocolo de estado referido pela skill em
  `p7-study-skill/references/LEARNER_STATE_PROTOCOL.md`;
- o ledger Python referido pela skill em `p7-study-skill/scripts/ledger.py`;
- somente o diretório `.p7-state` fornecido pelo harness para a sessão.

O executor não deve consultar relatórios, registros de adjudicação, fixtures
de avaliação ou histórico desta auditoria. A entrada acima é a única mensagem
do usuário; não há gabarito, resultado esperado ou explicação do defeito.
