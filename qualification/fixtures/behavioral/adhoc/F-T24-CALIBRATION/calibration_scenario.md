# T24 — lote de revisão com calibração, linha corrupta, tempo (fixture congelada)

**Classe:** C.

**Dados reais gerados:** `.p7-state/events.jsonl` neste diretório —
13 pares confiança+resultado (hash real via `ledger.py`), 1 linha corrompida
inserida no meio. Reproduzível via
`python qualification/tools/build_calibration_fixture.py`.

## Composição do lote (congelada)

- **40 itens de revisão no lote** apresentados ao aluno simulado nesta
  sessão (enunciados completos no pacote de execução manual).
- **13 desses itens** têm confiança pré-tentativa registrada — 12
  independentes sem dica (válidos para calibração) + 1 assistido por dica
  decisiva (`hint_level: decisive`, deve ser EXCLUÍDO do cálculo).
- **1 linha corrompida** inserida no meio do ledger (hash adulterado) —
  corrompe em cascata o par confiança+resposta do item 6 (2 registros
  afetados: a linha em si + a descontinuidade de cadeia que ela causa no
  próximo evento).
- **Orçamento de tempo:** 25 minutos para o lote inteiro.

## Resultado esperado da projeção tolerante (verificado nesta sessão)

```json
{
  "status": "available",
  "sample_size": 11,
  "brier_score": 0.3075,
  "mean_confidence_bias": 0.095455,
  "exclusions": {
    "outcome_without_confidence": 1,
    "confidence_without_outcome": 0,
    "assisted_or_nonindependent": 1,
    "corrupt_records": 2
  }
}
```

`sample_size: 11` (não 12) é o comportamento CORRETO — a corrupção em
cascata de uma linha remove o par inteiro (confiança + resultado) daquele
item, não só a linha tocada. `assisted_or_nonindependent: 1` confirma que o
item com dica decisiva foi excluído do cálculo, como deve ser.

## Entrada exata a fornecer ao executor (verbatim, sessão limpa)

> Quero revisar meu lote de 40 itens pendentes hoje. Tenho 25 minutos.

## Estado inicial

- Sessão nova. `.p7-state/` deste fixture já populado como estado inicial
  (13 eventos + 1 corrompido).
- O executor NÃO recebe o resultado de calibração pronto — deve calculá-lo
  (ou invocar a projeção real) a partir do ledger.

## Comportamento esperado (critério de aprovação)

- Trata o lote como **finito** (40 itens, não abre um número indefinido de
  itens extras) e respeita o orçamento de 25 minutos.
- Reporta Brier score e viés médio **válidos** (batendo com os números
  verificados acima, ou reproduzindo o mesmo cálculo se novos itens forem
  respondidos na sessão).
- **Contém** a linha corrompida — não trava o lote inteiro por causa dela;
  reporta a corrupção separadamente (ex.: "1 registro não pôde ser
  validado e foi excluído do cálculo").
- Pista/dica decisiva **não gradua** — o item assistido não entra no
  cálculo de calibração.

## Falha bloqueadora

- Revisa mais ou menos de 40 itens sem declarar a mudança de escopo.
- Cálculo de Brier/viés opaco (não mostra amostra, ou números
  incompatíveis com o ledger real).
- **Inclui a linha corrompida** no cálculo como se fosse válida (contamina
  o resultado em vez de excluí-la e registrar a exclusão).
- Trava/recusa processar o lote inteiro por causa de uma única linha
  corrompida (deveria conter, não abortar tudo).

## Detector automatizado

- Verifica presença de `brier`/"Brier" e um número de viés na resposta
  final.
- Verifica menção explícita a registro(s) excluído(s)/corrompido(s) — sua
  ausência quando o ledger real contém corrupção é falha.
- Verifica que o item com `hint_level: decisive` não é citado como parte da
  amostra de calibração.
