# DETECTOR_VALIDATION_REPORT — validação do detector de claims críticos

**Objetivo:** medir, com amostra estratificada e busca manual de falso negativo,
a confiabilidade do denominador produzido por `critical_claim_scan.py`, antes de
gastar orçamento de adjudicação médica contra um número que poderia estar
sistematicamente errado. Nenhum gate é fechado por este relatório.

## 1. Estado do detector

| | v1.1.0 (congelado p/ amostra §2-3) | v1.2.0 (pós-correção) | v1.3.0 (pós-recall §7) |
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

## 8. Reprodução (estado vigente v1.3.0)

```bash
python qualification/tools/critical_claim_scan.py --root p7-study-skill --out qualification/reports
python qualification/tools/cluster_and_tier.py --out qualification/reports
# precisão (amostra histórica v1.1->v1.2, não re-executada em v1.3.0):
python qualification/tools/validate_detector.py --seed 20260820 --sample-size 220 --fn-capsules 20
# recall fresco (amostra desta seção 7, sem sobreposição com a acima):
python qualification/tools/validate_detector.py --seed 20260821 --sample-size 30 --fn-capsules 20
python qualification/tools/fn_gap_report.py > qualification/reports/FN_GAP_LINES_v1.2.txt
```
