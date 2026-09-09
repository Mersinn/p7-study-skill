# BEHAVIORAL_EXECUTION_BLOCKER — Marco B

**Data:** 24/08/2026 (registro consolidado)
**Branch vigente:** `qualification/v1.0.0-codex` @ `48d0e44`
**Snapshot da tentativa:** `f56a1e5`  
**Fixture tentada:** T10 / `F-HET10`  
**Fixture SHA-256:** `c4acba1b848ccf3f1b42feb0ad99a635853d7716c66f8f415de62fda4a979016`

## Evidência

A sessão foi criada em ambiente headless descartável, sem `--resume`, com a
skill copiada do commit atual e `Bash,Edit,Write` desabilitados. A entrada
enviada foi a entrada exata congelada da fixture T10. O executor devolveu:

```text
API Error: Unable to connect to API (ConnectionRefused)
is_error=true; num_turns=1; input_tokens=0; output_tokens=0
```

O raw integral está em
`qualification/runs/behavioral/T10/infra_attempt_api_error.json`.

## Classificação

`INCONCLUSIVO — bloqueio operacional de superfície/rede.` Não é PASS, FAIL ou
adjudicação clínica/pedagógica. A tentativa não recebeu tokens de entrada nem
produziu inferência; portanto não conta para 3/3.

O retry fora do sandbox exigiria autorização explícita para enviar o pacote de
skill e os dados das fixtures a uma API externa. Sem essa autorização, não há
execução headless comportamental reproduzível disponível neste ambiente.

## Impacto nos gates

- `behavioral_sentinels_3_of_3`: permanece `pending`;
- T10: permanece `INCONCLUSIVO`, sem consumir ciclo de reparo;
- T12, T15, T16, T17, T20, T21, T22 e T23: não executados;
- nenhuma conclusão de release foi promovida.

## Desbloqueio necessário

Uma nova rodada exige uma superfície local/offline compatível ou autorização
explícita para exportar estas fixtures e o conteúdo da skill ao executor remoto.
Até lá, os marcos locais continuam executáveis, mas não substituem a evidência
comportamental exigida pelo gate.

## Reteste autorizado — 24/08/2026

A autorização para exportação foi recebida e uma nova sessão limpa T10 foi
tentada com o mesmo fixture e o snapshot da branch. O CLI foi iniciado, mas a
inferência não começou: o executor retornou `401 OAuth access token has
expired`, com `input_tokens=0`, `output_tokens=0`, `num_turns=1` e
`total_cost_usd=0`. O raw integral está em
`qualification/runs/behavioral/T10/infra_attempt_oauth_expired_20260824.json`.

O fluxo oficial `claude auth login --claudeai` abriu a autorização no navegador
e parou aguardando código interativo; não houve ação de credencial simulada.
Assim, o bloqueio atual é autenticação expirada do executor, não falta de
autorização da rodada. T10 continua `INCONCLUSIVE`, sem consumir reparo e sem
promover qualquer gate.
