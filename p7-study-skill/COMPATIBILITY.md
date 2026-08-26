# Compatibilidade e degradação

## Estado verificado nesta RC

| Superfície | Estado | Observação |
|---|---|---|
| Codex | bloqueado para qualificação final | execução real existe, mas T05 falhou; T19 e jornadas estão incompletos; longitudinal passou |
| Claude com skills locais | não avaliado nesta RC | OAuth expirado é pendência de compatibilidade Claude e não entra no denominador Codex |
| ChatGPT/Claude mobile | fallback por conversa/anexo | sem garantia de instalação de skill ou ledger local |
| Python | testado com 3.14 | scripts usam somente a biblioteca padrão |
| MCP | não implementado | explicitamente posterior à aprovação da skill |

“Compatível” não significa clinicamente aprovado. A RC continua bloqueada até a conclusão da revisão de claims e dos testes comportamentais.

## Camadas opcionais ausentes

`corpus_text/` e `vision_png/` não fazem parte do pacote portátil. Quando não estiverem acessíveis, o comportamento obrigatório é `metadata_only`: a skill pode usar a cápsula e informar a referência registrada, mas não pode afirmar que abriu, releu ou verificou a fonte bruta naquela sessão.

Se uma superfície não oferecer arquivos locais persistentes, o ledger deve ser exportado/importado explicitamente. Sem ledger acessível, declare “sessão sem histórico”; não simule memória longitudinal.
