# Auditoria de revalidação — P7 repair

Data: 2026-09-06T18:45:10.942839+00:00. Auditor: `agent:/root/release_auditor`.
Snapshot inicial: commit **DOCUMENTADO** `b0a9f23091e0cb92e97829e4d9d30fc05f51cf48`; Git HEAD não disponível no ZIP. Baseline medido em 2026-09-06T18:40:02.739134+00:00.

## Decisão

**PENDÊNCIA — a distribuição permite concluir e verificar o reparo de engenharia, mas não sustenta uma nova declaração de 17/17 gates reexecutados nem 54/54 testes aprovados.** Há 8/17 gates rechecáveis localmente e 9/17 dependentes de qualificação ausente. Nenhum gate foi executado/alterado por esta auditoria: é uma análise de executabilidade.

**VERIFICADO** — o baseline congelado registra 53/54 testes aprovados, 1/54 ignorado e 0/54 falhos. A execução não é regressão. O arquivo `scripts/release_evidence.py` só define funções: chamar `python3 scripts/release_evidence.py` termina sem reexecutar gate. A entrada funcional é `validate_gate_evidence(...)`, consumida por `scripts/validate_package.py`.

**DOCUMENTADO** — os 17/17 estados `passed`, 54/54 testes de repositório e as medições de jornadas são atestações v1.5.0, adjudicadas em 30/08/2026. Não foram reproduzidas nesta missão.

## Matriz de gates — universo fixo 17

| Gate | Baseline documentado | Denominador histórico | Nova verificação disponível |
|---|---|---:|---|
| `version_integrity` | passed | 1 | Mecânica local possível |
| `evidence_integrity` | passed | 1 | Mecânica local possível |
| `critical_inventory_complete` | passed | 3602 | Pendente: qualificação ausente |
| `high_risk_accounted` | passed | 2817 | Pendente: qualificação ausente |
| `p0_exposed_zero` | passed | 1 | Pendente: qualificação ausente |
| `p1_high_risk_exposed_zero` | passed | 1 | Pendente: qualificação ausente |
| `current_claim_traceability` | passed | 34 | Mecânica local possível |
| `behavioral_regression` | passed | 13 | Pendente: qualificação ausente |
| `p6_parity` | passed | 9 | Pendente: qualificação ausente |
| `longitudinal_resume` | passed | 2 | Pendente: qualificação ausente |
| `package_hygiene` | passed | 2 | Mecânica local possível |
| `clean_install` | passed | 1 | Mecânica local possível |
| `report_consistency` | passed | 1 | Mecânica local possível |
| `red_team` | passed | 7 | Pendente: qualificação ausente |
| `runtime_context` | passed | 6 | Pendente: qualificação ausente |
| `structured_provenance` | passed | 2392 | Mecânica local possível |
| `narrative_consistency` | passed | 1 | Mecânica local possível |

## Procedimentos e limites por gate

### version_integrity

Procedimento disponível: Conferir VERSION, registry e notas do candidato; não alterar o histórico v1.5.0.

Um candidato rc pode ter integridade de versão sem READY_FOR_RELEASE.

### evidence_integrity

Procedimento disponível: Importar validate_gate_evidence e executar validator standalone depois de congelar todos os substantivos e reconciliar.

Valida formato, hashes e coerência; não executa os testes alegados nos registros.

### critical_inventory_complete

Evidência necessária: 3602 ocorrências com mapping individual; qualification/reports/v1.5.0/INVENTORY_CLUSTERING_SUMMARY.json e inventário subjacente

Hash idêntico das cápsulas e registry indica preservação dos materiais; não reexecuta a contabilidade 3602/3602.

### high_risk_accounted

Evidência necessária: 2817 ocorrências high-risk com mapping individual e disposição; inventário/fixture de recuperação

Não reconstruir denominador por regex nova; isso mudaria o universo do gate.

### p0_exposed_zero

Evidência necessária: Casos e adjudicação do red team que desafiam recuperação clínica, com outputs brutos

Testes textuais de bloqueio são controles locais adicionais; não substituem qualificação de recuperação.

### p1_high_risk_exposed_zero

Evidência necessária: Casos e adjudicação do red team high-risk com outputs brutos

Ausência de alteração de cápsula não é nova prova comportamental de zero exposição.

### current_claim_traceability

Procedimento disponível: Verificar 34 claims current, suas FKs, evidence/locator/population/curricular_context/reviewed_at/reviewer_id e states; comparar bytes clínicos ao baseline.

Rastreabilidade estrutural; não revalidação humana/clínica dos 34 enunciados.

### behavioral_regression

Evidência necessária: MANIFEST original 24 casos, payloads/oráculos separados e harness dos 13 runs Codex (9 sentinelas + 4 core)

O manifesto original não vem no ZIP. Novos prompts não são rerun dos 13/13.

### p6_parity

Evidência necessária: Jornadas J01/J02/J03, três sessões válidas cada, baseline P6 e critérios originais

9/9 permanece histórico; preservar informação do 1 run histórico inconclusivo excluído.

### longitudinal_resume

Evidência necessária: Jornadas em duas sessões limpas e estados/ledgers originais para retomada 6→8

Testes unitários ledger não equivalem às duas sessões do gate.

### package_hygiene

Procedimento disponível: Executar build_distribution.py --verify-reproducible; comparar dois ZIPs e auditar entradas.

Preservar denominador 2 builds, sem incluir saída dentro da raiz do pacote.

### clean_install

Procedimento disponível: Extrair ZIP novo em diretório temporário; rodar reconcile --check e validate --json com --evidence-mode standalone.

Instalação estrutural pode funcionar em candidato HOLD; release gate precisa continuar bloqueado se gates abertos.

