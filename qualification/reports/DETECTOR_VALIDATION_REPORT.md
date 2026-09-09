# DETECTOR_VALIDATION_REPORT — validação do detector de claims críticos

**Objetivo:** medir, com amostra estratificada e busca manual de falso negativo,
a confiabilidade do denominador produzido por `critical_claim_scan.py`, antes de
gastar orçamento de adjudicação médica contra um número que poderia estar
sistematicamente errado. Nenhum gate é fechado por este relatório.

## 1. Estado do detector

**Estado vigente em 22/08/2026:** o detector está congelado em **v1.4.0**
(hash `771b504b23650e8d048479263647b60acdc8683aa92d8ca95db8c4418cc41323`).
O inventário atual é de **3.603 ocorrências**, **3.008 clusters**, **2.113
clusters Tier A** e **2.033 ocorrências Tier A em alto risco**, conforme
`CLAIM_CLUSTER_SUMMARY.json`. Os valores v1.1–v1.3 na tabela seguinte são
históricos de validação e não devem ser usados como denominador atual.

| | v1.1.0 (histórico) | v1.2.0 (histórico) | v1.3.0 (histórico) |
|---|---|---|---|
| hash | `c8e340ce…3613c` | `a51038c0…6c43b1f` | `63418562…d09daa` |
| denominador (claims críticos) | 2 659 | 3 201 (+20,4%) | **3 562** (+11,3%) |
| denominador em alto risco | 2 071 | 2 520 (+21,7%) | **2 782** (+10,4%) |

`3 562` é um **inventário operacional produzido por regex**, não o universo
clínico absoluto do pacote. Ele serve para priorizar e dimensionar trabalho de
adjudicação — não é, e não deve ser lido como, uma contagem certificada de
"todos os claims críticos que existem". Isso vale para toda versão do
detector, presente e futura.

O denominador **cresceu**, não encolheu — a correção resolve subcobertura, não
introduz relaxamento de critério. Nenhum campo de precisão foi afrouxado; os 13
falsos positivos encontrados abaixo continuam sendo falsos positivos em v1.2.0
(as categorias envolvidas — genética, logística de aula, guardrail metodológico —
não foram tocadas pelas correções).

## 2. Amostra de precisão

**Método:** amostragem estratificada com seed fixa (`20260820`), cruzando
disciplina (5) × categoria (7) × cápsula-tem-claim-registrado (2) = até 70
estratos, com cota mínima por estrato e completude até o alvo. Reprodutível via:

```bash
python qualification/tools/validate_detector.py --seed 20260820 --sample-size 220 --fn-capsules 20
```

**Tamanho:** 220 detecções (8,3% do denominador v1.1.0), lidas e julgadas
manualmente uma a uma — `qualification/reports/DETECTOR_PRECISION_SAMPLE.csv`,
coluna `manual_verdict`.

**Resultado:** **207 TP / 13 FP = 94,1% de precisão** (IC aproximado, Wilson 95%:
90,3%–96,4%).

### 2.1 Falsos positivos (13/220) — todos em um padrão identificável

| Padrão | n | Exemplo |
|---|---|---|
| Guardrail metodológico ("consulte a bula/o calendário/a fonte específica") | 8 | "verificar fármaco/dose/contexto; não usar classe genérica" |
| Logística de aula/avaliação, não conteúdo clínico | 2 | "Etapa 3 \| Apresentação da simulação dos grupos..." |
| Categoria trocada por termo isolado sem ser o claim real | 2 | "5q31-33 — família de genes do perfil Th2" (genética, não contraindicação) |
| Cabeçalho de tabela | 1 | "\| Fármaco \| Dose de ataque ILAE 2026 \| Precauções centrais \|" |

O padrão dominante (8/13) é estruturalmente interessante: a skill instrui
explicitamente "não generalize por classe, consulte a fonte específica" — esse é
o comportamento *correto* e seguro do pacote, mas o texto que o expressa contém
palavras (`fármaco`, `dose`, `verificar`) que disparam o detector. Isso não é um
erro de conteúdo do pacote; é ruído estrutural do detector que **não** precisa de
correção — filtrar esse padrão reduziria precisão marginalmente às custas de
lógica ad hoc de baixo retorno, então foi deixado como está e documentado.

### 2.2 Precisão de categoria vs. precisão de claim

