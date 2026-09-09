# Antipsicóticos, Sintomas Extrapiramidais e Síndrome Neuroléptica Maligna

## Metadados

- Disciplina: EISM
- Especialidade: Psiquiatria
- Unidade: II
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l2
- Transcription: confirmed
- Curricular alignment: confirmed
- Clinical validity: pending (overlay clozapina específico dos EUA; Brasil excluído de conduta atual)
- Independent review: reviewed_l2
- Reviewer ID: `agent:clinica_reparos:2026-08-20`
- Modelo: OpenAI Codex, modelo herdado; versão exata de serving não exposta
- Revisão clínica humana: pendente
- Camada de fonte usada: A+A'+B
- fonte_visual: sim (`Esquizofrenia_e_antipsic_ticos__4b3ccca107` pp.33–38 conferidas por imagem — slide do prof. Roberto Mendes)
- Fontes usadas: FAMENE_FARMACOTERAPIA_DAS_PSICOSES_2025_1__e5e9511748 (A', prof. Macêdo, texto nativo íntegro); Esquizofrenia_e_antipsic_ticos__4b3ccca107 (A, ESCANEADA, prof. Roberto Mendes, confirmado por imagem); Antipsico_ticos_II_unidade__bea4c8f456 (B, Karen); Antipsico_ticos_Tabela__1d16c62d2d (B, Bianca)
- Evidência de prova/devolutiva: blueprint marca frequência MUITO ALTA para "efeitos extrapiramidais e seu manejo: parkinsonismo x acatisia x distonia aguda x SNM, e fármacos que tratam cada um" (fontes: paciente 65 anos + haloperidol; DEV_SM/Integrada Q734 — distonia aguda; UFC 2016 adaptada — acatisia, resposta correta diazepam, distrator biperideno). O blueprint cita explicitamente que a questão de EP por haloperidol em paciente de 65 anos "aparece repetida quase literalmente entre fontes"
- Limitações da fonte: síndrome neuroléptica maligna e discinesia tardia não apareceram nas páginas visualizadas do deck ESCANEADA (Roberto Mendes) — dados desses dois vêm da tabela do slide A' (Macêdo) e da apostila B, convergentes; não há imagem de tabela de doses de clozapina na fonte visual
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

MUITO ALTA frequência. Vinheta clínica clássica: paciente idoso (~65 anos) em uso de haloperidol
desenvolve um sintoma motor — a prova espera que o aluno diferencie qual síndrome extrapiramidal é
(pelo tempo de uso + fenomenologia) e escolha o tratamento certo dentre alternativas que misturam
biperideno, propranolol/benzodiazepínico e dantroleno como distratores cruzados. Também cai
comando inverso ("assinale a INCORRETA") e questões sobre agranulocitose por clozapina
(reintrodução após neutropenia não é proibição absoluta).

## Conceito operacional mínimo

Todo antipsicótico bloqueia receptores D2. O bloqueio D2 na via nigroestriatal causa a síndrome
extrapiramidal (SEP); na via tuberoinfundibular causa hiperprolactinemia; na via mesolímbica trata
sintomas positivos; na via mesocortical, se bloqueada em excesso, piora sintomas negativos. 1ª
geração (típicos): maior SEP, menor risco metabólico. 2ª geração (atípicos, bloqueiam também
5HT2A): menor SEP e hiperprolactinemia, maior risco metabólico (peso, glicemia, triglicerídeos).

## Pivô clínico

Diante de qualquer sintoma motor após antipsicótico, a variável decisiva é o TEMPO DE USO +
FENOMENOLOGIA, não apenas "o paciente é idoso, logo dou biperideno":
- Horas a 1–5 dias, espasmo/postura anormal (olhos, pescoço, membros, língua) → distonia aguda →
  biperideno.
- 5–60 dias, inquietação motora, não consegue ficar sentado → acatisia → NÃO é biperideno;
  tratar com propranolol ou benzodiazepínico (± reduzir dose/trocar fármaco).
- 5–30 dias, bradicinesia + rigidez + tremor + marcha arrastada (SEP mais frequente; idoso maior
  risco) → parkinsonismo farmacológico → biperideno.
- Semanas a meses, rigidez EXTREMA + febre + PA instável + mioglobinemia → SNM → suspender o
  antipsicótico + dantroleno + suporte intensivo (nunca biperideno).
- Meses a anos, movimentos orofaciais estereotipados, idoso com risco 5x maior, pode ser
  irreversível → discinesia tardia → prevenção é a única estratégia eficaz.
Armadilha do blueprint: biperideno (anticolinérgico) NÃO é automaticamente seguro em idoso — o
efeito anticolinérgico agravado nessa faixa etária é o próprio ponto que a prova cobra.

## Palavras-âncora

distonia aguda · acatisia · parkinsonismo farmacológico (PIF) · discinesia tardia · síndrome
neuroléptica maligna · dantroleno · biperideno · propranolol · hiperprolactinemia · via
nigroestriatal/mesolímbica/mesocortical/tuberoinfundibular · agranulocitose · janela terapêutica
estreita (1ª geração)

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | tempo de uso + fenomenologia que discrimina distonia/acatisia/parkinsonismo/SNM/discinesia tardia | sinal-achado | operacional | regra mal-aprendida | dado só tempo+fenomenologia (sem nome da síndrome), forçar classificar antes de escolher o reversor — nunca ir direto a "biperideno" |
| reconhecer contraindicação | efeito anticolinérgico do biperideno agravado em idoso (não é "seguro por ser padrão") | contraindicacao | operacional | premissa não checada | antes de prescrever biperideno em idoso, checklist: confusão/retenção urinária/boca seca já presentes? |
| identificar complicação | febre + instabilidade de PA + mioglobinemia isola SNM das demais SEP | sinal-achado | factual | valor errado | flashcard de par SNM×acatisia/distonia pelos 3 sinais autonômicos, não só "rigidez" |
| aplicar critério | agranulocitose por clozapina não é contraindicação absoluta de reintrodução — depende de gravidade/tempo de resolução | limiar | factual | superextrapolação | card do protocolo de reintrodução + vinheta de neutropenia leve resolvida vs grave persistente |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Distonia aguda — tempo / tratamento | Horas ou 1–5 dias; biperideno 5mg/1mL IM ou EV | Esquizofrenia_e_antipsic_ticos p.33 (imagem, A); FAMENE Psicoses (A') | CONFIRMADO (dose exata só na imagem) |
| Acatisia — tempo / tratamento | 5–60 dias; ↓dose ou trocar fármaco; clonazepam/propranolol MAIS eficazes que biperideno | Esquizofrenia_e_antipsic_ticos p.35 (imagem, A); FAMENE Psicoses (A') | CONFIRMADO |
| Parkinsonismo farmacológico — tempo / tratamento | 5–30 dias; SEP mais frequente; idoso maior risco; biperideno VO/IM/EV | Esquizofrenia_e_antipsic_ticos p.34 (imagem, A); FAMENE Psicoses (A') | CONFIRMADO |
| Síndrome neuroléptica maligna — tempo / tratamento | Semanas a meses; interromper antipsicótico + dantroleno + suporte intensivo | FAMENE Psicoses (A', texto nativo) | CONFIRMADO |
| Discinesia tardia — tempo / risco idoso | Meses a anos; idoso risco 5x maior; irreversível se diagnóstico tardio | FAMENE Psicoses (A') | CONFIRMADO |
| Haloperidol — apresentações | cp/sol oral/inj 1, 5 e 10mg | FAMENE Psicoses (A', texto nativo) | CONFIRMADO |
| Clozapina — ANC, rótulo FDA 2025 | ANC basal; semanal 0–6 meses, a cada 2 semanas 6–12 meses, mensal após 12 meses se ANC normal | FDA label 2025, Table 2 | CURRENT_VERIFIED_US |
| Clozapina — limiares FDA | normal ≥1500/µL; leve 1000–1499: continuar e monitorar; moderada 500–999: interromper/hematologia; grave <500: interromper | FDA label 2025, Table 2 | CURRENT_VERIFIED_US |
| Clozapina REMS nos EUA | FDA removeu o REMS em 13/06/2025; o risco e a monitorização do rótulo permanecem | FDA notice 2025 | CURRENT_VERIFIED_US |
| Clozapina no Brasil | periodicidade e interrupção devem seguir bula Anvisa vigente/protocolo local; não importar REMS dos EUA | jurisdição ainda sem bula oficial 2026 resolvida | CURRENT_PENDING |
| “Associar fenitoína ou valproato se convulsão” | consta no material | fonte curricular | QUARANTINED — interação/conduta exige avaliação individual |
| Risperidona — dose de menor risco de SEP | <6mg/dia | FAMENE Psicoses (A') + B | CONFIRMADO |
| Quetiapina — dose por indicação | Hipnótico 25–50mg; antidepressivo <300mg XR; antipsicótico >300mg (até 800mg/dia) | FAMENE Psicoses (A') + FAMENE Insônia/Ansiedade p.42 (imagem, A') | CONFIRMADO (2 decks do mesmo professor convergem) |
| Benefício antipsicótico observado após | 1–2h da administração (psicose aguda) | FAMENE Psicoses (A', texto nativo) | CONFIRMADO |

## Pegadinhas

- Biperideno NÃO é a resposta automática para todo sintoma extrapiramidal — errado quando o
  quadro descrito é acatisia (tratar com propranolol/benzodiazepínico).
- Não confundir SNM (tratar com dantroleno, suspender antipsicótico) com acatisia ou distonia
  aguda — a diferença-chave é febre + instabilidade autonômica + rigidez extrema + tempo de
  evolução (semanas a meses).
- Idoso com SEP não implica "pode dar biperideno com segurança" — anticolinérgico agrava
  confusão/retenção urinária/boca seca em idoso; a prova usa esse raciocínio como armadilha.
- Reintrodução de clozapina após neutropenia não é uma regra simples: depende de
  gravidade, etiologia, jurisdição e balanço risco-benefício; decisão especializada.
- O fim do Clozapine REMS nos EUA em 2025 não eliminou risco nem monitorização do
  rótulo e não altera automaticamente a prática regulatória brasileira.
- A mesma vinheta de "comprimido amarelo" (agitação por ecstasy) aparece com gabaritos
  DIVERGENTES entre provas de anos diferentes — não fixar uma única resposta memorizada sem
  conferir a versão da prova em jogo.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Biperideno para acatisia | É o antídoto "padrão" para SEP que o aluno decora | regra mal-aprendida | Acatisia responde melhor a propranolol ou benzodiazepínico; biperideno é para distonia/parkinsonismo |
| Biperideno para SNM | Parece a mesma lógica dos outros SEP | analogia sem validação | SNM trata-se suspendendo o antipsicótico + dantroleno + suporte, não com anticolinérgico |
| "Idoso, então biperideno é seguro" | Anticolinérgico parece inócuo por ser "só para tremor" | premissa não checada | Em idoso, o efeito anticolinérgico central é agravado (confusão, retenção urinária) — a prova cobra exatamente essa cautela |
| “Sem REMS = sem hemograma/ANC” | confunde programa regulatório com risco | superextrapolação | FDA retirou o REMS, mas manteve recomendações de ANC no rótulo |

## Conduta

- Inicial: identificar tempo de uso do antipsicótico + fenomenologia do movimento (espasmo focal x
  inquietação x rigidez/bradicinesia x rigidez extrema+febre) antes de escolher a droga reversora.
- Definitiva: distonia e parkinsonismo → biperideno; acatisia → propranolol/benzodiazepínico
  (± ajuste de dose); discinesia tardia → prevenção (reconhecimento precoce + descontinuar);
  SNM → suspender antipsicótico + dantroleno + suporte intensivo.
- Condição da conduta: em idoso, pesar sempre o efeito anticolinérgico do biperideno antes de
  prescrever.
- Diferencial perigoso: SNM × síndrome serotoninérgica × hipertermia maligna — todas cursam com
  rigidez/febre, mas SNM tem instalação em dias/semanas após antipsicótico e responde a dantroleno.
- O que mudaria a decisão: febre + instabilidade de PA + mioglobinemia muda toda a conduta para
  SNM (emergência, suspender droga); tempo de uso menor que 5 dias aponta para distonia, não
  parkinsonismo.
- Clozapina: febre/infeção ou queda de ANC exige hemograma/ANC, avaliação de
  gravidade e protocolo da jurisdição. Não associar anticonvulsivante por memória.

## Mini-casos ativos

1. Paciente 65 anos, haloperidol há 3 dias, inquietação motora constante, não consegue ficar
   sentado → acatisia. Variável decisiva: tempo curto + fenomenologia de inquietação (não rigidez).
   Conduta: propranolol/benzodiazepínico, NÃO biperideno.
2. Mesmo paciente, mas há 3 semanas de uso, com rigidez, tremor, marcha em bloco, fácies
   inexpressiva → parkinsonismo farmacológico. Variável decisiva: tempo (5–30 dias) + rigidez.
   Conduta: biperideno.
3. Paciente em antipsicótico há 3 semanas, rigidez muscular extrema, febre 39,5°C, PA instável →
   SNM. Variável decisiva: febre + instabilidade autonômica + rigidez extrema. Conduta: suspender
   o antipsicótico + dantroleno + suporte intensivo.
4. Jovem, virgem de tratamento, horas após 1ª dose de haloperidol, crise oculógira e torcicolo →
   distonia aguda. Variável decisiva: tempo (horas) + jovem + espasmo focal. Conduta: biperideno
   5mg IM/EV.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Acatisia — tratamento | Propranolol ou benzodiazepínico (NÃO biperideno) | risco |
| SNM — tratamento | Suspender antipsicótico + dantroleno + suporte intensivo | risco |
| Distonia aguda — tempo e tratamento | Horas a 1–5 dias; biperideno 5mg IM/EV | dado numérico |
| Parkinsonismo farmacológico — tempo | 5–30 dias, SEP mais frequente, idoso maior risco | dado numérico |
| Discinesia tardia — risco no idoso | 5x maior; pode ser irreversível se diagnóstico tardio | dado numérico |
| Clozapina — ANC no rótulo FDA 2025 | semanal 0–6m; quinzenal 6–12m; mensal >12m, se normal | dado numérico |
| Fim do REMS nos EUA | não elimina risco/monitorização e não define regra brasileira | jurisdição |
| Risperidona — dose de menor SEP | <6mg/dia | dado numérico |
| Por que biperideno em idoso exige cautela | Efeito anticolinérgico central agravado (confusão, retenção urinária) | risco |

## Revisão

- Revisar quando: antes de qualquer simulado de EISM — este é o tema de maior frequência
  confirmada no blueprint.
- Critério de parada: quando conseguir, dado só o tempo de uso + fenomenologia (sem olhar a
  tabela), classificar corretamente distonia x acatisia x parkinsonismo x SNM x discinesia tardia
  e citar o tratamento certo de cada um, incluindo a armadilha do biperideno em idoso.

## Fontes de vigência — clozapina

- FDA, rótulo de clozapina, revisão 2025, Table 2: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/019758s106lbl.pdf
- FDA, remoção do Clozapine REMS efetiva em 13/06/2025: https://www.fda.gov/media/188418/download?attachment=
