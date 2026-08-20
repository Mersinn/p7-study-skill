# CAPSULE_GENERATION_POLICY — P7

Rege a geração e a verificação de cápsulas do P7.

Herda a política da P6 v2.1.0 com **uma correção material** (§4) e **uma adaptação
de fonte** (§3) exigidas pela natureza do acervo P7.

## 1. O que é uma cápsula

Pacote curto de estudo, no nível do tema, ancorado na fonte do professor.

Existe para que `Estudar Tema` recupere um tema estruturado e possa expor apenas a
view necessária, em vez de carregar o PDF bruto ou mostrar a cápsula inteira.

Não é: resumo integral · PDF copiado · aula alucinada · substituto dos guardrails
do Source Pack.

## 2. Entradas obrigatórias

1. o `p7_source_pack/` final (índice atômico, mapa de unidades, blueprint de prova);
2. `corpus_text/<source_id>.txt` para fontes NATIVAS;
3. `vision_png/<source_id>/pNNN.png` para fontes MISTAS e ESCANEADAS;
4. este arquivo, o `CAPSULE_TEMPLATE.md` e o `CAPSULE_REVIEW_CHECKLIST.md`.

Se só houver o Source Pack, gere cápsula **estrutural** e marque o conteúdo
faltante como `sem evidência na fonte`. Não preencha por plausibilidade.

## 3. A natureza real do acervo P7 — regra de fonte

O acervo P7 tem quatro camadas de autoridade, e elas **não** se equivalem:

| Camada | O que é | Autoridade | Onde vive |
|---|---|---|---|
| **A — slide do professor** | o que foi efetivamente ensinado e é cobrado | **máxima para alinhamento curricular/prova** | quase sempre MISTA/ESCANEADA |
| **A′ — referência indicada/diretriz atual** | livro, artigo, protocolo ou diretriz indicada ou usada para validar vigência | alta; necessária para atualização clínica quando aplicável | externa ou local |
| **B — apostila e resumos de turma** | compilados de alunos (ex.: APOSTILA SA II, RESUmed) | média | quase sempre NATIVA |
| **C — prova antiga / devolutiva** | evidência de **cobrança**, não de conteúdo | ver §5 | mista |

Consequência operacional, e é contraintuitiva:

> Entre os materiais didáticos locais, a camada B costuma ser mais fácil de ler,
> mas tem menos autoridade curricular que a camada A.

Em 99 de 423 fontes o slide do professor só existe como **fotografia da tela do
projetor tirada em sala de aula** — com reflexo, ângulo, recorte e, por vezes,
anotações manuscritas do próprio aluno sobrepostas.

Portanto:

- Nunca construa uma cápsula **apenas** da camada B quando existe camada A para o
  tema. A camada B serve de esqueleto; a camada A confirma e corrige.
- Nunca trate anotação manuscrita como conteúdo do professor. Ela é **do aluno**.
  Se a anotação for legível e relevante, registre-a como
  `anotação do aluno (não é fala do professor)`.
- Se a página estiver ilegível (reflexo, corte, desfoque), diga
  `página N ilegível` e siga. **Uma página declarada ilegível vale mais que uma
  página adivinhada.**
- Em conflito A × B, A prevalece para representar a aula/prova. Para vigência
  clínica, fonte A′ atual prevalece sobre slide antigo; preserve a versão do slide
  em `Para a prova/material histórico`, nunca como prática atual silenciosa.

## 4. Verificação — dois níveis, e o pesado fica para o fim do roadmap

A P6 v2.1.0 declara em `SKILL.md §10` que a verificação independente das cápsulas
de fonte escaneada está PENDENTE. A P7 separa auto-revisão L1 de revisão
independente L2 e de vigência clínica.

Decisão para o P7: **dois níveis**, com o caro adiado — não abolido.

### Nível 1 — checagem geral (padrão, roda sempre)

Executada pelo próprio gerador, ao final da cápsula, numa releitura curta:

- reabrir as páginas-fonte e reconferir **apenas os dados de precisão** que
  entraram na cápsula (§ lista abaixo);
- marcar cada um como conferido, ajustado, ou `confirmar no slide`;
- não reescrever a cápsula inteira — só a tabela de dados de precisão.

L1 registra `self_review: completed` e pode confirmar **transcrição**/alinhamento
curricular. Não marca revisão independente nem vigência clínica. A parte curricular
pode ser estudada com rótulo; claim crítico de dose, corte, janela, contraindicação
ou conduta permanece `clinical_validity: pending/quarantined` até validação atual.

