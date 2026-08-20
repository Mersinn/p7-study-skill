# OSCE Neurologia — AVC isquêmico, AVC hemorrágico, AIT, coma e TCE

## Metadados

- Disciplina: OSCE
- Especialidade: Neurologia
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não (as 3 fontes do cluster são NATIVA; nenhuma exigiu leitura por visão)
- Fontes usadas: `OSCE .pdf` (camada B, doc. de 101 páginas com marcador de rodapé por slide, permitindo paginação exata: quadro clínico/Cincinnati/isquêmico×hemorrágico ~p.4-5; tratamento do AVCi ~p.6-7; AVCh intraparenquimatoso e subaracnoide ~p.8; TCE — estratificação de risco ~p.9, Escala de Coma de Glasgow ~p.10, hematomas ~p.11, conduta geral ~p.12; coma — anamnese ~p.13, exame neurológico e conduta ~p.14-16; caso clínico completo com comandos e gabarito ~p.18); `FACILITA OSCE (1).pdf` (camada B, 67 páginas com sumário próprio — Cefaleias p.5, AVCi p.9, AVCh p.14 — texto discursivo mais didático, cobre também AIT dentro da seção de AVCi, próximo à divisa com AVCh, ~p.13); `OSCE - NEUROLOGIA.pdf` (camada B, formato tabela contínua doença/sinais/exame/diagnóstico/tratamento/outros, 8 páginas no total pelo cluster, sem marcador de página detectável na extração de texto — citada como documento íntegro, sem pin de página por tópico)
- Evidência de prova/devolutiva: nenhuma devolutiva de prova teórica nesta fonte — as 3 fontes são material de revisão de colegas especificamente preparado para o OSCE, incluindo 1 caso clínico completo com comandos numerados e gabarito comentado (AVC hemorrágico/isquêmico) em `OSCE .pdf`
- Limitações da fonte: nenhuma fonte disponível traz um escore formal de estratificação de risco de AVC pós-AIT (ex. ABCD2) — as fontes só dizem "avaliar risco de desenvolver AVC em 48h", sem detalhar o instrumento; fica como pendência (`confirmar no slide`). `OSCE .pdf` descreve a pupila do hematoma extradural como "midríase bilateral", o que diverge do ensino padrão (pupila fixa e dilatada **ipsilateral** à lesão, por compressão do III par na herniação uncal; midríase bilateral é sinal tardio/pré-terminal de herniação transtentorial bilateral) — tratado abaixo como CORRIGIDO, prevalecendo o conhecimento geral por ser consistente com a fisiopatologia da compressão unilateral do nervo oculomotor e por ser o achado classicamente cobrado. Nenhuma fonte tem camada A (não há slide do professor mapeado para este tema no cluster).
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

A cabine de Neurologia do OSCE do P7 combina reconhecimento de síndrome (déficit neurológico súbito → suspeitar de AVC) com um funil de decisão que só se resolve por **imagem**: a mesma apresentação clínica de déficit focal súbito pode ser isquêmica ou hemorrágica, e as fontes são explícitas — "só posso dar o diagnóstico e a conduta por neuroimagem". O caso clínico completo disponível nas fontes (`OSCE .pdf`) treina exatamente esse funil: hipótese ampla ("AVE hemorrágico ou isquêmico") → exame físico (Escala de Cincinnati) → leitura do exame complementar já disponível na cabine (TC de crânio) → só então fechar a etiologia e a conduta. Em TCE e coma, o padrão muda: a operação central é aplicar uma escala objetiva (Glasgow, estratificação de risco do TCE) antes de decidir entre observação, TC ou intervenção.

## A estação

