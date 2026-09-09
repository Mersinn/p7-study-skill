# Compatibilidade e degradação

## Estado verificado na v1.5.0

| Superfície | Estado | Observação |
|---|---|---|
| Codex | qualificado para revisão do usuário | T05/T08/T16 sentinelas, T19, jornadas e longitudinalidade passaram em sessões limpas |
| Claude com skills locais | não avaliado | OAuth expirado é pendência de compatibilidade Claude e não entra no denominador Codex |
| ChatGPT/Claude mobile | fallback por conversa/anexo | sem garantia de instalação de skill ou ledger local |
| Python | testado com 3.14 | scripts usam somente a biblioteca padrão |
| MCP | não implementado | explicitamente posterior à aprovação da skill |

“Compatível” não significa clinicamente aprovado. A v1.5.0 preserva 17 claims
`quarantined`, 1 `conflict` e conteúdo crítico não registrado como `pending`;
nenhum deles pode ser recuperado como prática atual. Claude não entra no
denominador Codex.

## Camadas opcionais ausentes

`corpus_text/` e `vision_png/` não fazem parte do pacote portátil. Quando não estiverem acessíveis, o comportamento obrigatório é `metadata_only`: a skill pode usar a cápsula e informar a referência registrada, mas não pode afirmar que abriu, releu ou verificou a fonte bruta naquela sessão.

Se uma superfície não oferecer arquivos locais persistentes, o ledger deve ser exportado/importado explicitamente. Sem ledger acessível, declare “sessão sem histórico”; não simule memória longitudinal.
