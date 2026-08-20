# Banco de estações OSCE modeladas com comandos e gabarito

## Metadados

- Disciplina: OSCE
- Especialidade: OSCE (banco de casos, multiespecialidade)
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não (fonte é NATIVA)
- Fontes usadas: `OSCE .pdf` (camada B, único documento mapeado para este tema no cluster — 101 páginas com marcador por slide, permitindo paginação exata. É um material de revisão de colega feito especificamente no formato caso clínico + comandos numerados + gabarito comentado, cobrindo Neurologia, Urologia, Nefrologia, Endocrinologia e Pediatria. As 6 estações abaixo foram modeladas a partir do conteúdo doutrinário confirmado nas cápsulas de especialidade já produzidas para este mesmo cluster de fontes — `osce_neurologia.md`, `osce_urologia.md` e `osce_pediatria.md` — para evitar repetir os 2 casos clínicos completos já usados como mini-caso nessas cápsulas (AVC em Neurologia ~p.18; HPB em Urologia ~p.40; diarreia com desidratação grave em Pediatria ~p.100); as estações aqui são vinhetas curtas novas, construídas sobre o mesmo corpo de dados já verificado)
- Evidência de prova/devolutiva: nenhuma devolutiva de prova teórica — a fonte é material de revisão de colega para o próprio OSCE
- Limitações da fonte: as estações abaixo são modelagens próprias (formato "estação curta" pedido para este tema-banco), não transcrição literal de um caso já pronto na fonte — o **conteúdo médico** de cada uma vem das tabelas de dados de precisão já verificadas nas cápsulas de especialidade citadas acima (que remetem às páginas exatas de `OSCE .pdf`, `OSCE - NEUROLOGIA.pdf`, `OSCE - UROLOGIA.pdf`, `OSCE - PEDIATRIA.pdf` e `FACILITA OSCE (1).pdf`), não uma página nova não verificada. Nenhuma fonte tem camada A.
- Verificação nível 1: CONFIRMADO (os dados clínicos de cada estação foram conferidos contra a tabela "Dados de precisão" já revisada nas cápsulas de especialidade correspondentes, listadas fonte a fonte abaixo)

## Como cai

Este tema não é um assunto clínico — é o **formato do dia da prova**: várias cabines temáticas curtas, cada uma com 2-4 comandos, aplicadas em sequência. O erro mais caro nesse formato não é de conteúdo médico, é de **execução da estação**: responder o comando errado, pular a higienização das mãos, ou gastar o tempo todo em uma única cabine por excesso de detalhamento quando o comando pedia uma resposta objetiva. Por isso, o treino ideal é rodar estações curtas cronometradas, comando por comando, sem o aluno ver a estação inteira de uma vez.

## Banco de estações (bloco central desta cápsula)

### Estação 1 — Neurologia: TCE leve com sinal de alarme

- **Caso:** paciente de 24 anos, vítima de queda de bicicleta, GCS 15 na chegada, sem déficit focal. Refere 1 episódio de vômito no trajeto e cefaleia que não melhora com analgésico simples.
- **Comando 1:** classifique o risco deste TCE.
- **Comando 2:** qual a conduta a partir dessa classificação?
- **Comando 3:** cite 2 achados de exame físico que, se presentes, mudariam a classificação para alto risco.
- **Gabarito/checklist:** (1) risco **moderado** — vômito e cefaleia progressiva sem melhora já preenchem o critério, mesmo com GCS 15 e sem déficit focal; (2) TC de crânio + observação hospitalar (não alta domiciliar, não internação direta sem TC); (3) déficit neurológico focal ou lesão penetrante/fratura em afundamento (classificam como alto risco → TC + internação). *Fonte dos dados: `osce_neurologia.md`, tabela "Estratificação de risco do TCE" (`OSCE .pdf`, ~p.9).*

### Estação 2 — Urologia: cólica renal com dúvida de conduta

- **Caso:** homem, 45 anos, dor lombar em cólica há 6h, sem febre, TC sem contraste mostra cálculo de 0,9cm em ureter proximal, sem hidronefrose.
- **Comando 1:** qual o exame padrão-ouro para o diagnóstico (já realizado neste caso)?
- **Comando 2:** este cálculo tem indicação de eliminação espontânea?
- **Comando 3:** cite a conduta cirúrgica indicada se o paciente tiver contraindicação a litotripsia extracorpórea.
- **Gabarito/checklist:** (1) TC de crânio sem contraste — **não**, é TC de **abdome/vias urinárias** sem contraste (armadilha de comando: exigir precisão anatômica); (2) não — cálculo de 0,9cm já ultrapassa a faixa de eliminação espontânea confiável (<0,5cm); (3) ureteroscopia (quando há contraindicação à LECO, conforme o algoritmo por tamanho/localização). *Fonte dos dados: `osce_urologia.md`, tabela "Litíase — corte de tamanho para indicação cirúrgica" (`OSCE .pdf`, ~p.20-21).*