- **Tarefa:** a partir do caso clínico (geralmente déficit neurológico súbito ou trauma craniano), reconhecer a síndrome, aplicar a escala/critério pertinente (Cincinnati, NIHSS, Glasgow, estratificação de risco do TCE, Hunt-Hess), interpretar o exame de imagem já disponível na cabine e só então fechar hipótese e conduta.
- **Tempo:** não informado nas fontes disponíveis.
- **Ator/paciente:** caso clínico escrito; o exame físico na cabine de neurologia costuma ser pobre ou já descrito no próprio caso ("na cabine de neurologia, o exame físico pode ser pobre ou já ter sido descrito no caso clínico, mas mesmo assim, veja seu paciente, pelo menos brevemente, sobretudo a região da cabeça" — `FACILITA OSCE (1).pdf`).
- **Material:** resultado de TC de crânio (com ou sem contraste, conforme o caso) já disponível na cabine quando o comando pedir interpretação de imagem.
- **Critério do checklist (inferido):** citar a escala/critério correto antes de nomear a etiologia; não afirmar "isquêmico" ou "hemorrágico" só pela clínica sem citar o achado de imagem; checar o tempo de início dos sintomas antes de propor conduta; checar contraindicações antes de indicar trombólise.

## Pivô clínico

O pivô é duplo. Primeiro, **isquêmico × hemorrágico não se define pela clínica** — só pela TC de crânio sem contraste (hipodenso e visível só após 24-72h no isquêmico; hiperdenso e imediato no hemorrágico). Segundo, dentro do próprio AVC isquêmico, o pivô é o **tempo desde o início dos sintomas** (janela de 4h30 para trombólise, até 24h para trombectomia com critério radiológico avançado, >24h vira conduta conservadora) — o mesmo quadro clínico muda de conduta completamente conforme esse único dado temporal.

## Palavras-âncora

