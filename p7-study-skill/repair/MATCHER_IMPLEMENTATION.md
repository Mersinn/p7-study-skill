# Implementação do matcher — reparo P7

VERIFICADO em 2026-09-08T13:56:23.832290+00:00. Código SHA-256 `2a3c748c9e6466fc1f8617c72fe1b6dae6a4cb7f44d7133e619d0e713f07b00c`. Baseline SHA-256 `ed2bf614d30a4b16ed0a599e2788314a4c896e179a3c70b7f3584ef99fd33e3b`; origem ZIP/commit documentado no BASELINE.

## API e limites

`referenced_source_ids` retorna objeto com source_ids, status, level e candidates. Níveis diferentes não são reduzidos a booleano silencioso. L0 mantém IDs completos literais; múltiplas citações exatas não sobrepostas são preservadas. L1 retira somente sufixo terminal __hash10 hexadecimal; stems menores que seis caracteres ficam excluídos de L1–L3. L2 aplica fold em ambos. L3 exige stem completo e cada underscore consome exatamente um caractere de palavra; não consome zero, dois, espaço, quebra de linha ou barra.

Candidatos competem pelo nível mais exato; empate inferido preserva candidates e devolve ambiguous sem source_ids. Inferências precisam começar célula/segmento de citação, para não usar palavras clínicas em comentários como se fossem nomes de fonte. A coluna Fonte é identificada pelo cabeçalho. L0 legada conserva a busca literal na linha; ausência explícita na linha prevalece.

`precision_rows` grava apenas estados nomeados e conserva todas as 2.392 linhas/claim_text. O catálogo agrega referências explícitas por célula e referências de precisão; mantém source_match_levels_by_id, status observados e política de união declarada. Uma declaração de ausência não apaga a documentação de outra célula da mesma cápsula. O contador de cápsulas com fonte declara que mistura níveis somente para inventário de identidade, não confiança clínica.

Limite importante: resolved significa associação documental no nível vencedor, não que todas as referências da célula foram identificadas. Fontes adicionais podem continuar não identificadas; nenhum resultado afirma que o documento foi aberto.

## Delta verificado — denominador fixo 2.392

| Estado | Antes | Depois |
|---|---:|---:|
| exact (antes denominado resolved) | 75 | 75 |
| stem | 0 | 245 |
| folded | 0 | 0 |
| placeholder | 0 | 5 |
| declared_no_source | 0 | 24 |
| ambiguous | 0 | 33 |
| unresolved_source_reference | 2.317 | 2.010 |

VERIFICADO: 250/2.392 novos vínculos (245 stem + 5 placeholder). A diminuição de 307 unresolved inclui esses 250 vínculos, 24 declarações legítimas de ausência e 33 ambiguidades; não comunicar 307 como novas resoluções. 75/75 vínculos legados e todos os seus IDs preservados.

## Divergências do estado herdado

CONFLITO: a família de nomes `Casos_Cli_nicos_P7_1` possui underscore adicional em relação a `Casos_Clinicos_P7_1`. O placeholder de exatamente um caractere não pode apagar esse caractere extra. Não foi criada regra de deleção, alias ou correspondência aproximada adicional para perseguir a estimativa de centenas de ganhos.

CONFLITO: a nota literal de metadata-only/supersessão ocorre em 4/17 claims, não 8/17; a proveniência de overlays clínicos permanece independente desta correspondência curricular.

PENDÊNCIA: não há 5 matches folded reais. A amostra tem 20 verificações lexicais reais, distribuídas como 5 controles exact, 10 stem e 5 placeholder. O requisito original de 5 por nível não é declarado satisfeito.

## Testes

O teste de proveniência mantém o denominador 2.392 e verifica igualdade entre CSV gerado e fonte, domínio de status, ausência explícita, IDs existentes no manifesto e preservação literal. A contagem congelada 2.317 foi substituída por esses invariantes, mediante autorização do usuário. O teste de fixture comportamental não foi alterado para remover seu skip; nenhuma fixture foi fabricada.

Verificação adversarial independente: 33/33 checks no RED_TEAM.json, incluindo casos sintéticos de folded e placeholder e invariantes sobre os dados reais. Esse denominador não substitui os 54 testes nem os 17 gates históricos.

VERIFICADO: cápsulas e registry clínico não foram modificados pelo matcher. DECISÃO HUMANA NECESSÁRIA: qualquer futura liberação clínica exige revisão da fonte e assinatura conforme o contrato.
