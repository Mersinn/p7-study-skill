# Hiperfunção hipofisária

## Metadados

- Disciplina: EISA_II
- Especialidade: Endocrinologia
- Unidade: IV_UNIDADE
- Prioridade: alta
- Risco clínico: medio
- Status: reviewed_l1
- Camada de fonte usada: A+B (A cobre só Hiperprolactinemia; Hipercortisolismo/Cushing, Acromegalia e Hipertireoidismo central são B apenas)
- fonte_visual: sim (`HIPERFUN_O_HIPOFIS_RIA_PARTE_01__0c915df866`, todas as 9 páginas abertas — ver limitação abaixo sobre a natureza dessa renderização)
- Fontes usadas: HIPERFUN_O_HIPOFIS_RIA_PARTE_01__0c915df866 (camada A, slide Profa. Mirna Alves de Sá — só Hiperprolactinemia); APOSTILA_SA_II_P7___e43cc7bc21 pp.230-234 (camada B, para Hipercortisolismo/Cushing, Acromegalia e Hipertireoidismo central)
- Evidência de prova/devolutiva: `cai: false` no cluster — sem registro de cobrança rastreada neste tema especificamente, mas prioridade alta e risco médio atribuídos pelo cluster. Padrões de erro de EISA II aplicáveis por analogia: "definitiva antes da inicial" (cirurgia vs medicamento por hormônio) e "premissa não checada" (efeito gancho).
- Limitações da fonte: o arquivo camada A é um `.pptx` que o pipeline de renderização (PyMuPDF) converteu para PNG em formato de TEXTO CORRIDO (sem cores, tabelas ou imagens do slide original) — portanto a "conferência visual" aqui é texto-sobre-texto, não uma leitura do desenho real do slide; a fidelidade do conteúdo é alta (bate 100% com o `.txt`), mas não há verificação de formatação/ênfase visual. Além disso, este arquivo é só a "PARTE 01" da aula (Hiperprolactinemia) — a "Parte 02" (Acromegalia, Cushing, TSH central), citada no título, não está no acervo extraído; a APOSTILA usada para essas 3 seções tem redação quase idêntica à da Parte 01 (mesma estrutura, mesmos termos), o que sugere fidelidade ao mesmo slide de origem, mas isso é inferência, não confirmação direta — registrado como B, não A.
- Verificação nível 1: CONFIRMADO

## Como cai

Vinheta com par ACTH+cortisol pedindo para localizar a causa do hipercortisolismo (hipófise/ectópico x adrenal); vinheta de amenorreia/galactorreia pedindo o próximo passo diagnóstico (RNM x pesquisa de macroprolactina, conforme sintomática ou não); caso de macroadenoma grande com PRL discretamente elevada (efeito gancho); pergunta sobre qual hormônio hipofisário em excesso tem tratamento medicamentoso como primeira linha (só a prolactina).

## Conceito operacional mínimo

Hiperfunção hipofisária = excesso de hormônio(s) hipofisário(s), isolado ou combinado, mais comumente por adenoma secretor. Os 4 subtipos cobrados: Hiperprolactinemia (PRL), Hipercortisolismo (Cushing, via ACTH), Acromegalia/gigantismo (GH), Hipertireoidismo central (TSH). Cada eixo tem seu próprio fluxo diagnóstico (qual exame vem primeiro) e sua própria lógica de tratamento (medicamento x cirurgia como 1ª linha) — não existe fluxo único "tumor hipofisário = cirurgia".

## Pivô clínico

A prolactina é a EXCEÇÃO na hipófise: em todos os outros excessos hormonais hipofisários (GH, ACTH), a cirurgia transesfenoidal é a primeira linha; só no prolactinoma o agonista dopaminérgico (medicamento) vem antes da cirurgia, mesmo em macroadenoma. Aplicar a regra geral "tumor hipofisário → operar" ao prolactinoma é o erro mais previsível deste tema.

## Palavras-âncora

Cabergolina (1ª escolha); bromocriptina (gestação); efeito gancho (hook effect, diluir 1:100); macroprolactina (recuperação >65% negativa / <30% positiva); ACTH-dependente x independente; doença de Cushing (70-80% dos ACTH-dependentes); Liddle 1 e Liddle 2; IGF-1 (triagem de acromegalia); GH pós-TOTG (padrão-ouro, corte 0,4 ng/mL); cetoconazol (Cushing, se precisar de medicamento).

## Operação × movimento

> A camada Diagnos: o que a prova EXIGE fazer neste tema, e como se erra fazendo.