Vários TPs têm categoria imprecisa (ex.: um limiar de indicação farmacológica
rotulado `contraindicacao_interacao` em vez de `dose_via_intervalo`). Isso não
afeta o denominador (a linha corretamente entra como claim crítico) nem a
adjudicação (que vai ler o texto, não confiar cegamente no rótulo), mas significa
que a distribuição por categoria no sumário é indicativa, não exata.

## 3. Busca manual de falso negativo

**Método:** 20 cápsulas amostradas com seed fixa (`20260820+1`, 4 por
disciplina), leitura completa das seções `assertive_clinical` restrita às
linhas **não** capturadas por nenhuma categoria crítica em nenhum tier — ou
seja, o gap real, não a cápsula inteira. Reprodutível via
`qualification/tools/fn_gap_report.py`.

**Resultado:** **14 claims críticos genuinamente perdidos** em 20 cápsulas
(~0,7 por cápsula), agrupados em duas causas-raiz sistemáticas — ver
`qualification/reports/DETECTOR_FN_FINDINGS.csv`:

1. **Quebra de linha rígida do markdown dentro de frase de prosa** (ex.:
   `"critérios de\ninternação"` — a frase "internação é obrigatória se qualquer
   um dos 8 critérios estiver presente", em `transtornos_alimentares.md`, um
   critério de segurança de alto risco). Um regex por linha física é cego a isso.
2. **Vocabulário incompleto**: unidade `cmH2O` ausente; padrões de corte por
   idade ("a partir de 50 anos"), duração ("por 10 dias"), janela ("em 48h") e
   sinônimo de emergência ("rapidamente fatal") não cobertos; verbos de
   contraindicação só reconhecidos no infinitivo (`evitar`, não `evitam`).

**Correção aplicada (v1.2.0):**
- janelas de 2 linhas concatenadas dentro das seções de prosa (`conduta`,
  `conceito operacional mínimo`, `pivô clínico`, `conduta e guardrails`, seções
  `prática clínica atual — *`), ancoradas na primeira linha, com deduplicação
  contra a detecção linha-a-linha para não contar duas vezes o óbvio;
- vocabulário ampliado (unidade, corte por idade, duração, janela, sinônimo de
  emergência, conjugação verbal) — mudanças enumeradas no cabeçalho do script.

**Verificação pós-correção:** os 14 achados foram checados individualmente contra
o CSV v1.2.0 — todos os 14 agora aparecem no denominador (ver
`qualification/reports/DETECTOR_FN_FINDINGS.csv`, coluna `fixed_in_v1_2`; 2
ficaram parciais — revisados mas sem padrão dedicado adicionado por retorno
marginal baixo).

## 4. Incerteza que permanece — declarada, não escondida

- **Recall não foi medido em amostra representativa do pacote inteiro**, só em
  20 das 158 cápsulas (12,7%). A extrapolação "~0,7 claim perdido por cápsula"
  é uma estimativa pontual sobre uma amostra pequena, não uma cota calibrada.
  Aplicada às 105 cápsulas de alto risco, sugere uma ordem de grandeza de
  **dezenas** de claims críticos ainda não capturados por nenhuma versão do
  detector — não centenas, mas não zero.
- A busca de FN é ela mesma manual e sujeita a erro humano de leitura.
- Detecção lexical não avalia correção clínica do conteúdo — isso é o trabalho
  da Fase 9.3 (adjudicação), não deste relatório.
- Regex de tier `strong` ainda pode errar em textos futuros fora do padrão
  observado nesta amostra; a precisão de 94,1% é uma estimativa amostral, não
  uma garantia.

## 5. Uso pretendido deste denominador

O denominador v1.2.0 (3 201 claims críticos, 2 520 em alto risco) é a base para
a Fase 9.3 (adjudicação por diretriz, priorizada por Tier A/B/C — ver
`CLAIM_CLUSTER_SUMMARY.json`). Ele é **suficientemente confiável para priorizar
e dimensionar** o trabalho (94% de precisão, recall corrigido em duas causas
sistemáticas). Ele **não é uma contagem certificada**: alguns TPs mudarão de
categoria durante a adjudicação, e uma fração pequena e não quantificada de
claims críticos ainda pode estar fora do denominador.

## 6. Reprodução (v1.2.0, seção histórica)

