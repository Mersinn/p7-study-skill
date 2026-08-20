# Release candidate — P7 Study Companion v1.0.0-rc.1

Esta versão **não é a v1.0.0 final**. Ela recupera regressões funcionais da P6, introduz rastreabilidade e mantém a liberação bloqueada enquanto os gates clínicos e o piloto não forem concluídos.

## Engenharia de recuperação

- schemas canônicos versionados para cápsulas, claims, fontes, evidência de avaliação, eventos, hipóteses e revisão;
- enums normalizados para unidade, prioridade e risco, com aliases preservados;
- prioridade calculável por fórmula pública; rótulo legado não é tratado como prioridade calculada;
- inventário, manifesto, métricas, índice técnico e tabela de precisão gerados deterministicamente;
- ledger local append-only com retomada e agenda 48 h / 7 d / 21 d;
- acerto frágil, com pista ou não independente não promove estágio;
- Codex metadata, contrato de manutenção, privacidade e compatibilidade explícitos.

## Correção do inventário

O baseline auditado tinha 156 cápsulas físicas. “Semiologia pediátrica” e “Aleitamento materno”, embora anunciadas como as duas últimas, não existiam como arquivos autônomos: apareciam apenas parcialmente em cápsulas compostas. A recuperação adicionou ambas de forma rastreável, totalizando 158; a contagem final é derivada do filesystem e não está hardcoded no validador.

## Gates ainda obrigatórios

- zero P0;
- nenhum P1 clínico de alto risco aberto;
- claims críticos atuais com fonte/versionamento/localizador e revisão adequada, ou quarentena explícita;
- testes comportamentais e sentinelas aprovados;
- piloto de 5–8 colegas em duas sessões separadas por 48 h;
- instalação limpa comprovada.

`python scripts/validate_package.py --release-gate` deve falhar enquanto algum desses requisitos estiver aberto. MCP permanece fora desta release.
