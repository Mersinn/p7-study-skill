#!/usr/bin/env python3
"""Index adjudication specs separately from executor-only payloads."""
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
    {"id": "T22", "class": "S", "fixture_dir": "F-LEDGER", "fixture_file": "F-LEDGER/ledger_scenario.md"},
    {"id": "T23", "class": "S", "fixture_dir": "adhoc", "fixture_file": "adhoc/T23_sessao_sem_historico.md"},
    {"id": "T24", "class": "C", "fixture_dir": "adhoc", "fixture_file": "adhoc/F-T24-CALIBRATION/calibration_scenario.md"},
]

PAYLOADS = {
    "T01": ["execution_payloads/REMAINING_INPUTS.md"],
    "T02": ["execution_payloads/T02_inputs.md"],
    "T03": ["execution_payloads/T03_inputs.md"],
    "T04": ["execution_payloads/REMAINING_INPUTS.md"],
    "T05": ["execution_payloads/REMAINING_INPUTS.md"],
    "T06": ["execution_payloads/F-THEME_inputs.md"],
    "T07": ["execution_payloads/F-THEME_inputs.md"],
    "T08": ["execution_payloads/F-DOC_input.md"],
    "T09": ["execution_payloads/F-MAPPED_input.md"],
    "T10": ["execution_payloads/F-HET10_items.md"],
    "T11": ["execution_payloads/F-CON10_inputs.md"],
    "T12": ["execution_payloads/F-INCOMPLETE_input.md"],
    "T13": ["execution_payloads/T13_T14_inputs.md"],
    "T14": ["execution_payloads/T13_T14_inputs.md"],
    "T15": ["execution_payloads/REMAINING_INPUTS.md"],
    "T16": ["execution_payloads/REMAINING_INPUTS.md"],
    "T17": ["execution_payloads/REMAINING_INPUTS.md"],
    "T18": ["execution_payloads/T18_inputs.md"],
    "T19": ["execution_payloads/F-AUTH-OSCE_inputs.md"],
    "T20": ["execution_payloads/F-DERIVED-OSCE_items.md"],
    "T21": ["execution_payloads/T21_OSCE_items.md"],
    "T22": ["execution_payloads/F-LEDGER_surface_inputs.md", "F-LEDGER/.p7-state/events.jsonl", "F-LEDGER/.p7-state/ledger_meta.json"],
    "T23": ["execution_payloads/REMAINING_INPUTS.md"],
    "T24": ["execution_payloads/F-T24_inputs.md", "adhoc/F-T24-CALIBRATION/.p7-state/events.jsonl", "adhoc/F-T24-CALIBRATION/.p7-state/ledger_meta.json"],
}


def explicit_files(paths: list[str]) -> list[dict]:
    return [{"path": rel, "sha256": sha256_file(ROOT / rel)} for rel in paths]


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
            "adjudication_spec_files": fixture_files,
            "executor_payload_files": explicit_files(PAYLOADS[t["id"]]),
        }
        if "class_note" in t:
            entry["class_note"] = t["class_note"]
        entries.append(entry)

    manifest = {
        "schema_version": "1.1.0",
        "suite": "T01-T24",
        "source": "p7-study-skill/references/EVALUATION_SUITE.md",
        "frozen_at": "2026-08-20",
        "protocol_note": (
            "Cada teste roda 3x em sessao limpa (S exige 3/3; C exige >=2/3 sem "
            "a mesma falha bloqueadora repetida). Executor ve so entrada+fixture; "
            "adjudicador ve o criterio oculto depois. adjudication_spec_files sao "
            "PROIBIDOS ao executor; executor_payload_files sao a lista exaustiva "
            "de arquivos permitidos e hasheados. O raw/record preserva o turno "
            "exato enviado e sua ordem."
        ),
        "tests": entries,
    }
    out_path = Path(__file__).resolve().parents[1] / "fixtures" / "behavioral" / "MANIFEST.json"
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
    print(f"wrote {out_path} with {len(entries)} test entries, "
          f"{sum(len(e['adjudication_spec_files']) for e in entries)} specs and "
          f"{sum(len(e['executor_payload_files']) for e in entries)} executor files hashed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
