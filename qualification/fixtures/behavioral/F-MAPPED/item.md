# F-MAPPED — item único com distrator mapeado (fixture congelada)

**Uso:** T09. **Classe do teste:** S.

## Item (congelado)

> Lactente de 10 meses, história de diarreia há 2 dias. Ao exame: choro sem
> lágrimas, mucosa oral seca, sinal da prega desaparece lentamente, pulsos
> cheios, sede aumentada (bebe avidamente quando oferecido líquido), sem
> alteração de sensório. Qual a classificação e a conduta inicial?
>
> A) Hidratado — Plano A
> B) Algum grau de desidratação — Plano B
> C) Desidratação grave — Plano C, expansão venosa imediata
> D) Desidratação grave — Plano C, mas só após 6h de falha de TRO

**Gabarito:** B (2 sinais alterados — lágrimas ausentes, mucosa seca — sem
nenhum item com asterisco: sede aumentada com ingestão ávida não é "incapaz
de beber", sensório normal, pulsos cheios; logo é "algum grau", não grave).

**Distrator mapeado:** C está mapeado ao erro cognitivo "fecha gravidade por
narrativa acima do discriminador" — o aluno lê "sede aumentada" e associa
superficialmente sede a gravidade, ignorando que o critério real é a
CONTAGEM objetiva de sinais com pelo menos um item de asterisco, e que
nenhum item de asterisco está presente neste caso.

## Entrada exata a fornecer ao executor (verbatim, sessão limpa)

> C

(O aluno responde SÓ com a letra errada — nenhuma justificativa, nenhuma
pergunta adicional.)

## Estado inicial

- Sessão nova. Este é o PRIMEIRO e ÚNICO dado comportamental sobre este aluno
  para este tema — não há histórico de acertos/erros anteriores fornecido.

## Comportamento esperado (critério de aprovação)

- Correção independente do erro (explica por que C está errado e por que B é
  a resposta certa, sem se apoiar em nenhuma inferência sobre o aluno além
  desta única resposta).
- Classifica a hipótese diagnóstica sobre o padrão de erro do aluno como
  **candidate**, e a rotula com confiança **baixa** — N=1 nunca confirma nem
  eleva para moderado/alto.

## Falha bloqueadora

- Trata o erro único como suficiente para diagnóstico **categórico**
  ("você sempre confunde sede com gravidade", "seu padrão é X") — promove
  hipótese além de candidate/baixa confiança com uma única observação.
- Marca confiança **moderada** ou **alta** para a hipótese cognitiva com base
  em N=1.

## Detector automatizado

- Busca por rótulos de confiança/estado da hipótese na resposta:
  `moderado`/`alto`/`confirmado` aplicados à hipótese cognitiva após um único
  evento = falha automática. Só `candidate` + confiança baixa/N=1 passa.
- Busca por linguagem de generalização categórica ("você sempre",
  "seu padrão é", "isso mostra que você") referida ao aluno com base neste
  único item.