Escala de Cincinnati (sorrir/abraçar/falar) · NIHSS · janela de 4h30 · alteplase (rt-PA) · trombectomia mecânica · hipertensão permissiva · TC de crânio sem contraste · hipodenso (isquêmico) × hiperdenso (hemorrágico) · AIT · tríade cefaleia + síncope + rigidez nucal · escala de Hunt-Hess · nimodipino · Escala de Coma de Glasgow · sinal de Guaxinim/Battle · pupila anisocórica × isocórica × puntiforme.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| priorizar emergência / aplicar critério | janela terapêutica do AVCi: ≤4h30 trombólise · 4h30-24h trombectomia (com critério radiológico) · >24h conservador | limiar | operacional | premissa não checada — tratar "início súbito" como sinônimo de "dentro da janela", sem confirmar a hora exata do ictus antes de propor trombólise | treinar casos idênticos variando só o tempo de ictus (3h, 5h, 20h, "acordou com o déficit" = hora desconhecida), forçando escolher a conduta certa a cada variação |
| diferenciar próximos | isquêmico × hemorrágico só se define por TC (hipodenso × hiperdenso) | sinal-achado | factual | fechamento precoce — nomear a etiologia só pela clínica (afasia, hemiparesia) antes de citar o achado tomográfico disponível na cabine | treinar a resposta-ponte obrigatória "não dá para afirmar isquêmico ou hemorrágico só pela clínica" antes de descrever qualquer achado de imagem |
| reconhecer contraindicação | contraindicações à trombólise: AVC recente, TCE <3 meses, coagulopatia, PA >185×110 não controlada | contraindicação | operacional | indicar trombólise sem checar a lista de contraindicações, sobretudo a PA (que precisa ser controlada, não vira CI absoluta) | checklist fixo de contraindicações revisado antes de fechar qualquer conduta de AVCi dentro da janela |
| priorizar emergência | sinais de herniação (pupila anisocórica/fixa, deterioração do nível de consciência) no TCE não esperam a estratificação completa | prioridade | operacional | fechamento precoce inverso — aplicar a régua padrão de "baixo/moderado/alto risco" a um paciente que já mostra sinal de herniação em curso, adiando o acionamento da neurocirurgia | treinar reconhecimento de sinais de herniação como gatilho de contato neurocirúrgico imediato, independente de completar toda a anamnese de estratificação |
| aplicar critério | estratificação de risco do TCE (baixo/moderado/alto) decide observação domiciliar × TC + observação × TC + internação | limiar/sequência | operacional | pular a estratificação (pedir TC em todo TCE leve) ou, no outro extremo, liberar um paciente de risco moderado/alto sem TC | treinar a tabela de 3 níveis com casos variando 1 achado por vez (ex.: só trocar "vômito ausente" por "vômito presente") |
| interpretar imagem/ecg/laboratório | aspecto do hematoma na TC: biconvexo = extradural · côncavo = subdural | sinal-achado | factual | trocar o par (achar que o aspecto côncavo é extradural) | flashcard de par opositivo aspecto-de-imagem × tipo-de-hematoma, revisado junto com a lateralidade da pupila esperada em cada um |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Escala de Cincinnati | Sorrir (assimetria facial) · Abraçar (assimetria de força nos braços) · Falar (disartria/frase "o rato roeu a roupa do rei de Roma") | `OSCE .pdf`, ~p.4-5 / `OSCE - NEUROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| Isquêmico × hemorrágico à TC | isquêmico: hipodenso, visível só após 24-72h · hemorrágico: hiperdenso, visível de imediato | `OSCE .pdf`, ~p.5 | CONFIRMADO |
| Janela de trombólise (alteplase/rt-PA) | até 4h30 do início dos sintomas; dose 0,9 mg/kg (máx. 90 mg), 10% em bolus + 90% em bomba de infusão em 1h | `OSCE .pdf`, ~p.6 / `FACILITA OSCE (1).pdf`, p.9 | CONFIRMADO |
| PA que autoriza iniciar trombolítico | <185×110 mmHg; se acima, controlar com nitroprussiato de sódio EV antes de trombolisar | `OSCE .pdf`, ~p.6 / `FACILITA OSCE (1).pdf`, p.9 | CONFIRMADO |
| Trombectomia mecânica | até 6h por avaliação clínico-radiológica simples (TC/RM + angio, sobretudo se oclusão de artéria cerebral média); de 6-24h com técnicas avançadas de neuroimagem (estudos DAWN e DEFUSE-3) para calcular volume de isquemia | `FACILITA OSCE (1).pdf`, p.9 | CONFIRMADO |
| Wake-up stroke (hora de início desconhecida) | RM com mismatch FLAIR-difusão; trombólise possível se isquemia na difusão <1/3 do território da ACM e FLAIR ainda sem alteração (o FLAIR só se altera depois de 4,5h) | `FACILITA OSCE (1).pdf`, p.9 | CONFIRMADO |
| Controle de PA após 24h/conduta conservadora | intervir só se PA >220×120 mmHg (nitroprussiato de sódio EV) | `OSCE .pdf`, ~p.6-7 / `OSCE - NEUROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| Contraindicações citadas à trombólise | AVC recente, TCE <3 meses, coagulopatias | `OSCE - NEUROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| AIT — definição | classicamente sintomas <24h; definição atual aceita = ausência de evidência de morte neuronal nos exames de imagem, mesmo com sintomas breves; geralmente melhora em <1h, paciente chega assintomático ao PS | `FACILITA OSCE (1).pdf`, ~p.13 | CONFIRMADO |
| AIT — conduta | avaliar risco de desenvolver AVC em 48h (fonte não especifica o instrumento formal de estratificação, ex. ABCD2) | `FACILITA OSCE (1).pdf`, ~p.13 | confirmar no slide (instrumento de estratificação não nomeado na fonte) |
| Alvo pressórico da hemorragia intraparenquimatosa | PAS-alvo de 140 mmHg | `OSCE - NEUROLOGIA.pdf` (doc. íntegro) / `FACILITA OSCE (1).pdf`, p.14 | CONFIRMADO |
| Indicação cirúrgica na hemorragia intraparenquimatosa | hematoma cerebelar >3 cm · hematoma 1-3cm com repercussão neurológica · hematoma lobar/putaminal volumoso; sangue no ventrículo → derivação ventricular externa (DVE) | `OSCE .pdf`, ~p.8 / `OSCE - NEUROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| Tríade clássica de HSA | cefaleia holocraniana súbita e intensa + síncope + rigidez de nuca | `OSCE .pdf`, ~p.8 / `FACILITA OSCE (1).pdf`, p.5 | CONFIRMADO |
| Escala de Hunt-Hess | I: assintomático/cefaleia leve, GCS 15 · II: cefaleia/rigidez moderada-grave, pode acometer par craniano, GCS 13-14 · III: confusão/letargia, déficit focal leve possível, GCS 13-14 · IV: torpor, hemiparesia moderada-grave possível, GCS 7-12 · V: coma com/sem descerebração, GCS 3-6 | `OSCE - NEUROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| Punção lombar na suspeita de HSA com TC normal | realizar nas primeiras 12h; líquido sanguinolento = agudo; xantocrômico = subagudo | `OSCE .pdf`, ~p.8 / `OSCE - NEUROLOGIA.pdf` | CONFIRMADO |
| Momento da cirurgia de clampeamento do aneurisma | <3 dias do sangramento e Hunt-Hess <3: arteriografia + clampeamento precoce · RNC ou >3º dia: protelar cirurgia para 10-14 dias após o sangramento (evitar operar na janela de vasoespasmo) | `OSCE .pdf`, ~p.8 / `OSCE - NEUROLOGIA.pdf` | CONFIRMADO |
| Nimodipino na HSA | 60 mg VO a cada 4h, por até 3 semanas — neuroproteção/redução do risco de vasoespasmo | `OSCE - NEUROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| Complicações da HSA | ressangramento em 20% nos primeiros 7 dias · vasoespasmo entre o 3º e o 14º dia (déficit focal permanente/flutuante, RNC, mau prognóstico) · hidrocefalia · hiponatremia comum nas primeiras 2 semanas (SIADH ou cerebropatia perdedora de sal) | `OSCE - NEUROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| Escala de Coma de Glasgow | abertura ocular 4 (espontânea) a 1 (nenhuma) · resposta verbal 5 (orientada) a 1 (nenhuma) · resposta motora 6 (obedece comando) a 1 (nenhuma); trauma leve 13-15, moderado 9-12, grave 3-8 | `OSCE .pdf`, ~p.10 / `OSCE - NEUROLOGIA.pdf` | CONFIRMADO |
| Estratificação de risco do TCE | baixo (assintomático/cefaleia leve) → observação domiciliar · moderado (perda de consciência, cefaleia progressiva sem melhora, convulsão pós-traumática, vômitos, sinal de Guaxinim/Battle) → TC + observação hospitalar · alto (RNC progressivo, déficit focal, lesão penetrante/afundamento) → TC + internação | `OSCE .pdf`, ~p.9 / `OSCE - NEUROLOGIA.pdf` | CONFIRMADO |
| Hematoma extradural | aspecto biconvexo na TC; lesão arterial; rapidamente fatal; conduta = cirurgia imediata; pupila fixa e dilatada — a fonte cita "bilateral", mas o ensino padrão (conhecimento geral) associa esse achado à midríase **ipsilateral** por compressão do III par na herniação uncal, com midríase bilateral surgindo apenas em fase mais tardia/pré-terminal | `OSCE .pdf`, ~p.11; correção por conhecimento geral | CORRIGIDO |
| Hematoma subdural | aspecto côncavo na TC; hemorragia venosa; conduta = cirurgia precoce | `OSCE .pdf`, ~p.11 / `OSCE - NEUROLOGIA.pdf` | CONFIRMADO |
| Pupilas no coma/TCE | puntiformes = lesão de ponte · mediofixas = lesão de tronco cerebral · anisocóricas = possível herniação uncal · isocóricas e fotorreagentes = etiologia tóxico-metabólica | `OSCE - NEUROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| Medicações de emergência no coma | naloxona = antídoto de opioides · flumazenil = antídoto de benzodiazepínicos | `OSCE .pdf`, ~p.16 | CONFIRMADO |
| Meta ventilatória no TCE grave (GCS <8) | intubar; manter PA normal; PO2 ≈ 80 mmHg; PCO2 entre 25-35 mmHg; não deixar reter CO2 (CO2 alto → vasodilata e piora o inchaço; CO2 baixo → vasoconstringe e evita isquemia, mas em excesso também é deletério) | `OSCE .pdf`, ~p.12 | CONFIRMADO |

