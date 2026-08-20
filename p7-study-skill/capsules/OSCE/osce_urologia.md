# OSCE Urologia — litíase, hiperplasia prostática benigna, câncer de próstata, câncer renal e trauma urogenital

## Metadados

- Disciplina: OSCE
- Especialidade: Urologia
- Unidade: A_DEFINIR
- Prioridade: alta
- Risco clínico: alto
- Status: reviewed_l1
- Camada de fonte usada: B
- fonte_visual: não (as 3 fontes do cluster são NATIVA)
- Fontes usadas: `OSCE .pdf` (camada B, 101 páginas com marcador por slide, paginação exata: litíase ~p.20; HPB ~p.24; câncer de próstata ~p.28; trauma urinário ~p.31; câncer renal ~p.36; caso clínico de HPB com comandos e gabarito ~p.40); `OSCE - UROLOGIA.pdf` (camada B, formato tabela contínua doença/sinais/exame/diagnóstico/tratamento/outros, 7 páginas pelo cluster, sem marcador de página detectável — citado como documento íntegro); `FACILITA OSCE (1).pdf` (camada B, 67 páginas com sumário próprio — HPB p.42, câncer de próstata p.45, trauma urogenital p.47 — texto discursivo; não cobre litíase nem câncer renal)
- Evidência de prova/devolutiva: nenhuma devolutiva de prova teórica — as 3 fontes são material de revisão de colegas para o OSCE, incluindo 1 caso clínico completo com comandos numerados e gabarito comentado (HPB) em `OSCE .pdf`
- Limitações da fonte: as duas fontes tabulares (`OSCE .pdf` e `OSCE - UROLOGIA.pdf`) divergem no corte de tamanho do cálculo ureteral/renal que orienta LECO × ureteroscopia — uma usa a faixa 0,5-1,5 cm conforme localização, a outra usa um corte único de 0,7 cm — ambas registradas abaixo sem fundir os números, já que nenhuma tem camada A para desempatar; tratar como **divergência registrada**, não como erro de uma das fontes. `OSCE - UROLOGIA.pdf` não tem marcador de página detectável na extração de texto, então é citado como documento íntegro.
- Verificação nível 1: CONFIRMADO_COM_CORREÇÕES

## Como cai

A cabine de Urologia mistura dois padrões de raciocínio. Em **litíase e HPB**, a operação central é aplicar um algoritmo de decisão por tamanho/localização (cálculo) ou por peso/sintoma predominante (próstata) — a fonte literalmente desenha fluxogramas do tipo "se sim/se não". Em **câncer de próstata, câncer renal e trauma urogenital**, a operação central é aplicar um critério objetivo (PSA, Gleason, classificação de Bosniak, grau de trauma renal) antes de decidir conduta, e diferenciar achados semelhantes de doenças vizinhas (HPB × câncer de próstata; hematúria de litíase × de trauma × de câncer). O caso clínico disponível nas fontes (`OSCE .pdf`) treina exatamente o segundo padrão: hipótese pelo quadro clínico → achado esperado no toque retal → conduta condicionada ao peso da próstata.

## A estação

- **Tarefa:** a partir do caso clínico (sintomas urinários, hematúria, dor lombar em cólica, ou trauma abdominal), reconhecer a síndrome urológica, examinar/descrever o toque retal quando pertinente, interpretar o exame complementar já disponível (USG, TC, PSA, USGTR) e propor conduta condicionada ao critério objetivo correto (tamanho do cálculo, peso da próstata, PSA/Gleason, grau do trauma).
- **Tempo:** não informado nas fontes disponíveis.
- **Ator/paciente:** caso clínico escrito; toque retal pode ser pedido como exame físico a descrever (posição de litotomia, luva e lubrificante, apalpar a próstata pela via retal).
- **Material:** resultado de USGTR, PSA, USG de vias urinárias ou TC de abdome já disponível na cabine, conforme o caso.
- **Critério do checklist (inferido):** descrever a técnica do toque retal e localizar a alteração na próstata quando houver (usar a divisão em 6 regiões: lobo direito/esquerdo × região basal/médio-basal/apical); citar o critério objetivo (tamanho do cálculo, peso da próstata, PSA) antes de propor conduta; checar contraindicação de fármaco (nitrato com inibidor de fosfodiesterase; glaucoma de ângulo estreito com anticolinérgico) antes de fechar a orientação terapêutica.

