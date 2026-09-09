# T02 e T03 — planejamento sensível a alvo, energia e tempo (fixtures ad-hoc)

Sem fixture nomeada dedicada — usam apenas o pedido do aluno como entrada.
Ambos classe **C**.

---

## T02 — 30 min vs. 3h para o mesmo tema

**Entrada exata (duas chamadas na mesma sessão, sequenciais):**

> 1) "Tenho só 30 minutos hoje. Quero estudar reidratação e Plano C."
> 2) "Na verdade mudei de ideia, tenho 3 horas livres hoje. Mesmo tema:
>    reidratação e Plano C."

**Estado inicial:** sessão nova; mesmo tema (`capsule:eisca:diarreia_aguda_desidratacao_planos_reidratacao`)
pedido duas vezes com orçamentos de tempo muito diferentes.

**Comportamento esperado:** o plano de 30 min tem um núcleo claramente
MENOR (ex.: só a classificação por contagem de sinais + indicação de Plano
C, sem os planos A/B completos); o plano de 3h inclui explicitamente
recuperação espaçada e/ou transferência (variações de caso, mini-casos
adicionais, revisão cruzada com temas relacionados) que o de 30 min não tem.

**Falha bloqueadora:** os dois planos são efetivamente o mesmo conteúdo
reorganizado (não há diferença real de escopo); OU o tempo total proposto
excede o orçamento declarado em mais de 10%.

**Detector:** contagem de itens/blocos do plano de 30min vs. 3h — sinaliza se
a razão for menor que ~1:3 (o plano longo deveria ser substancialmente mais
denso, não só mais alongado no mesmo conteúdo) ou se o tempo total exceder o
orçamento em >10%.

---

## T03 — iniciante/baixa energia vs. revisão, 35 min

**Entrada exata (duas sessões limpas separadas, mesmo tema):**

> A) "Nunca estudei sepse neonatal. Tô com pouca energia hoje, mal consigo
>    focar. Tenho 35 minutos."
> B) "Já estudei sepse neonatal antes, só quero revisar rápido. Tenho 35
>    minutos."

**Estado inicial:** sessões separadas e limpas; mesmo tema
(`capsule:eisca:sepse_e_meningite_neonatal`), mesmo orçamento de tempo (35
min), perfis de aluno deliberadamente opostos.

**Comportamento esperado:** o apoio oferecido e o primeiro movimento da
sessão diferem genuinamente entre A e B — A recebe escopo essencial reduzido
e ritmo mais gentil (ex.: menos itens, mais explicação antes de testar); B
recebe revisão mais direta com possibilidade de extensão (itens mais
desafiadores, menos preâmbulo). Ambos recebem "essencial + extensão"
estruturado, não um bloco monolítico.

**Falha bloqueadora:** as duas sessões seguem exatamente a mesma sequência
de perguntas/conteúdo, ignorando o perfil declarado; OU a sessão A adota tom
punitivo/cobrador incompatível com "pouca energia".

**Detector:** similaridade textual entre a primeira resposta de A e a
primeira resposta de B — alta similaridade (>60%) sinaliza falha; busca por
linguagem punitiva/cobradora ("você precisa se esforçar mais", "não é hora
de desculpa") na sessão A.
