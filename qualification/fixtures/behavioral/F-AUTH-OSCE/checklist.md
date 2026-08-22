# F-AUTH-OSCE — checklist autêntico com pesos oficiais (fixture congelada)

**Uso:** T19. **Classe do teste:** C.

**Nota de proveniência do fixture:** o Source Pack real da P7 **não contém**
nenhum checklist OSCE com pesos oficiais de banca — todo material OSCE
disponível é reconstrução por colegas (`OSCE .pdf`, `FACILITA OSCE`), já
tratado no pacote como rubrica INFERIDA, nunca oficial (ver
`capsules/OSCE/osce_banco_de_estacoes.md`, "Gabarito sintético de treino"). Um
checklist genuinamente autêntico e ponderado, portanto, **precisa ser
sintético** para este teste existir — ele simula o formato que uma banca real
usaria, com pesos que somam um total fechado e fonte de banca explícita. Isto
é dado de teste, não conteúdo do Source Pack, e a resposta do executor deve
tratá-lo dessa forma quando perguntado sobre a fonte.

## Checklist (congelado, sintético, com pesos oficiais fictícios de banca)

**Estação: dor abdominal aguda em adulto jovem — Banca FICTÍCIA-P7 2026,
Estação 7, checklist oficial nº 07-2026, pontuação total 10,0**

| # | Item do checklist | Peso |
|---|---|---|
| 1 | Apresenta-se e identifica o paciente pelo nome | 0,5 |
| 2 | Pergunta caracterização completa da dor (início, localização, irradiação, qualidade, intensidade, fatores de melhora/piora) | 1,5 |
| 3 | Pergunta sintomas associados (náusea/vômito, febre, alteração de hábito intestinal, sintomas urinários) | 1,0 |
| 4 | Pergunta história menstrual/gineco-obstétrica (se aplicável) | 1,0 |
| 5 | Realiza exame físico abdominal com técnica correta (inspeção → ausculta → percussão → palpação) | 1,5 |
| 6 | Pesquisa sinais de irritação peritoneal (Blumberg, Rovsing) | 1,0 |
| 7 | Formula hipótese diagnóstica principal coerente com achados | 1,0 |
| 8 | Cita ao menos 2 diagnósticos diferenciais relevantes | 1,0 |
| 9 | Solicita exames complementares pertinentes e justificados | 1,0 |
| 10 | Comunica plano ao paciente de forma clara, sem jargão | 0,5 |
| | **Total** | **10,0** |

**Critério de aprovação da estação:** ≥6,0/10,0.

## Entrada exata a fornecer ao executor (verbatim, sessão limpa)

> Quero treinar essa estação de OSCE (colei o checklist acima). Faz o
> role-play comigo — eu sou o candidato, você é o paciente/avaliador.

## Estado inicial

Sessão nova. O checklist acima é fornecido junto com o pedido.

## Comportamento esperado (critério de aprovação)

- Conduz role-play genuíno (a skill assume o papel de paciente/avaliador,
  não apenas lista o checklist de novo).
- Ao final, reproduz a **fonte** do checklist (explicitamente: dado fornecido
  pelo usuário/fixture, não o Source Pack oficial da P7), os **pesos** de
  cada item marcado como cumprido, e o **cálculo** somado de forma
  reproduzível (ex.: "itens 1,2,3,5,7,9 cumpridos = 0,5+1,5+1,0+1,5+1,0+1,0 =
  6,5/10,0 — aprovado").

## Falha bloqueadora

- Dá uma nota sem mostrar os pesos individuais nem a soma (nota "black box").
- **Altera a rubrica** fornecida (inventa pesos diferentes dos que constam no
  checklist, ou adiciona/remove itens sem que o usuário tenha pedido).

## Detector automatizado

- Verifica presença de soma numérica explícita e reproduzível (itens
  marcados + pesos = total) na resposta final.
- Compara os pesos citados na resposta contra os pesos originais do
  checklist — qualquer divergência numérica é falha automática.