### Nível 2 — verificação independente adversarial (fim do roadmap)

Revisor independente identificado que **relê a fonte antes de ver a cápsula**,
extrai os dados por conta própria e só então compara. Registre `reviewer_id`, tipo
`model | human` e data. Um segundo modelo é revisão independente de geração, não
validação clínica humana; nunca o descreva como tal.

Roda em lote, ao final da construção da skill, priorizando: cápsulas de
`risco_clinico: alto` · cápsulas com muitos números · temas de farmacologia.

Cápsula que passa recebe `independent_review: reviewed_l2`. Vigência clínica
continua sendo estado separado e exige fonte atual apropriada.

Enquanto L2 não rodou, use `independent_review: not_reviewed`. Para claim crítico,
ausência de revisão/vigência é bloqueio de uso clínico assertivo: ensine o conteúdo
curricular rotulado, mas abstenha da conduta ou apresente versão atual validada por
fonte independente.

Alvos da verificação (nos dois níveis):

- dose, posologia, via, intervalo, dose máxima;
- cutoff, escore, critério diagnóstico, número de critérios exigidos;
- tempo (janela terapêutica, latência de resposta, tempo de sintoma para diagnóstico);
- classificação e estadiamento;
- contraindicação e interação;
- qualquer número que apareça na cápsula.

Estados são ortogonais, por cápsula e claim:

- `transcription: pending | confirmed | conflict | quarantined`;
- `curricular_alignment: pending | confirmed | conflict | quarantined`;
- `clinical_validity: pending | current | historical_only | conflict | quarantined`;
- `independent_review: not_reviewed | reviewed_l2`;
- conflito, pendência e quarentena são registrados separadamente e nomeados.

Não use `CONFIRMADO` genérico. Uma transcrição fiel de slide antigo pode estar
`transcription: confirmed` e `clinical_validity: historical_only/quarantined`.

## 5. Anti-circularidade (invariante herdada — não relaxar)

> Artefato derivado não pode virar evidência independente para validar, priorizar
> ou aumentar a recorrência que lhe deu origem.

Na prática:

- a cápsula **consome** prioridade; nunca **gera** prioridade;
- texto gerado por IA não conta como evidência; cápsula não é fonte nova;
- duplicata do mesmo slide não conta duas vezes; resumo derivado do slide não
  dobra o peso do slide;
- cápsula atualizada não pode elevar a própria prioridade;
- prova e devolutiva elevam **evidência de cobrança**, nunca **autoridade médica**;
- camadas sempre rotuladas e separadas: conteúdo didático · evidência de cobrança ·
  inferência pedagógica · regra médica · incerteza.

Cápsulas vivem em `capsules/` como artefatos versionados. **Nunca** entram no
manifesto nem recalculam prioridade.

Ressalva: uma cápsula PODE ser avaliada por uso real (desempenho, erro residual,
feedback). Isso valida a **eficácia da cápsula**, não revalida a recorrência
temática que a originou.

## 6. Ordem de geração

Não gere tudo de uma vez.

1. Cluster piloto da disciplina em curso → revisar → só então o resto.
2. Dentro de cada cluster, ordem por `prioridade` do Source Pack.
3. Tema com `forca_fonte: ausente` **não gera cápsula**. Ele gera uma linha em
   `00_COVERAGE_GAPS.md`.

## 7. Tamanho e divulgação progressiva

Não há corte normativo em KB. Preserve a cobertura necessária do tema e organize
views da mesma cápsula: `study_core`, `precision`, `diagnos`, `cards` e
`source_notes`. O primeiro turno deve preferir `study_core`; os demais módulos são
sob demanda.

Meça tokens realmente carregados, tempo até a primeira tentativa, conclusão,
transferência, esforço e preferência. Comprima ou divida apenas quando teste de uso
mostrar custo sem benefício; nunca remova precisão clínica para satisfazer bytes.

## 8. Falhas proibidas

- afirmar "o slide do professor diz X" para tema sem leitura da camada A;
- converter anotação manuscrita do aluno em fala do professor;
- adivinhar número em página com reflexo;
- marcar L1 como revisão independente ou chamar segundo modelo de validação humana;
- usar claim crítico com vigência pendente/conflitante fora de quarentena;
- silenciar divergência entre gerador e verificador;
- gerar cápsula para tema com fonte ausente.
