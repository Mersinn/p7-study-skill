# P7 Study Skill 1.5.0

**Estado dos gates:** `READY_FOR_RELEASE`. **Decisão de produto:**
`READY_FOR_USER_REVIEW`. Isso não autoriza merge, tag ou publicação.

## Escopo da v1.5.0

- integridade de gates baseada em artefato, SHA-256 e snapshot;
- inventário ocorrência → claim/disposição para todo o denominador crítico;
- runtime mais curto, com references carregadas sob demanda;
- separação operacional entre currículo, prática clínica atual e Learner State;
- proveniência estruturada e vocabulário normalizado;
- builder determinístico, auditoria de ZIP e instalação limpa do artefato final.

## Resultado fechado

- 54/54 testes do repositório passaram no snapshot final.
- Codex: 13/13 verificações comportamentais e 9/9 jornadas válidas passaram.
- Longitudinalidade: 2/2 sessões limpas válidas; a sessão B avançou de 6 para 8 eventos.
- Registry clínico: 52 claims = 34 `current` + 17 `quarantined` + 1 `conflict`.
- Claims `current`: 34/34 com rastreabilidade exigida.
- Inventário: 3.602/3.602 ocorrências primárias e 2.817/2.817 de alto risco têm
  destino explícito; pendência/quarentena não é promovida a prática atual.
- Claude permanece não avaliado por incompatibilidade OAuth, fora do denominador Codex.

## Condição de finalização

`VERSION = 1.5.0`, os 17/17 gates comprovados e o ZIP final validado permitem
revisão do usuário. O usuário ainda decide merge, tag e publicação.