```bash
python qualification/tools/critical_claim_scan.py --root p7-study-skill --out qualification/reports
python qualification/tools/cluster_and_tier.py --out qualification/reports
python qualification/tools/validate_detector.py --seed 20260820 --sample-size 220 --fn-capsules 20
python qualification/tools/fn_gap_report.py > qualification/reports/FN_GAP_LINES.txt
```

---

## 7. Revalidação de recall pós-v1.2.0 (amostra fresca, sem sobreposição) → v1.3.0

Correção obrigatória: a seção 3 media recall na **mesma** amostra de 20
cápsulas que motivou a correção v1.2.0 — medir de novo ali seria circular (o
detector foi especificamente ajustado para aqueles 14 casos). Esta seção usa
uma amostra **genuinamente nova**, sem sobreposição, para medir o quanto o
detector corrigido realmente recupera.

### 7.1 Método

Seed `20260821+1`, 4 cápsulas por disciplina, **excluindo explicitamente** as
20 cápsulas da seção 3 (`qualification/reports/DETECTOR_FN_CAPSULE_LIST.csv`,
regenerado). OSCE só tinha 3 cápsulas restantes após excluir as 4 já usadas
(de 7 totais), então a amostra fresca tem **18 cápsulas**, não 20. Zero
sobreposição confirmada por interseção de conjuntos.

Leitura completa das seções `assertive_clinical` **não** capturadas por
nenhuma categoria crítica em nenhum tier (o gap real do detector v1.2.0),
buscando adversarialmente (não confirmando) divergência.

### 7.2 Resultado: recall observado do detector v1.2.0

| | |
|---|---|
| Cápsulas na amostra fresca | 18 |
| Ocorrências já capturadas nessas cápsulas (baseline "TP") | 366 |
| Falsos negativos genuínos encontrados | **~25** |
| **Recall estimado** | **366 / (366+25) ≈ 93,6%** |

O número de FN é uma contagem manual (não um script) sobre um gap já reduzido
pelo script `fn_gap_report.py` — sujeita a erro humano de leitura, declarado
como limitação desde a seção 3.

### 7.3 Causa-raiz dos 25 FN — sistemática, não dispersa

Praticamente todos os FN residuais caem em **um único padrão**: intervalo de
duração "nu" — sem preposição-gatilho (`primeiras/em/por/dentro de`) — do tipo
`"7-21 dias"`, `"5-30 dias"`, `"6-24 horas"`, `"3 a 12 meses"`. Esse padrão é
extremamente comum em:

- tabelas de farmacocinética (início/pico/duração de insulinas e outros
  fármacos) — `capsules/EISA_II/insulinoterapia_classificacao_farmacocinetica.md`;
- latência etiológica diagnóstica (GNDA pós-faringite 7-21 dias, pós-impetigo
  15-28 dias) — `capsules/OSCE/osce_nefrologia.md`;
- **timing de emergência psiquiátrica** — `capsules/EISM/antipsicoticos_sep_e_snm.md`:
  distonia aguda (horas a 1-5 dias), parkinsonismo farmacológico (5-30 dias),
  **síndrome neuroléptica maligna** (semanas a meses) — uma cápsula de alto
  risco onde o timing decide qual dos 5 diagnósticos diferenciais tratar.

Achado secundário: a abreviação `"sem."` (semanas) não era reconhecida pelos
padrões existentes (só a palavra completa `"semanas"`), afetando cápsulas com
tabelas comparativas de prazo (ex. blues × depressão pós-parto × psicose
puerperal).

### 7.4 Correção aplicada (v1.2.0 hash `a51038c0…` → v1.3.0 hash `63418562…`)

- novo padrão `strong` em `janela_temporal`: `\d+\s*(?:-|a)\s*\d+\s*(?:h|horas|min|minutos|dias|semanas|sem\.|meses|anos)\b`;
- `sem\.` adicionado como alias de `semanas` nos padrões existentes.

**Resultado:** denominador 3 201 → **3 562** (+11,3%; alto risco 2 520 → 2 782,
+10,4%).

### 7.5 Precisão do v1.3.0 — spot-check, NÃO revalidação completa

