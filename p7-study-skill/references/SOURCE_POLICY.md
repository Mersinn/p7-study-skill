# SOURCE_POLICY — P7

Como decidir em que fonte confiar, quanto confiar, e o que dizer quando a fonte
não sustenta a afirmação.

## 1. A regra que governa tudo

> Nunca afirme que algo "está no material" sem poder apontar o `source_id`.

Se não puder apontar, a frase correta é uma destas:

- "sem evidência dedicada no Source Pack — vou pelo conhecimento geral, e sinalizo";
- "há fonte, mas é fraca para esse ponto";
- "esse dado precisa ser confirmado no slide original".

Fingir cobertura é a única falha inaceitável desta skill.

## 2. As camadas de autoridade do acervo P7

O acervo P7 tem 423 fontes indexadas. Elas **não** têm o mesmo peso.

| Camada | O que é | Autoridade |
|---|---|---|
| **A** | slide da aula do professor | **máxima** — é o que foi ensinado e é o que cai |
| **A′** | artigo, diretriz e referência bibliográfica indicada (Riella, Jones/AHA, DBHA, tratados, guias de bolso) | **alta** — é a fonte que o professor cita e o gabarito segue |
| **B** | apostila e resumos de turma (APOSTILA SA II, RESUmed, Resumos/) | média |
| **C** | prova antiga e devolutiva | evidência de **cobrança**, nunca autoridade médica |

Consequências operacionais:

- Camada B é **esqueleto**, não veredito. Onde existir A ou A′ para o tema, ela
  confirma e corrige a B.
- Divergência A × B → prevalece **A**. Divergência A × A′ → declare as duas e diga
  qual o professor segue, se souber; a diretriz vence em ponto de conduta, o slide
  vence em "o que cai".
- Anotação manuscrita é do **aluno**, não do professor. Se for usada, rotule.
- Camada C nunca vira autoridade médica. Responde "como cai", não "o que é verdade".

## 2.1 Slides fotografados — método, não lamento

99 das 423 fontes não têm camada de texto. A maioria são **slides do professor
fotografados da tela do projetor** em sala.

Isso **não** os torna ilegíveis nem de segunda classe. Eles são densos e são
cruciais — continuam sendo camada A. Significa apenas que o acesso a eles é por
**leitura visual da página renderizada**, não por extração de texto.

Como trabalhar com eles:

- as páginas estão pré-renderizadas em `vision_png/<source_id>/pNNN.png`;
- leia a página como imagem e transcreva o que está escrito, com fidelidade a
  números, unidades, critérios e tabelas;
- descreva em palavras o que é visual (fluxograma, algoritmo, esquema, imagem
  clínica, traçado);
- foto com reflexo, corte ou desfoque em **parte** da página não invalida o
  resto — use o que está legível e marque só o trecho perdido;
- se um dado específico não estiver legível, escreva `confirmar no slide` para
  aquele dado. Não descarte a página inteira por causa de um número.

Regra que permanece dura: **nunca extraia conteúdo de uma fonte ESCANEADA pelo
`.txt`**. Aquele texto é catálogo grosso — serve para saber que o arquivo existe e
de que tema trata. O conteúdo vem da leitura visual.

## 3. Tipos de fonte no manifesto

Todo `source_id` carrega um `tipo_fonte`:

- `NATIVA` — tem camada de texto; `corpus_text/<id>.txt` é confiável.
- `MISTA` — texto parcial; parte do conteúdo só existe em imagem.
- `ESCANEADA` — sem camada de texto útil; o `.txt` vem vazio ou com lixo.

Para `MISTA` e `ESCANEADA`, o conteúdo real só é acessível por **visão** sobre
`vision_png/<source_id>/pNNN.png`.

Regra dura: **nunca descreva o conteúdo de uma fonte ESCANEADA a partir do `.txt`.**
Aquele texto é catálogo grosso — serve para saber que o arquivo existe e talvez de
que tema trata. Não serve para dose, critério, cutoff, tabela ou traçado.

## 4. Ordem de consulta

Ao planejar ou selecionar evidência de tema:

1. `p7_source_pack/00_ATOMIC_THEME_INDEX.csv` — o tema existe? com que força?
2. `p7_source_pack/00_UNIT_TOPIC_MAP.md` — cai em qual unidade?
3. `p7_source_pack/00_EXAM_BLUEPRINT.md` — como é cobrado?
4. `capsules/CAPSULE_INDEX.md` — já existe cápsula? com que status?
5. `p7_source_pack/00_SOURCE_MANIFEST.csv` — quais arquivos concretos?
6. `p7_source_pack/00_COVERAGE_GAPS.md` — o que sabidamente falta?

Só desça para o arquivo bruto quando a cápsula for insuficiente, ou quando houver
risco clínico, dado numérico decisivo, conteúdo visual ou ambiguidade.

## 5. Regras duras de índice

- `filename` e caminho têm mais autoridade que qualquer preview ou tema inferido.
- `tema_provavel` é pista de índice, não verdade.
- "existe arquivo" ≠ "existe fonte forte". `forca_fonte` é declarada, não presumida.
- Duplicata não conta como cobertura extra. O acervo P7 tem muita duplicata (mesmo
  tema em 3–4 PDFs, às vezes com mojibake no nome). Consolide no tema canônico.
- `unidade: A_DEFINIR` não bloqueia estudo; limita a precisão do recorte.
- Resumo derivado de um slide **não** dobra o peso daquele slide.

## 6. Força da fonte — como classificar

- `forte` — fonte dedicada, substancial, camada A legível ou camada B extensa e
  consistente.
- `media` — fonte parcial, só resumo de terceiros, ou camada A só parcialmente
  legível.
- `fraca` — só menção dentro de outro tema, ou camada A ilegível sem camada B.
- `ausente` — tema pertence ao currículo mas não há arquivo.

Quando duas evidências discordarem da força, fique com a **menor** e registre.

## 7. O que dizer quando a fonte é fraca

Diga. Em uma linha, sem cerimônia, e siga ensinando:

> Fonte fraca para esse tema (só resumo de turma, sem o slide). Vou pelo
> conhecimento geral consolidado e marco o que precisa de conferência.

Não interrompa o estudo por fonte fraca. Interrompa a **afirmação de precisão**.

## 8. Falhas proibidas

- dizer "o slide do professor diz X" sem ter lido a camada A daquele tema;
- extrair número de fonte ESCANEADA pelo `.txt`;
- tratar anotação manuscrita como conteúdo do professor;
- tratar prova antiga como material didático;
- contar duplicata como evidência independente;
- promover `forca_fonte` para deixar o mapa bonito;
- citar `source_id` que não existe no manifesto.
