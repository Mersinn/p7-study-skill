# 00_TAXONOMY_AXIS — P7

Eixo de classificação das 423 fontes indexadas. Um arquivo tem **um**
`source_type` e **um** `source_role` — valores compostos são proibidos.

## Os três eixos, que não se confundem

| Eixo | Pergunta que responde | Valores |
|---|---|---|
| `source_type` | o que o arquivo **é** | slide · resumo · prova_antiga · devolutiva · osce · caso_clinico · administrativo · outro |
| `source_role` | para que ele **serve** | professor_slide · review_summary · exam_evidence · practical_training · curricular_admin · unknown |
| `tipo_fonte` | como ele é **lido** | NATIVA · MISTA · ESCANEADA |

`tipo_fonte` é legibilidade, não autoridade. Um slide ESCANEADO continua sendo
camada A. Confundir os dois eixos foi o erro que quase apagou a camada do
professor das cápsulas.

## Distribuição de `source_type`

| source_type | arquivos |
|---|---|
| resumo | 235 |
| slide | 99 |
| devolutiva | 34 |
| prova_antiga | 31 |
| caso_clinico | 11 |
| osce | 7 |
| outro | 6 |

## Distribuição de `source_role`

| source_role | arquivos |
|---|---|
| review_summary | 235 |
| professor_slide | 99 |
| exam_evidence | 65 |
| practical_training | 18 |
| unknown | 6 |

## Distribuição de `tipo_fonte` (legibilidade)

| tipo_fonte | arquivos |
|---|---|
| NATIVA | 324 |
| ESCANEADA | 52 |
| MISTA | 47 |

## Validação

- valores compostos em `source_type`/`source_role`: **0** (por construção)
- provas antigas identificadas: **31**
- devolutivas identificadas: **34**
- evidência de prova fora da pasta PROVAS ANTIGAS: **0**
- slides do professor: **99**
- total indexado: **423**

## Camada planner-ready

- `00_ATOMIC_THEME_INDEX.csv` — 162 temas canônicos com prioridade, risco e força
- `00_UNIT_TOPIC_MAP.md` — escopo por unidade (autoridade para prova de unidade)
- `00_CALENDARIO_2026_2.md` — 109 aulas datadas; responde 'quanto tempo eu tenho'
- `00_MAPA_OPERACAO_MOVIMENTO.md` — 152 itens dissecados, camada metacognitiva
- `00_INTERLIGACOES.md` — 73 temas que vivem em duas cadeiras
