## Assistant turn 1

Estação iniciada.

Tarefa: conduza anamnese, verbalize o exame abdominal, formule hipótese/diferenciais, solicite exames e explique o plano à paciente.  
Tempo: não informado — use um cronômetro externo, se desejar.  
Paciente: Ana Luiza, 24 anos, em pronto atendimento por dor abdominal aguda.  
Material: apenas entrevista; descreva em voz alta o que faria no exame físico.  
Avaliação: rubrica sintética fornecida para treino, com pontuação ponderada.

*Paciente:* “Oi… estou com uma dor forte na barriga desde hoje.”

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
Proveniência da rubrica: checklist sintético/fictício fornecido pelo usuário para este treino; não é de banca real nem do Source Pack.

| Item | Peso original | Evidência observada | Pontos |
|---|---:|---|---:|
| 1 | 0,5 | Apresentou-se e confirmou a identificação. | 0,5 |
| 2 | 1,5 | Investigou todos os elementos solicitados da dor. | 1,5 |
| 3 | 1,0 | Perguntou todos os sintomas associados previstos. | 1,0 |
| 4 | 1,0 | Perguntou DUM e possibilidade de gestação. | 1,0 |
| 5 | 1,5 | Descreveu inspeção → ausculta → percussão → palpação. | 1,5 |
| 6 | 1,0 | Incluiu Blumberg e Rovsing. | 1,0 |
| 7 | 1,0 | Hipótese principal: apendicite. | 1,0 |
| 8 | 1,0 | Citou dois diferenciais relevantes. | 1,0 |
| 9 | 1,0 | Solicitou hemograma, PCR, urina, β-hCG e ultrassom, com justificativa geral pertinente. | 1,0 |
| 10 | 0,5 | Explicou investigação, analgesia e vigilância de forma compreensível. | 0,5 |

Soma total: `0,5 + 1,5 + 1,0 + 1,0 + 1,5 + 1,0 + 1,0 + 1,0 + 1,0 + 0,5 = 10,0/10,0`

Escore de treino: **10,0/10,0**.

Desempenho: estação bem estruturada, sem troca de tarefa e com sequência correta do exame abdominal. Para soar ainda mais natural no OSCE, faça as perguntas uma a uma e aguarde a resposta da paciente antes de seguir; ao solicitar exames, diga brevemente a finalidade de cada um.
