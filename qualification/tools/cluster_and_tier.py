#!/usr/bin/env python3
"""Normaliza, deduplica e classifica por dano os claims críticos detectados.

Consome `qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv` (produzido por
`critical_claim_scan.py`, versão congelada — ver FROZEN_DETECTOR.md) e faz dois
trabalhos mecânicos que não devem consumir julgamento de modelo:

1. **Clustering** — o mesmo fato clínico aparece em várias cápsulas (a mesma
   dose, o mesmo corte, o mesmo alarme). Adjudicar cada ocorrência
   isoladamente seria trabalho redundante e caro. Duas ocorrências entram no
   mesmo cluster somente quando:
     a) mesma categoria E mesmo conjunto de tokens numéricos/unidades
        (`92-94%`, `1:10.000`, `4,5h` etc.) — critério primário; ou
     b) mesma categoria E texto normalizado quase idêntico (sem números),
        para claims não numéricos como contraindicações nomeadas.
   Nenhuma junção por similaridade temática vaga. Cada cluster preserva TODAS
   as ocorrências (cápsula, linha, seção, texto) — nada é descartado.

2. **Classificação por dano (A/B/C)** — regra determinística e auditável:
     A — pode alterar conduta, urgência, dose, via, contraindicação, janela
         ou segurança imediata. Quarentena bloqueadora obrigatória se não
         resolvido e apresentado como prática atual.
     B — clinicamente relevante, sem dano imediato previsível (critério
         diagnóstico/estadiamento sem gatilho de ação na própria linha).
     C — descritivo, acadêmico ou curricular (epidemiologia, componente de
         escore sem alvo terapêutico).

As regras estão em ACTION_TRIGGER_TERMS / DIAGNOSTIC_TERMS abaixo. O script
não decide se o CONTEÚDO do claim está certo — só sua forma e seu risco.

Uso:
    python qualification/tools/cluster_and_tier.py \
        --detections qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv \
        --out qualification/reports
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0.0"

ALWAYS_A = {
    "dose_via_intervalo",
    "contraindicacao_interacao",
    "emergencia_sinal_alarme",
    "janela_temporal",
    "calendario_regra_jurisdicional",
}

# sequencia_terapeutica é quase sempre A (ordem terapêutica = segurança), mas
# checamos gatilho de ação mesmo assim por disciplina de auditoria.
SEQUENCE_CATEGORY = "sequencia_terapeutica"
CUTOFF_CATEGORY = "cutoff_escore_estadiamento"

ACTION_TRIGGER_TERMS = [
    r"\bindicad[oa]s?\b", r"\btratar se\b", r"\biniciar\b", r"\bencaminhar\b",
    r"\binternar\b", r"\bdialise\b", r"\bdialitico\b", r"\bcirurgia\b",
    r"\bpaaf\b", r"\bbiopsia\b", r"\btransplante\b", r"\bsuspender\b",
    r"\balvo\b", r"\bmeta de\b", r"\btitular\b", r"\bajustar dose\b",
    r"\breduzir dose\b", r"\baumentar dose\b", r"\bescalonar\b",
    r"\btrombolise\b", r"\btrombectomia\b", r"\bantibioticoterapia\b",
    r"\bventilacao\b", r"\bintubacao\b", r"\bnefrectomia\b", r"\badrenalectomia\b",
    r"\breidratacao\b", r"\bhemodialise\b", r"\boxigenoterapia\b",
]
DIAGNOSTIC_ONLY_TERMS = [
    r"\bdiagnostico\b", r"\bclassificacao\b", r"\bestadiamento\b",
    r"\bescore de\b", r"\bpontuacao\b", r"\bcorte para\b", r"\brisco de\b",
]

ACTION_RE = re.compile("|".join(ACTION_TRIGGER_TERMS))
DIAG_RE = re.compile("|".join(DIAGNOSTIC_ONLY_TERMS))


def strip_accents(text: str) -> str:
    return "".join(ch for ch in unicodedata.normalize("NFD", text) if unicodedata.category(ch) != "Mn")


def normalize(text: str) -> str:
    return strip_accents(text).lower().replace("×", "x")


def core_text(text: str) -> str:
    """Normaliza para comparação: remove pipes de tabela, colapsa espaço."""
    t = normalize(text)
    t = re.sub(r"\|", " ", t)
    t = re.sub(r"[^\w\s.,%<>≤≥:/-]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def tier_for(category: str, text: str) -> str:
    t = normalize(text)
    if category in ALWAYS_A:
        return "A"
    if category == SEQUENCE_CATEGORY:
        return "A"
    if category == CUTOFF_CATEGORY:
        if ACTION_RE.search(t):
            return "A"
        if DIAG_RE.search(t):
            return "B"
        return "C"
    return "B"  # fallback conservador; não deveria ocorrer no denominador atual


def stable_id(*parts: str) -> str:
    return hashlib.sha256("␟".join(parts).encode("utf-8")).hexdigest()[:16]


def load_detections(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [row for row in csv.DictReader(handle) if row["in_sweep_denominator"] == "True"]


def cluster_key(row: dict[str, Any], numeric_tokens: set[str]) -> str:
    if numeric_tokens:
        return f"num␟{row['category']}␟{'+'.join(sorted(numeric_tokens))}"
    return f"txt␟{row['category']}␟{core_text(row['text'])}"


NUM_TOKEN = re.compile(
    r"\d+(?:[.,]\d+)?\s*(?:mg/kg/dia|mcg/kg/min|mg/kg|mcg/kg|ml/kg|mg/dl|mg/l|g/dl|"
    r"mmol/l|meq/l|ng/ml|pg/ml|mg/m2|ui/kg|mg|mcg|µg|g|kg|ml|mmhg|mmol|meq|ui|%)"
    r"|\d+(?:[.,]\d+)?"
)


def numeric_tokens(text: str) -> set[str]:
    out = set()
    for m in NUM_TOKEN.finditer(normalize(text)):
        tok = re.sub(r"\s+", "", m.group(0)).replace(",", ".")
        if tok in {str(n) for n in range(0, 11)}:
            continue
        out.add(tok)
    return out


def build_clusters(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        nt = numeric_tokens(row["text"])
        key = cluster_key(row, nt)
        groups.setdefault(key, []).append(row)

    clusters = []
    for key, members in groups.items():
        tiers = {tier_for(m["category"], m["text"]) for m in members}
        # cluster herda o tier mais severo entre suas ocorrências (A > B > C)
        tier = "A" if "A" in tiers else ("B" if "B" in tiers else "C")
        representative = min(members, key=lambda m: (m["capsule_path"], int(m["line_no"])))
        capsules = sorted({m["capsule_id"] for m in members})
        risks = sorted({m["risk"] for m in members})
        disciplines = sorted({m["discipline"] for m in members})
        categories = sorted({m["category"] for m in members})
        clusters.append(
            {
                "cluster_id": stable_id(key),
                "tier": tier,
                "tier_basis": "mixed" if len(tiers) > 1 else "uniform",
                "category": "+".join(categories),
                "occurrence_count": len(members),
                "capsule_count": len(capsules),
                "capsule_ids": " ; ".join(capsules),
                "risk_levels": " ; ".join(risks),
                "disciplines": " ; ".join(disciplines),
                "representative_capsule_path": representative["capsule_path"],
                "representative_line_no": representative["line_no"],
                "representative_text": representative["text"],
                "cluster_key_type": key.split("␟", 1)[0],
                "members": members,
            }
        )
    clusters.sort(key=lambda c: (c["tier"], -c["occurrence_count"]))
    return clusters


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--detections", type=Path, default=Path("qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv"))
    parser.add_argument("--out", type=Path, default=Path("qualification/reports"))
    args = parser.parse_args()

    rows = load_detections(args.detections)
    clusters = build_clusters(rows)

    cluster_rows = [{k: v for k, v in c.items() if k != "members"} for c in clusters]
    write_csv(
        args.out / "CLAIM_CLUSTERS.csv",
        cluster_rows,
        [
            "cluster_id", "tier", "tier_basis", "category", "occurrence_count", "capsule_count",
            "capsule_ids", "risk_levels", "disciplines", "representative_capsule_path",
            "representative_line_no", "representative_text", "cluster_key_type",
        ],
    )

    occurrence_rows = []
    for c in clusters:
        for m in c["members"]:
            occurrence_rows.append(
                {
                    "cluster_id": c["cluster_id"],
                    "tier": c["tier"],
                    "capsule_id": m["capsule_id"],
                    "capsule_path": m["capsule_path"],
                    "line_no": m["line_no"],
                    "section": m["section"],
                    "risk": m["risk"],
                    "discipline": m["discipline"],
                    "category": m["category"],
                    "resolved": m["resolved"],
                    "text": m["text"],
                }
            )
    write_csv(
        args.out / "CLAIM_CLUSTER_OCCURRENCES.csv",
        occurrence_rows,
        ["cluster_id", "tier", "capsule_id", "capsule_path", "line_no", "section", "risk",
         "discipline", "category", "resolved", "text"],
    )

    by_tier = {"A": 0, "B": 0, "C": 0}
    by_tier_occ = {"A": 0, "B": 0, "C": 0}
    by_tier_high_risk_occ = {"A": 0, "B": 0, "C": 0}
    for c in clusters:
        by_tier[c["tier"]] += 1
        by_tier_occ[c["tier"]] += c["occurrence_count"]
        by_tier_high_risk_occ[c["tier"]] += sum(1 for m in c["members"] if m["risk"] == "high")

    single_capsule_clusters = sum(1 for c in clusters if c["capsule_count"] == 1)
    multi_capsule_clusters = sum(1 for c in clusters if c["capsule_count"] > 1)

    summary = {
        "schema_version": SCHEMA_VERSION,
        "detector_hash_frozen": "771b504b23650e8d048479263647b60acdc8683aa92d8ca95db8c4418cc41323",
        "detector_schema_version": "1.4.0 (CONGELADO — ver DETECTOR_VALIDATION_REPORT.md secao 11.5)",
        "input_occurrences": len(rows),
        "clusters_total": len(clusters),
        "dedup_ratio": round(len(rows) / len(clusters), 2) if clusters else 0,
        "clusters_single_capsule": single_capsule_clusters,
        "clusters_multi_capsule": multi_capsule_clusters,
        "clusters_by_tier": by_tier,
        "occurrences_by_tier": by_tier_occ,
        "high_risk_occurrences_by_tier": by_tier_high_risk_occ,
        "tier_A_clusters_needing_adjudication": by_tier["A"],
        "limitations": [
            "Classificacao A/B/C e regra lexical deterministica sobre a categoria e o texto "
            "da linha; nao e julgamento medico. Amostra sera validada manualmente a parte.",
            "Clustering por token numerico pode sub-agrupar (mesma dose escrita com "
            "unidades/formatacao diferentes cai em clusters distintos) — sub-agrupamento e "
            "seguro (nunca funde fatos diferentes), mas superestima o numero de clusters unicos.",
            "Nenhum gate fechado por este artefato.",
        ],
    }
    (args.out / "CLAIM_CLUSTER_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8", newline="",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
