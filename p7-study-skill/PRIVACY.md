# Privacidade e dados do aluno

## Padrão local

O histórico longitudinal fica em `.p7-state/` no dispositivo do aluno. O ledger é append-only, usa cadeia de hashes para detectar alteração acidental e pode ser exportado em JSONL/CSV. O diretório é ignorado pelo Git e não integra manifestos de release.

Não há sincronização, telemetria, upload, Google Sheets ou MCP habilitado por padrão. O uso de um modelo hospedado ainda pode transmitir ao provedor aquilo que o próprio aluno inserir na conversa; aplicam-se os termos e controles desse provedor.

## Não registrar

- nome, prontuário ou outro identificador de paciente;
- caso clínico real identificável;
- credenciais, tokens ou links privados;
- notas pessoais de colegas sem consentimento.

Use casos anonimizados ou sintéticos. Para compartilhar o ledger, exporte somente os campos necessários e revise o arquivo antes do envio.

## Remoção

Apagar `.p7-state/` remove o histórico local e suas projeções. A operação não é executada automaticamente pela skill e não desfaz cópias que o aluno tenha exportado ou enviado a terceiros.
