#!/usr/bin/env python3
"""Para cada capsula da amostra de FN, imprime as linhas de secao assertiva
que o detector NAO marcou como critical_category (independente de tier), para
revisao manual de falso negativo. Reduz o trabalho de leitura ao gap real."""
from __future__ import annotations
import csv
import re
import unicodedata
from pathlib import Path

def strip_accents(t): return "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
def norm(t): return strip_accents(t).lower().replace("×", "x")

SECTION_CLASS = {
    "conceito operacional minimo": "assertive_clinical", "pivo clinico": "assertive_clinical",
    "palavras-ancora": "assertive_clinical", "dados de precisao": "assertive_clinical",
    "conduta": "assertive_clinical", "conduta e guardrails": "assertive_clinical",
    "cards minimos": "assertive_clinical", "revisao": "assertive_clinical", "a estacao": "assertive_clinical",
    "trombolise intravenosa": "assertive_clinical", "trombectomia mecanica": "assertive_clinical",
    "suporte que nao deve virar alvo automatico": "assertive_clinical",
    "operacao x movimento": "pedagogic_meta", "demanda x movimento": "pedagogic_meta",
    "como cai": "pedagogic_meta", "distratores sedutores": "pedagogic_meta", "pegadinhas": "pedagogic_meta",
    "pegadinhas e seguranca": "pedagogic_meta", "mini-casos ativos": "pedagogic_meta",
    "metadados": "provenance", "fontes de vigencia clinica": "provenance", "estados de verificacao": "provenance",
    "camada de fonte": "provenance", "divergencias resolvidas": "provenance",
    "fontes ilegiveis / nao encontradas": "provenance", "pendencia a confirmar": "provenance",
    "reconciliacao das duas capsulas anunciadas": "provenance", "para a prova/material historico": "historical",
}

def classify(s: str) -> str:
    if s in SECTION_CLASS:
        return SECTION_CLASS[s]
    if s.startswith("pratica clinica atual"):
        return "assertive_clinical"
    if s.startswith("mini-casos"):
        return "pedagogic_meta"
    if not s:
        return "preamble"
    return "assertive_clinical"

def main():
    root = Path("p7-study-skill")
    caps = [l.strip() for l in Path("qualification/reports/DETECTOR_FN_CAPSULE_LIST.csv").read_text(encoding="utf-8").splitlines()[1:] if l.strip()]
    det_rows = list(csv.DictReader(open("qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv", encoding="utf-8")))
    flagged_critical = set()  # (capsule_path, line_no) flagged as critical_category, ANY tier
    for r in det_rows:
        if r["critical_category"] == "True":
            flagged_critical.add((r["capsule_path"], r["line_no"]))

    for cap in caps:
        print("=" * 100)
        print(cap)
        section = ""
        for i, raw in enumerate(open(root / cap, encoding="utf-8"), start=1):
            line = raw.rstrip("\n")
            m = re.match(r"^#{1,6}\s+(.*)$", line)
            if m:
                section = norm(m.group(1)).strip()
                continue
            if not line.strip():
                continue
            cls = classify(section)
            if cls != "assertive_clinical":
                continue
            key = (cap, str(i))
            if key in flagged_critical:
                continue
            print(f"  L{i:4d} [{section[:24]:24s}] {line.strip()[:180]}")

if __name__ == "__main__":
    main()
