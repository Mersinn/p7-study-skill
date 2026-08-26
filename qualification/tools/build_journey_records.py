#!/usr/bin/env python3
"""Build reproducible Codex journey records and an arithmetic summary."""
from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURE_DIR = ROOT / "qualification" / "fixtures" / "journeys"
RUN_DIR = ROOT / "qualification" / "runs" / "journeys_codex"
ADJ_PATH = ROOT / "qualification" / "records" / "journey_adjudications.jsonl"
SUMMARY_PATH = ROOT / "qualification" / "reports" / "SCRIPTED_JOURNEYS_SUMMARY.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def fixture_path(journey_id: str) -> Path:
    matches = sorted(FIXTURE_DIR.glob(f"{journey_id}_*.json"))
    if len(matches) != 1:
        raise RuntimeError(f"expected one fixture for {journey_id}, got {matches}")
    return matches[0]


def git_object(spec: str) -> str:
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", "rev-parse", spec],
        cwd=ROOT,
        text=True,
    ).strip()


def main() -> int:
    adjudications = load_jsonl(ADJ_PATH)
    counts: Counter[str] = Counter()
    by_journey: dict[str, Counter[str]] = defaultdict(Counter)
    records: list[dict] = []
    for adj in adjudications:
        journey_id = adj["journey_id"]
        run_number = int(adj["run_number"])
        fixture = fixture_path(journey_id)
        fixture_data = json.loads(fixture.read_text(encoding="utf-8"))
        raw_path = RUN_DIR / journey_id / f"run{run_number}_raw.md"
        if not raw_path.is_file():
            raise FileNotFoundError(raw_path)
        allowed = []
        for rel in fixture_data.get("allowed_files", []):
            allowed_path = ROOT / rel
            allowed.append({"path": rel, "sha256": sha256(allowed_path)})
        record = {
            **adj,
            "surface": "Codex",
            "executor": "multi_agent_v1__spawn_agent",
            "reasoning_effort": "high",
            "skill_tree_sha": git_object(f"{adj['skill_snapshot_sha']}:p7-study-skill"),
            "fixture_file": fixture.relative_to(ROOT).as_posix(),
            "fixture_sha256": sha256(fixture),
            "fixture_turns_sha256": hashlib.sha256(
                json.dumps(fixture_data["turns"], ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
            "allowed_files": allowed,
            "raw_file": raw_path.relative_to(ROOT).as_posix(),
            "raw_sha256": sha256(raw_path),
        }
        record_path = raw_path.with_name(f"run{run_number}_record.json")
        record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        records.append(record)
        counts[record["adjudication"]] += 1
        by_journey[journey_id][record["adjudication"]] += 1

    dependency_hashes = {
        ADJ_PATH.relative_to(ROOT).as_posix(): sha256(ADJ_PATH),
        Path(__file__).resolve().relative_to(ROOT).as_posix(): sha256(Path(__file__).resolve()),
    }
    for journey_id in sorted(by_journey):
        path = fixture_path(journey_id)
        dependency_hashes[path.relative_to(ROOT).as_posix()] = sha256(path)
    summary = {
        "schema_version": "1.0.0",
        "surface": "Codex",
        "runs_total": len(records),
        "runs_by_adjudication": dict(sorted(counts.items())),
        "runs_by_journey": {key: dict(sorted(value.items())) for key, value in sorted(by_journey.items())},
        "journey_gate_rule": "each journey PASS 3/3 in clean sessions",
        "dependency_hashes": dependency_hashes,
    }
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