### report_consistency

Procedimento disponível: Cruzar relatório atual e delta com CSVs/counters canônicos e registrar cada número como novo ou herdado.

Não reutilizar 54/54 ou 17/17 herdados como medições novas.

### red_team

Evidência necessária: Amostra canônica de 37 linhas e sete alvos reparados: relatório, fixtures, adjudicação

O red team do matcher é novo escopo. Não reusar 7/7 como resultado desse escopo.

### runtime_context

Evidência necessária: Definição dos seis bundles e medidas v1.4/v1.5 em RUNTIME_CONTEXT_v1.5.0.json

Bytes md preservados provam ausência de alteração local; não reproduzem redução 36,74%–60,57%.

### structured_provenance

Procedimento disponível: Recalcular 2392 linhas, IDs estáveis, níveis, ausência declarada, ambiguidades e preservação dos 75 vínculos existentes; amostra independente.

2392/2392 contabilizadas não equivale a 2392 fontes resolvidas; matching não comprova conteúdo de PDF.

### narrative_consistency

Procedimento disponível: Rodar testes de contratos/narrativa e auditar consumidores/contagens atualizadas.

O teste de proveniência terá adaptação autorizada: relatar sua mudança e executar novos casos adversariais separadamente.

## Teste ignorado

`test_behavioral_manifest_separates_executor_payload_from_oracle` procura `../qualification/fixtures/behavioral/MANIFEST.json`, fora da raiz portátil. Exige schema `1.1.0`, 24/24 entradas e conjuntos disjuntos de arquivos de adjudicação/payload. O ZIP não distribui o manifesto, os payloads ou os oráculos. Criar 24 entradas fictícias apenas para satisfazer o teste seria falsificação de evidência de qualificação. Obter o checkout original é a correção legítima. Novos testes do matcher são um denominador adicional explícito, nunca substitutos do teste ignorado.

## Renovação correta de evidências standalone

1. Preservar integralmente os registros v1.5.0 (artefato, manifesto, release_gates e release_evidence) em `repair/` antes de qualquer renovação. Não editar nomes dos adjudicadores históricos ou suas datas.
2. Gerar relatório novo por gate com baseline_status, fresh_status, measurement_kind, before/after counts, command, exit_code, limitações e snapshot. Usar `not_reexecuted` na camada externa para o que não pôde ser medido; esse valor não pertence ao enum do registry de gates.
3. Se publicar um candidato completo, o estado honesto é `1.5.1-rc.1` e `HOLD`, com os gates não reexecutáveis `pending`. Todos os 17 IDs são preservados. Isso é uma pendência declarada de qualificação; não deve ser apresentado como regressão clínica ou desaparecimento da evidência histórica. Ao detectar qualquer queda de gate, respeitar a parada do contrato e não avançar silenciosamente às fases dependentes.
4. A atualização de atestações ativas só pode incluir os gates realmente passados no novo snapshot. Arquivar as antigas fora do arquivo ativo; deixá-las ativas para gates pendentes causa `EVIDENCE_ATTESTATION_ORPHAN`.
5. Usar snapshot `standalone`, contendo `package_manifest_path` e `package_manifest_sha256`, sem inventar Git HEAD. O commit b0a9… só identifica a origem histórica. Atestação nova identifica o agente real e timestamp real; limitações distinguem integridade mecânica de aprovação clínica.
6. Congelar alterações substantivas, gerar relatório de evidência pelo workflow de geração, rodar reconcile --write e --check. Hash do manifesto deve ser calculado após a reconciliação. O arquivo `registry/release_evidence.json` está excluído do manifesto para evitar ciclo; atualizá-lo por último não muda o snapshot. Artefatos em `artifacts/` não se editam manualmente conforme AGENTS.md.
7. Executar `validate_package.py --evidence-mode standalone --json` e `--release-gate --json`. No candidato HOLD, o segundo deve continuar vermelho por gates pendentes; estruturalmente válido não significa release aprovado. Não alterar o validador nem limiares para obter verde.

**CONFLITO** — se o orquestrador optar por preservar a versão 1.5.0 durante o reparo, as atestações históricas continuam legíveis, mas seus hashes de snapshot deixam de corresponder ao pacote modificado. Só anexar um delta não revalida a atestação ativa. Não emitir o ZIP modificado como 1.5.0 release verificado. Entregar patch + pacote candidato identificado é honesto; 1.5.1 final exige evidência faltante.

## Ataques de release prioritários

- Não trocar denominador de 2.392 linhas por quantidade apenas de linhas que conseguiram match.
- Não somar `declared_no_source` aos resolvidos. Separar exact/stem/folded/placeholder.
- Preservar múltiplos IDs exatos explícitos e detectar empate entre candidatos concorrentes; uma ambiguidade não pode apagar fonte já explícita sem declaração.
- Hash de cápsulas inalterado não comprova correção semântica do novo link L3. O red team do matcher verifica a identidade da referência, não sustentação clínica do documento ausente.
- Manter 34/52 current, 17/52 quarantined e 1/52 conflict se nenhuma revisão humana ocorrer; zero promoções é verificável por diff byte a byte do registry.
- Não promover Claude de not_evaluated; não adicionar sua superfície ao denominador Codex.

## Fecho de escopo

**VERIFICADO** — esta auditoria só leu arquivos de produção e criou `repair/RELEASE_AUDIT.md` e `repair/RELEASE_REQUIREMENTS.json`. Não editou release gates, registry, artefatos, versão, cápsulas ou testes. **DECISÃO HUMANA NECESSÁRIA** — revisão clínica humana continua obrigatória antes de qualquer promoção; autorização ampla de implementação não constitui leitura e assinatura de enunciados médicos.
