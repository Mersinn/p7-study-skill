# Relatório final de qualificação — P7 Study Skill 1.5.0

## Decisão

`READY_FOR_USER_REVIEW` — não autoriza merge, tag nem publicação.

- Codex: **qualificado**.
- Claude: **não avaliado**; OAuth é pendência de compatibilidade e não entra no denominador Codex.
- Conteúdo clínico: **liberável com quarentenas explícitas**.
- Registry mecânico: `READY_FOR_RELEASE`, 17/17 gates com evidência atestada.

## Evidência aritmética

- Testes no repositório: 54/54 PASS.
- Cápsulas: 158/158 reconciliadas.
- Behavioral Codex: 13/13 PASS = 9/9 sentinelas + 4/4 core, em sessões limpas.
- Jornadas válidas: 9/9 PASS = J01 3/3 + J02 3/3 + J03 3/3. Um run histórico
  `INCONCLUSIVE` permanece preservado e fora do denominador.
- Longitudinalidade: 2/2 sessões limpas válidas; sessão B avançou de 6 para 8 eventos.
- Registry clínico: 52/52 classificados = 34 `current` + 17 `quarantined` + 1 `conflict`.
- Rastreabilidade `current`: 34/34 PASS.
- Inventário primário: 3.602/3.602 ocorrências com destino explícito.
- Alto risco: 2.817/2.817 ocorrências com destino explícito.
- Linhas estruturadas: 2.392/2.392 contabilizadas = 75 resolvidas + 2.317
  `unresolved` explícitas.
- Red-team amostral canônico: 37 linhas = 10 current + 17 quarantined + 1 conflict
  + 3 históricas + 6 pending/unregistered; 36 alto risco + 1 baixo; 19 cápsulas.
- Reparos materiais dirigidos: 7/7 PASS; P0 abertos 0, P1 abertos 0 no escopo qualificado.
- Runtime: 6/6 bundles menores, redução de 36,74% a 60,57%.
- Gates: 17/17 PASS.

## Artefato final e instalação limpa

- ZIP: `dist/P7-Study-Skill-1.5.0.zip`.
- SHA-256: `21416ca72252856ce4d7b189b3f742a4bc1720d7f8276eec5ec31e4db92ed55f`.
- Duas construções: 2/2 byte a byte idênticas; 253 entradas; raiz única;
  0 caminhos inseguros, 0 duplicatas case-insensitive e 0 entradas proibidas.
- Standalone: 54 testes executados = 53 PASS + 1 SKIP esperado da fixture de
  qualificação não distribuída; 158/158 cápsulas; validação normal e release gate
  com `error=0`, `warn=28`, `info=2` e exit code 0.
- A cópia descartável confirmou `corpus_text=False`, `vision_png=False` e
  `.p7-state=False`.

## Interpretação clínica correta

“Contabilizado” não significa “clinicamente resolvido”. O inventário prova que
cada ocorrência tem uma disposição operacional. Claims `pending`, `quarantined`,
`conflict`, curriculares ou históricos não são promovidos a prática atual e sua
recuperação clínica fica bloqueada. Claims `current` exigem fonte vigente,
localizador, contexto e revisão compatível com o risco.

Os slides atuais organizados em `C:\Users\emers\P7\p7-slides professores\`
foram registrados como mapa de fonte: 14 slides de professor, 1 capítulo e 8
complementos estudantis, além do índice. Esse mapeamento melhora a ancoragem
curricular, mas não representa revisão clínica profunda das 1.013 páginas.

## Superfícies

| Superfície | Resultado | Denominador |
|---|---|---|
| Codex | qualificado | 13/13 behavioral; 9/9 jornadas válidas |
| Claude | não avaliado | 0 execuções qualificadas; OAuth pendente |

Resultados Claude e Codex não foram misturados.

## Limitações e autoridade

- O pacote não substitui julgamento clínico nem diretriz vigente.
- A ausência das camadas opcionais `corpus_text/` e `vision_png/` força
  degradação honesta para `metadata_only`.
- A qualificação não é estudo de usabilidade com alunos reais.
- `READY_FOR_USER_REVIEW` entrega uma primeira versão defensável; somente o
  usuário decide merge, tag e publicação.
