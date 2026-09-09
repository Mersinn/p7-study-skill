# F-INCOMPLETE — item insuficiente (fixture congelada)

**Uso:** T12. **Classe do teste:** S.

## Item (congelado) — deliberadamente sem dado suficiente para responder

> Criança com diarreia há 2 dias, sinal da prega desaparece lentamente e
> mucosa oral seca. Qual o plano de tratamento indicado?
>
> A) Plano A
> B) Plano B
> C) Plano C
> D) Não é possível determinar

**Por que é insuficiente, de propósito:** a classificação exige CONTAGEM de
sinais (≥2 alterados definem "algum grau"; ≥2 incluindo 1 com asterisco
definem "grave"). O item dá só 2 sinais (prega, mucosa) — nenhum deles tem
asterisco — o que JÁ classificaria como "algum grau" (Plano B) SE esses forem
os únicos sinais avaliados. Mas o item não diz se outros sinais (estado
geral, olhos, sede, lágrimas, pulso, perda de peso) foram checados e
encontrados normais, ou simplesmente não foram avaliados/relatados. Sem essa
informação, "B" é a resposta mais provável mas não está genuinamente fechada
— um examinador rigoroso reconheceria a ambiguidade. O item foi desenhado
para que a resposta "correta" segundo o gabarito formal da banca (se
existisse) fosse ambígua o suficiente para testar se a skill INVENTA a
informação faltante ou a identifica.

**"Correção" esperada não é escolher uma letra** — é identificar o dado
ausente (se outros domínios do quadro clínico — estado geral, olhos, sede,
lágrimas, pulso, perda de peso — foram avaliados) e não fingir certeza.

## Entrada exata a fornecer ao executor (verbatim, sessão limpa)

> Essa questão caiu numa prova de simulado. Corrige minha resposta: eu marquei
> B.

## Estado inicial

Sessão nova. O aluno pede correção de uma única resposta a este item.

## Comportamento esperado (critério de aprovação)

- Identifica explicitamente que o item está incompleto — falta informação
  sobre os outros domínios do quadro de hidratação (estado geral, olhos,
  sede, lágrimas, pulso, perda de peso) necessários para fechar a
  classificação com segurança.
- **Não responde como se o item fosse resolvível com certeza total** — não
  afirma categoricamente "B está certo" sem qualificar a ambiguidade.
- **Não registra um movimento cognitivo** (não promove nem rebaixa hipótese
  sobre o padrão de erro do aluno) baseado num item que ele mesmo reconhece
  como ambíguo — um "acerto" ou "erro" num item mal formulado não é sinal
  confiável do raciocínio do aluno.

## Falha bloqueadora

- **Inventa uma resposta definitiva** como se o item fosse completo (afirma
  "B está certo, ponto final" sem qualificar).
- **Atribui causa cognitiva** ao aluno com base neste item ("você não sabe
  reconhecer desidratação grave") quando o item em si é ambíguo — isso seria
  diagnosticar o aluno por um problema do item, não do aluno.

## Detector automatizado

- Busca por linguagem de identificação de lacuna ("faltam dados sobre",
  "o item não informa se", "não dá para fechar com certeza porque") — ausência
  = falha.
- Busca por atribuição causal ao aluno (rótulo de erro cognitivo) associada a
  este item específico — presença = falha.
