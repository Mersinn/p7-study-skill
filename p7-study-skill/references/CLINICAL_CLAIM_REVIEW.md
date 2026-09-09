# Revisão de claims clínicos críticos

Este registro separa transcrição curricular de vigência clínica. A fonte de
verdade canônica é `registry/clinical_claims.jsonl`. Qualquer CSV é somente uma
view gerada e nunca deve receber edição manual como segunda fonte de verdade.

## O que entra na varredura

Extrair todo enunciado que contenha dose, concentração, unidade, corte, janela,
contraindicação, indicação de emergência, sequência terapêutica, critério de
internação/alta, algoritmo dependente de diretriz, calendário, dispositivo ou
afirmação OSCE apresentada como oficial.

Buscar tanto números quanto expressões absolutas: `sempre`, `nunca`, `obrigatório`,
`contraindicado`, `padrão-ouro`, `suspenso`, `zera`, `imperdoável`, `até X horas`,
`mg/kg`, `mL/kg`, `%`, `SpO2`, `FC`, `PA`, `RNI`, `ANC`.

## Estados ortogonais

- `curricular_status`: `checked`, `pending`, `conflict`, `not_applicable`.
- `clinical_validity`: `current`, `pending`, `historical`, `conflict`,
  `quarantined`, `jurisdiction_specific`.
- `self_review_l1`: `pending` ou `completed`.
- `independent_review`: `pending`, `agent_blind_pass`, `human_clinician_pass`.

`checked` e `CONFIRMADO` nunca promovem a vigência clínica. `pending`, `conflict`
e `quarantined` ficam excluídos de conduta atual pelo gate e só podem aparecer em
painel histórico ou como lacuna.

## Loop finito

1. Extrair claim e seu localizador curricular.
2. Fixar população, cenário e jurisdição.
3. Conferir fonte oficial atual/primária e registrar versão/data/localizador.
4. Segunda extração cega, com identidade do revisor. L2 por agente não equivale a
   humano; nunca alegar validação clínica humana sem ela.
5. Havendo divergência, fazer no máximo duas tentativas de resolução. Persistindo,
   marcar `conflict`/`quarantined` e abster.
6. Atualizar cápsula com painéis `Prática clínica atual` e `Para a prova/material
   histórico` separados.

## Proveniência desta rodada

- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta.
- Natureza: revisão por agente com fontes oficiais; revisão clínica humana não foi
  alegada e permanece pendente onde indicado.
