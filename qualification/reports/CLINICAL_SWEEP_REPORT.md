# CLINICAL_SWEEP_REPORT — P7 v1.0.0 (qualificação)

**Branch:** `qualification/v1.0.0-codex`
**Base:** `origin/qualification/v1.0.0-claude` @ `0a9f558a9727e3bb6aa1fb7e9b967517b53128bb`
**Estágio vigente (22/08/2026):** detector v1.4.0 congelado; 3.603 ocorrências,
3.008 clusters, 2.113 clusters Tier A e 2.033 ocorrências Tier A em cápsulas de
alto risco. Claims canônicos: 52 (43 `current`, 8 `quarantined`, 1 `conflict`).
Adjudicação por diretriz e fechamento dos gates continuam **em andamento**.
**Gates fechados por este documento:** nenhum.

> **Nota de leitura:** as seções que preservam números v1.1–v1.3 abaixo são
> snapshots históricos do processo. Para o estado vigente, use o snapshot acima,
> `CLAIM_CLUSTER_SUMMARY.json`, `CRITICAL_CLAIM_SCAN_SUMMARY.json` e a view
> canônica `CANONICAL_CLAIM_COVERAGE.csv`. O detector v1.4.0 não deve ser
> alterado sem regressão concreta e nova validação.

---

## 1. O que este relatório é

É o **denominador** da varredura clínica, produzido por código determinístico e
reproduzível, não por leitura de modelo. Ele responde a uma única pergunta que
até agora não tinha resposta numérica no projeto:

> Quantas afirmações clínicas críticas a P7 realmente faz, e quantas delas estão
> rastreadas?

Sem esse número, `critical_claim_sweep`, `p0_zero` e `p1_high_risk_zero` não
podiam ser fechados nem honestamente discutidos — não havia como afirmar "100%
dos claims críticos" sem saber o total.

## 2. Método

Ferramenta: [`qualification/tools/critical_claim_scan.py`](../tools/critical_claim_scan.py)

1. **Detecção lexical por categoria**, nas dez classes exigidas pelo contrato de
   qualificação (dose/via/intervalo/máximo; cutoff/escore/estadiamento; janela
   temporal; contraindicação/interação; emergência/sinal de alarme; sequência
   terapêutica; internação/alta; algoritmo dependente de diretriz;
   calendário/regra jurisdicional; afirmação absoluta).
2. **Força de sinal (`tier`)**: `strong` = padrão específico (número + unidade,
   corte numérico explícito, verbo de contraindicação, termo de emergência
   nomeado); `weak` = conectivo de prosa ou termo genérico (`após`, `evitar`,
   `imediatamente`, `classificação`).
3. **Classe de seção**: `assertive_clinical` (conduta, dados de precisão, cards,
   pivô, palavras-âncora, revisão, prática atual), `pedagogic_meta` (distratores,
   pegadinhas, mini-casos, como cai, operação × movimento), `provenance`
   (metadados, fontes), `historical` (Para a prova/material histórico).
4. **Ligação a claims registrados** apenas com **evidência textual explícita**:
   mesma cápsula **e** interseção não vazia de tokens numéricos/unidades entre a
   linha e o claim. Coincidência temática sem número **não** conta como
   rastreabilidade.

**Denominador primário do gate:**
`tier == strong` **e** categoria crítica **e** `section_class == assertive_clinical`.

### 2.1 Correção de precisão aplicada durante a construção

A primeira versão do detector produziu 5 988 detecções críticas. A auditoria da
própria ferramenta encontrou falso positivo sistemático: a lista de vias de
administração incluía tokens de duas letras (`ic`, `io`, `u`, `l`, `g`) que
colidem com siglas clínicas — `IC` (insuficiência cardíaca) era lido como via de
administração. Os tokens curtos foram rebaixados para `weak` e o denominador
passou a exigir tier forte.

### 2.2 Precisão medida do denominador final

Amostra determinística de 20 entradas espaçadas uniformemente sobre o
denominador (passo fixo, não aleatório — reproduzível):
**19/20 são afirmações clínicas críticas genuínas** (cortes de TIRADS, TFG mínima
para iSGLT2, Hb <7 g/dL em talassemia maior, contraindicação de topiramato em
glaucoma, dose hipnótica × antidepressiva de mirtazapina, alvo de SpO2 92–94%).
1/20 é falso positivo (`hipersensibilidade` em frase de genética do Th2).
**Precisão estimada ≈ 95%.**

Recall não foi medido e não é reivindicado. O tier `weak` (2 577 detecções) e as
seções `pedagogic_meta` (2 700) ficam **fora** do denominador: isso é perda de
cobertura assumida e auditável, não zero.

---

## 3. Resultado

