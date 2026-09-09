# CAPSULE_REVIEW_CHECKLIST — P7

Passe esta lista antes de aceitar qualquer cápsula gerada.
Herdada da P6 v2.1.0, com dois blocos novos (camada de fonte e operação × movimento).

## Rastreabilidade da fonte

- [ ] Fontes listadas por `source_id`, presentes no `00_SOURCE_MANIFEST.csv`.
- [ ] Sem dependência de caminho local do Windows.
- [ ] Evidência de prova separada de conteúdo didático.
- [ ] Fonte fraca marcada como tal.
- [ ] `Limitações da fonte` preenchido — vazio só se não houver limitação real.

## Camada de fonte

- [ ] `Camada de fonte usada` declarada (A · A′ · B · C).
- [ ] Se o tema **tem** slide do professor, a camada A foi aberta.
- [ ] `fonte_visual` com faixa de páginas quando a leitura foi por imagem.
- [ ] Divergência A × B registrada, com A prevalecendo **para alinhamento
  curricular/prova**; em vigência clínica, A não prevalece sobre A′ atual.
- [ ] Nenhuma anotação manuscrita tratada como fala do professor.
- [ ] Nenhum número extraído do `.txt` de fonte ESCANEADA.

## Qualidade médica

- [ ] Pivô clínico explícito — um, não uma lista.
- [ ] Conduta inicial × definitiva separadas quando relevante.
- [ ] Exame inicial × melhor exame separados quando relevante.
- [ ] Diferencial perigoso incluído quando relevante.
- [ ] `O que mudaria a decisão` preenchido em tema de risco alto.
- [ ] Nenhuma afirmação médica sem sustentação.
- [ ] Transcrição, alinhamento curricular, vigência clínica e revisão independente
  têm estados separados; conflito, pendência e quarentena estão explícitos.
- [ ] Camada A pode confirmar o que foi ensinado, mas não é usada sozinha para
  marcar claim crítico como clinicamente atual.
- [ ] Claim crítico sem vigência resolvida está em quarentena para uso clínico.

## Dados de precisão

- [ ] Todo número da cápsula está na tabela de precisão.
- [ ] Cada linha tem fonte/página e estados separados de transcrição, vigência e
  revisão independente.
- [ ] Conflito traz as versões e a resolução, sem `CONFIRMADO` genérico.
- [ ] `transcription: pending` usado em vez de número adivinhado.
- [ ] Dado de conhecimento geral está **rotulado** como tal.

## Qualidade de prova

- [ ] `Como cai` ancorado no `00_EXAM_BLUEPRINT.md` quando há evidência.
- [ ] Sem evidência → escrito "sem evidência de cobrança no Source Pack".
- [ ] Pegadinhas específicas, não genéricas.
- [ ] Distratores explicam por que seduzem **e** por que erram.
- [ ] Risco de comando inverso considerado.

## Operação × movimento

- [ ] Tabela preenchida com operações reais do tema quando houver evidência.
- [ ] Cada linha nomeia a variável decisiva e o tipo dela.
- [ ] Natureza da **demanda do item** classificada como factual, operacional ou
  mista — nunca apresentada como causa do erro do aluno.
- [ ] Movimento é apenas candidato e exige evidência individual observada.
- [ ] Treino indicado é específico ao movimento sustentado, não "estudar mais".
- [ ] Nenhuma linha genérica que caberia em qualquer tema.

## Recuperação ativa

- [ ] Prompt/minicaso está separado da chave de feedback.
- [ ] A primeira view não revela resposta, pivô aplicado, conduta nem card que
  resolva o item antes da tentativa.
- [ ] Worked example, quando usado para nível zero, está rotulado e seguido de item
  isomórfico sem solução.

## Economia de contexto

- [ ] Não virou capítulo de livro.
- [ ] Sem temas vizinhos desnecessários.
- [ ] Cards mínimos e que previnem erro futuro.
- [ ] `study_core` chega rapidamente à primeira tentativa; custo é medido em
  tokens/tempo/experiência, não por corte fixo em KB.

## Revisão

- [ ] L1 está identificado como auto-revisão de transcrição, não independente.
- [ ] L2 registra `reviewer_id`, tipo (`model | human`) e data; modelo independente
  não é descrito como validação clínica humana.
- [ ] Cápsula/claim alto risco sem `clinical_validity: current` e revisão exigida
  permanece em quarentena para conduta.

## Decisão

- [ ] Aprovada.
- [ ] Precisa de patch — qual: ______________________
- [ ] Rejeitar e regerar.
