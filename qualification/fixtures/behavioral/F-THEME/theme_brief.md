# F-THEME — tema com respostas internas (fixture congelada)

**Uso:** T05, T06, T07. **Classe do teste:** T05=S, T06=C, T07=C.
**Cápsula ancorada:** `capsule:eisca:asma_em_pediatria`
(`capsules/EISCA/asma_em_pediatria.md`, risco alto, presente no pacote).

## Pivô clínico congelado (extraído da cápsula em 2026-08-20)

> Há ameaça à vida, hipoxemia, fadiga ou resposta insuficiente? Idade e
> dispositivo mudam a dose; SpO2 isolada não escolhe suporte ventilatório.

Conduta correta esperada, resumida: classificar por
consciência/fala/esforço/FR-FC/SpO2; tratar em PARALELO — SABA inalatório + O2
se hipoxemia + corticoide sistêmico precoce (não esperar SABA falhar antes do
corticoide, exceto crises muito leves).

## T05 — sentinela: "estudar ativamente" não pode terminar em resposta pronta

**Redesenho de 2026-08-20 (decisão do usuário):** a primeira versão desta
entrada era "Quero estudar asma na infância agora — a parte de crise aguda."
— um pedido amplo, sem sinal explícito de que o aluno quer prática/teste. Rodado
3x contra `Modo — Estudar Tema`, produziu revelação completa (pivô resolvido,
conduta, cards) nas 3 vezes. Decisão do usuário ao revisar o achado: para um
pedido amplo *sem sinal de prática*, revelar tudo de uma vez é aceitável —
"não há problema em fazer a revelação" nesse caso. A entrada foi redesenhada
abaixo para carregar sinal INEQUÍVOCO de que o aluno quer ser testado antes de
ver a resposta, que é o cenário que T05 realmente pretende medir.

**Entrada exata:** "Quero estudar asma na infância agora — crise aguda. Mas
quero que você me teste primeiro, não me explica nada ainda — me dá um caso
pra eu tentar resolver antes."

**Estado inicial:** sessão nova, nenhum histórico prévio deste tema.

**Comportamento esperado:** a skill apresenta o cenário/pergunta pivô PRIMEIRO
("há ameaça à vida, hipoxemia, fadiga ou resposta insuficiente?" ou uma
vinheta equivalente) e espera a tentativa do aluno ANTES de revelar a
resposta, o pivô aplicado ou a conduta — agora sem ambiguidade, porque o
aluno pediu explicitamente para ser testado antes de receber explicação.

**Falha bloqueadora:** a primeira resposta da skill já contém a resposta, o
pivô resolvido, a conduta completa ou um card revelador — sem que o aluno
tenha tentado nada — **apesar do pedido explícito de ser testado primeiro**.

**Detector:** presença de `Resposta:`, `Gabarito:`, "a conduta é", ou a frase
completa do pivô clínico ANTES de qualquer pergunta ao aluno na mesma
resposta.

## T06 — core: aluno nunca estudou este tema

**Entrada exata:** "Nunca vi asma em pediatria antes. Quero aprender do
zero."

**Estado inicial:** sessão nova, aluno declara explicitamente zero exposição
prévia.

**Comportamento esperado:** worked example rotulado como tal (exemplo
resolvido, mostrando o raciocínio passo a passo) → depois um item
ISOMÓRFICO (mesma estrutura de decisão, cenário de superfície diferente,
ex. trocar a idade/achado mas manter "ameaça à vida/hipoxemia/fadiga/resposta
insuficiente" como a mesma variável decisiva) apresentado como teste, com
scaffolding que desaparece (fading) nas tentativas seguintes.

**Falha bloqueadora:** só expõe conteúdo (nunca testa) OU pula direto para um
teste impossível de resolver sem exposição prévia nenhuma (sem worked example
antes).

**Detector:** verifica presença de rótulo explícito tipo "exemplo resolvido"
ou "vou te mostrar um caso já resolvido" ANTES do primeiro item testado; e
presença de um segundo item de prática após o exemplo.

## T07 — core: pedido de nova explicação

**Entrada exata (após uma explicação inicial qualquer sobre o pivô de asma
já ter sido dada na mesma sessão):** "Não entendi; explica de outro jeito."

**Estado inicial:** já houve pelo menos uma explicação anterior nesta mesma
sessão sobre o pivô de asma (classificar por
consciência/fala/esforço/FR-FC/SpO2; tratar em paralelo).

**Comportamento esperado:** nova REPRESENTAÇÃO do mesmo conteúdo (não repete
o texto anterior com sinônimos triviais — muda a forma: analogia, tabela,
fluxograma, exemplo concreto diferente), seguida de checagem de compreensão,
e retorno explícito ao alvo original (o pivô clínico de asma).

**Falha bloqueadora:** chama o aluno de "não prestou atenção" / atribui a
dificuldade a falha de esforço do aluno; ou apenas repete a explicação
anterior quase palavra por palavra.

**Detector:** similaridade textual alta (>70% de sobreposição de frases)
entre a explicação original e a nova explicação sinaliza falha; presença de
linguagem culpabilizadora ("você não prestou atenção", "já expliquei isso")
sinaliza falha bloqueadora.
