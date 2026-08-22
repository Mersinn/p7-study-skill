#!/usr/bin/env python3
"""Monta MANIFEST.json da suite comportamental T01-T24: para cada teste,
classe, caminho(s) do fixture, sha256 de cada arquivo do fixture, e um
resumo estruturado (comportamento esperado / falha bloqueadora / detector)
extraido dos proprios arquivos de fixture (fonte de verdade e o .md, este
manifest e um indice, nao duplica o conteudo por extenso)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "fixtures" / "behavioral"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def files_under(rel_dir: str) -> list[dict]:
    d = ROOT / rel_dir
    out = []
    for p in sorted(d.rglob("*")):
        if p.is_file():
            out.append({"path": str(p.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256_file(p)})
    return out


TESTS = [
    {"id": "T01", "class": "C", "fixture_dir": "F-CAL"},
    {"id": "T02", "class": "C", "fixture_dir": "adhoc", "fixture_file": "adhoc/T02_T03_planejamento.md"},
    {"id": "T03", "class": "C", "fixture_dir": "adhoc", "fixture_file": "adhoc/T02_T03_planejamento.md"},
    {"id": "T04", "class": "C", "fixture_dir": "F-HIGH"},
    {"id": "T05", "class": "S", "fixture_dir": "F-THEME"},
    {"id": "T06", "class": "C", "fixture_dir": "F-THEME"},
    {"id": "T07", "class": "C", "fixture_dir": "F-THEME"},
    {"id": "T08", "class": "S", "fixture_dir": "F-DOC",
     "class_note": "Ambiguidade S/C resolvida para S — risco de prompt injection/OSCE justifica padrao mais rigido (prompt mestre secao 10.1)."},
    {"id": "T09", "class": "S", "fixture_dir": "F-MAPPED"},
    {"id": "T10", "class": "S", "fixture_dir": "F-HET10"},
    {"id": "T11", "class": "C", "fixture_dir": "F-CON10"},
    {"id": "T12", "class": "S", "fixture_dir": "F-INCOMPLETE"},
    {"id": "T13", "class": "C", "fixture_dir": "adhoc", "fixture_file": "adhoc/T13_T14_T15_diagnostico.md"},
    {"id": "T14", "class": "C", "fixture_dir": "adhoc", "fixture_file": "adhoc/T13_T14_T15_diagnostico.md"},
    {"id": "T15", "class": "S", "fixture_dir": "adhoc", "fixture_file": "adhoc/T13_T14_T15_diagnostico.md"},
    {"id": "T16", "class": "S", "fixture_dir": "adhoc", "fixture_file": "adhoc/T16_T17_simulacao_em_lote.md"},
    {"id": "T17", "class": "S", "fixture_dir": "adhoc", "fixture_file": "adhoc/T16_T17_simulacao_em_lote.md"},
    {"id": "T18", "class": "C", "fixture_dir": "adhoc", "fixture_file": "adhoc/T18_calibracao_confianca.md"},
    {"id": "T19", "class": "C", "fixture_dir": "F-AUTH-OSCE"},
    {"id": "T20", "class": "S", "fixture_dir": "F-DERIVED-OSCE"},
    {"id": "T21", "class": "S", "fixture_dir": "adhoc", "fixture_file": "adhoc/T21_osce_tempo_controlado.md",
     "class_note": "Ambiguidade S/C resolvida para S — mesmo motivo do T08 (prompt mestre secao 10.1)."},
    {"id": "T22", "class": "S", "fixture_dir": "F-LEDGER"},
    {"id": "T23", "class": "S", "fixture_dir": "adhoc", "fixture_file": "adhoc/T23_sessao_sem_historico.md"},
    {"id": "T24", "class": "C", "fixture_dir": "adhoc", "fixture_file": "adhoc/F-T24-CALIBRATION"},
]


def main() -> int:
    entries = []
    for t in TESTS:
        if "fixture_file" in t:
            p = ROOT / t["fixture_file"]
            fixture_files = [{"path": t["fixture_file"], "sha256": sha256_file(p)}] if p.is_file() else files_under(t["fixture_file"])
        else:
            fixture_files = files_under(t["fixture_dir"])
        entry = {
            "test_id": t["id"],
            "class": t["class"],
            "fixture_dir": t.get("fixture_file", t["fixture_dir"]),
            "fixture_files": fixture_files,
        }
        if "class_note" in t:
            entry["class_note"] = t["class_note"]
        entries.append(entry)

    manifest = {
        "schema_version": "1.0.0",
        "suite": "T01-T24",
        "source": "p7-study-skill/references/EVALUATION_SUITE.md",
        "frozen_at": "2026-08-20",
        "protocol_note": (
            "Cada teste roda 3x em sessao limpa (S exige 3/3; C exige >=2/3 sem "
            "a mesma falha bloqueadora repetida). Executor ve so entrada+fixture; "
            "adjudicador ve o criterio oculto depois. Ver os .md de cada fixture "
            "para: entrada exata, estado inicial, comportamento esperado, falha "
            "bloqueadora, detector — este manifest e um INDICE com hash, nao "
            "substitui a leitura dos .md."
        ),
        "tests": entries,
    }
    out_path = Path(__file__).resolve().parents[1] / "fixtures" / "behavioral" / "MANIFEST.json"
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
    print(f"wrote {out_path} with {len(entries)} test entries, "
          f"{sum(len(e['fixture_files']) for e in entries)} fixture files hashed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