| Operação exigida | Variável decisiva | Tipo | Natureza | Movimento provável no erro | Treino que corrige |
|---|---|---|---|---|---|
| interpretar laboratório | par ACTH + cortisol: ambos altos = hipófise/ectópico (ACTH-dependente); cortisol alto + ACTH baixo/normal = adrenal (ACTH-independente) | sinal-achado | operacional | erro de leitura — interpretar o cortisol isolado, ou inverter a lógica (achar que ACTH baixo aponta para doença de Cushing hipofisária) | treino de pares ACTH/cortisol embaralhados, exigindo classificar dependente x independente antes de cogitar etiologia específica |
| diferenciar próximos passos | sintomático (→ RNM de sela direto) x assintomático (→ pesquisa de macroprolactina primeiro) | sequência | operacional | pular a etapa — pedir RNM de sela em paciente assintomático com PRL elevada incidental, sem antes excluir macroprolactinemia (achado benigno) | mini-casos-par (sintomática x assintomática) forçando escolher o próximo exame certo antes de avançar |
| aplicar critério | efeito gancho: macroadenoma grande + PRL discretamente elevada = discrepância que exige diluição 1:100 antes de excluir prolactinoma | sinal-achado | operacional | premissa não checada — aceitar PRL "normal-baixa" como exclusão de prolactinoma sem checar o tamanho do tumor no enunciado | casos-par (tumor grande + PRL baixa vs tumor pequeno + PRL baixa), treinando reconhecer quando a discrepância exige diluição |
| conduta definitiva | qual hormônio em excesso muda a ordem cirurgia × medicamento (PRL = medicamento 1ª linha; GH e ACTH = cirurgia 1ª linha) | prioridade | operacional | superextrapolação — aplicar "tumor hipofisário = cirurgia primeiro" ao prolactinoma, que é a exceção nomeada | tabela fixa por hormônio (PRL/GH/ACTH) com a 1ª linha de cada, treinada contra vinhetas trocando o hormônio-alvo |
| aplicar critério | GH basal isolado tem grande flutuação — o padrão-ouro é o teste de supressão pós-TOTG (corte 0,4 ng/mL) | limiar | factual | valor errado — usar GH basal único como se fosse confirmatório, ignorando a flutuação pulsátil | card fixo "GH e cortisol nunca se dosam isolados/basais para diagnóstico — sempre teste dinâmico" |

## Dados de precisão