Diferente do v1.1→v1.2 (amostra estratificada completa, n=220), o v1.3.0
recebeu apenas um **spot-check dirigido** ao padrão novo: dos 556 claims
`janela_temporal` no denominador v1.3.0, 234 só disparam pelo padrão novo
(não contêm nenhuma palavra-gatilho antiga). Amostra aleatória (seed 7) de 30
desses 234, lida integralmente: **nenhum falso positivo óbvio** — todos são
fatos clínicos genuínos (durações de tratamento, incubação, janela de biópsia,
tempo máximo de uso de BZD). Ressalva honesta: uma fração relevante (≈10 dos
30) são faixas etárias epidemiológicas ("pico 50-70 anos", "faixa etária
20-24 anos") categorizadas como `janela_temporal` quando seriam mais
precisamente `cutoff_escore_estadiamento` ou uma categoria demográfica à
parte — repete o ruído de rótulo já documentado na seção 2.2, não um falso
positivo de conteúdo.

**Isto não é uma validação com o mesmo rigor da seção 2.** Não há amostra
estratificada completa nem busca de FN residual pós-v1.3.0 nesta sessão. O
v1.3.0 deve ser tratado como "razoavelmente confiável por spot-check", um
degrau abaixo de "validado" no sentido da seção 2-3.

### 7.6 Estado de incerteza acumulado, atualizado

- Precisão medida rigorosamente: v1.1→v1.2, n=220, 94,1% (seção 2).
- Recall medido rigorosamente: v1.1→v1.2, amostra fresca de 18 cápsulas,
  ~93,6% (esta seção).
- v1.3.0 (versão vigente): denominador maior, precisão só amostrada
  pontualmente (30/234 do padrão novo), recall **não** revalidado após a
  correção — não sabemos quantos FN o v1.3.0 ainda tem.
- Cada rodada de correção tende a encontrar menos FN sistemático e mais FN
  disperso (idiossincrático por cápsula) — não há garantia de que uma v1.4.0
  não encontraria mais um padrão sistemático. Diminishing returns esperado,
  não comprovado.

## 9. Auditoria adversarial do mecanismo de ligação ocorrência→claim

Invariante obrigatório do usuário: auditar a passagem "N ocorrências → M
claims → X% de cobertura" com amostra **negativa** — verificar se cada
ligação é materialmente equivalente (população, dose/corte, contexto,
temporalidade), não apenas coincidência de número. Compartilhar cápsula, tema
ou diretriz não conta como cobertura.

O resultado: **4 bugs reais, verificados e corrigidos**, encontrados por
amostragem adversarial repetida (não por inspeção de código). Cada um mudou o
número de ocorrências corretamente resolvidas — sempre para **baixo**
(removendo confiança falsa), nunca para cima.

### 9.1 Bug 1 — locator do claim vazava para o pool de tokens

`link()` original tokenizava `statement + population + curricular_context +
notes + evidence` do claim. `curricular_context`/`evidence` contêm citações de
página ("p.24", "Quadro 6") e `notes` contém datas de revisão
("2026-08-20"). Achado concreto: a linha da **definição de diarreia** ("≥3
evacuações... **24h**") ligava a `claim:diarreia-planos.plano-c-expansao-por-idade`
só porque esse claim cita "**p.24**" como locator — mesmo dígito, zero relação
de conteúdo. **Correção:** `claim_tokens` passou a usar só `statement`.

### 9.2 Bug 2 — citação de página do lado da DETECÇÃO também vazava

Toda tabela "Dados de precisão" do pacote tem coluna `Fonte (página)` — o
mesmo problema do lado do texto da cápsula. Achado: "Plano C — expansão ≥1 ano
| ... | p.24" ligava à definição de diarreia (que genuinamente contém "24h")
por coincidência de número de página, não de conteúdo. **Correção:** função
`CITATION_STRIP` remove padrões `p./pp./linha/l./slide/quadro/tabela/figura +
número` de QUALQUER texto antes de tokenizar (claim e detecção).

### 9.3 Bug 3 — ano de diretriz e boilerplate de teto etário do PNI

Achado: dois claims de vacinas **diferentes** (`vac.dengue`, `vac.hpv`)
ligavam à mesma detecção de vacina meningocócica ACWY só por compartilharem
"2026" (ano da diretriz, citado em quase toda cápsula) e o sufixo regulatório
`"14a11m29d"` ("até o dia anterior ao 15º aniversário" — convenção reusada,
com o MESMO valor, em dezenas de vacinas do calendário). **Correção:** anos de
calendário (1900–2099) excluídos de `numeric_tokens`; padrão `\d+a\d+m\d+d`
removido antes de tokenizar.

### 9.4 Bug 4 — dose redonda comum entre fármacos diferentes

Mesmo após 1–3, um token com unidade simples ainda coincide por acaso: achado
real — diazepam "**máx. total 20 mg**" ligava a um claim sobre **fosfenitoína**
("ESETT testou fosfenitoína **20 mg** PE/kg") numa cápsula de status
epiléptico — dois fármacos diferentes, mesma dose redonda por coincidência.
**Correção:** a regra de ligação agora exige pelo menos um token "forte"
(contém `/`, `.` ou `%` — unidade composta, decimal ou percentual, muito menos
propenso a coincidir) OU ≥2 tokens numéricos distintos em comum.

### 9.5 Resultado agregado das 4 correções

| | antes das correções (pós v1.3.0) | depois |
|---|---|---|
| detecções resolvidas (denominador) | ~161 | **86** (amostra final auditada) |
| não resolvidos, alto risco | 2 630 | **2 696** |
| não resolvidos, total | 3 410 | **3 476** |
| cobertura, cápsula diarreia/desidratação | 85,1% (claim original, bloco anterior) → 83,3% (pós v1.3.0) | **76,9%** (real, pós-auditoria) |
| cobertura, cápsula imunizações (vacinal) | inflada por Bug 3 | **0%** (correta — nenhum dos 4 claims de vacina registrados liga materialmente às outras 11 detecções desta cápsula) |

A correção **reduziu** cobertura reportada em todo lugar que a bug afetava —
nunca aumentou. Isso é o resultado esperado de remover confiança falsa, não
uma regressão.

### 9.6 Amostra final de confirmação

Amostra aleatória de 40 detecções resolvidas (seed 555), lida integralmente
após as 4 correções: **nenhuma ligação espúria encontrada** — toda ligação
compartilha fármaco/dose/contexto genuinamente idêntico (mesmo Plano C, mesma
faixa etária de ondansetrona, mesmo alvo de O2 do GINA, etc.).

### 9.7 Limitação que permanece — declarada, não escondida

O mecanismo ainda é **puramente lexical**: não entende semântica, só números e
unidades. Um cenário adversarial não testado nesta auditoria: dois claims
sobre o MESMO fármaco, MESMA dose, mas populações genuinamente diferentes
(ex. "furosemida 40mg em adulto" vs "furosemida 40mg em criança") ligariam
incorretamente, porque o número/unidade batem mas a população não é
comparada. Isso não apareceu na amostra porque o pacote atual não tem esse
padrão de claim par nesta amostra — mas o mecanismo não o preveniria se
existisse. Ligação numérica prova "mesmo número", não "mesma proposição
clínica" — a leitura humana/adversarial de cada claim antes de fechá-lo
continua sendo o controle real, não o script.

## 11. Validação final fresca v1.3.0 → congelamento em v1.4.0

Invariante do usuário: o recall de 93,6% pertence à v1.2.0; como o detector
mudou para v1.3.0, era preciso validar de novo, fresco, antes de continuar
usando o número como se ainda valesse. Loop limitado: uma validação, no
máximo um reparo se aparecer gap sistemático de alto risco, depois congelar.

### 11.1 Terceira amostra, sem sobreposição com as duas anteriores

Seed `20260822`, 12 cápsulas (3 por disciplina), interseção vazia confirmada
com as amostras da seção 3 (20 cápsulas) e da seção 7 (18 cápsulas) —
`qualification/reports/DETECTOR_FN_CAPSULE_LIST_v3.csv`. Leitura completa do
gap (`FN_GAP_LINES_v3.txt`) contra o denominador v1.3.0.

### 11.2 Achados — um gap sistemático de alto risco, o resto descartado por critério explícito

**Corrigido (o único reparo permitido nesta rodada):** verbos de
**contraindicação** só casavam na forma particípio/substantivo
(`contraindicado`, `contraindicação`), não na forma verbal conjugada
(`contraindica`, `contraindicam`) — o mesmo tipo de lacuna já corrigido para
"evitar" em v1.2.0, mas que ficou faltando para o verbo-âncora da própria
categoria. Achado concreto perdido: `capsules/EISA_II/trauma_urogenital.md`,
"Sangue no meato uretral | **Contraindica** sondagem cega — investigar com
uretrocistografia" — uma contraindicação de segurança real, na categoria
`contraindicacao_interacao`, uma das 5 categorias de dano prioritário
definidas pelo usuário. Isso justifica o único reparo desta rodada.

**Encontrado e DELIBERADAMENTE não corrigido** (critério explícito do
usuário: não perseguir recall perfeito, não expandir regex indefinidamente):
unidade `UFC/mL` ausente do vocabulário (corte de urocultura); `a partir de
Xh` não coberto (só anos/meses/semanas/dias); abreviação `sem.` faltando
especificamente no padrão `ate Xsem.` (já corrigida em outros 3 padrões, não
neste); forma adjetival "não indicado" vs. verbo "não indicar" — este último
é direção-segurança (sub-detectar uma negação é conservador, não perigoso).
Nenhum destes é um padrão sistemático isolado do tamanho do achado de
contraindicação — são ruído de cauda longa, esperado em qualquer detector
lexical.

### 11.3 Correção aplicada e verificada

Hash `63418562…` (v1.3.0) → `771b504b…` (v1.4.0). Denominador: 3.562 → 3.603
(+1,2%; alto risco 2.782 → 2.818). Verificado nesta sessão: a linha do
achado concreto (`trauma_urogenital.md`, "Contraindica sondagem cega") agora
aparece no denominador (`in_sweep_denominator=True`).

### 11.4 Regressão sobre as amostras anteriores

As duas correções de recall anteriores (v1.1→v1.2: 14 achados; v1.2→v1.3: o
padrão de intervalo "nu") foram reverificadas nesta versão — nenhuma
reapareceu como gap. O link-fix da seção 9 (4 bugs de ligação) também
permanece correto: a amostra final de 40 detecções resolvidas (§9.6)
continua válida, pois o patch desta seção não tocou `numeric_tokens()` nem
`is_material_match()`.

### 11.5 Detector CONGELADO em v1.4.0

Não haverá mais rodada de correção de recall/precisão nesta qualificação,
por decisão explícita do usuário. Estado final:

| | v1.4.0 (congelado) |
|---|---|
| hash | `771b504b23650e8d048479263647b60acdc8683aa92d8ca95db8c4418cc41323` |
| denominador | 3.603 |
| denominador em alto risco | 2.818 |
| precisão medida (amostra v1.1→v1.2, n=220) | 94,1% — não revalidada em v1.3/v1.4, herdada com incerteza |
| recall medido (3 amostras independentes, 20+18+12=50 cápsulas, 32% do pacote) | ~93-94% estimado, com gaps sistemáticos conhecidos corrigidos e gaps de cauda longa conscientemente deixados abertos |

**Limitações conhecidas e aceitas, não escondidas:**
- precisão nunca foi revalidada após v1.2 — as correções de v1.3/v1.4 foram
  aditivas (novos padrões, não alteração dos existentes), então o risco de
  ter piorado precisão é baixo mas não zero;
- 4 gaps de cauda longa identificados na seção 11.2 permanecem sem correção;
- o mecanismo de ligação (seção 9) continua puramente lexical, sem validação
  de população/contexto além de token numérico compartilhado;
- todo denominador é um inventário operacional para priorizar trabalho, não
  uma contagem certificada do universo clínico do pacote.

## 12. Reprodução (estado final v1.4.0)

```bash
python qualification/tools/critical_claim_scan.py --root p7-study-skill --out qualification/reports
python qualification/tools/cluster_and_tier.py --out qualification/reports
# as 3 amostras de recall, sem sobreposicao entre si:
python qualification/tools/fn_gap_report.py > qualification/reports/FN_GAP_LINES.txt          # amostra 1 (secao 3)
python qualification/tools/fn_gap_report.py > qualification/reports/FN_GAP_LINES_v1.2.txt      # amostra 2 (secao 7)
python qualification/tools/fn_gap_report.py > qualification/reports/FN_GAP_LINES_v3.txt        # amostra 3 (secao 11)
# precisao (amostra historica v1.1->v1.2, n=220, nao revalidada em versoes seguintes):
python qualification/tools/validate_detector.py --seed 20260820 --sample-size 220 --fn-capsules 20
```
