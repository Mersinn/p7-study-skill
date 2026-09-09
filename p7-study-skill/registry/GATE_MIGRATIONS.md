# Histórico de migração de gates de release

Este arquivo preserva o histórico de gates que foram **substituídos**, para que
nenhuma substituição possa ser lida como aprovação. `registry/release_gates.json`
é a fonte de verdade do estado atual; este arquivo é a fonte de verdade da
*procedência* de cada gate.

Regra: um gate retirado **nunca** é registrado como `passed`. Ele é registrado
aqui como `superseded`, com motivo, autoridade e gate substituto.

---

## 2026-08-20 — `pilot_5_to_8_students_48h` → `scripted_user_journeys`

- **Estado do gate retirado:** `superseded` (jamais executado, jamais `passed`).
- **Estado histórico no momento da retirada:** `pending`, `evidence: []`,
  nota "Piloto humano não executado."
- **Autoridade:** decisão explícita do usuário (proprietário do produto), registrada
  no handoff de continuidade e no prompt mestre de qualificação da v1.0.0.
- **Motivo declarado:** não haverá recrutamento de colegas de turma nem dependência
  de participantes humanos como requisito de release. Feedback humano real
  permanece possível **após** o release, como observação opcional, e não bloqueia
  a v1.0.0.
- **Gate substituto:** `scripted_user_journeys` — jornadas sintéticas ponta a ponta,
  executadas pelo agente em sessões limpas, com perfis de estudante variados,
  entrada e estado inicial congelados, transcrições preservadas, repetições e
  adjudicação contra critérios objetivos.
- **O que a substituição NÃO transfere:** o gate novo não pode ser descrito como
  estudo de usabilidade humano, nem como validação por usuários reais, nem como
  evidência de preferência, carga subjetiva ou desejabilidade. Ele mede apenas
  comportamento observável do sistema: conclusão de tarefa, violações de
  sequência, revelação precoce, invenção diagnóstica, duplicação de revisão,
  abstenção correta e incidentes críticos.
- **Perda de cobertura assumida:** nenhum dado de experiência humana real integra
  a qualificação da v1.0.0. Isso é uma limitação declarada do release, não um
  requisito satisfeito.

---

## 2026-08-20 — correção de nota stale em `critical_claim_sweep`

- **Alteração:** a nota citava "103 cápsulas de alto risco"; o artefato
  determinístico atual (`artifacts/METRICS.json`, `capsules.by_risk.high`)
  registra **105**, após a criação das cápsulas de Aleitamento Materno e
  Semiologia Pediátrica.
- **Natureza:** correção de denominador stale. O gate **permanece `pending`**;
  nenhuma conclusão de varredura foi alterada, adiantada ou fechada.

---

## 2026-08-27 — migração da qualificação 1.0.0 para os gates v1.5.0

- **Autoridade:** contrato explícito do usuário para a v1.5.0.
- **Snapshot de origem:** `6fc906fdc2522c340a8d4f4c67a942f5c62433bb`,
  tree `ec5b387c72470d05eca505d4350e16049c3d9932`.
- `critical_claim_sweep`, `p0_zero` e `p1_high_risk_zero` foram reabertos e
  desdobrados em `critical_inventory_complete`, `high_risk_accounted`,
  `p0_exposed_zero`, `p1_high_risk_exposed_zero` e
  `current_claim_traceability`. A amostra clínica reparada permanece evidência
  válida de processo, mas não substitui 3.602/3.602 ocorrências.
- `behavioral_sentinels_3_of_3`, `behavioral_core_2_of_3` e
  `scripted_user_journeys` foram substituídos por `behavioral_regression` e
  `p6_parity`. Seus raws e adjudicações não foram apagados; os gates atuais
  ficam `pending` porque a v1.5.0 alterará o bundle de runtime.
- `longitudinal_resume_end_to_end` migrou para `longitudinal_resume` mantendo
  `passed`: ledger, schemas dependentes e fixture não mudaram neste snapshot.
- `clean_install` voltou a `pending`: a evidência herdada não testa o ZIP v1.5.0.
- Foram adicionados gates explícitos de versão, integridade de evidência,
  higiene, consistência de relatórios, red team, custo de contexto, proveniência
  estruturada e coerência narrativa.
- **Decisão após a migração:** `HOLD`. Nenhum PASS clínico foi transferido por
  narrativa e nenhum PASS comportamental histórico foi descartado.

---

## 2026-08-30 — fechamento verificável da v1.5.0

- Os 17 gates atuais foram fechados a partir de registros canônicos, hashes e
  denominadores explícitos; nenhum gate retirado foi convertido retroativamente em PASS.
- O inventário 3.602/3.602 e o alto risco 2.817/2.817 significam destino clínico
  explícito. `pending`, `quarantined` e `conflict` continuam bloqueados para prática atual.
- `READY_FOR_RELEASE` é somente o estado mecânico do registry. A decisão de produto
  é `READY_FOR_USER_REVIEW`; merge, tag e publicação não foram autorizados.
- Claude permaneceu `not_evaluated` por OAuth e não foi misturado ao denominador Codex.
