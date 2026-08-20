#!/usr/bin/env python3
"""Build or check deterministic package artifacts without rewriting capsules."""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from p7lib import (
    PACKAGE_ROOT,
    build_capsule_catalog,
    build_manifest,
    build_metrics,
    canonical_json,
    index_capsule_paths,
    load_json,
    load_jsonl,
    precision_rows,
)


def pretty_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def precision_csv(rows: list[dict[str, Any]]) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=["capsule_path", "section_row", "claim_text", "source_ids"], lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def clinical_claims_csv(root: Path) -> str:
    records = load_jsonl(root / "registry" / "clinical_claims.jsonl")
    fieldnames = [
        "claim_id", "capsule_id", "statement", "claim_type", "criticality", "population",
        "curricular_context", "transcription", "curricular_alignment", "clinical_validity",
        "self_review_l1", "independent_review", "reviewer_id", "reviewed_at", "evidence_json", "notes",
    ]
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for record in records:
        states = record.get("states", {})
        writer.writerow(
            {
                "claim_id": record.get("claim_id"),
                "capsule_id": record.get("capsule_id"),
                "statement": record.get("statement"),
                "claim_type": record.get("claim_type"),
                "criticality": record.get("criticality"),
                "population": record.get("population"),
                "curricular_context": record.get("curricular_context"),
                "transcription": states.get("transcription"),
                "curricular_alignment": states.get("curricular_alignment"),
                "clinical_validity": states.get("clinical_validity"),
                "self_review_l1": states.get("self_review_l1"),
                "independent_review": states.get("independent_review"),
                "reviewer_id": record.get("reviewer_id"),
                "reviewed_at": record.get("reviewed_at"),
                "evidence_json": canonical_json(record.get("evidence", [])),
                "notes": record.get("notes", ""),
            }
        )
    return stream.getvalue()


def generated_index(catalog: list[dict[str, Any]], root: Path) -> str:
    aliases = load_json(root / "registry" / "aliases.json")
    lines = [
        "# Índice canônico gerado — P7",
        "",
        "> Gerado deterministicamente; não editar. O índice pedagógico humano permanece em `capsules/CAPSULE_INDEX.md`.",
        "",
        f"Total de cápsulas físicas: **{len(catalog)}** (baseline auditado: 156; recuperação líquida: {len(catalog) - 156:+d}).",
        "",
        "## Coberturas anunciadas sem cápsula autônoma",
        "",
    ]
    for item in aliases["topic_aliases"]:
        targets = ", ".join(f"`{target}`" for target in item["target_capsule_ids"])
        lines.append(f"- `{item['alias_id']}` — **{item['coverage']}**; destinos: {targets}. {item['note']}")
    lines.extend(["", "## Cápsulas", "", "| ID | Disciplina | Unidade | Prioridade legada normalizada | Risco | Fonte | Arquivo |", "|---|---|---|---|---|---|---|"])
    for item in catalog:
        lines.append(
            f"| `{item['capsule_id']}` | {item['discipline'] or 'UNKNOWN'} | {item['unit'] or 'UNKNOWN'} | "
            f"{item['priority']} (legado: {item['legacy_priority_normalized'] or 'UNKNOWN'}) | {item['risk'] or 'UNKNOWN'} | {item['source_resolution']} | `{item['path']}` |"
        )
    lines.append("")
    return "\n".join(lines)


def artifacts(root: Path) -> dict[str, str]:
    catalog = build_capsule_catalog(root)
    return {
        "CAPSULE_CATALOG.json": pretty_json({"schema_version": "1.0.0", "capsules": catalog}),
        "CAPSULE_INDEX.generated.md": generated_index(catalog, root),
        "METRICS.json": pretty_json(build_metrics(root)),
        "PACKAGE_MANIFEST.json": pretty_json(build_manifest(root)),
        "PRECISION_ROWS.csv": precision_csv(precision_rows(root)),
        "CLINICAL_CLAIMS.csv": clinical_claims_csv(root),
    }


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        os.replace(temp_name, path)
    except Exception:
        Path(temp_name).unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="atomically update artifacts/")
    mode.add_argument("--check", action="store_true", help="fail if artifacts are absent or stale")
    parser.add_argument("--root", type=Path, default=PACKAGE_ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    expected = artifacts(root)
    artifact_dir = root / "artifacts"
    if args.write:
        for name, content in expected.items():
            atomic_write(artifact_dir / name, content)
        print(f"wrote {len(expected)} deterministic artifacts to {artifact_dir}")
        return 0
    stale = []
    for name, content in expected.items():
        path = artifact_dir / name
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            stale.append(name)
    discovered = {item["path"] for item in build_capsule_catalog(root)}
    indexed = index_capsule_paths(root)
    if discovered != indexed:
        stale.append("capsules/CAPSULE_INDEX.md:set-mismatch")
    if stale:
        print("stale or inconsistent: " + ", ".join(stale))
        return 1
    print(f"artifacts current; {len(discovered)} capsules reconciled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
