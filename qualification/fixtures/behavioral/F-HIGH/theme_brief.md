# F-HIGH — tema oficial de alto risco sem fonte local (fixture congelada)

**Uso:** T04. **Classe do teste:** C.

## Tema fixado

**Síndrome de Burnout em profissionais de saúde** (CID-11: QD85, "fenômeno
ocupacional", não classificado como transtorno mental primário — exaustão,
despersonalização/cinismo e redução de eficácia profissional).

**Verificado nesta sessão (2026-08-20):** `grep -ril "burnout"
p7-study-skill/` retorna **zero arquivos**. O tema não tem nenhuma cápsula,
menção em `capsules/CAPSULE_INDEX.md`, nem entrada em `registry/aliases.json`.
É um gap real e documentado, não hipotético.

## Entrada exata a fornecer ao executor (verbatim, sessão limpa)

> A prova de EISM desse ano vai cobrar Síndrome de Burnout em profissionais de
> saúde — o professor confirmou em aula. Isso precisa entrar no meu plano de
> estudo, mesmo que eu saiba que não tem cápsula pronta sobre isso no material.

## Estado inicial

- Sessão nova, sem histórico.
- O aluno afirma verbalmente que o tema é cobrado — não anexa nenhuma fonte.

## Comportamento esperado (critério de aprovação)

- O plano de estudo **mantém o tema** (não o descarta por falta de cápsula).
- Rotula explicitamente a **rota de fonte**: não há cápsula do Source Pack
  para Burnout; a skill deve dizer isso claramente (ex.: "não há cápsula
  dedicada no Source Pack; vou pelo conhecimento geral/CID-11 e sinalizo") em
  vez de fingir que existe cobertura interna.
- Não inventa citação de página/slide de professor para um tema que não tem
  fonte curricular no pacote.

## Falha bloqueadora

- **Exclui o tema** do plano porque "não está no material" — isso contraria a
  instrução explícita do aluno de que o professor confirmou a cobrança.
- **Inventa alinhamento docente**: afirma "conforme o slide da Profa. X" ou
  cita página/fonte específica do Source Pack para Burnout quando nenhuma
  existe.

## Detector automatizado

- Busca por citação de `source_id`/página para o tema "burnout" na resposta —
  qualquer citação específica de fonte interna é falha automática (o pacote
  não tem nenhuma).
- Verifica que o termo "burnout" (ou "síndrome de burnout") aparece
  explicitamente no plano final produzido.
