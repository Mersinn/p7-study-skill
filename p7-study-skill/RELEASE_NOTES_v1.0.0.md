# RELEASE NOTES — P7 Diagnos v1.0.0

Primeira versão. Sucede a `p6-study-skill` v2.1.0, herdando a arquitetura e
corrigindo dois defeitos conhecidos dela.

## O que existe

| Camada | Conteúdo |
|---|---|
| Roteador | `SKILL.md` — 6 modos + triagem Igor |
| Protocolos | 15 arquivos em `references/` |
| Source pack | 161 temas · 354 fontes referenciadas · 12 artefatos |
| Cápsulas | por disciplina, com verificação nível 1 |
| Geração | contrato, template e checklist de revisão |

## O acervo por trás

423 fontes indexadas, extraídas de 9 arquivos do Drive do P7 (~3,2 GB).
9,5M de caracteres. 428 arquivos no total; 5 não extraídos (2 vídeos, 2 `.ppt`
legado sem conversor, 1 PDF de imagem pura).

**99 dessas fontes são slides do professor fotografados da tela do projetor.** Eles
são densos e cruciais, e continuam sendo a camada de maior autoridade — muda só o
método de acesso, que é leitura visual das páginas pré-renderizadas.

## Os 6 modos

1. `Plano de Guerra` — alvo, prazo, escopo
2. `Estudar Tema` — índice → cápsula → fonte
3. `Resolver Questão` — Diagnos: operação × movimento
4. `Simular Prova / Arguição / OSCE`
5. `Aula Viva` — **novo** · captura a aula recém-assistida por 4 lentes e produz delta
6. `Contraprova` — **novo** · testa a hipótese sobre o erro em vez de declará-la

Mais `igor me salva!` como entrada de desbloqueio.

## O que o P7 tem e o P6 não tinha

**Camada metacognitiva.** 152 questões reais de provas e devolutivas dissecadas por
4 extratores independentes: operação exigida, variável decisiva e seu tipo, mapa
distrator→movimento, erro da turma, raciocínio do professor. Mais 33 padrões de
erro por disciplina, cada um com a intervenção que o corrige.
Ver `p7_source_pack/00_MAPA_OPERACAO_MOVIMENTO.md`.

**Calendário datado.** 109 aulas de 2026.2 com data, cadeira, subárea e tema, e os
blocos de cada unidade. A skill calcula o prazo em vez de perguntar.

**Interligações entre cadeiras.** 73 temas que vivem em duas cadeiras, com o ângulo
de cada uma sobre o mesmo objeto clínico.

**Verificação de cápsula em dois níveis.** A P6 declara em `SKILL.md §10` que a
verificação por segundo agente está PENDENTE, transferindo ao aluno a conferência
manual de cada dose. No P7 o nível 1 (releitura dos dados de precisão pelo gerador)
roda sempre; o nível 2 (independente adversarial) roda em lote priorizando risco
alto e psicofarmacologia.

**Regra do silêncio.** Derivada do piloto Diagnos 1C-A (2026-07-28, 40 agentes
cegos), onde o motor concluiu que o aluno "não processou o comando" apenas porque
ele não mencionou o comando — a única refutação limpa do piloto.
`QUESTION_INTELLIGENCE_P7.md` §8 proíbe **essa** inferência e, no mesmo movimento,
protege o motor: alternativa marcada, padrão do bloco, estrutura do item, semântica
do enunciado e trajetória seguem sendo sinal legítimo. Responder só com a letra
**não** é `INDETERMINADO`.

**Drill trocado.** `ECG_DRILL` (P6) → `EXAME_ESTADO_MENTAL_DRILL` (P7). Mesma
mecânica — forçar a sequência antes do diagnóstico — aplicada ao erro dominante da
psiquiatria de graduação.

## Achados do acervo que valem para a prova

- **O banco de questões é reciclado.** O bloco V/F sobre achados ultrassonográficos
  na DRC aparece idêntico em 4 provas. A questão de TFG (clearance 24h × CKD-EPI) é
  palavra por palavra igual entre 2024.1 e 2025.1. Cintilografia renal, em 3.
- **O item errado quase nunca é grosseiro** — é um número/limiar trocado ou um
  qualificador absoluto ("obrigatório", "sempre", "nunca").
- **Bibliografia por subárea**, extraída das devolutivas: Riella (nefro), Vilar
  (endócrino), Nitrini (neuro), Kanski (oftalmo), Robbins/Bogliolo (patologia),
  Nelson Rodrigues + EAU (uro).
- Quase metade dos erros mapeados é **operacional**, não lacuna de conteúdo.

## Limites declarados

Não é app · banco · API · RAG · embeddings · integração MedPattern · parser de PDF
em runtime. Cápsulas são construídas offline e versionadas.

Dado sintético não conta como evidência de aprendizagem humana.

## Pendências conhecidas

- verificação nível 2 ainda não executada;
- as cápsulas de EISM da primeira onda não têm a seção `Operação × movimento`
  (foram escritas antes dela existir);
- IESEC e Relações Étnico-Raciais sem material no acervo;
- pendências `confirmar no slide` estão contadas no `CAPSULE_INDEX.md` e nomeadas
  dentro de cada cápsula.
