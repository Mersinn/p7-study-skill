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

> **SUPERSEDIDO em duas rodadas posteriores no mesmo dia — ver §1b e §1c.**
> Esta entrada original fechou claims só com fonte SECUNDÁRIA (§1b corrigiu
> para fonte primária real) e a "cobertura 85,1%" abaixo incluía ligações
> espúrias por bug de tokenização (§1c corrigiu; número real: **76,9%**).
> Mantida por histórico — não usar os números desta seção como vigentes.

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

## 1b. Reabertura contra fonte PRIMÁRIA (2026-08-20, mesmo dia)

Correção obrigatória: fonte secundária (WebFetch de artigo de educação
médica) não é suficiente para fechar `current` — só descoberta, não
validação. Extração de texto real via PyMuPDF dos PDFs SBP "Diarreia Aguda
Infecciosa" e protocolo municipal Rio 2025 (ambos citando/reproduzindo
BRASIL/MS/SVSA "Manejo do paciente com diarreia", 2023). Detalhe completo em
`P0_P1_FIXES_LOG.md`.

**Achado real via leitura adversarial (não confirmatória):** o item-asterisco
de gravidade do domínio "sede" na cápsula estava descrito como "sede
ausente/bebe pouco" — o Quadro 2 primário mostra que "sem sede" é o valor do
**Plano A** (sem desidratação, o oposto), e o asterisco correto é "**não é
capaz de beber**" (incapacidade de ingerir líquidos). **Corrigido no texto da
cápsula** (4 ocorrências) — é um P1 real de classificação, não só um achado
de registro. Duas correções adicionais de precisão (zinco "14 dias" → "10-14
dias"; ondansetrona "0,2mg/kg" → "2mg (0,2-0,4mg/kg)", ambas confirmadas no
texto primário).

Os 5 claims da §1 foram **substituídos** (não duplicados) por 7 claims com
locator em fonte primária real: definição/duração, classificação por sinais
(corrigida), Plano B volume+falha 6h, Plano C expansão por idade incluindo
RN/cardiopata (antes pending, agora com locator real), zinco (corrigido),
ondansetrona (o quarantined da §1 foi **revertido** — o próprio documento
primário mostra as duas formas de dose, mg e mg/kg, como equivalentes, não
conflitantes), osmolaridade do SRO. Indicações de Plano C (íleo/abdome
agudo/vômitos biliosos) e taxa de SOG (20 mL/kg/h) permanecem `pending` — não
encontradas no texto primário lido nesta sessão.

## 1c. Auditoria adversarial da ligação ocorrência→claim (2026-08-20, mesmo dia)

Auditoria obrigatória (ver `DETECTOR_VALIDATION_REPORT.md` §9) encontrou e
corrigiu 4 bugs reais no mecanismo de ligação por token numérico — o mais
relevante para esta cápsula: citação de página ("p.24") tokenizava como
conteúdo clínico e ligava espuriamente a definição de diarreia (que
genuinamente contém "24h") ao claim de Plano C. Após as 4 correções:

| | §1 (secundária) | §1b (primária) | §1c (link corrigido) |
|---|---|---|---|
| Cobertura da cápsula | 85,1% | 83,3% | **76,9%** (7/34 linhas-denominador ainda não resolvidas, 18/78 ocorrências) |

A queda de 83,3% → 76,9% é a remoção de confiança falsa, não uma regressão —
essas ligações nunca foram válidas. **76,9% é o número vigente** para esta
cápsula.

---

## 2. Ritmo observado e projeção honesta

Uma cápsula bem fundamentada em diretriz única, com pesquisa real contra fonte
primária (múltiplas buscas + fetches + extração de PDF + leitura adversarial +
adjudicação + registro em schema), consumiu um ciclo de trabalho não trivial e
fechou 7 claims genuínos, com uma correção de conteúdo real (P0/P1) no
caminho. Após a auditoria de linkage (§1c), o denominador de alto risco não
resolvido está em **2 696** (up from 2 630 pré-auditoria — a auditoria reduziu
cobertura reportada, como deveria). Extrapolar
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

---

## 3. `capsule:eisca:sepse_e_meningite_neonatal` (2026-08-22)

