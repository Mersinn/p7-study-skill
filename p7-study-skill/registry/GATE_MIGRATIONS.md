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
