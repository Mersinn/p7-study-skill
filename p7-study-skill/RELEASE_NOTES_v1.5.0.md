# P7 Study Skill 1.5.0-rc.1

**Estado:** `HOLD`. Esta release candidate não autoriza merge, tag ou publicação.

## Escopo da v1.5.0

- integridade de gates baseada em artefato, SHA-256 e snapshot;
- inventário ocorrência → claim/disposição para todo o denominador crítico;
- runtime mais curto, com references carregadas sob demanda;
- separação operacional entre currículo, prática clínica atual e Learner State;
- proveniência estruturada e vocabulário normalizado;
- builder determinístico, auditoria de ZIP e instalação limpa do artefato final.

## Estado herdado

Os resultados comportamentais, longitudinais e clínicos da qualificação 1.0.0
foram preservados. Gates clínicos baseados em amostra foram reabertos porque não
demonstram cobertura do universo. O gate longitudinal permanece aprovado porque
seu bundle não mudou; comportamento e paridade P6 serão reexecutados somente nos
bundles afetados pela refatoração.

## Condição de finalização

Somente `VERSION = 1.5.0`, os 17 gates comprovados e o ZIP final validado permitem
`READY_FOR_RELEASE`. Isso ainda não significa merge ou publicação.
