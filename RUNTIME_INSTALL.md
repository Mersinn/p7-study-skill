# Instalação da P7

Para instalar como skill no Claude, use **P7-Study-Skill-1.5.1-rc.1-runtime.zip**. O ZIP contém a pasta `p7-study-skill/`, com 207 arquivos e todas as 158 cápsulas completas. O estado da versão permanece **candidato / HOLD**; a redução do pacote não aprova os gates de qualificação pendentes.

O pacote `-engineering.zip` guarda a distribuição completa de manutenção. Testes, relatórios de reparo e evidências de release ficam fora da skill de uso. Os índices e registros consultados pelo tutor permanecem no runtime.

O corpo das instruções e as cápsulas são preservados byte a byte. Somente a descrição de descoberta do `SKILL.md` é reduzida para 183 caracteres no ZIP runtime, respeitando o limite de 200 descrito no [guia oficial do Claude](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). Não foi confirmado um limite oficial de 200 ou 250 arquivos.

O usuário realizará o upload no Claude. O teste de importação real ainda não foi observado; a verificação local cobre a estrutura do ZIP, dependências, preservação do conteúdo e execução dos scripts extraídos.

Para gerar as duas distribuições e executar a verificação local, na raiz do repositório:

```text
python tools/build_runtime_distribution.py --root p7-study-skill --output-dir dist/runtime
```

O gerador não altera a fonte. O relatório de build fica fora do ZIP de uso e comprova a preservação das cápsulas, as exclusões de manutenção, as referências verificadas, a reprodução determinística e o teste do ledger com dados sintéticos.

Depois de instalar, um pedido simples para começar é: **Tenho 30 minutos para estudar EISCA; começa comigo por uma questão.**