| Dado | Valor | Fonte (página) | Status |
|---|---|---|---|
| Ordem de frequência dos adenomas hipofisários secretores | 1. Prolactina · 2. GH · 3. FSH/LH · 4. ACTH · 5. TSH | HIPERFUNÇÃO HIPOFISÁRIA slide 9 | CONFIRMADO |
| Hiperprolactinemia — prevalência por sexo | mulheres 10× mais que homens; prolactinoma = 40-66% dos tumores hipofisários | HIPERFUNÇÃO HIPOFISÁRIA slide 13 | CONFIRMADO |
| PRL — causa fisiológica x adenoma | fisiológica: PRL <50 ng/mL (exceto gravidez) · adenoma produtor: PRL >100 ng/mL · >150-200 ng/mL: fortemente sugestivo de prolactinoma | APOSTILA p.230-231 (só B — não presente na Parte 01 do slide) | CONFIRMADO_COM_CORREÇÕES — dado rotulado como B, sem confirmação em A |
| Efeito gancho | se houver discrepância entre o tamanho do tumor e a PRL pouco elevada, afastar artefato de gancho diluindo a amostra 1:100 | HIPERFUNÇÃO HIPOFISÁRIA slide 18 | CONFIRMADO |
| Diagnóstico — sintomático | RNM de sela túrcica com contraste: normal = hiperPRL idiopática; adenoma = prolactinoma | HIPERFUNÇÃO HIPOFISÁRIA slide 18 | CONFIRMADO |
| Diagnóstico — assintomático | pesquisa de macroprolactina: recuperação >65% = negativa; <30% = positiva (macroprolactinemia) | HIPERFUNÇÃO HIPOFISÁRIA slide 18 | CONFIRMADO |
| Tratamento — cabergolina | 0,5 a 2 mg/semana, 1 a 2×/semana; 1ª escolha; agonistas dopaminérgicos mantidos por ~2 anos | HIPERFUNÇÃO HIPOFISÁRIA slide 19 | CONFIRMADO |
| Tratamento — bromocriptina | 2,5 a 7,5 mg/dia, 2 a 3×/dia; preferida na gestação | HIPERFUNÇÃO HIPOFISÁRIA slide 19 | CONFIRMADO |
| Prolactinoma — exceção da hipófise | é o único excesso hormonal hipofisário cuja 1ª linha é medicamentosa, não cirúrgica, mesmo em macroadenoma | HIPERFUNÇÃO HIPOFISÁRIA slide 19; APOSTILA p.231 (concordam, "diferentemente dos outros casos... aqui a 1ª opção é medicamentosa") | CONFIRMADO |
| Cirurgia transesfenoidal no prolactinoma — indicações | crescimento apesar do tratamento medicamentoso · intolerância/resistência/contraindicação ao agonista dopaminérgico · compressão persistente do quiasma óptico · fístula liquórica | HIPERFUNÇÃO HIPOFISÁRIA slide 19 | CONFIRMADO |
| Hipercortisolismo — localização pelo par ACTH/cortisol | ACTH e cortisol ambos altos = origem hipofisária/ectópica (ACTH-dependente) · cortisol alto + ACTH baixo/normal = origem adrenal (ACTH-independente) | APOSTILA p.231 (só B) | CONFIRMADO_COM_CORREÇÕES — rotulado B |
| Doença de Cushing — proporção | 70-80% dos casos ACTH-dependentes | APOSTILA p.232 (só B) | CONFIRMADO_COM_CORREÇÕES — rotulado B |
| Testes de detecção/confirmação de hipercortisolismo | Liddle 1 (cortisol pós 1mg dexametasona): + se ≥1,8 mcg/dL · Cortisol urinário livre 24h: + se 3-4× LSN · Cortisol salivar da meia-noite: + se ≥2× LSN · Liddle 2 (0,5mg 6/6h por 2 dias): + se ≥1,8 mcg/dL | APOSTILA p.232 (só B) | CONFIRMADO_COM_CORREÇÕES — rotulado B; nenhum dado de A disponível para confronto |
| Tratamento de Cushing — medicamento de escolha (quando indicado) | cetoconazol; geralmente não necessário antes de operar, indicado em casos graves ou sem remissão | APOSTILA p.232 (só B) | CONFIRMADO_COM_CORREÇÕES — rotulado B |
| Acromegalia — triagem e confirmação | IGF-1 (triagem, secreção integrada e estável) · GH basal não serve (secreção pulsátil, grande flutuação) · padrão-ouro: GH pós-TOTG (75g dextrosol, dosar a cada 30min por 2h) — normal = supressão <0,4; acromegalia = não suprime (>0,4) | APOSTILA p.233-234 (só B) | CONFIRMADO_COM_CORREÇÕES — rotulado B |
| Acromegalia — tratamento | cirurgia (CTE) é 1ª escolha; medicamentoso (análogo de somatostatina ou agonista dopaminérgico) é adjuvante ou, em casos selecionados, pode ser primário; radioterapia para tumores agressivos não controlados | APOSTILA p.234 (só B) | CONFIRMADO_COM_CORREÇÕES — rotulado B |

## Pegadinhas

- Prolactinoma é a ÚNICA exceção: mesmo em macroadenoma (>10mm), a 1ª linha é medicamento (agonista dopaminérgico), não cirurgia — em GH e ACTH, é o oposto (cirurgia 1ª linha).
- PRL "pouco elevada" em paciente com macroadenoma grande não exclui prolactinoma — pensar em efeito gancho e diluir a amostra 1:100 antes de descartar.
- Sintomático x assintomático mudam o próximo exame: sintomático vai direto para RNM; assintomático precisa primeiro excluir macroprolactinemia (pesquisa de macroprolactina), NÃO pular direto para RNM.
- GH basal isolado não serve para diagnosticar acromegalia (secreção pulsátil, flutua muito ao longo do dia) — o exame confirmatório é o teste de supressão pós-sobrecarga de glicose (GH pós-TOTG).
- ACTH baixo/normal com cortisol alto aponta para a ADRENAL, não para a hipófise — é fácil inverter essa lógica achando que "ACTH baixo" significa "não é hipofisário e por isso mais simples".

## Distratores sedutores

| Distrator | Por que seduz | Movimento que sugere | Por que erra |
|---|---|---|---|
| Macroadenoma hipofisário produtor de prolactina, sem contraindicação a agonista dopaminérgico → indicar cirurgia transesfenoidal como 1ª linha | regra geral "tumor grande = opera" | superextrapolação da regra geral | Prolactinoma é a exceção — agonista dopaminérgico (cabergolina) é 1ª linha mesmo em macroadenoma, sem contraindicação |
| Paciente assintomático com PRL levemente elevada em exame de rotina → solicitar RNM de sela túrcica de imediato | "PRL alta = investigar tumor" é o reflexo | pular etapa / definitiva antes da inicial | Assintomático deve primeiro excluir macroprolactinemia (pesquisa específica) — RNM é para quem já tem quadro sintomático sugestivo |
| Macroadenoma de 2cm à RNM, PRL discretamente elevada (60 ng/mL) → concluir que é um tumor hipofisário não-funcionante, não prolactinoma | PRL "normal-baixa" parece afastar prolactinoma | premissa não checada | A discrepância tamanho×PRL sugere efeito gancho — diluir a amostra 1:100 antes de excluir prolactinoma |
| Cortisol alto + ACTH baixo → pensar em doença de Cushing (hipofisária) | "Cushing" é o nome mais familiar para hipercortisolismo | analogia sem validação funcional | ACTH baixo com cortisol alto aponta para causa ADRENAL (ACTH-independente) — doença de Cushing hipofisária cursa com ACTH alto |
| Suspeita de acromegalia: dosar GH basal único e, se normal, excluir o diagnóstico | GH parece o exame "direto" para uma doença de excesso de GH | valor errado por não checar a variável (pulsatilidade) | GH basal isolado flutua demais para excluir — usar IGF-1 (triagem) e GH pós-TOTG (confirmação, corte 0,4) |

