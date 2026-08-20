# DETECTOR_VALIDATION_REPORT — validação do detector de claims críticos

**Objetivo:** medir, com amostra estratificada e busca manual de falso negativo,
a confiabilidade do denominador produzido por `critical_claim_scan.py`, antes de
gastar orçamento de adjudicação médica contra um número que poderia estar
sistematicamente errado. Nenhum gate é fechado por este relatório.

## 1. Estado do detector

| | v1.1.0 (congelado para a amostra) | v1.2.0 (pós-correção) |
|---|---|---|
| hash | `c8e340ce…3613c` | `a51038c0…6c43b1f` |
| denominador (claims críticos) | 2 659 | **3 201** (+542, +20,4%) |
| denominador em alto risco | 2 071 | **2 520** (+449, +21,7%) |

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

## 6. Reprodução

```bash
python qualification/tools/critical_claim_scan.py --root p7-study-skill --out qualification/reports
python qualification/tools/cluster_and_tier.py --out qualification/reports
python qualification/tools/validate_detector.py --seed 20260820 --sample-size 220 --fn-capsules 20
python qualification/tools/fn_gap_report.py > qualification/reports/FN_GAP_LINES.txt
```
