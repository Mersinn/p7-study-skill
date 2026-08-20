# CLAIM_ADJUDICATION_LOG — Fase 9.2/9.3, adjudicação por cápsula-tópico

Registro cronológico de cápsulas adjudicadas contra diretriz, em ordem de
prioridade por dano (`qualification/reports/CAPSULE_ADJUDICATION_WORKLIST.csv`).
Cada entrada documenta o que foi pesquisado, o que foi fechado, o que ficou
pendente e por quê. Nenhuma entrada aqui fecha `critical_claim_sweep`,
`p0_zero` ou `p1_high_risk_zero` sozinha — eles fecham quando o worklist
inteiro (Tier A) estiver resolvido ou explicitamente em quarentena.

Limitação estrutural declarada para todo este log: **este ambiente não tem
ferramenta de renderização/OCR de PDF** (`pdftoppm` ausente). Fontes primárias
em PDF escaneado ou comprimido (a maioria dos documentos oficiais do MS/SBP)
não podem ser lidas diretamente — só HTML/texto acessível via `WebFetch`. Isso
é contornado corroborando cada claim contra **múltiplas fontes secundárias
independentes**, datadas, que descrevem o mesmo documento primário com valores
numéricos explícitos — mas é uma base evidencial mais fraca que ler o PDF
primário diretamente, e está registrado em cada `source_version` afetada.

---

## 1. `capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao` (2026-08-20)

**Rank no worklist:** #1 (54 claims Tier A não resolvidos, o maior passivo do
pacote). **Fonte curricular original:** slide fotografado, Profa. Liane
Carvalho Viana, citando tabela do MS 2023.

**Pesquisa realizada:** WebSearch (MS Brasil diarreia + WHO diarrhoea plan A/B/C
2026) → identificação do documento primário "Manejo do paciente com diarreia"
(MS, atualização 2023, unificando MS/SBP/SBI). Tentativa de `WebFetch` direto
nos PDFs oficiais (SBP, Rio 2025, gov.br) — **falhou**: PDFs escaneados/
comprimidos, sem texto extraível neste ambiente. Dois artigos secundários de
educação médica (Estratégia MED, Grupo MedCof), ambos descrevendo a mesma
atualização MS 2023 com números explícitos, foram lidos com sucesso via
`WebFetch` e usados como evidência corroborativa cruzada.

**Fechado (5 claims, `registry/clinical_claims.jsonl`):**

| claim_id | Estado | Achado |
|---|---|---|
| `claim:diarreia-planos.plano-c-expansao-por-idade` | `current` | Correspondência **exata** com fonte secundária: 30 mL/kg em 1h + 70 mL/kg em 5h (<1 ano); 30 mL/kg em 30min + 70 mL/kg em 2h30 (≥1 ano) — inclusive o corte etário reformulado em 2023 de <5/≥5 para <1/≥1 ano, que a cápsula já usava corretamente. |
| `claim:diarreia-planos.plano-b-falha-6h` | `current` | Duas fontes secundárias confirmam o limiar de 6h para escalonar a Plano C. |
| `claim:diarreia-planos.classificacao-por-contagem-sinais` | `current` | Método de contagem por 5 domínios e corte de perda de peso >10% confirmados estruturalmente. |
| `claim:diarreia-planos.zinco-dose-idade` | `current`, com nota | 10mg/<6m e 20mg/≥6m confirmados; a cápsula usa duração fixa "14 dias" enquanto as fontes dizem "10-14 dias" — não é erro de segurança (14 está dentro do intervalo), mas fica anotado para correção editorial futura. |
| `claim:diarreia-planos.ondansetrona-dose-idade` | **`quarantined`** | Achado real de divergência de forma: a cápsula expressa a dose 6-24 meses por peso (0,2 mg/kg/dose); a fonte secundária do protocolo 2023 usa dose fixa por faixa etária (2mg). Numericamente convergem para uma criança típica (8-12kg → 1,6-2,4mg ≈ 2mg), então não há evidência concreta de erro — mas as duas formas não foram reconciliadas contra a fonte primária nesta sessão. As faixas 2-10 anos (4mg) e >10 anos (8mg) batem exatamente; só a faixa mais jovem ficou em quarentena. |

**Impacto mensurado:** denominador de claims críticos da cápsula 74 (v1.2.0);
não resolvidos caiu de 54 (pré-adjudicação) para **11** — cobertura de
rastreabilidade **85,1%** (era 0%). O salto além dos 5 claims registrados
ocorre porque a ligação detecção→claim usa tokens numéricos compartilhados: um
único claim de dose resolve todas as ocorrências duplicadas daquele mesmo
número na cápsula (tabela + card + palavras-âncora + conduta frequentemente
repetem o mesmo dado).

**Permanece pendente nesta cápsula (11 detecções, 3 famílias de claim):**
indicações objetivas de Plano C (perda >10%, contraindicação de TRO, choque,
vômitos biliosos, falha da TRO); expansão RN/cardiopata grave (10 mL/kg em
30min); osmolaridade do SRO (245 mOsm/L) e taxa de SOG (20 mL/kg/h). Nenhuma
fonte secundária lida nesta sessão continha esses números — não foram
promovidos sem locator real, conforme a regra de não inflar confiança.

**Evidência nova no registry:** 4 `source` + 4 `source_version` (MS 2023,
WHO/UNICEF joint statement, 2 artigos secundários), 1 `reviewer`
(`agent:qualificacao_p7:2026-08-20-claude`) — ver `registry/reviewers.json`.

---

## 2. Ritmo observado e projeção honesta

Uma cápsula bem fundamentada em diretriz única, com pesquisa real (múltiplas
buscas + fetches + leitura + adjudicação + registro em schema), consumiu um
ciclo de trabalho não trivial e fechou 5 claims/74 detecções. O worklist tem
**150 cápsulas com Tier A**, somando **2 378 ocorrências de alto risco ainda
não resolvidas** após este primeiro lote (era 2 441 antes). Extrapolar
linearmente não é seguro — cápsulas variam muito em quantas diretrizes
distintas tocam e em quão acessível é a fonte primária — mas o volume deixa
claro que **fechar `critical_claim_sweep` integralmente é um programa de
múltiplos blocos de trabalho, não uma tarde**. Isso confirma a leitura já
registrada em `CLINICAL_SWEEP_REPORT.md`: a distância até o gate é real e
grande, e cada cápsula fechada com rigor vale mais que muitas fechadas
superficialmente.

**Próximas cápsulas no worklist** (por dano, não resolvido Tier A):
`nefropatia_diabetica` (42), `sepse_e_meningite_neonatal` (40),
`osce_neurologia` (39), `osce_urologia` (37) — ver
`qualification/reports/CAPSULE_ADJUDICATION_WORKLIST.csv` para a lista
completa e ordenada.