### Estação 3 — Pediatria: assistência ao recém-nascido, 1º minuto de vida

- **Caso:** RN a termo, líquido amniótico meconial espesso, nasce chorando e com bom tônus.
- **Comando 1:** o aspecto do líquido meconial muda a conduta inicial?
- **Comando 2:** qual a conduta imediata?
- **Comando 3:** quando o APGAR deve ser calculado?
- **Gabarito/checklist:** (1) não — a fonte é explícita que o aspecto do líquido não importa na decisão inicial, só as 3 perguntas (IG>34sem? respira/chora? bom tônus?) importam; (2) contato pele a pele com a mãe + clampeamento tardio do cordão + incentivo à amamentação na 1ª hora; (3) no 1º e no 5º minuto de vida (repetir a cada 5min se <7 no 5º) — **nunca** antes da decisão inicial, pois demora a calcular. *Fonte dos dados: `osce_pediatria.md`, tabelas "Reanimação neonatal — 3 perguntas iniciais" e "APGAR" (`FACILITA OSCE (1).pdf`, p.49).*

### Estação 4 — Pediatria: crise asmática, sequenciamento de conduta

- **Caso:** menino, 7 anos, asmático conhecido, chega com sibilância, uso de musculatura acessória, SatO2 92%, consciente e orientado.
- **Comando 1:** qual a 1ª linha de tratamento farmacológico?
- **Comando 2:** se não houver resposta adequada na 1ª hora, qual o próximo passo?
- **Comando 3:** este paciente tem indicação de antibiótico de rotina?
- **Gabarito/checklist:** (1) broncodilatador (beta-2 de curta ação, salbutamol/fenoterol) + anticolinérgico (brometo de ipratrópio), nebulização a cada 20min por até 1h; (2) corticoide sistêmico (prednisona VO ou metilprednisolona EV) — **não** pular direto para ele sem antes ter tentado o broncodilatador; SatO2 92% (<94%) mas consciente → considerar VNI, não IOT direta; (3) não — 80% das exacerbações são virais; antibiótico só com forte suspeita bacteriana (febre, escarro purulento, consolidação radiográfica). *Fonte dos dados: `osce_pediatria.md`, tabela "Crise asmática — manejo (mnemônico B-C-D)" (`OSCE - PEDIATRIA.pdf` / `FACILITA OSCE (1).pdf`, p.53).*

### Estação 5 — Urologia: trauma abdominal com suspeita de lesão renal

- **Caso:** vítima de acidente automobilístico, consciente, PAS 110x70 (estável), equimose em flanco esquerdo, hematúria macroscópica discreta.
- **Comando 1:** a intensidade da hematúria é proporcional à gravidade da lesão renal?
- **Comando 2:** qual o exame de escolha neste paciente (estável)?
- **Comando 3:** cite 2 critérios que indicariam tratamento cirúrgico em vez de conservador.
- **Gabarito/checklist:** (1) não — a hematúria não é proporcional à gravidade da lesão, é um erro comum assumir isso; (2) TC de abdome com contraste (padrão-ouro para diagnóstico e estadiamento em paciente estável — não USG FAST, que é reservada a paciente instável); (3) lesão grau IV ou V (atinge via coletora ou rim fraturado/avulsão de hilo), instabilidade hemodinâmica (PAS<90), ou hematoma perirrenal pulsátil/expansivo identificado em laparotomia. *Fonte dos dados: `osce_urologia.md`, tabelas "Trauma renal — classificação" e "Trauma renal — conduta por gravidade" (`OSCE .pdf`, ~p.31).*

### Estação 6 — Neurologia: coma de origem indeterminada

- **Caso:** paciente encontrado inconsciente na rua, sem testemunha, sem documentos. GCS 7. Pupilas isocóricas e fotorreagentes.
- **Comando 1:** cite 2 medicações de emergência que podem ser consideradas empiricamente.
- **Comando 2:** o achado pupilar (isocórica e fotorreagente) sugere que tipo de etiologia?
- **Comando 3:** GCS 7 exige qual conduta imediata de via aérea?
- **Gabarito/checklist:** (1) naloxona (antídoto de opioides) e flumazenil (antídoto de benzodiazepínicos), após colher sangue para investigar intoxicação; (2) etiologia tóxico-metabólica (pupilas isocóricas e fotorreagentes classicamente apontam para essa causa, diferente de anisocoria = herniação uncal, ou puntiforme = lesão de ponte); (3) intubação orotraqueal — GCS <8 é o corte fixo para proteção de via aérea. *Fonte dos dados: `osce_neurologia.md`, tabelas "Pupilas no coma/TCE" e "Medicações de emergência no coma" (`OSCE .pdf`, ~p.14-16).*

## Pivô clínico

O pivô comum às 6 estações não é o diagnóstico — é a **precisão do comando**: cada estação tem pelo menos 1 comando desenhado para testar se o candidato lê a pergunta exata (ex.: "TC padrão-ouro" não é TC de crânio na cólica renal; "a hematúria é proporcional à gravidade?" tem resposta objetivamente não) em vez de responder com o bloco de conhecimento decorado inteiro.