**Rank no worklist pós-priorização por categoria:** #3, dominado por
`emergencia_sinal_alarme` (30 de 40 não resolvidos) — cápsula só camada B
(duas anotações de aula convergentes, sem slide do professor).

**Pesquisa realizada:** WebSearch para localizar diretriz/revisão real →
identificados protocolos institucionais e uma revisão de literatura da SPRS
(Sociedade de Pediatria do RS), "Boletim Científico de Pediatria" 2012
(Silveira RC & Procianoy RS). `WebFetch` direto falhou num PDF (erro de
certificado) e falhou em decodificar outro (stream binário); o segundo foi
salvo localmente e o texto extraído via **PyMuPDF** (mesmo método já
validado nesta sessão) — 7 páginas, 31.089 caracteres, leitura completa.

**Fechado (3 claims `current`, 1 `conflict`):**

| claim_id | Estado | Achado |
|---|---|---|
| `claim:sepse-neonatal.janela-precoce-tardia` | `current`, com nota | Fonte primária confirma a janela mas a descreve como faixa "48 a 72 horas", não um corte único. 72h (valor da cápsula) é a simplificação amplamente usada — não é erro, mas registrado como menos preciso que a faixa da fonte. |
| `claim:sepse-neonatal.amniorrexe-fator-risco-maior` | `current` | Confirmado exatamente (>18h) na Tabela 1 da fonte primária. O multiplicador "risco 4x" da cápsula não foi confirmado nem contradito nesta fonte. |
| `claim:sepse-neonatal.esquema-empirico-precoce` | `current`, com nota | Núcleo (ampicilina + gentamicina) confirmado textualmente. Penicilina G e amicacina como alternativas não foram citadas nesta fonte especificamente — mantidas sem alteração, não contraditas. |
| `claim:sepse-neonatal.febre-materna-limiar` | **`conflict`** | Achado real de divergência numérica: a cápsula usa **>38°C** (3 ocorrências, incluindo o pivô clínico central) para febre materna intraparto como fator de risco maior; a fonte primária usa **>37,5°C**. Não resolvido nesta sessão — pode ser variação real de protocolo, não erro. Cápsula **não alterada** até segunda fonte independente. |

**Achado explicitamente NÃO promovido:** o esquema empírico da sepse **tardia**
(a cápsula lista "oxacilina+cefepima OU vancomicina+meropenem OU
piperacilina+tazobactam") não foi confirmado — a fonte primária lida afirma
textualmente que **não há dados de estudos randomizados** que estabeleçam o
melhor esquema empírico tardio, e a escolha depende do perfil local de
resistência da UTI. Permanece `pending`. Também permanecem pending: critérios
de choque séptico, hemograma infeccioso (3/7 critérios), cinética de PCR,
meta de hematócrito, e o "escore de Rodwell" citado nas devolutivas (já
sinalizado como não localizado pela própria cápsula).

**Limitação de mecanismo observada e registrada:** a cobertura automática
desta cápsula em `CRITICAL_CLAIM_COVERAGE.csv` mostra 0% mesmo com 4 claims
registrados — não é um erro de registro. É o efeito esperado e aceito do
endurecimento da ligação numérica feito na auditoria da seção 9 do
`DETECTOR_VALIDATION_REPORT.md`: valores de tempo "nus" como "18h" não têm
caractere de unidade reconhecido por `numeric_tokens()` (que só reconhece
unidades de dose), então um único token bare como "18" não satisfaz mais
`is_material_match()` sozinho. Direção seguros (sub-contagem, não
super-contagem) — os claims estão genuinamente registrados e rastreáveis via
`registry/clinical_claims.jsonl`, só não aparecem no contador automático.
Não gera novo reparo no detector (já congelado) — registrado como limitação
conhecida do mecanismo de ligação, não do inventário de claims.

**Evidência nova no registry:** 1 `source` + 1 `source_version` (SPRS
Boletim, 2012), reutilizando o `reviewer` já registrado.

Pacote: 20/20 testes, reconcile 158 cápsulas, validate error=0 warn=36
info=2. Nenhum gate fechado.
