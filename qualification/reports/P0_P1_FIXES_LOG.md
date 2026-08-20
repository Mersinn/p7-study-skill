# P0_P1_FIXES_LOG — correções de conteúdo clínico encontradas por adjudicação

Registro de correções REAIS de texto de cápsula (não apenas registro de
claim), encontradas ao comparar cápsula contra fonte primária efetivamente
lida nesta sessão. Diferente de `CLAIM_ADJUDICATION_LOG.md` (que documenta o
fechamento de claims), este arquivo isola os casos em que a cápsula **estava
errada** e foi corrigida — evidência de que a varredura está fazendo o
trabalho que se propõe a fazer, não apenas catalogando.

---

## 2026-08-20 — `capsules/EISCA/diarreia_aguda_desidratacao_planos_reidratacao.md`

### Achado 1 — classificação de gravidade (P1, risco de má-classificação)

**Texto anterior (4 ocorrências):** "sede ausente/bebe pouco" listado como o
item com asterisco (critério de gravidade) do domínio "sede" na classificação
de desidratação grave.

**Fonte primária lida nesta sessão** (SBP, "Diarreia Aguda Infecciosa",
Depto. Científico de Gastroenterologia — Quadro 2, citando MS/OMS):

| Domínio | Plano A | Plano B | Plano C (asterisco = grave) |
|---|---|---|---|
| Sede | Sem sede | Sedento, bebe rápido e avidamente | **Não é capaz de beber\*** |

**Problema:** "sede ausente" é na verdade o valor do **Plano A** (sem
desidratação) na tabela primária — o oposto do que a cápsula estava usando
como sinal de gravidade. O item de asterisco correto é a **incapacidade de
ingerir líquidos**, um achado clinicamente distinto (e mais grave) de "não ter
sede".

**Risco se não corrigido:** um aluno (ou, pior, uma aplicação clínica real
inspirada no material) poderia classificar erroneamente "sede ausente" como
sinal de gravidade, quando na verdade uma criança sem sede que bebe
normalmente está no espectro **hidratado**, não desidratado grave — o inverso
clinicamente perigoso da leitura correta.

**Correção aplicada:** as 4 ocorrências ("sede ausente/bebe pouco", "sede
ausente") foram substituídas por "incapaz de ingerir líquidos" / "incapaz de
beber", replicando a linguagem exata do documento primário. Os outros dois
itens de asterisco (estado geral letárgico/comatoso; pulsos fracos/ausentes)
já estavam corretos e não foram alterados.

**Evidência:** `claim:diarreia-planos.classificacao-por-contagem-sinais`,
`registry/clinical_claims.jsonl`.

### Achado 2 — duração do zinco (baixo risco, precisão)

**Texto anterior:** duração fixa "14 dias" (3 ocorrências).
**Fonte primária:** "durante 10 a 14 dias".
**Risco:** nenhum risco de segurança (14 é o extremo superior do intervalo
correto, não subdosagem nem sobredosagem) — imprecisão editorial, corrigida
para o intervalo exato.

### Achado 3 — dose de ondansetrona (precisão, não erro de segurança)

**Texto anterior:** "0,2 mg/kg/dose" (faixa 6-24 meses), sem a forma de dose
fixa.
**Fonte primária:** "2 mg (0,2 a 0,4 mg/kg)" — o documento primário apresenta
as duas formas como equivalentes.
**Risco:** a cápsula tinha apenas o extremo inferior do intervalo por peso;
não é erro (0,2 mg/kg está dentro do intervalo válido), mas omitia a forma de
dose fixa mais usada na prática e o extremo superior do intervalo.
**Correção:** cápsula atualizada para "2 mg (0,2-0,4 mg/kg)".

---

## Método usado para chegar a estes achados

Os PDFs primários oficiais (MS, SBP, protocolos municipais) em geral não são
legíveis via `WebFetch` neste ambiente (retornam stream binário). A correção
foi extrair o texto localmente com **PyMuPDF** (biblioteca já instalada,
`import fitz`) a partir dos PDFs já baixados por `WebFetch`, e então ler o
texto extraído **adversarialmente** — procurando ativamente por divergência
com a cápsula, não apenas confirmação. Isso é o que permitiu encontrar o
Achado 1, que uma leitura confirmatória superficial teria deixado passar
(a cápsula "parecia" fazer sentido lida isoladamente).

Ferramenta reutilizável: extração de texto de PDF via
`python -c "import fitz; ..."` sobre qualquer PDF salvo por `WebFetch` em
`tool-results/`. Não requer `pdftoppm`/poppler — `pdftotext` também está
disponível neste ambiente (`/mingw64/bin/pdftotext`) como alternativa.
