# CURRICULUM_DECISION_LOG — P7

Decisões que moldaram os 161 temas canônicos, e os erros cometidos no caminho.
Existe para que a próxima sessão não refaça o trabalho nem repita o engano.

## 1. Deduplicação — do erro à regra

**Erro cometido.** A primeira versão do merge unia dois temas sempre que
compartilhassem qualquer *alias*. Isso encadeou transitivamente: *Esquizofrenia e
Transtornos Psicóticos* fundiu com *Farmacoterapia das psicoses* porque ambos
tinham o alias "psicoses" — e o nome perdedor **desapareceu do currículo**.
Esquizofrenia, Transtorno Bipolar, Ansiedade, Demências e TEPT sumiram assim.
Detectado ao conferir manualmente os temas nucleares de EISM.

**Regra que ficou.** Perder um tema central é muito pior que carregar uma
quase-duplicata. O merge automático só une por **nome canônico normalizado
idêntico**. Aliases viram metadado. As quase-duplicatas vão para juízo humano ou
de adjudicador.

**Resultado.** 232 temas das 6 frentes → 204 por merge conservador → 162 após 42
fusões e 2 reclassificações decididas por adjudicador → 161 após remover um
placeholder.

## 2. Farmacologia não é cadeira

**Decisão.** Os 7 temas de Farmacologia foram movidos para `EISA_II` com
especialidade `Farmacologia`.

**Autoridade.** O horário oficial 2026.2 mostra o código `SA II / Far` — Farmacologia
é subárea de Saúde do Adulto II. A pasta separada no Drive era organização de
arquivo, confirmado pelo usuário.

**Ressalva preservada.** O material de Farmacologia carrega numeração de prova
**própria**, que não coincide com as unidades de EISA II. "III unidade" num arquivo
de farmaco ≠ 3ª prova de EISA II. Ver `00_COVERAGE_GAPS.md`.

## 3. Pediatria antes de órgão

**Erro cometido.** A resolução de disciplina por especialidade casava "Oncologia
**pediátrica**" com "oncologia" e mandava 18 temas de EISCA para EISA II.

**Regra que ficou.** O marcador pediátrico (`pediatr*`, `neonatolog*`, `hebiatria`,
`criança`, `adolescente`, `puericultura`) precede qualquer especialidade de órgão.

## 4. Três eixos que não se confundem

**Erro cometido.** Eu tratava legibilidade como se fosse autoridade. Ao montar a
lista de fontes para os geradores de cápsula, ordenei com `NATIVA` primeiro e cortei
em 6 — e como os slides do professor são quase todos fotografados (`ESCANEADA`),
eles caíam fora justamente nos temas com muita fonte nativa. **Filtrei a camada de
maior autoridade.** Duas cápsulas (Depressão, Esquizofrenia) declararam "sem slide
de aula localizado" para temas que têm slide.

**Regra que ficou.** Ver `00_TAXONOMY_AXIS.md`:

- `source_type` — o que o arquivo **é**;
- `source_role` — para que **serve**;
- `tipo_fonte` — como é **lido**.

Camada A nunca é truncada da lista de fontes e vem primeiro. Um slide ESCANEADO
continua sendo camada A.

## 5. Interligação não é duplicata

**Decisão.** 73 temas vivem em duas cadeiras e permanecem como **um** tema com
vínculo declarado, não como dois.

**Critério.** A doença e a farmacoterapia dela são **duas aulas**, dois conjuntos de
questão, dois tipos de erro — ficam separadas. Mas *Depressão* em EISM e
*Antidepressivos* em EISA II/Farmaco são ângulos do mesmo objeto: viram vínculo.
Ver `00_INTERLIGACOES.md`.

**Erro cometido.** A primeira detecção de vínculo usava fonte compartilhada sem
filtro, e a APOSTILA de 246 páginas ligava tudo a tudo (121 vínculos, muitos
absurdos — otites ↔ diarreia). Corrigido: fonte "hub" (>4 temas) não gera vínculo,
e a raiz lexical exige termo clínico longo. Resultado: 73 vínculos reais.

## 6. Unidade — quem manda

Onde a árvore `Resumos das Unidades` e a divisão por prova dos slides discordarem
da frente de disciplina, **prevalece a árvore de unidades**. `A_DEFINIR` não
bloqueia estudo; limita a precisão do recorte, e isso é dito em uma linha.

## 7. O que ficou de fora, e por quê

- **Placeholder do RESUmed** — "Saúde Mental — conteúdo integral do compilado
  RESUmed (não lido)" não é tema canônico; é um arquivo que o cartógrafo registrou
  como se fosse tema. Removido, não gera cápsula.
- **3 decisões do adjudicador não aplicadas** por divergência de nome entre a
  decisão e o currículo (registradas em `06_CURRICULO_FINAL.json`,
  campo `decisoes_dedup_aplicadas`).
- **IESEC e Relações Étnico-Raciais** aparecem no horário oficial mas não têm
  material no acervo enviado. Fora do escopo desta versão, por ausência de fonte.

## 8. Padrão de erro deste projeto — a vigiar

Nos três bugs sérios desta construção, a falha foi **pré-filtragem silenciosa feita
por mim**, não erro dos agentes. Os agentes reportaram fielmente o que receberam:
quando disseram "sem slide localizado", era verdade sobre a lista que eu lhes dei.

Regra: antes de reduzir uma lista que vai para um agente, pergunte o que a redução
está removendo — e se o que sobra ainda representa o todo.
