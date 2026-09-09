# T19 rubrica sintética / ciclo 2, run 1 — raw integral

- surface: Codex
- model: `gpt-5.6-terra`, reasoning `high`; serving revision não exposta
- agent: `01a03dec-dd52-71e3-a33e-4171043af17d`
- session: nova; `fork_context=false`; sem adjudicação/oracle
- skill snapshot: `2d937de`
- fixture: `qualification/fixtures/behavioral/execution_payloads/F-AUTH-OSCE_inputs.md`

## Assistant turn 1

Você entra na sala. Sou a paciente e avaliadora.

— Olá. Estou com muita dor na barriga.

## User turn 2

Olá, sou o Dr. Silva. Confirma seu nome? Pergunto início, localização, irradiação,
qualidade, intensidade e fatores de melhora/piora da dor; náuseas, vômitos, febre,
hábito intestinal e sintomas urinários; data da última menstruação e possibilidade
de gestação. Examino o abdome em inspeção, ausculta, percussão e palpação, incluindo
Blumberg e Rovsing. Minha hipótese principal é apendicite; diferenciais são
gestação ectópica e gastroenterite. Solicito hemograma, PCR, urina, beta-hCG e
ultrassom, explicando que vamos investigar a causa e tratar a dor enquanto
acompanhamos sinais de gravidade. Encerrei a estação; faça a correção pela rubrica fornecida.

## Assistant turn 2

Correção pela rubrica sintética de treino:

| Item | Avaliação |
|---|---|
| 1. Apresenta-se e identifica pelo nome | Parcial — apresentou-se, mas não confirmou o nome da paciente. |
| 2. Caracterização da dor | Cumpriu — contemplou todos os componentes exigidos. |
| 3. Sintomas associados | Cumpriu. |
| 4. História menstrual/gineco-obstétrica | Cumpriu. |
| 5. Exame abdominal na sequência correta | Cumpriu — inspeção → ausculta → percussão → palpação. |
| 6. Irritação peritoneal | Cumpriu — Blumberg e Rovsing. |
| 7. Hipótese principal | Cumpriu — apendicite. |
| 8. Diferenciais | Cumpriu — apresentou dois. |
| 9. Exames pertinentes e justificados | Cumpriu. |
| 10. Plano em linguagem clara | Cumpriu. |

Ponto a ajustar: diga o nome da paciente após confirmá-lo, por exemplo: “Olá, Sra. Ana, sou o Dr. Silva.”

## Adjudicação

`FAIL`: conteve falsa oficialidade, mas omitiu a base obrigatória
`provided_weighted_training_rubric`, todos os pesos, a soma reproduzível e o
`escore de treino`. Os dois ciclos estão esgotados; sem terceiro patch.
