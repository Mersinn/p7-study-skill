# Instalação da P7

Use **P7-Study-Skill-1.5.1.zip** para instalar a versão final no Claude ou no Codex. O ZIP compacto contém a pasta `p7-study-skill/` com todas as 158 cápsulas e os índices necessários ao tutor, em 199 entradas (abaixo do limite de 200 arquivos). As 18 referências operacionais foram agrupadas em 10 arquivos com o conteúdo preservado e âncoras internas verificadas.

A distribuição de engenharia fica no GitHub para manutenção; ela inclui relatórios, testes e evidências de desenvolvimento. O usuário final deve usar o ZIP compacto de 199 entradas. O construtor reproduzível é `tools/build_compact_distribution.py`; o ZIP de engenharia não é o arquivo de upload.

O conteúdo clínico e educacional foi preservado. A descrição de descoberta do `SKILL.md` é reduzida somente na cópia runtime para cumprir o limite documentado de descrição do Claude. As quarentenas, o conflito e os estados pendentes continuam explícitos.

O upload real no Claude ou no Codex será feito pelo usuário. A verificação local cobre a estrutura do ZIP, a contagem de 199 entradas, a preservação byte a byte das cápsulas e das fontes curriculares, o round-trip das 18 referências e o smoke test do ledger.