| Métrica | Valor |
|---|---|
| Cápsulas varridas | **158** |
| Cápsulas de alto risco | **105** |
| Detecções totais (todas as categorias/tiers) | 7 587 |
| **Denominador da varredura (claims críticos)** | **2 659** |
| Denominador em linhas distintas | 2 116 |
| **Denominador em cápsulas de alto risco** | **2 071** (1 625 linhas) |
| **Claims registrados em `registry/clinical_claims.jsonl`** | **41** |
| **Não resolvidos (total)** | **2 598** |
| **Não resolvidos (alto risco)** | **2 010** |
| **Cápsulas de alto risco com ZERO claim registrado** | **94 de 105** |

**Cobertura de rastreabilidade: 61 / 2 659 = 2,3 %** (alto risco: 61/2 071 = 2,9 %).

### 3.1 Por categoria (denominador)

| Categoria | Claims |
|---|---|
| cutoff/escore/estadiamento | 1 283 |
| dose/via/intervalo/máximo | 775 |
| contraindicação/interação | 208 |
| emergência/sinal de alarme | 201 |
| sequência terapêutica | 103 |
| janela temporal | 64 |
| calendário/regra jurisdicional | 25 |

### 3.2 Por disciplina (não resolvidos)

| Disciplina | Não resolvidos |
|---|---|
| EISA_II | 1 285 |
| EISCA | 759 |
| CASOS_CLINICOS | 179 |
| OSCE | 178 |
| EISM | 197 |

### 3.3 Distribuição por cápsula de alto risco

mínimo 1 · mediana 18 · média 19,7 · máximo 54 · soma 2 071

Cápsulas com maior passivo (todas com **zero** claims registrados):

| Não resolvidos | Cápsula |
|---|---|
| 54 | `capsules/EISCA/diarreia_aguda_desidratacao_planos_reidratacao.md` |
| 46 | `capsules/EISCA/sepse_e_meningite_neonatal.md` |
| 43 | `capsules/EISA_II/nefropatia_diabetica.md` |
| 43 | `capsules/OSCE/osce_urologia.md` |
| 42 | `capsules/EISA_II/doencas_paratireoides_hiperparatireoidismo_osteoporose.md` |
| 41 | `capsules/EISA_II/diabetes_complicacoes_agudas_cronicas.md` |
| 41 | `capsules/OSCE/osce_pediatria.md` |
| 40 | `capsules/EISCA/anemia_ferropriva.md` |

As 11 cápsulas de alto risco **com** claims registrados são exatamente as
sentinelas reparadas na fase anterior (reanimação neonatal, estado de mal, asma
pediátrica, AVC isquêmico, lítio/bipolar, antipsicóticos/SNM, abstinência
alcoólica, aleitamento, imunizações, coma, semiologia pediátrica). Mesmo nelas a
cobertura é parcial: p.ex. estado de mal epiléptico tem 6 claims registrados
para 26 claims críticos detectados (17 não resolvidos).

---

## 4. Leitura honesta do resultado

O trabalho clínico anterior **não foi uma varredura**. Foi um **reparo dirigido de
sentinelas**: encontrou e corrigiu os P0 mais perigosos em 11 cápsulas. Isso é
real e não deve ser desfeito. Mas o registry cobre 2,3 % das afirmações críticas
que a skill efetivamente entrega ao aluno.

Consequências diretas:

- `critical_claim_sweep` **não pode** ser fechado hoje, e a distância até o
  fechamento é de aproximadamente **duas ordens de grandeza**, não de um último
  quilômetro.
- `p0_zero` e `p1_high_risk_zero` são, no estado atual, **indetermináveis**: não
  é possível afirmar "zero P0" sobre 2 598 afirmações nunca adjudicadas. A
  ausência de P0 conhecido não é evidência de ausência de P0.
- A nota anterior do gate ("o registry cobre sentinelas recuperadas, mas não
  certifica varredura independente") estava **correta** e agora está
  quantificada.

## 5. O que este relatório NÃO estabelece

- Não afirma que os 2 598 claims não resolvidos estejam errados. A maioria
  provavelmente está correta — eles simplesmente **não estão rastreados**.
- Não mede recall do detector.
- Não substitui revisão clínica humana. Nenhuma revisão humana ocorreu.
- Não fecha, adianta ou enfraquece nenhum gate.

## 6. Artefatos

| Arquivo | Conteúdo |
|---|---|
| `qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv` | 7 587 detecções, uma por linha, com `detection_id` estável, tier, classe de seção, ligação e texto |
| `qualification/reports/CRITICAL_CLAIM_COVERAGE.csv` | cobertura por cápsula: detectado / denominador / registrado / não resolvido |
| `qualification/reports/CRITICAL_CLAIM_SCAN_SUMMARY.json` | sumário determinístico com limitações declaradas |

Reprodução:

```bash
python qualification/tools/critical_claim_scan.py --root p7-study-skill --out qualification/reports
```

## 7. Estado dos gates após esta fase

Inalterado. Oito gates abertos, decisão **HOLD**.
