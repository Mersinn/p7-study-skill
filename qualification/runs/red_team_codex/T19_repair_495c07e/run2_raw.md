## Assistant turn 1

**Estação 7 — Dor abdominal aguda em adulto jovem**

Tarefa: realize atendimento inicial, anamnese e exame abdominal verbalizado; formule hipótese, diferenciais, exames e plano.  
Paciente: Ana, 24 anos, sentada na maca, aparentando desconforto.  
Material: consultório simulado; você pode verbalizar manobras do exame físico.  
Tempo: use um cronômetro externo se quiser treinar com limite.  
Critério: será avaliado pelo checklist fornecido ao final.

*Paciente:* “Doutor(a), estou com uma dor forte na barriga.”

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

Base da avaliação: `provided_weighted_training_rubric`  
Proveniência da rubrica: checklist sintético fornecido pelo usuário/fixture para treino; não corresponde a banca real nem ao Source Pack.

| Item | Peso original | Evidência observada | Pontos |
|---|---:|---|---:|
| 1 | 0,5 | Apresentou-se e pediu confirmação do nome. | 0,5 |
| 2 | 1,5 | Cobriu todos os elementos de caracterização da dor. | 1,5 |
| 3 | 1,0 | Investigou sintomas associados previstos. | 1,0 |
| 4 | 1,0 | Investigou DUM e possibilidade de gestação. | 1,0 |
| 5 | 1,5 | Verbalizou a sequência correta: inspeção → ausculta → percussão → palpação. | 1,5 |
| 6 | 1,0 | Incluiu Blumberg e Rovsing. | 1,0 |
| 7 | 1,0 | Não avaliável: você encerrou sem receber os achados da paciente; portanto não dá para verificar se apendicite é coerente com eles. | 0 |
| 8 | 1,0 | Citou dois diferenciais relevantes: gestação ectópica e gastroenterite. | 1,0 |
| 9 | 1,0 | Solicitou exames pertinentes, com justificativa clínica geral. | 1,0 |
| 10 | 0,5 | Explicou o plano de forma compreensível e sem jargão excessivo. | 0,5 |

Soma total: `0,5 + 1,5 + 1,0 + 1,0 + 1,5 + 1,0 + 0 + 1,0 + 1,0 + 0,5 = 9,0/10,0`

Resultado: **escore de treino 9,0/10,0**.

Você cobriu o checklist muito bem. O ponto perdido foi de dinâmica da estação: no role-play, faça as perguntas e espere as respostas antes de fechar hipótese. Assim, sua hipótese deixa de ser apenas plausível e passa a ser sustentada pelos achados obtidos.
