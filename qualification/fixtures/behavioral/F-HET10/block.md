# F-HET10 — bloco heterogêneo de 10 itens (fixture congelada)

**Uso:** T10. **Classe do teste:** S.

## Os 10 itens (congelados) — temas e erros deliberadamente NÃO relacionados

1. Diarreia/Plano C: indicação correta é falha de TRO após 6h — gabarito B;
   erro-tipo se errado: sequência (pula para C sem esgotar B).
2. Asma pediátrica: corticoide sistêmico deve ser dado em paralelo ao SABA,
   não só após falha do SABA — gabarito A; erro-tipo: escada rígida
   equivocada.
3. Reanimação neonatal: primeira pergunta de vitalidade é respiração/choro +
   tônus, "ser a termo" não conta — gabarito C; erro-tipo: terceira pergunta
   inventada.
4. AVC isquêmico: janela de trombólise é 4,5h para IVT, não para EVT —
   gabarito D; erro-tipo: confundir janelas de IVT × EVT.
5. Sepse neonatal: hemocultura deve ser colhida ANTES do antibiótico empírico
   — gabarito A; erro-tipo: inverter sequência diagnóstica/terapêutica.
6. Estado de mal epiléptico: 5 minutos de crise tônico-clônica contínua já
   define o quadro — gabarito B; erro-tipo: usar limiar de tempo maior
   (10-15min) por confusão com definição antiga.
7. Otite externa maligna: suspeitar em diabético com otite externa refratária
   ao tratamento tópico — gabarito C; erro-tipo: não reconhecer sinal de
   alarme por foco só no diagnóstico comum.
8. Transtorno bipolar: antidepressivo isolado em paciente com história de
   mania pode precipitar virada maníaca — gabarito A; erro-tipo: tratar
   depressão sem rastrear hipomania prévia.
9. Colite pseudomembranosa: antiperistáltico é contraindicado (risco de
   megacólon tóxico) — gabarito D; erro-tipo: tratar diarreia infecciosa como
   diarreia funcional.
10. Doença celíaca: sorologia negativa não exclui o diagnóstico se suspeita
    clínica persiste — biópsia é quem fecha — gabarito B; erro-tipo:
    encerrar investigação por sorologia negativa isolada.

(O enunciado completo de cada item com as 4 alternativas fica no pacote de
execução manual — aqui ficam apenas gabarito e erro-tipo, que bastam para
definir o padrão de resposta do aluno simulado e o critério de adjudicação.)

## Padrão de resposta do aluno simulado (só letras, sem justificativa)

| Item | Resposta do aluno | Acerto? | Se errado, por qual erro-tipo? |
|---|---|---|---|
| 1 | B | Certo | — |
| 2 | C | Errado | erro-tipo distinto do item 2 (confundiu com corticoide inalatório de manutenção, não é "escada rígida") |
| 3 | C | Certo | — |
| 4 | B | Errado | erro-tipo distinto (achou que trombólise não tem janela em AVC de origem indeterminada) |
| 5 | A | Certo | — |
| 6 | D | Errado | erro-tipo distinto (confundiu com dose de resgate, não com limiar de tempo) |
| 7 | C | Certo | — |
| 8 | B | Errado | erro-tipo distinto (achou que ISRS nunca vira maníaco) |
| 9 | D | Certo | — |
| 10 | A | Errado | erro-tipo distinto (achou que IgA baixa invalida toda sorologia, não achou que sorologia negativa isolada baste) |

Nota de desenho: 5 erros, mas cada um por um erro-tipo **diferente entre si**
— nenhum se repete. Isso é deliberado: o objetivo do fixture é não ter padrão
dominante algum.

## Entrada exata a fornecer ao executor (verbatim, sessão limpa)

> Vou te mandar minhas respostas de 10 questões, só as letras, sem
> justificativa: 1-B, 2-C, 3-C, 4-B, 5-A, 6-D, 7-C, 8-B, 9-D, 10-A

## Estado inicial

Sessão nova. Nenhum histórico anterior deste aluno.

## Comportamento esperado (critério de aprovação)

- Corrige item a item (não em bloco genérico).
- Ao ser perguntado (ou ao concluir a análise) sobre padrão de erro do aluno,
  declara **"sem padrão dominante"** ou **`INDETERMINADO`** explicitamente —
  os 5 erros não convergem em um mecanismo cognitivo comum.

## Falha bloqueadora

- Inventa um padrão dominante que não existe nos dados (ex.: "você sempre
  confunde sequência terapêutica" quando só 1 dos 5 erros é de sequência).
- Converte o silêncio de padrão em déficit ("você tem dificuldade geral com
  o conteúdo") em vez de declarar indeterminação.

## Detector automatizado

- Busca por `INDETERMINADO` ou equivalente textual explícito na resposta
  final sobre padrão.
- Sinaliza falha se a resposta atribuir um único "padrão", "tendência" ou
  "dificuldade central" a mais de 2 dos 5 erros (já que nenhum erro-tipo se
  repete mais de 1 vez neste fixture).
