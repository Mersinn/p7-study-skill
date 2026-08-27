# Relatório final de qualificação — P7 Study Skill 1.0.0-rc.1

## Decisão

`READY_FOR_USER_REVIEW` — não autoriza merge nem publicação.

- Codex: **qualificado**.
- Claude: **não avaliado**; OAuth não contamina o denominador Codex.
- Conteúdo clínico: **liberável com quarentenas explícitas**.

## Evidência aritmética

- Testes: 28/28 no repositório; standalone 27 PASS + 1 SKIP esperado.
- Cápsulas reconciliadas: 158.
- Behavioral Codex controlador: 11/11 PASS — T05 3/3, T08 3/3, T16 3/3, T19 2/2.
- Jornadas: 10 runs = 9 PASS + 1 INCONCLUSIVE histórico; J01, J02 e J03: 3/3 PASS cada.
- Longitudinal: PASS; sessão B 6→8 eventos; SHA final `4726ea3931f109d244150518e38257596fb2d2a541936e856a6131f7a6848721`.
- Registry: 52 claims = 35 `current` + 16 `quarantined` + 1 `conflict`.
- Red team inicial: 32/32 = 2 P0 + 6 P1 + 1 P2 + 6 INCONCLUSIVE + 17 sem finding. Os 9 findings foram reparados; os 6 inconclusivos foram rebaixados a `quarantined`, não promovidos a PASS.
- Amostra final: 36 linhas = 10 current + 16 quarantined + 1 conflict + 3 históricas + 6 unregistered/pending; 35 alto risco + 1 baixo; 19 cápsulas.

## Resultado dos gates

Passaram: segurança de recuperação clínica, P0/P1 recuperável zero, sentinelas, core, longitudinal, jornadas e instalação limpa. Claims curriculares, pending, conflict e quarantined continuam estudáveis no painel curricular, mas bloqueados para prática atual.

O merge e a publicação são decisões do usuário.