## Pivô clínico

O pivô muda por tema, mas o padrão é sempre "o número decide a conduta, não o diagnóstico": em HPB, é o **peso da próstata (corte de 40g)** que decide monoterapia com alfa-bloqueador × terapia combinada com inibidor de 5-alfa-redutase; em câncer de próstata, é a combinação **PSA + relação livre/total** que decide biópsia; em trauma renal, é o **grau (I-V) à TC** que decide conduta conservadora × cirúrgica; em litíase, é o **tamanho e a localização do cálculo** que decidem entre eliminação espontânea, LECO, ureteroscopia ou nefrolitotomia percutânea.

## Palavras-âncora

Sinal de Giordano · cólica renal · TC sem contraste (litíase) · LECO × ureteroscopia × nefrolitotomia percutânea · toque retal (próstata adenomatosa × endurecida/nodular) · IPSS · PSA total e relação livre/total · Gleason primário + secundário · Bosniak · trauma renal grau I-V · uretrorragia · "nunca sondar" (trauma de uretra).

## Operação × movimento

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| aplicar critério | peso da próstata: <40g monoterapia (alfa-bloqueador) × ≥40g terapia combinada (+ inibidor de 5-alfa-redutase) | limiar | operacional | valor errado — prescrever monoterapia em próstata >40g, ou terapia combinada em próstata pequena e assintomática de armazenamento | flashcard de limiar fixo (40g) + 3 casos variando só o peso da próstata em torno do corte |
| diferenciar próximos | HPB × câncer de próstata: HPB acomete a zona de transição/periuretral (sintomas de esvaziamento predominam) × câncer acomete a zona periférica (geralmente assintomático) | fato | factual | narrativa acima do discriminador — assumir que sintoma urinário exuberante aponta para câncer, quando na verdade aponta mais para HPB | tabela-espelho HPB × câncer de próstata (localização, sintoma predominante, achado do toque), revisada como par opositivo |
| aplicar critério | indicação de biópsia prostática: TR suspeito, PSA >10 (absoluto), PSA 4-10 com relação livre/total <10% (contexto: pacientes >55 anos), PSA >2,5 com fator de risco até 55 anos | limiar | operacional | aplicar o corte de PSA "padrão" (4,0) fora da faixa etária/fator de risco que o valida | tabela única de limiares de PSA por idade/fator de risco, testada com casos variando só a idade |
| reconhecer contraindicação | inibidor de fosfodiesterase (tadalafila) é CI com uso de nitrato; anticolinérgico é CI em glaucoma de ângulo estreito | contraindicação | operacional | prescrever a terapia combinada de HPB sem perguntar sobre uso de nitrato ou história de glaucoma | checklist de contraindicação obrigatório antes de fechar qualquer orientação de tratamento combinado de HPB |
| priorizar emergência | trauma urogenital: paciente instável (PAS <90) é indicação de laparotomia exploradora independente do grau à TC — a TC só é feita em paciente estável | prioridade | operacional | pedir TC de abdome com contraste antes de reconhecer que o paciente está hemodinamicamente instável | treinar o gatilho fixo "estável → TC; instável → USG FAST → laparotomia" como primeira pergunta de qualquer caso de trauma urogenital |
| reconhecer contraindicação | trauma de uretra: nunca sondar (pode transformar lesão parcial em completa) | contraindicação | operacional | passar sonda vesical de alívio num paciente com uretrorragia + fratura de bacia, achando que resolve a retenção | fixar a tríade uretrorragia + incapacidade de urinar + trauma pélvico = contraindicação absoluta de sondagem, solicitar uretrocistografia antes |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Litíase — dor por localização | JUP: dor lombar/flanco · ureter médio: dor lombar/flanco + irradiação para testículo/lábios vaginais ipsilaterais · JVU: dor em baixo ventre + polaciúria + disúria | `OSCE .pdf`, ~p.20 | CONFIRMADO |
| Sinal de Giordano | punho-percussão em T12; positivo sugestivo de pielonefrite | `OSCE .pdf`, ~p.20 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| Diagnóstico de litíase | padrão-ouro: TC sem contraste; USG mostra cálculos hiperecogênicos com sombra acústica posterior; EAS pode mostrar hematúria/cristais/infecção | `OSCE .pdf`, ~p.20 | CONFIRMADO |
| Litíase — tratamento clínico | alfa-bloqueador (tansulosina) se cálculo entre 0,5-1 cm; <0,5cm tendência à eliminação espontânea; analgesia com AINE/opioide; aumento de ingesta hídrica | `OSCE .pdf`, ~p.20 | CONFIRMADO |
| Litíase — corte de tamanho para indicação cirúrgica (versão 1) | cálculo ureteral ≤1cm sem CI à LECO: LECO ou ureteroscopia; ≤1cm com CI: ureteroscopia; >1cm: ureteroscopia. Renal ≤1,5cm (polo superior/médio): LECO ou ureteroscopia conforme CI; polo inferior: ureteroscopia ou NLP; >1,5cm: nefrolitotomia percutânea (NLP) | `OSCE .pdf`, ~p.20-21 | CONFIRMADO (fonte 1) |
| Litíase — corte de tamanho para indicação cirúrgica (versão 2, diverge da anterior) | sem dor/infecção/ureter distal: tansulosina + AINE por 10 dias (nunca buscopam); sem hidronefrose e sem sinal de alerta, >0,7cm: LECO; hidronefrótico sem sinal de alerta: litotripsia intracorpórea; cálice superior/médio ≤0,7cm: duplo J; >2,0cm: nefrolitotomia percutânea | `OSCE - UROLOGIA.pdf` (doc. íntegro) | CONFIRMADO (fonte 2) — corte diverge da fonte 1 (0,5-1,5cm × 0,7-2,0cm); sem camada A para desempatar, registrar ambas |
| Contraindicações à LECO | infecção urinária, hidronefrose, gestação, infecção/sepse | `OSCE - UROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| Litíase + pielonefrite/hidronefrose com sinal de alerta | cateter duplo J + antibiótico (ceftriaxona) | `OSCE - UROLOGIA.pdf` (doc. íntegro) | CONFIRMADO |
| HPB — sintomas de esvaziamento × armazenamento | esvaziamento: jato fraco, intermitência, esvaziamento incompleto, hesitação, disúria/estrangúria, micção dupla, gotejamento pós-miccional · armazenamento: polaciúria, nictúria, urgência, urge-incontinência | `OSCE .pdf`, ~p.24 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| HPB — toque retal | próstata lisa, firme, elástica, adenomatosa e aumentada (sem nódulos); endurecimento/nódulo exige PSA + biópsia + USGTR | `OSCE .pdf`, ~p.24 / `FACILITA OSCE (1).pdf`, p.42 | CONFIRMADO |
| Indicação de biópsia prostática | toque retal suspeito (endurecido/nódulo); PSA >10 = indicação absoluta; PSA 4-10 (zona cinzenta) → relação livre/total <10% biopsia, >10% sugere HPB; PSA >2,5 até 55 anos com fator de risco; cinética de PSA >0,75 ng/dL/ano | `OSCE .pdf`, ~p.24 / `FACILITA OSCE (1).pdf`, p.42 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| Valores de referência de PSA por idade | 45 anos + fator de risco ou 50-55 anos: <2,5 ng/mL · >55 anos: <4,0 ng/mL | `OSCE .pdf`, ~p.24 | CONFIRMADO |
| HPB — tratamento medicamentoso por peso | próstata <40g: monoterapia com alfa-bloqueador (tansulosina/doxazosina) · próstata ≥40g: alfa-bloqueador + inibidor de 5-alfa-redutase (finasterida bloqueia só o tipo 2; dutasterida bloqueia tipo 1 e 2) | `OSCE .pdf`, ~p.24 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| Resposta esperada ao inibidor de 5-alfa-redutase | redução de ~50% do volume prostático e do PSA após 6 meses de uso contínuo; se o PSA não cair pela metade, alto risco de indicação de biópsia | `FACILITA OSCE (1).pdf`, p.42 | CONFIRMADO |
| HPB — armazenamento predominante e disfunção erétil | queixa de armazenamento sem glaucoma de ângulo estreito: associar anticolinérgico/antimuscarínico (solifenacina/oxibutinina); HPB + disfunção erétil sem uso de nitrato: associar inibidor de fosfodiesterase (tadalafila/sildenafila) | `OSCE .pdf`, ~p.24 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| HPB — cirurgia por tamanho | próstata ≤80g (ou ≤60-70g conforme a fonte tabular): RTU de próstata · >80g (ou >60-70g): prostatectomia transvesical · risco cirúrgico/CI e sem lobo médio: Urolift · impossibilidade de suspender anticoagulante: laser | `OSCE .pdf`, ~p.24 / `OSCE - UROLOGIA.pdf` (corte de 60-70g, diverge levemente do corte de 80g da outra fonte) | CONFIRMADO_COM_DIVERGÊNCIA — registrar os dois cortes |
| HPB — indicações absolutas de cirurgia | ITU recorrente apesar de tratamento clínico; litíase vesical; deterioração do trato urinário superior; hematúria secundária à HPB; >1 episódio de retenção urinária aguda; falha do tratamento clínico + lobo médio | `FACILITA OSCE (1).pdf`, p.42 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| Câncer de próstata — quadro clínico | geralmente assintomático/oligossintomático (zona periférica, distante da uretra); pode haver obstrução infravesical súbita, hematúria macroscópica, dor óssea, uremia, anemia, perda de peso | `OSCE .pdf`, ~p.28 / `FACILITA OSCE (1).pdf`, p.45 | CONFIRMADO |
| Rastreio de câncer de próstata | todos os homens a partir de 50 anos; antecipar para 45 anos se fator de risco (sobrepeso/obesidade, raça negra, história familiar) | `FACILITA OSCE (1).pdf`, p.45 | CONFIRMADO |
| Biópsia prostática — técnica | guiada por USG transretal; mínimo de 12 fragmentos (2 por sextante) | `OSCE .pdf`, ~p.28 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| Escore de Gleason | soma do padrão histológico primário (mais frequente) + secundário (segundo mais frequente); 6 = baixo risco; 7 = risco intermediário; 8-10 = alto risco | `OSCE .pdf`, ~p.28 / `FACILITA OSCE (1).pdf`, p.45 | CONFIRMADO |
| Indicação de cintilografia óssea no câncer de próstata | PSA >20 ng/mL + biópsia positiva; Gleason >7 + biópsia positiva; doença localmente avançada; fosfatase alcalina elevada; dor óssea | `OSCE .pdf`, ~p.28 | CONFIRMADO |
| Câncer de próstata — manejo por estágio | doença localizada: prostatectomia radical, radioterapia, braquiterapia (expectativa de vida >5 anos e sem sintomas urinários) ou observação vigilante (idoso, tumor indolente) · metástase: bloqueio androgênico — orquiectomia bilateral (padrão-ouro), análogos de LHRH, estrógenos, antiandrógenos | `OSCE .pdf`, ~p.28 / `FACILITA OSCE (1).pdf`, p.45 | CONFIRMADO |
| Trauma urogenital — epidemiologia geral | trato urogenital acometido em ~10% dos traumas abdominais; 90% fechados; rim é o órgão mais acometido (80% das lesões contusas) | `FACILITA OSCE (1).pdf`, p.47 | CONFIRMADO |
| Trauma renal — classificação | G1: hematoma subcapsular não expansivo · G2: laceração <1cm · G3: >1cm sem atingir via coletora · G4: >1cm atingindo via coletora (risco de urinoma) · G5: rim fraturado/avulsão do hilo | `OSCE .pdf`, ~p.31 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| Trauma renal — conduta por gravidade | conservador (G I-III): internação em UTI, seriar Hb/Ht, seriar imagem · cirúrgico (G IV-V, instabilidade hemodinâmica, hematoma perirrenal pulsátil/expansivo, ferimento penetrante): laparotomia exploradora; G5 → nefrectomia | `OSCE .pdf`, ~p.31 / `OSCE - UROLOGIA.pdf` | CONFIRMADO |
| Trauma de bexiga | 10% das fraturas pélvicas; extraperitoneal é mais comum; intraperitoneal → laparotomia + rafia; extraperitoneal → sonda vesical de demora por 10 dias | `OSCE .pdf`, ~p.31 / `FACILITA OSCE (1).pdf`, p.47 | CONFIRMADO |
| Trauma de uretra | contraindicação absoluta de sondagem (pode converter lesão parcial em completa); posterior (mais comum, 70%, associada a fratura de bacia) → uretrocistografia, tratamento com cistostomia + correção tardia (3 meses); anterior (associada a fratura de pênis) → uretrografia, reparo/desbridamento ou exploração cirúrgica | `OSCE .pdf`, ~p.31 / `FACILITA OSCE (1).pdf`, p.47 | CONFIRMADO |
| Câncer renal — tríade clássica | hematúria + dor lombar + massa palpável em flanco | `OSCE .pdf`, ~p.36 | CONFIRMADO |
| Classificação de Bosniak | I: <1% chance de malignidade · II: 3-5% · IIF: >5%, acompanhar · III/IV: casos avançados, indicação cirúrgica | `OSCE .pdf`, ~p.36 | CONFIRMADO |
| Câncer renal — manejo | doença localizada: nefrectomia total (ou parcial se bilateral, rim único, IRC prévia, tumor <4cm) · doença avançada ressecável: nefrectomia total + linfadenectomia · irressecável: cirurgia citorredutora + imunoterapia | `OSCE .pdf`, ~p.36 | CONFIRMADO |

## Pegadinhas

**Imperdoáveis:**

- Fechar hipótese de câncer de próstata num paciente com sintomas urinários exuberantes sem considerar que HPB é a explicação mais compatível com a localização periuretral do sintoma.
- Prescrever monoterapia com alfa-bloqueador numa próstata ≥40g descrita no caso — a fonte é explícita que esse peso exige terapia combinada.
- Prescrever inibidor de fosfodiesterase para HPB com disfunção erétil sem perguntar sobre uso de nitrato.
- Sondar um paciente com uretrorragia + fratura de bacia + incapacidade de urinar — é a contraindicação mais citada nas fontes de trauma urogenital.
- Solicitar TC de abdome com contraste como primeiro passo num paciente hemodinamicamente instável — a fonte manda USG FAST e laparotomia direto, sem passar pela TC.

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| "PSA de 6 ng/mL = biópsia obrigatória" | o candidato lembra que "PSA alto = câncer" e generaliza qualquer PSA elevado como indicação absoluta | superextrapolação | PSA entre 4-10 é zona cinzenta — só indica biópsia se a relação PSA livre/total for <10% (em paciente >55 anos); sozinho, o valor não fecha a indicação |
| Toque retal descrito como "próstata endurecida e nodular" sendo interpretado automaticamente como câncer sem mencionar necessidade de PSA/biópsia | o achado "parece" patognomônico | fechamento precoce | mesmo com toque suspeito, a confirmação diagnóstica exige PSA + biópsia prostática guiada — o toque suspeito só define a indicação de investigar, não fecha o diagnóstico sozinho |
| Tratar toda hematúria macroscópica em paciente jovem sem trauma como "provável litíase" | litíase é a causa mais comum e mais "decorada" de hematúria com dor lombar | narrativa acima do discriminador | a tríade clássica de câncer renal (hematúria + dor lombar + massa palpável) também cursa com hematúria e dor — o discriminador é a presença de massa e o achado à imagem, não só o sintoma isolado |
| Em trauma renal estável com hematúria leve, já indicar cirurgia "porque é trauma" | ansiedade de tratar trauma sempre como emergência cirúrgica | definitiva antes da inicial | hematúria não é proporcional à gravidade da lesão — a conduta depende do grau à TC e da estabilidade hemodinâmica, não da intensidade da hematúria isolada |

## Conduta

- Inicial: em litíase, analgesia + hidratação + definir localização/tamanho do cálculo à imagem; em sintomas prostáticos, toque retal + PSA; em trauma, ABCDE/XABCDE e definir estabilidade hemodinâmica antes de qualquer exame de imagem.
- Definitiva: litíase conforme tamanho/localização (eliminação espontânea, alfa-bloqueador, LECO, ureteroscopia ou nefrolitotomia percutânea); HPB conforme peso da próstata e sintoma predominante; câncer de próstata conforme estágio (localizado × metastático) usando PSA/Gleason/cintilografia; câncer renal conforme Bosniak e tamanho/lateralidade; trauma urogenital conforme grau da lesão e estabilidade do paciente.
- Condição da conduta: instabilidade hemodinâmica muda toda a sequência diagnóstica no trauma (pula a TC, vai direto para USG FAST/laparotomia); presença de sinal de alerta (RED FLAG: taquipneia, RNC, hipotensão, febre, taquicardia) numa litíase obstruída com pielonefrite muda a conduta de analgesia isolada para drenagem urgente + antibiótico.
- Diferencial perigoso: bexigoma (retenção urinária aguda com massa hipogástrica palpável) é emergência que exige sondagem vesical imediata (ou cistostomia se a sonda não passar); trauma de uretra é a situação em que sondar — a conduta mais reflexa de um médico diante de retenção urinária — é justamente a contraindicação.
- O que mudaria a decisão: tamanho e localização do cálculo; peso da próstata (corte de 40g); presença de nódulo/endurecimento ao toque; grau do trauma renal (I-V) e estabilidade hemodinâmica; uso concomitante de nitrato ou história de glaucoma de ângulo estreito antes de prescrever a combinação de HPB.

## Mini-casos ativos

1. M.J.N., 60 anos, nictúria e dificuldade para iniciar/manter o jato urinário nos últimos meses, sensação de esvaziamento incompleto, impotência sexual associada. Hipertenso e diabético. USGTR: próstata com 55g. PSA: 4 ng/dL. Relação PSA livre/total >10%. **Pivô:** próstata de 55g (≥40g) exige terapia combinada — tansulosina + dutasterida + tadalafila —, não monoterapia; antes de prescrever a tadalafila é obrigatório perguntar sobre uso de nitrato; se a velocidade do PSA subir >0,75 ng/dL/ano, reavaliar indicação de biópsia.
2. Paciente com dor lombar em cólica súbita, hematúria microscópica, sem febre, cálculo de 0,8cm em ureter proximal à TC, sem hidronefrose. **Pivô:** o tamanho (>0,5-0,7cm conforme a fonte) já ultrapassa o limiar de eliminação espontânea confiável — a conduta passa a ser intervencionista (LECO ou ureteroscopia conforme contraindicação), não apenas analgesia e hidratação expectante.
3. Homem, 68 anos, hematúria macroscópica indolor, sem sintomas urinários de esvaziamento, massa palpável em flanco esquerdo. **Pivô:** ausência de sintoma urinário de esvaziamento (que apontaria para HPB/próstata) somada à massa em flanco desloca a hipótese para câncer renal — solicitar TC de abdome (exame de escolha) em vez de investigar próstata.
4. Vítima de acidente motociclístico, hipotenso (PAS 80), com equimose em flanco direito e distensão abdominal. **Pivô:** a instabilidade hemodinâmica (PAS <90) já indica USG FAST e, se houver líquido livre, laparotomia exploradora direta — pedir TC de abdome com contraste antes disso atrasa uma decisão que já está indicada pelo estado hemodinâmico.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| Corte de peso da próstata que decide monoterapia × terapia combinada na HPB | 40g (< 40g monoterapia com alfa-bloqueador; ≥40g associa inibidor de 5-alfa-redutase) | limiar |
| PSA >10 ng/mL sempre indica o quê? | Biópsia prostática (indicação absoluta) | regra |
| Zona da próstata acometida por HPB × câncer de próstata | HPB = zona de transição/periuretral; câncer = zona periférica | fato |
| Fórmula do escore de Gleason | Padrão histológico primário (mais frequente) + secundário (segundo mais frequente) | fato |
| O que NUNCA fazer diante de uretrorragia + fratura de bacia? | Sondar o paciente (pode converter lesão parcial em completa) | contraindicação |
| Paciente de trauma hemodinamicamente instável: qual exame primeiro? | USG FAST (não TC) — se líquido livre, laparotomia exploradora | sequência |
| Classificação de Bosniak III e IV | Casos avançados — indicação cirúrgica (risco de malignidade relevante) | limiar |

## Revisão

- Revisar quando: antes de qualquer simulação de estação de urologia, e sempre que o caso trouxer um valor numérico (peso da próstata, PSA, tamanho do cálculo, grau do trauma) — é aí que a maioria dos movimentos de erro se concentra.
- Critério de parada: quando conseguir, dado um caso de sintoma urinário ou hematúria, decidir corretamente entre HPB, câncer de próstata, litíase e câncer renal só pelos achados objetivos (não pela narrativa), em 4 variações de caso sem consultar a fonte.