## Palavras-âncora

Comando por comando · classificar antes de tratar · exame padrão-ouro específico do órgão certo · "a intensidade do achado não é proporcional à gravidade" · GCS <8 = via aérea · corte fixo antes da conduta.

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| executar a tarefa pedida | 1 comando = 1 resposta objetiva, sem antecipar comandos futuros | sequência | operacional | sobre-elaboração — responder com todo o protocolo decorado quando o comando pediu só a classificação de risco ou só o exame padrão-ouro | treinar resposta cronometrada de 1 frase por comando, proibido "encadernar" todos os comandos numa resposta só |
| aplicar critério | classificar (risco, grau, gravidade) antes de propor conduta em qualquer estação | sequência | operacional | pular a classificação e ir direto para a conduta "que parece certa" pela narrativa do caso | fixar o hábito de nomear a classificação em voz alta antes de qualquer palavra sobre tratamento |
| interpretar imagem/ecg/laboratório | nomear o exame padrão-ouro exato do órgão/sistema certo (não um exame genérico "de imagem") | fato | factual | trocar o exame padrão-ouro por outro semelhante (TC de crânio × TC de abdome; USG FAST × TC com contraste) | treinar pares "queixa → exame padrão-ouro exato", nunca "exame de imagem" genérico |

## Dados de precisão

Todos os dados clínicos usados nas 6 estações já estão verificados nível 1 nas tabelas "Dados de precisão" de `osce_neurologia.md`, `osce_urologia.md` e `osce_pediatria.md` (mesmas fontes do cluster) — remissão feita estação a estação acima para não duplicar a tabela.

## Pegadinhas

**Imperdoáveis (aplicam-se a qualquer estação do banco, não só às 6 modeladas aqui):**

- Responder um comando futuro dentro da resposta de um comando anterior (sobre-elaboração).
- Nomear um exame padrão-ouro genérico ("exame de imagem") em vez do exame específico do órgão pedido.
- Pular a classificação formal (risco/grau/gravidade) e ir direto para a conduta.
- Não se apresentar, não lavar as mãos, não se despedir — ver `formato_roteiro_osce_p7.md` para o roteiro fixo de toda estação.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Achar que a intensidade de um achado (hematúria, dor, sibilância) é proporcional à gravidade da doença | é intuitivo pensar "mais sintoma = mais grave" | narrativa acima do discriminador | várias das fontes deste cluster fazem questão de registrar a exceção explicitamente (ex.: "hematúria não é proporcional à gravidade da lesão renal") — é um padrão de armadilha repetido, não um caso isolado |
| Responder "TC de crânio" para qualquer comando que peça "TC" num paciente com queixa abdominal/urológica | TC de crânio é o exame mais praticado nos casos de neurologia do mesmo banco | pivô perdido | o órgão-alvo do exame muda com a queixa — a estação de cólica renal pede TC de vias urinárias/abdome, não de crânio |

## Conduta

- Inicial: em toda estação, cumprir a sequência fixa do roteiro geral do OSCE do P7 (cumprimentar → lavar as mãos → ler o caso → exame físico/exames disponíveis) antes de responder qualquer comando de conteúdo médico.
- Definitiva: responder comando por comando, na ordem, citando a classificação formal antes da conduta e o exame padrão-ouro específico antes de qualquer interpretação de achado.
- Condição da conduta: cada estação tem seu próprio corte/critério objetivo — não existe "resposta padrão" que sirva para todas; a variável decisiva muda a cada cabine.
- Diferencial perigoso: comandos que pedem apenas classificação/exame não devem ser respondidos com a conduta terapêutica completa — isso é pontuado como erro de execução, não como conhecimento extra.
- O que mudaria a decisão: o verbo do comando (classifique / cite / qual a conduta / qual o exame) decide o formato exato da resposta esperada.

## Mini-casos ativos

As 6 estações do banco acima já cumprem a função de mini-casos ativos desta cápsula — cada uma com pivô, comando e gabarito explícitos.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Antes de responder a conduta, o que classificar primeiro? | O grau/risco/gravidade formal do caso (nunca pular direto para o tratamento) | regra |
| A intensidade da hematúria é proporcional à gravidade do trauma renal? | Não | fato |
| GCS de corte para intubação orotraqueal | <8 | limiar |
| O aspecto do líquido amniótico muda a decisão inicial da reanimação neonatal? | Não — só as 3 perguntas (IG, respira/chora, tônus) decidem | regra |
| Antibiótico de rotina na crise asmática pediátrica? | Não — só com forte suspeita de infecção bacteriana | regra |

## Revisão

- Revisar quando: na semana antes do OSCE, rodando as 6 estações cronometradas (2-3 min cada), sempre comando por comando.
- Critério de parada: quando conseguir responder as 6 estações completas, sem sobre-elaborar nenhum comando e sem trocar o exame padrão-ouro de nenhuma delas, em menos de 15 minutos ao todo.
