#!/usr/bin/env python3
"""Private append-only learner ledger and deterministic 48h/7d/21d scheduler."""

from __future__ import annotations

import argparse
import csv
import json
import os
import tempfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from p7lib import SCHEMA_VERSION, canonical_json, sha256_bytes


ALLOWED_EVENT_TYPES = {
    "confidence_recorded",
    "answer_submitted",
    "feedback_shown",
    "review_completed",
    "note_recorded",
}
INTERVALS = (timedelta(hours=48), timedelta(days=7), timedelta(days=21))


def parse_datetime(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("occurred_at/due_at must include a timezone")
    return parsed.astimezone(timezone.utc)


def format_datetime(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


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


def init_state(state_dir: Path) -> None:
    state_dir.mkdir(parents=True, exist_ok=True)
    meta_path = state_dir / "ledger_meta.json"
    if not meta_path.exists():
        atomic_write(
            meta_path,
            json.dumps(
                {
                    "schema_version": SCHEMA_VERSION,
                    "storage": "local_private_append_only",
                    "review_intervals": ["PT48H", "P7D", "P21D"],
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
        )
    (state_dir / "events.jsonl").touch(exist_ok=True)


def read_events(state_dir: Path, verify_chain: bool = True) -> list[dict[str, Any]]:
    path = state_dir / "events.jsonl"
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    previous: str | None = None
    seen: set[str] = set()
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        event = json.loads(raw)
        event_id = event.get("event_id")
        if event_id in seen:
            raise ValueError(f"duplicate event_id at line {line_number}: {event_id}")
        seen.add(event_id)
        if verify_chain:
            if event.get("previous_hash") != previous:
                raise ValueError(f"broken previous_hash at line {line_number}")
            claimed = event.get("record_hash")
            unsigned = {key: value for key, value in event.items() if key != "record_hash"}
            actual = sha256_bytes(canonical_json(unsigned).encode("utf-8"))
            if claimed != actual:
                raise ValueError(f"broken record_hash at line {line_number}")
            previous = claimed
        events.append(event)
    return events


def read_events_tolerant(state_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Contain corrupt lines for projections; strict validation remains read_events()."""
    path = state_dir / "events.jsonl"
    if not path.exists():
        return [], []
    events: list[dict[str, Any]] = []
    corrupt: list[dict[str, Any]] = []
    seen: set[str] = set()
    previous_accepted: str | None = None
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            event = json.loads(raw)
        except json.JSONDecodeError as exc:
            corrupt.append({"line": line_number, "reason": "invalid_json", "detail": str(exc), "raw_sha256": sha256_bytes(raw.encode("utf-8"))})
            continue
        event_id = event.get("event_id")
        if not event_id or event_id in seen:
            corrupt.append({"line": line_number, "reason": "missing_or_duplicate_event_id", "event_id": event_id, "raw_sha256": sha256_bytes(raw.encode("utf-8"))})
            continue
        unsigned = {key: value for key, value in event.items() if key != "record_hash"}
        actual = sha256_bytes(canonical_json(unsigned).encode("utf-8"))
        if event.get("record_hash") != actual:
            corrupt.append({"line": line_number, "reason": "record_hash_mismatch", "event_id": event_id, "raw_sha256": sha256_bytes(raw.encode("utf-8"))})
            continue
        if event.get("previous_hash") != previous_accepted:
            corrupt.append({"line": line_number, "reason": "chain_discontinuity", "event_id": event_id, "expected_previous_hash": previous_accepted, "observed_previous_hash": event.get("previous_hash")})
        seen.add(event_id)
        events.append(event)
        previous_accepted = event["record_hash"]
    return events, corrupt


def validate_event_input(event: dict[str, Any], existing: list[dict[str, Any]]) -> None:
    required = {"event_id", "learner_id", "occurred_at", "event_type", "interaction_id", "payload"}
    missing = sorted(required - event.keys())
    if missing:
        raise ValueError("missing event fields: " + ", ".join(missing))
    if event["event_type"] not in ALLOWED_EVENT_TYPES:
        raise ValueError(f"unsupported event_type: {event['event_type']}")
    if any(item["event_id"] == event["event_id"] for item in existing):
        raise ValueError(f"duplicate event_id: {event['event_id']}")
    parse_datetime(event["occurred_at"])
    if not isinstance(event["payload"], dict):
        raise ValueError("payload must be an object")
    if event["event_type"] == "confidence_recorded":
        value = event["payload"].get("confidence")
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= value <= 1:
            raise ValueError("confidence must be a number from 0 to 1")
    if event["event_type"] in {"answer_submitted", "review_completed"}:
        if not event.get("capsule_id") or not event.get("concept_id"):
            raise ValueError("answer/review events require capsule_id and concept_id")
        if event["payload"].get("result") not in {"correct", "incorrect"}:
            raise ValueError("answer/review payload.result must be correct or incorrect")
        if event["payload"].get("movement_candidate"):
            if event["payload"].get("retrieval_quality") not in {"robust", "fragile", "guessed"}:
                raise ValueError("movement evidence requires retrieval_quality")
            if not isinstance(event["payload"].get("independent"), bool):
                raise ValueError("movement evidence requires independent boolean")
            if event["payload"].get("hint_level") not in {"none", "minor", "decisive"}:
                raise ValueError("movement evidence requires hint_level")
    if event["event_type"] == "review_completed":
        if event["payload"].get("retrieval_quality") not in {"robust", "fragile", "guessed"}:
            raise ValueError("review payload.retrieval_quality must be robust, fragile or guessed")
        if not isinstance(event["payload"].get("independent"), bool):
            raise ValueError("review payload.independent must be boolean")
        if event["payload"].get("hint_level") not in {"none", "minor", "decisive"}:
            raise ValueError("review payload.hint_level must be none, minor or decisive")
    if event["event_type"] == "feedback_shown":
        prior_confidence = any(
            item["interaction_id"] == event["interaction_id"] and item["event_type"] == "confidence_recorded"
            for item in existing
        )
        if not prior_confidence and event["payload"].get("confidence_declined") is not True:
            raise ValueError("record confidence before feedback, or set confidence_declined=true")
    parent_event_id = event.get("parent_event_id")
    parent_event = next((item for item in existing if item["event_id"] == parent_event_id), None)
    if parent_event_id is not None and parent_event is None:
        raise ValueError("parent_event_id must reference an earlier event")
    if event["event_type"] == "review_completed":
        expected_key = "|".join([event["learner_id"], event["capsule_id"], event["concept_id"]])
        if event.get("review_task_id") != expected_key:
            raise ValueError("review_completed requires the stable review_task_id")
        if parent_event_id is None:
            raise ValueError("review_completed requires parent_event_id")
        if parent_event["event_type"] not in {"answer_submitted", "review_completed"}:
            raise ValueError("review parent must be an answer_submitted or review_completed event")
        for field in ("learner_id", "capsule_id", "concept_id"):
            if parent_event.get(field) != event.get(field):
                raise ValueError(f"review parent must have the same {field}")
        parent_key = parent_event.get("review_task_id") or "|".join(
            [parent_event["learner_id"], parent_event["capsule_id"], parent_event["concept_id"]]
        )
        if parent_key != expected_key:
            raise ValueError("review parent must belong to the same review task")


def append_event(state_dir: Path, event: dict[str, Any]) -> dict[str, Any]:
    init_state(state_dir)
    existing = read_events(state_dir)
    validate_event_input(event, existing)
    stored = {
        "schema_version": SCHEMA_VERSION,
        "event_id": event["event_id"],
        "learner_id": event["learner_id"],
        "occurred_at": format_datetime(parse_datetime(event["occurred_at"])),
        "event_type": event["event_type"],
        "interaction_id": event["interaction_id"],
        "capsule_id": event.get("capsule_id"),
        "concept_id": event.get("concept_id"),
        "parent_event_id": event.get("parent_event_id"),
        "review_task_id": event.get("review_task_id"),
        "payload": event["payload"],
        "previous_hash": existing[-1]["record_hash"] if existing else None,
    }
    stored["record_hash"] = sha256_bytes(canonical_json(stored).encode("utf-8"))
    with (state_dir / "events.jsonl").open("a", encoding="utf-8", newline="") as handle:
        handle.write(canonical_json(stored) + "\n")
    return stored


def project_reviews(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    tasks: dict[str, dict[str, Any]] = {}
    for event in events:
        if event["event_type"] not in {"answer_submitted", "review_completed"}:
            continue
        key = event.get("review_task_id") or "|".join([event["learner_id"], event["capsule_id"], event["concept_id"]])
        occurred = parse_datetime(event["occurred_at"])
        result = event["payload"]["result"]
        robust_independent = (
            result == "correct"
            and event["payload"].get("retrieval_quality") == "robust"
            and event["payload"].get("independent") is True
            and event["payload"].get("hint_level") == "none"
        )
        status = "scheduled"
        if event["event_type"] == "answer_submitted" or result == "incorrect" or key not in tasks:
            stage = 0
        elif robust_independent:
            if tasks[key]["stage"] == 2:
                stage = 2
                status = "completed"
            else:
                stage = tasks[key]["stage"] + 1
        else:
            stage = tasks[key]["stage"]
        due = None if status == "completed" else occurred + INTERVALS[stage]
        tasks[key] = {
            "schema_version": SCHEMA_VERSION,
            "review_key": key,
            "learner_id": event["learner_id"],
            "capsule_id": event["capsule_id"],
            "concept_id": event["concept_id"],
            "stage": stage,
            "status": status,
            "due_at": format_datetime(due) if due else None,
            "source_event_id": event["event_id"],
        }
    return [tasks[key] for key in sorted(tasks)]


def project_hypotheses(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        movement = event.get("payload", {}).get("movement_candidate")
        if movement and event["event_type"] in {"answer_submitted", "review_completed"}:
            groups[(event["learner_id"], movement)].append(event)
    hypotheses = []
    for (learner_id, movement), evidence in sorted(groups.items()):
        independent = [
            item
            for item in evidence
            if item["payload"].get("independent") is True
            and item["payload"].get("hint_level") == "none"
            and item["payload"].get("retrieval_quality") == "robust"
        ]
        contexts = {
            item["payload"].get("transfer_context") or item.get("concept_id")
            for item in independent
            if item["payload"].get("transfer_context") or item.get("concept_id")
        }
        has_valid_transfer = any(item["payload"].get("transfer_valid") is True for item in independent)
        valid_transfer_count = sum(item["payload"].get("transfer_valid") is True for item in independent)
        status = "confirmed" if len(independent) >= 2 and len(contexts) >= 2 and has_valid_transfer else "candidate"
        hypotheses.append(
            {
                "schema_version": SCHEMA_VERSION,
                "hypothesis_id": f"hypothesis:{learner_id}:{movement}",
                "learner_id": learner_id,
                "movement": movement,
                "status": status,
                "evidence_event_ids": [item["event_id"] for item in evidence],
                "independent_context_count": len(contexts),
                "valid_transfer_count": valid_transfer_count,
                "updated_at": max(item["occurred_at"] for item in evidence),
            }
        )
    return hypotheses


def calibration(events: list[dict[str, Any]], minimum: int = 10, corrupt_count: int = 0) -> dict[str, Any]:
    confidences: dict[str, float] = {}
    outcomes: dict[str, tuple[int, bool]] = {}
    for event in events:
        if event["event_type"] == "confidence_recorded":
            confidences[event["interaction_id"]] = float(event["payload"]["confidence"])
        elif event["event_type"] in {"answer_submitted", "review_completed"}:
            independent = (
                event["payload"].get("independent") is True
                and event["payload"].get("hint_level") == "none"
            )
            outcomes[event["interaction_id"]] = (1 if event["payload"]["result"] == "correct" else 0, independent)
    common = set(confidences) & set(outcomes)
    paired = sorted(key for key in common if outcomes[key][1])
    exclusions = {
        "outcome_without_confidence": len(set(outcomes) - set(confidences)),
        "confidence_without_outcome": len(set(confidences) - set(outcomes)),
        "assisted_or_nonindependent": len(common) - len(paired),
        "corrupt_records": corrupt_count,
    }
    if len(paired) < minimum:
        return {"status": "insufficient_data", "sample_size": len(paired), "minimum": minimum, "exclusions": exclusions}
    brier = sum((confidences[key] - outcomes[key][0]) ** 2 for key in paired) / len(paired)
    bias = sum(confidences[key] - outcomes[key][0] for key in paired) / len(paired)
    bin_specs = [(0.0, 0.25), (0.25, 0.5), (0.5, 0.75), (0.75, 1.0000001)]
    bins = []
    for lower, upper in bin_specs:
        members = [key for key in paired if lower <= confidences[key] < upper]
        bins.append(
            {
                "range": f"{lower:.2f}-{min(upper, 1.0):.2f}",
                "n": len(members),
                "mean_confidence": round(sum(confidences[key] for key in members) / len(members), 6) if members else None,
                "accuracy": round(sum(outcomes[key][0] for key in members) / len(members), 6) if members else None,
            }
        )
    return {
        "status": "available",
        "sample_size": len(paired),
        "minimum": minimum,
        "brier_score": round(brier, 6),
        "mean_confidence_bias": round(bias, 6),
        "exclusions": exclusions,
        "bins": bins,
    }


def write_projections(state_dir: Path) -> None:
    events, corrupt = read_events_tolerant(state_dir)
    tasks = project_reviews(events)
    fieldnames = ["schema_version", "review_key", "learner_id", "capsule_id", "concept_id", "stage", "status", "due_at", "source_event_id"]
    from io import StringIO

    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(tasks)
    atomic_write(state_dir / "review_tasks.csv", output.getvalue())
    atomic_write(
        state_dir / "learner_hypotheses.json",
        json.dumps({"schema_version": SCHEMA_VERSION, "hypotheses": project_hypotheses(events)}, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    atomic_write(
        state_dir / "calibration.json",
        json.dumps(calibration(events, corrupt_count=len(corrupt)), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    atomic_write(
        state_dir / "corrupt_records.json",
        json.dumps({"schema_version": SCHEMA_VERSION, "count": len(corrupt), "records": corrupt}, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )


def export_events_csv(state_dir: Path, destination: Path) -> None:
    events = read_events(state_dir)
    fieldnames = ["schema_version", "event_id", "learner_id", "occurred_at", "event_type", "interaction_id", "capsule_id", "concept_id", "parent_event_id", "review_task_id", "payload_json", "previous_hash", "record_hash"]
    from io import StringIO

    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for event in events:
        row = {key: event.get(key) for key in fieldnames if key != "payload_json"}
        row["payload_json"] = canonical_json(event["payload"])
        writer.writerow(row)
    atomic_write(destination, output.getvalue())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=Path(".p7-state"))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    append = sub.add_parser("append")
    append.add_argument("--event-json", required=True)
    sub.add_parser("validate")
    sub.add_parser("project")
    export = sub.add_parser("export-csv")
    export.add_argument("destination", type=Path)
    args = parser.parse_args()
    state_dir = args.state_dir.resolve()
    if args.command == "init":
        init_state(state_dir)
    elif args.command == "append":
        print(canonical_json(append_event(state_dir, json.loads(args.event_json))))
    elif args.command == "validate":
        events = read_events(state_dir)
        print(f"valid ledger: {len(events)} events")
    elif args.command == "project":
        init_state(state_dir)
        write_projections(state_dir)
        print(f"projections updated in {state_dir}")
    elif args.command == "export-csv":
        export_events_csv(state_dir, args.destination.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
