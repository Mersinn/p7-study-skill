# Red team independente — reparo de proveniência

VERIFICADO em 2026-09-08T13:58:16.535849+00:00. Origem DOCUMENTADA `b0a9f23091e0cb92e97829e4d9d30fc05f51cf48`. HEAD de origem medido: indisponível (ZIP).

## Identidade e denominadores

- Código `scripts/p7lib.py`: SHA-256 `2a3c748c9e6466fc1f8617c72fe1b6dae6a4cb7f44d7133e619d0e713f07b00c`.
- Manifesto `00_SOURCE_MANIFEST.csv`: SHA-256 `3b5fd6c8d9933e6e42fe2d2f0859b60e0cd3cb88a6c0d9b6e08c68305f00b641`.

VERIFICADO: 33/33 checks independentes passaram; nenhum desses checks substitui qualquer um dos 17 gates históricos. O denominador de precisão permanece 2.392/2.392 linhas, com as mesmas chaves (capsule_path, section_row) após normalizar o tipo string/integer e com claim_text integralmente preservado.

| Estado | Antes / 2.392 | Depois / 2.392 |
|---|---:|---:|
| resolved genérico legado | 75 | 0 |
| resolved:exact | 0 | 75 |
| resolved:stem | 0 | 245 |
| resolved:folded | 0 | 0 |
| resolved:placeholder | 0 | 5 |
| declared_no_source | 0 | 24 |
| ambiguous | 0 | 33 |
| unresolved_source_reference | 2.317 | 2.010 |

VERIFICADO: 75/75 linhas exatas preservam os mesmos IDs, incluindo 8/8 linhas com citações explícitas múltiplas. 24/24 linhas com marcador de ausência ficam declared_no_source e sem IDs. A queda de unresolved inclui 250 novos vínculos inferidos, 24 declarações honestas de ausência e 33 ambiguidades explicitadas; estes dois últimos grupos não são fontes resolvidas.

## Ataques executados

| Check independente | Veredito |
|---|---|
| exact literal | PASS |
| exact dominates inferred | PASS |
| distinct explicit IDs preserved | PASS |
| stem same-level collision | PASS |
| stem dominates placeholder | PASS |
| folded diacritics | PASS |
| folded dominates placeholder | PASS |
| folded collision | PASS |
| placeholder one character | PASS |
| placeholder cannot eat zero | PASS |
| placeholder cannot eat two | PASS |
| placeholder cannot cross space | PASS |
| placeholder cannot cross slash | PASS |
| placeholder same-level collision | PASS |
| no prose prefix matching | PASS |
| no left-substring | PASS |
| no right-substring | PASS |
| unknown hash not inferred | PASS |
| short stem rejected | PASS |
| short exact preserved | PASS |
| non-hash stem not inferred | PASS |
| declared general dominates exact | PASS |
| declared absent dominates exact | PASS |
| declared general dominates inferred | PASS |
| semicolon segment anchoring | PASS |
| backtick source title | PASS |
| precision denominator and row identities | PASS |
| all legacy resolved IDs preserved | PASS |
| all legacy explicit multiple citations preserved | PASS |
| declared absence never resolved | PASS |
| no generic status | PASS |
| resolved IDs exist in manifest | PASS |
| source corpus unchanged | PASS |

Fixtures e resultados detalhados estão em RED_TEAM.json; reprodução: `python3 repair/adversarial_checks.py --root <p7-study-skill> --baseline <BASELINE.json> --output <RED_TEAM.json>`.

## Síntese e limites

VERIFICADO: colisões stem/folded/placeholder no mesmo nível retornam ambiguous; exact prevalece sobre inferência, stem sobre folded/placeholder e folded sobre placeholder. O placeholder consome um caractere de palavra e não atravessa espaço/barra, não consome zero ou dois caracteres. O stem não invade nomes maiores ou IDs com hash desconhecido. Stems curtos não são inferidos. Ausência explícita prevalece inclusive sobre ID exato.

VERIFICADO: resultado do matcher contém source_ids, status, level e candidates; precisão guarda source_reference_status específico, nunca resolved genérico. O catálogo preserva source_match_levels_by_id e declara source_resolution_policy. Esta revisão verificou o contrato dos campos diretamente no código; não interpreta a união das referências como validade clínica. Numa célula com citações múltiplas inferidas, a política de melhor nível pode identificar apenas uma parte: isso está declarado também na amostra.

VERIFICADO: a amostra manual lexical tem 20/20 pares compatíveis entre citação, ID e caminho do manifesto. Inclui 5 controles L0 existentes, 10 novos L1 e as 5 linhas L3 disponíveis. Não se observou falso vínculo lexical nos 20 itens. Isso não estabelece taxa populacional de falsos positivos: amostra intencional, não aleatória, e todos os 5 itens L3 pertencem ao mesmo DOCX.

PENDÊNCIA: 0/2.392 linhas reais folded; requisito original de 5 exemplos reais por nível não atendido. A execução L2 é testada por fixtures sintéticas explicitamente separadas. L3 verifica compatibilidade nominal: não recupera informação perdida no manifesto e não pode provar identidade sem qualquer possibilidade de homônimo; empate catalogado é recusado. Nenhuma validação lexical prova que o documento sustenta o enunciado clínico.

VERIFICADO: SOURCE_REQUESTS.json contém 17/17 claims de quarentena e 53/53 ocorrências de fontes curriculares com source_id e rel_path iguais ao manifesto. Não foi identificada incompatibilidade factual de mapeamento nesta checagem. DOCUMENTADO: QUARANTINE_TRIAGE declara a origem operacional A–D e separa ausência de fonte da validade; não representa promoção de claim.

PENDÊNCIA: não foram executadas jornadas de qualificação históricas neste workstream, nem validadores sobre estado intermediário. PDFs/documentos primários não disponíveis: transcription e suporte clínico não reavaliados. Não houve pesquisa web em substituição aos arquivos curriculares.

DECISÃO HUMANA NECESSÁRIA: leitura e adjudicação das evidências clínicas continuam exigidas. Este relatório não assina revisão clínica de nível independente nem autoriza saída de quarentena. Nenhum arquivo clínico ou cápsula foi editado por este revisor.

CONFLITO: requisito literal de 54/54 aprovações e 17/17 jornadas reexecutadas não pode ser satisfeito apenas por estes checks; o baseline documenta 53 testes aprovados, um ignorado e fixtures de qualificação ausentes. Não houve mudança de denominador para declarar sucesso.

Reparo adversarial aplicado por este agente: 0/1 rodadas; nenhum defeito material novo encontrado nos ataques enumerados. O encerramento de release permanece a cargo do orquestrador, condicionado às pendências declaradas.
