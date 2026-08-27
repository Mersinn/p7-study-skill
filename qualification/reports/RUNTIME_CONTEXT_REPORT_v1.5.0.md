# Custo de contexto por modo — P7 v1.5.0

**Baseline:** `6fc906f`  
**Métrica:** bytes UTF-8; tokens = `ceil(bytes/4)`, estimativa comparativa e não
tokenização do modelo.  
**Fonte reproduzível:** `qualification/tools/measure_runtime_context.py` e
`RUNTIME_CONTEXT_v1.5.0.json`.

| Modo | Antes (bytes / tokens est.) | Depois (bytes / tokens est.) | Redução |
|---|---:|---:|---:|
| Plano de Guerra | 45.151 / 11.288 | 19.638 / 4.910 | 56,51% |
| Estudar Tema, bundle fixo | 70.138 / 17.535 | 44.115 / 11.029 | 37,10% |
| Resolver Questão | 59.308 / 14.827 | 33.364 / 8.341 | 43,74% |
| Simular Prova | 42.737 / 10.685 | 16.712 / 4.178 | 60,90% |
| OSCE | 45.852 / 11.463 | 19.844 / 4.961 | 56,72% |
| Retomada | 53.735 / 13.434 | 27.606 / 6.902 | 48,63% |

O `SKILL.md` caiu de 37.327 para 11.198 bytes. Detalhes de modo não foram
apagados: passaram a uma referência única carregada sob demanda. O custo dinâmico
de cápsula permanece separado do bundle fixo: 158 cápsulas, mediana 13.936 bytes,
p95 20.283 e máximo 23.957.

Este relatório mede custo de ativação, não qualidade. O gate `runtime_context`
permanece aberto até que sessões limpas A/B confirmem question-first,
personalização, segurança e Diagnos no snapshot refatorado.
