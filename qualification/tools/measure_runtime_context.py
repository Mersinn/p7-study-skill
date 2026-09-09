#!/usr/bin/env python3
"""Measure deterministic fixed runtime bundles before and after the v1.5 refactor."""

from __future__ import annotations

import argparse
import json
import math
import statistics
import subprocess
from pathlib import Path


BUNDLES = {
    "plano_de_guerra": ["SKILL.md", "references/TARGET_AWARE_STUDY_PLANNER.md"],
    "estudar_tema": ["SKILL.md", "references/ACTIVE_STUDY_QUESTION_FIRST.md", "capsules/CAPSULE_INDEX.md"],
    "resolver_questao": ["SKILL.md", "references/QUESTION_INTELLIGENCE_P7.md"],
    "simular_prova": ["SKILL.md", "references/SIMULATION_PROTOCOL.md"],
    "osce": ["SKILL.md", "references/CASE_OSCE_TUTOR.md"],
    "retomada": ["SKILL.md", "references/LEARNER_STATE_PROTOCOL.md"],
}


def git_bytes(repo: Path, ref: str, package_dir: str, relative: str) -> int:
    path = f"{package_dir}/{relative}"
    proc = subprocess.run(
        ["git", "show", f"{ref}:{path}"],
        cwd=repo,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return len(proc.stdout)


def current_bytes(package: Path, relative: str) -> int:
    return len((package / relative).read_bytes())


def tokens_estimate(byte_count: int) -> int:
    return math.ceil(byte_count / 4)


def bundle_measure(repo: Path, package: Path, baseline_ref: str) -> dict[str, object]:
    package_dir = package.relative_to(repo).as_posix()
    modes: dict[str, object] = {}
    for mode, files in BUNDLES.items():
        before_files = {path: git_bytes(repo, baseline_ref, package_dir, path) for path in files}
        after_files = {path: current_bytes(package, path) for path in files}
        before = sum(before_files.values())
        after = sum(after_files.values())
        modes[mode] = {
            "files": files,
            "before": {"bytes": before, "estimated_tokens": tokens_estimate(before), "files": before_files},
            "after": {"bytes": after, "estimated_tokens": tokens_estimate(after), "files": after_files},
            "reduction": {
                "bytes": before - after,
                "percent": round((before - after) * 100 / before, 2) if before else 0.0,
            },
        }

    capsule_sizes = sorted(path.stat().st_size for path in (package / "capsules").rglob("*.md") if path.name != "CAPSULE_INDEX.md")
    capsule_stats = {
        "count": len(capsule_sizes),
        "min_bytes": min(capsule_sizes),
        "median_bytes": int(statistics.median(capsule_sizes)),
        "p95_bytes": capsule_sizes[math.ceil(len(capsule_sizes) * 0.95) - 1],
        "max_bytes": max(capsule_sizes),
        "note": "dynamic capsule cost is separate from the fixed Estudar Tema bundle",
    }
    return {
        "schema_version": "1.0.0",
        "baseline_ref": baseline_ref,
        "token_estimate": "ceil(utf8_bytes/4); comparative estimate, not tokenizer output",
        "bundles": modes,
        "dynamic_capsule": capsule_stats,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--package", type=Path)
    parser.add_argument("--baseline-ref", default="6fc906f")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    repo = args.repo.resolve()
    package = (args.package or (repo / "p7-study-skill")).resolve()
    result = bundle_measure(repo, package, args.baseline_ref)
    rendered = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8", newline="\n")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
