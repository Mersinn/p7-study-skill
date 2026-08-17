# ERROR_NOTEBOOK & REVIEW QUEUE — P7

Caderno de erros e fila de revisão.

Um erro só vale se virar **intervenção**. Registrar erro sem intervenção é
colecionar fracasso.

## 1. O que entra no caderno

Entra:

- erro com **movimento identificado** (ver `QUESTION_INTELLIGENCE_P7.md` §5);
- acerto frágil (chutou e acertou) — entra como **fragilidade**, não como erro;
- conduta vaga em cenário de alto risco;
- pivô perdido em caso ou minicaso;
- falha de sequência no drill de estado mental.

**Não** entra:

- erro em item ambíguo, incompleto ou inválido (o item é que está errado);
- erro de digitação ou desatenção sem padrão;
- movimento `INDETERMINADO` — sem evidência, não há o que registrar;
- erro de sessão técnica (quando se estava construindo a skill, não estudando).

Registrar `INDETERMINADO` como "lacuna de conteúdo" é a falha que o piloto
Diagnos 1C-A expôs. Ver `QUESTION_INTELLIGENCE_P7.md` §8.

## 2. Registro mínimo

```yaml
erro:
  data: ""
  disciplina: ""          # EISA_II | EISCA | EISM | CASOS | OSCE
  tema: ""
  operacao_exigida: ""
  movimento_realizado: ""
  confianca_do_diagnostico: ""   # baixa | moderada | alta
  evidencia: ""                  # o sinal OBSERVADO que sustenta
  intervencao: ""                # o que fazer diferente da próxima vez
  card_gerado: ""
  revisar_em: ""
```

`evidencia` é obrigatório e tem de citar algo que o aluno **produziu**. Se o campo
só puder ser preenchido com "ele não mencionou X", o registro não é válido.

## 3. Intervenção por movimento

Cada movimento tem uma intervenção própria. Genérico ("estudar mais") não conta.

| Movimento | Intervenção |
|---|---|
| lacuna de conteúdo | cápsula do tema + 3 minicasos |
| valor errado | card de dose/cutoff + conferir no slide original |
| regra mal-aprendida | reconstruir a regra a partir do caso, não decorar de novo |
| troca de comando | sublinhar o comando antes de ler as alternativas |
| erro de leitura | reler enunciado e listar dados antes de olhar alternativas |
| pivô perdido | treino de "qual o único dado que muda a conduta?" |
| analogia sem validação | "estrutura E função batem entre fonte e alvo?" |
| narrativa acima do discriminador | "qual a ÚNICA variável que separa as duas finalistas?" |
| fechamento precoce | forçar sequência completa antes do diagnóstico (drill EEM) |
| definitiva antes da inicial | separar sempre conduta inicial × definitiva |
| provável antes da perigosa | listar o diferencial perigoso primeiro |
| acerto frágil | refazer a questão em 48h sem consultar |

## 4. Fila de revisão

Revisão espaçada simples, ancorada em **erro**, não em calendário genérico:

- erro novo → revisar em **48h**;
- acertou na revisão → **7 dias**;
- acertou de novo → **21 dias**;
- errou de novo → volta para 48h e a **intervenção muda** (a anterior não funcionou);
- tema de risco clínico alto → nunca sai da fila; revisita mínima mensal.

Antes de prova: a fila é ordenada por `evidência de cobrança × risco clínico`, não
por data.

## 5. Cards

Gere card só quando ele **previne erro futuro**.

Tipos: pivô · conduta · pegadinha · distrator · diferencial perigoso · erro
pessoal · regra de prova · dose.

Nunca gere lote grande durante a correção. Um card bom vale dez genéricos.

Card de dose e cutoff só entra com o valor **verificado** (cápsula com
`Verificação independente: CONFIRMADO`). Valor não verificado vira card com
`confirmar no slide`.

## 6. Leitura do padrão

A cada ~10 erros registrados, produza uma leitura curta:

```text
Movimento dominante:
Disciplina/tema onde concentra:
Intervenção que já falhou:
Próxima intervenção:
```

Regras de honestidade:

- não declare padrão com menos de 3 ocorrências independentes;
- não conte o mesmo erro duas vezes por ter aparecido em duas questões do mesmo
  simulado;
- padrão inferido de auto-relato pós-gabarito tem teto de confiança **moderada**;
- se os movimentos estão espalhados sem concentração, diga isso — "sem padrão
  dominante" é um resultado legítimo.
