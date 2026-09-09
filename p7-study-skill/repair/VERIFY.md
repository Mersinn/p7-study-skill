# Reproduzir a verificação técnica

Executar a partir da raiz `p7-study-skill/` do candidato, usando Python 3.11+:

```bash
python3 scripts/run_tests.py
python3 repair/adversarial_checks.py --root .
python3 scripts/reconcile_package.py --check
python3 scripts/validate_package.py --evidence-mode standalone
python3 scripts/validate_package.py --release-gate --evidence-mode standalone
```

Resultados esperados: suíte 53 aprovados + 1 ignorado de 54; checks adversariais33/33; reconcile0; validador estrutural0; release gate1 por nove gates pending. O teste ignorado depende do manifesto original em `../qualification/fixtures/behavioral/MANIFEST.json`; não criar um substituto fictício.

O checker adversarial não grava arquivos por padrão. Para registrar nova execução, passar `--output` com caminho externo ao pacote. Os JSONs de repair são evidências congeladas; editar um arquivo substantivo exige reconciliar e renovar atestações, não apenas reexecutar o validador.

`release_evidence.py` é um módulo de validação importado pelo validador. Executá-lo diretamente não reexecuta os gates. Nenhum destes comandos verifica uma página clínica primária nem promove claims.