## Conduta

- Inicial (hiperprolactinemia): excluir causas secundárias (drogas, gestação, insuficiência renal, hipotireoidismo primário); dosar PRL; separar sintomático (RNM) de assintomático (macroprolactina).
- Definitiva (prolactinoma): agonista dopaminérgico (cabergolina 1ª escolha; bromocriptina na gestação) por ~2 anos — é a EXCEÇÃO entre os adenomas hipofisários.
- Definitiva (acromegalia e Cushing): cirurgia transesfenoidal é 1ª linha; medicamento é adjuvante/segunda linha (cetoconazol no Cushing; análogo de somatostatina ou agonista dopaminérgico na acromegalia).
- Condição da conduta: cirurgia no prolactinoma só se crescimento apesar do medicamento, intolerância/resistência/contraindicação ao agonista, compressão do quiasma óptico ou fístula liquórica.
- Diferencial perigoso: PRL discretamente elevada + tumor grande = checar efeito gancho antes de excluir prolactinoma; ACTH baixo com cortisol alto = origem adrenal, não hipofisária.
- O que mudaria a decisão: presença de sintomas muda o próximo exame (RNM x macroprolactina); tamanho do tumor desproporcional à PRL muda a necessidade de diluir a amostra.

## Mini-casos ativos

Mulher com amenorreia e galactorreia, RNM de sela com adenoma de 15mm, PRL 220 ng/mL, sem contraindicação a medicamento → variável decisiva: é prolactinoma (macroadenoma, PRL compatível) → iniciar cabergolina, NÃO indicar cirurgia de imediato.

Paciente assintomático, PRL 45 ng/mL em exame de rotina, sem uso de drogas relacionadas → variável decisiva: ausência de sintomas → pesquisar macroprolactina antes de RNM.

Paciente com macroadenoma de 2,5cm à RNM mas PRL de apenas 70 ng/mL → variável decisiva: discrepância tamanho×PRL → suspeitar de efeito gancho, diluir a amostra 1:100 antes de excluir prolactinoma.

Paciente com fácies cushingoide, ACTH indetectável, cortisol elevado → variável decisiva: ACTH baixo + cortisol alto → causa ADRENAL (ACTH-independente), não hipofisária — investigar adrenal, não hipófise.

## Cards mínimos

| Frente | Verso | Tipo |
|---|---|---|
| 1ª linha no prolactinoma (mesmo macroadenoma) | Agonista dopaminérgico (cabergolina) — exceção entre os adenomas hipofisários | pegadinha |
| 1ª linha em acromegalia e Cushing | Cirurgia transesfenoidal | dado |
| Cabergolina — dose | 0,5-2 mg/semana, 1-2×/semana | dado |
| Bromocriptina — quando preferir | Gestação; 2,5-7,5 mg/dia, 2-3×/dia | dado |
| PRL elevada + tumor grande desproporcional | Suspeitar efeito gancho → diluir amostra 1:100 | pegadinha |
| Assintomático com PRL elevada — próximo passo | Pesquisa de macroprolactina (não RNM direto) | dado |
| ACTH e cortisol ambos altos | Origem hipofisária/ectópica (ACTH-dependente) | dado |
| ACTH baixo/normal + cortisol alto | Origem adrenal (ACTH-independente) | pegadinha |
| Exame para excluir acromegalia com segurança | GH pós-TOTG (supressão <0,4 = normal); GH basal isolado não serve | pegadinha |
| Doença de Cushing — proporção dos ACTH-dependentes | 70-80% | dado |

## Revisão

- Revisar quando: antes de vinheta com par ACTH/cortisol, e antes de caso de PRL elevada com adenoma hipofisário.
- Critério de parada: escolher corretamente medicamento x cirurgia como 1ª linha por hormônio (PRL/GH/ACTH) em 3 casos seguidos, e classificar ACTH-dependente x independente sem erro em pares embaralhados.