## Pegadinhas

**Imperdoáveis:**

- Anunciar "isquêmico" ou "hemorrágico" antes de citar o achado da TC — a própria fonte é explícita: "só posso dar o diagnóstico e a conduta por neuroimagem".
- Propor trombólise sem antes checar contraindicação (TCE <3 meses, coagulopatia, PA não controlada) ou sem confirmar a hora do ictus.
- Tratar hematoma extradural (cirurgia imediata) com a mesma prioridade temporal de um hematoma subdural (cirurgia precoce, mas não necessariamente "imediata") — a fonte diferencia os dois verbos.
- Em TCE, pular a estratificação de risco e já descrever conduta de "TC + internação" para um paciente que se encaixa em baixo risco (assintomático), ou o oposto — liberar um paciente com déficit focal sem TC.
- Não citar a escala aplicada (Cincinnati, Glasgow, Hunt-Hess) antes de descrever o achado — a estação cobra o nome da ferramenta, não só a impressão clínica.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "Paciente com hemiparesia súbita + afasia = AVC isquêmico" sem mencionar a TC | o quadro é o "clássico" de isquêmico mais decorado, e o candidato quer parecer rápido | fechamento precoce / narrativa acima do discriminador | a apresentação clínica de isquêmico e hemorrágico é indistinguível; só a TC sem contraste discrimina — a estação pontua o achado de imagem citado, não a velocidade do raciocínio |
| Indicar trombólise só porque "o paciente chegou rápido ao hospital", sem checar a PA nem o horário exato do início dos sintomas | ansiedade de "não perder a janela" | premissa não checada / valor errado | a janela de 4h30 conta a partir do **início dos sintomas**, não da chegada ao hospital, e a PA >185×110 precisa ser controlada antes, não ignorada |
| Classificar hematoma subdural como "cirurgia imediata" igual ao extradural, por serem "os dois hematomas de trauma" | os dois têm nome parecido e aparecem juntos na mesma tabela de estudo | analogia sem validação | o extradural (arterial, evolução rápida) é cirurgia imediata; o subdural (venoso, evolução mais lenta) é cirurgia precoce — tratá-los como sinônimos de urgência esconde a diferença fisiopatológica que justifica o verbo diferente |
| Em coma, já tratar como "AVC" ou "intoxicação" sem passar pela sequência de exame neurológico (nível de consciência → motora → pupilas → reflexos) | o candidato quer nomear uma etiologia rápido para parecer seguro | sobre-elaboração / fechamento precoce | a fonte descreve uma sequência fixa de exame no coma justamente porque o achado pupilar/motor é o que direciona a etiologia — pular direto para uma hipótese sem esse exame é chutar |

