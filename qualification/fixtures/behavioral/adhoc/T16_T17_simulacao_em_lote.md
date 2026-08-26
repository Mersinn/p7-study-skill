# T16 e T17 — simulação de questões em lote (fixtures ad-hoc)

Ambos classe **S**.

---

## T16 — "simula 10 questões" (sem qualificar formato)

**Entradas exatas, na mesma sessão:**

> 1) "Simula 10 questões de EISCA pra mim."
> 2) "Na primeira, marco B com 60% de confiança."
> 3) "Na segunda, marco A com 50% de confiança."

**Estado inicial:** sessão nova. O pedido não especifica "todas juntas" nem
"sem feedback" — é o pedido padrão, ambíguo por default.

**Comportamento esperado:** entrega **apenas a questão 1**, sem gabarito; após a
primeira tentativa, corrige somente a questão 1 e entrega somente a questão 2;
após a segunda, corrige somente a questão 2 e entrega somente a questão 3.

**Falha bloqueadora:** despeja as 10 questões de uma vez (viola o formato
padrão de uma-a-uma); OU revela a resposta/gabarito junto com a questão 1.

**Detector:** em cada resposta conta exatamente um novo enunciado; verifica índices
1→2→3, ausência de duplicação e ausência de feedback de item ainda não tentado.

---

## T17 — "fechado, 10 juntas, sem feedback"

**Entrada exata:** "Quero as 10 questões de uma vez, fechado, sem feedback
até eu terminar todas."

**Estado inicial:** sessão nova. Pedido explícito e inequívoco do formato em
lote — o OPOSTO do T16, testando se a skill respeita a instrução explícita
quando dada (em vez de forçar o padrão uma-a-uma contra o pedido do aluno).

**Comportamento esperado:** entrega as 10 questões de uma vez (respeitando o
pedido explícito); zero feedback/gabarito é mostrado até o aluno enviar
todas as 10 tentativas.

**Falha bloqueadora:** entrega uma a uma contra o pedido explícito do aluno
(ignora a instrução clara); OU revela feedback/gabarito de algum item antes
do aluno completar as 10 tentativas.

**Detector:** conta quantos enunciados de questão aparecem na primeira
resposta — deve ser 10, não 1 (aqui a regra se inverte em relação ao T16,
porque o pedido do aluno também se inverteu); busca por `Resposta:`/
`Gabarito:` antes da 10ª tentativa do aluno ser recebida.

**Nota de desenho:** T16 e T17 são deliberadamente o par oposto um do outro
— o mesmo detector de "vazou gabarito cedo" se aplica aos dois, mas o
critério de "quantas questões na primeira resposta" se inverte porque o
pedido do aluno mudou. Isso testa se a skill responde ao que foi pedido, não
a uma regra fixa e cega de "sempre uma por vez".
