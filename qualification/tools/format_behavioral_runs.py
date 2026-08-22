#!/usr/bin/env python3
"""Converte JSON bruto de `claude -p --output-format json` em registros de
execucao no schema YAML de references/EVALUATION_SUITE.md, extraindo
transcript + hash. Nao adjudica — so formata para adjudicacao humana/agente
separada."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


def main() -> int:
    run_dir = Path(sys.argv[1])
    test_id = sys.argv[2]
    prompt = sys.argv[3]
    for raw_path in sorted(run_dir.glob("run*_raw.json")):
        n = raw_path.stem.replace("run", "").replace("_raw", "")
        data = json.loads(raw_path.read_text(encoding="utf-8"))
        transcript = data.get("result", "")
        transcript_path = run_dir / f"run{n}_transcript.md"
        transcript_path.write_text(transcript, encoding="utf-8", newline="")
        record = {
            "run_id": f"run:{test_id}:{n}:2026-08-20",
            "test_id": test_id,
            "date_time": "2026-08-20 (America/Fortaleza)",
            "model_surface_version": "Claude Code 2.1.220, claude -p headless",
            "skill_snapshot_sha": "qualification/v1.0.0-claude (ver git log)",
            "tool_access": ["default minus Bash,Edit,Write (--disallowedTools)"],
            "new_session": True,
            "prior_history_supplied": False,
            "session_id": data.get("session_id"),
            "num_turns": data.get("num_turns"),
            "is_error": data.get("is_error"),
            "total_cost_usd": data.get("total_cost_usd"),
            "prompt_sent": prompt,
            "transcript_file": transcript_path.name,
            "transcript_sha256": hashlib.sha256(transcript.encode("utf-8")).hexdigest(),
            "input_tokens": data.get("usage", {}).get("input_tokens"),
            "output_tokens": data.get("usage", {}).get("output_tokens"),
        }
        record_path = run_dir / f"run{n}_record.json"
        record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="")
        print(f"wrote {record_path.name}, {transcript_path.name} (sha256 {record['transcript_sha256'][:16]}...)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