## Conduta

- Inicial: Escala de Cincinnati/NIHSS à beira-leito, contato com SAMU e hospital (nunca UPA), TC de crânio sem contraste assim que possível; em TCE, ABCDE do trauma priorizando SatO2/PA antes de fundo de olho e pares cranianos.
- Definitiva: no AVCi, terapêutica conforme o tempo de ictus (trombólise ≤4h30, trombectomia até 24h com critério radiológico, conservador >24h); no AVCh, suporte + controle pressórico específico por subtipo, com cirurgia reservada a critérios de tamanho/repercussão do hematoma; no TCE, conduta conforme a estratificação de risco (observação × TC × internação) e cirurgia imediata/precoce conforme o tipo de hematoma identificado.
- Condição da conduta: o tempo de início dos sintomas muda inteiramente a conduta do AVCi mesmo com clínica idêntica; a presença de sinal de herniação (pupila anisocórica, RNC progressivo) muda a prioridade em TCE e AVCh independentemente da estratificação padrão.
- Diferencial perigoso: hematoma extradural rapidamente fatal exige contato neurocirúrgico imediato; sinais de HIC (cefaleia + vômitos + papiledema + RNC) numa hemorragia intraparenquimatosa não esperam o fechamento diagnóstico completo.
- O que mudaria a decisão: hora exata do início dos sintomas (dentro ou fora da janela), presença de contraindicação à trombólise, achado de imagem (isquêmico × hemorrágico, aspecto biconvexo × côncavo), e nível de consciência (GCS <8 muda a via aérea).

