# CLEAN_INSTALL_REPORT — P7 Study Skill 1.5.0

## Estado

O gate permanece condicionado à execução final sobre o ZIP determinístico da
v1.5.0. O snapshot do repositório já passou 54/54 testes e reconciliou 158/158
cápsulas; os números standalone serão preenchidos após a extração descartável.

## Contrato da execução final

1. construir duas vezes e exigir ZIPs byte a byte idênticos;
2. extrair em diretório descartável, sem histórico, `corpus_text/` ou `vision_png/`;
3. executar testes, reconciliação, validação normal e `--release-gate` em modo standalone;
4. registrar SHA-256 do ZIP, contagens exatas, warnings e código de saída;
5. não converter ausência de camada opcional em PASS clínico.

## Compatibilidade separada

Claude permanece `not_evaluated` por OAuth. Essa pendência não bloqueia a
instalação Codex e não entra no denominador standalone.