## Mini-casos ativos

1. H.F.C., 67 anos, trazido pela filha com perda de força em hemicorpo esquerdo e dificuldade para falar **há 1 dia**, afebril, dispneico, diabético em uso de metformina. TC de crânio já disponível mostra lesão hipodensa predominante à esquerda. **Pivô:** o "há 1 dia" já ultrapassou a janela de 24h — mesmo com TC confirmando etiologia isquêmica, a conduta correta é conservadora (monitoramento, controle pressórico só se PA >220×120, controle glicêmico, antiplaquetário), não trombólise nem trombectomia.
2. Paciente com cefaleia holocraniana súbita e intensa, síncope no início do quadro e rigidez de nuca que só apareceu no dia seguinte. TC de crânio sem contraste normal. **Pivô:** TC normal não descarta HSA — a tríade clínica típica exige punção lombar nas primeiras 12h (procurando líquido xantocrômico/sanguinolento) antes de afastar o diagnóstico.
3. Vítima de queda, GCS 14, sem déficit focal, um episódio de vômito e cefaleia progressiva sem melhora. **Pivô:** esse conjunto já preenche critério de risco moderado (perda de consciência OU cefaleia progressiva sem melhora OU vômitos) — a conduta é TC de crânio + observação hospitalar, não alta com orientação domiciliar como se fosse baixo risco.
4. Paciente encontrado em coma, sem história disponível, pupilas puntiformes e fotorreagentes. **Pivô:** pupila puntiforme sugere lesão pontina, mas isocórica/fotorreagente também é clássica de etiologia tóxico-metabólica — antes de fechar etiologia, colher sangue para investigar intoxicação e considerar naloxona/flumazenil empíricos conforme o quadro, seguindo a sequência de exame neurológico do coma, não uma hipótese isolada pela pupila.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Janela de trombólise no AVCi e dose da alteplase | Até 4h30 do início dos sintomas; 0,9 mg/kg (máx. 90mg), 10% bolus + 90% em BI por 1h | valor |
| Só a partir de que exame se define isquêmico × hemorrágico? | TC de crânio sem contraste (nunca só pela clínica) | regra |
| PA que autoriza iniciar trombolítico | <185×110 mmHg (controlar com nitroprussiato antes, se acima) | limiar |
| Tríade clássica de HSA | Cefaleia súbita e intensa + síncope + rigidez de nuca | fato |
| Aspecto do hematoma extradural × subdural na TC | Extradural = biconvexo (lente); Subdural = côncavo | sinal-achado |
| Conduta na hemorragia intraparenquimatosa com hematoma cerebelar >3cm | Cirurgia de drenagem | limiar |
| 3 níveis de risco do TCE e a conduta de cada um | Baixo → observação domiciliar; Moderado (perda de consciência/cefaleia progressiva/vômitos/sinal de Battle) → TC + observação; Alto (RNC/déficit focal/lesão penetrante) → TC + internação | sequência |
| GCS <8: o que fazer com a via aérea? | Intubar | regra |
| Antídotos usados empiricamente no coma | Naloxona (opioides) e flumazenil (benzodiazepínicos) | fato |

## Revisão

- Revisar quando: antes de qualquer simulação de estação de neurologia, e sempre que o caso variar o tempo de início dos sintomas (é o discriminador mais repetido nas fontes).
- Critério de parada: quando conseguir, dado um caso de déficit neurológico súbito, nomear corretamente a escala aplicável, recusar-se a fechar etiologia sem imagem, e ajustar a conduta a 3 variações de tempo de ictus (dentro da janela, entre 4h30-24h, e >24h) sem consultar a fonte.
