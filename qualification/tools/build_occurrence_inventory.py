#!/usr/bin/env python3
"""Build the v1.5.0 deterministic occurrence-to-disposition inventory.

This is deliberately an *inventory* tool, not a clinical adjudicator.  It
consumes the frozen detector's primary denominator and gives every detector
occurrence exactly one auditable destination.  Existing registry records are
only referenced read-only; all otherwise-unlinked occurrences become named
candidate claims with ``clinical_validity: pending``.  No candidate is promoted
to ``current`` by text similarity or plausibility.

Candidate clustering is intentionally narrower than ordinary de-duplication:
two candidates are equivalent only when their category and normalized source
text are identical after whitespace/Markdown-punctuation normalization.  Thus a
different number, unit, route, population, context, timing, or jurisdiction is
never auto-merged.  The expected cost is false splits, which are safer than a
false merge before clinical adjudication.

Usage:
    python qualification/tools/build_occurrence_inventory.py \
      --detections qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv \
      --claims p7-study-skill/registry/clinical_claims.jsonl \
      --out qualification/reports/v1.5.0
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = "1.5.0-inventory.1"
INPUT_SCHEMA_VERSION = "critical-claim-scan/1.4.0"

SENSITIVE_NUMERIC_RE = re.compile(
    r"\b\d+(?:[.,]\d+)?\s*(?:mg/kg/dia|mcg/kg/min|mg/kg|mcg/kg|ml/kg|"
    r"mg/dl|mg/l|g/dl|mmol/l|meq/l|ng/ml|pg/ml|mg/m2|ui/kg|cmh2o|"
    r"mg|mcg|µg|g|kg|ml|mmhg|mmol|meq|ui|%|h|horas|min|minutos|dias|"
    r"semanas|meses|anos)\b|\b\d+(?:[.,]\d+)?\b",
    re.IGNORECASE,
)
ROUTE_RE = re.compile(
    r"\b(?:via oral|endovenos[ao]|intravenos[ao]|intramuscular|subcutane[ao]|"
    r"intraosse[ao]|sublingual|inalatori[ao]|nebuliz(?:acao|acao)|retal|"
    r"intranasal|intratecal|topic[ao]|\bev\b|\biv\b|\bim\b|\bvo\b|\bsc\b|\bsl\b)",
    re.IGNORECASE,
)
POPULATION_RE = re.compile(
    r"\b(?:recem-nascid[oa]s?|rn\b|neonat[oa]s?|lactentes?|criancas?|"
    r"pediatric[oa]s?|adolescentes?|adultos?|idosos?|gestantes?|gravidez|"
    r"puérperas?|puerperas?|lactantes?|imunossuprimid[oa]s?)\b",
    re.IGNORECASE,
)
CONTEXT_RE = re.compile(
    r"\b(?:emergencia|urgencia|uti|cti|ambulatori[oa]|internacao|alta|"
    r"pre-operatori[oa]|pos-operatori[oa]|agud[oa]|cronico|primeira linha|"
    r"segunda linha|terceira linha|refratari[oa])\b",
    re.IGNORECASE,
)
JURISDICTION_RE = re.compile(
    r"\b(?:brasil|sus|pni|anvisa|cfm|ministerio da saude|oms|who|nice|"
    r"idsa|gina|aha|asa|ada|sbp|sbc|sbd)\b",
    re.IGNORECASE,
)
WORD_RE = re.compile(r"[a-zA-ZÀ-ÿ]+")


def stable_id(prefix: str, *parts: str) -> str:
    digest = hashlib.sha256("\u241f".join(parts).encode("utf-8")).hexdigest()[:20]
    return f"{prefix}:{digest}"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_accents(text: str) -> str:
    return "".join(
        char for char in unicodedata.normalize("NFD", text)
        if unicodedata.category(char) != "Mn"
    )


def normalized_text(text: str) -> str:
    """Only normalize formatting.  Do not abstract clinical content."""
    value = strip_accents(text).lower().replace("×", "x")
    value = value.replace("|", " ")
    value = re.sub(r"[*_`#]", " ", value)
    # Sentence punctuation and table formatting are not material.  A decimal
    # separator is material, so punctuation between two digits is preserved.
    value = re.sub(r"(?<!\d)[,.;:!?]+|[,.;:!?]+(?!\d)", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def unique_matches(pattern: re.Pattern[str], text: str) -> list[str]:
    return sorted({normalized_text(match.group(0)) for match in pattern.finditer(text)})


def sensitive_signature(text: str) -> dict[str, list[str]]:
    """Expose material discriminators; unknown is never inferred as equal."""
    return {
        "numeric_values": unique_matches(SENSITIVE_NUMERIC_RE, text),
        "routes": unique_matches(ROUTE_RE, text),
        "population_markers": unique_matches(POPULATION_RE, text),
        "context_markers": unique_matches(CONTEXT_RE, text),
        "jurisdiction_markers": unique_matches(JURISDICTION_RE, text),
    }


def candidate_key(row: dict[str, str]) -> str:
    # Exact textual identity is the primary guard.  The signature is included
    # explicitly so a future relaxation cannot silently merge material changes.
    signature = json.dumps(sensitive_signature(row["text"]), ensure_ascii=False, sort_keys=True)
    return "\u241f".join((row["category"], normalized_text(row["text"]), signature))


def parse_bool(value: str) -> bool:
    return value.strip().lower() == "true"


def load_primary_occurrences(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if parse_bool(row["in_sweep_denominator"])]
    ids = [row["detection_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("detection_id is not unique in the primary denominator")
    return sorted(rows, key=lambda row: row["detection_id"])


def load_registry(path: Path) -> dict[str, dict[str, Any]]:
    registry: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            claim_id = record["claim_id"]
            if claim_id in registry:
                raise ValueError(f"duplicate registry claim_id: {claim_id}")
            registry[claim_id] = record
    return registry


def linked_claim_ids(row: dict[str, str], registry: dict[str, dict[str, Any]]) -> list[str]:
    ids = sorted({value for value in row["linked_claim_ids"].split() if value})
    missing = [claim_id for claim_id in ids if claim_id not in registry]
    if missing:
        raise ValueError(f"detector links missing registry claims: {missing}")
    return ids


def occurrence_record(row: dict[str, str], detections_sha256: str) -> dict[str, Any]:
    """A lossless ClaimOccurrence projection of the frozen detector row."""
    return {
        "schema_version": SCHEMA_VERSION,
        "record_type": "ClaimOccurrence",
        "detection_id": row["detection_id"],
        "detector": {"schema_version": INPUT_SCHEMA_VERSION, "input_sha256": detections_sha256},
        "capsule": {"capsule_id": row["capsule_id"], "path": row["capsule_path"]},
        "locator": {"line_no": int(row["line_no"]), "section": row["section"], "source": row["source"]},
        "text": row["text"],
        "category": row["category"],
        "tier": row["tier"],
        "risk": row["risk"],
        "discipline": row["discipline"],
        "section_class": row["section_class"],
        "entry_reason": "frozen_detector_primary_denominator",
        "scanner_link": {
            "linked_claim_ids": row["linked_claim_ids"].split(),
            "link_basis": row["link_basis"],
            "resolved": parse_bool(row["resolved"]),
        },
    }


def registry_reference(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "record_type": "CanonicalClinicalClaimReference",
        "claim_id": record["claim_id"],
        "origin": "read_only_registry_reference",
        "statement": record.get("statement", ""),
        "capsule_id": record.get("capsule_id", ""),
        "claim_type": record.get("claim_type", ""),
        "criticality": record.get("criticality", ""),
        "clinical_validity": record.get("states", {}).get("clinical_validity", "unknown"),
        "registry_record_sha256": hashlib.sha256(
            json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }


def candidate_claim(candidate_id: str, key: str, members: list[dict[str, str]]) -> dict[str, Any]:
    representative = min(
        members,
        key=lambda row: (row["capsule_path"], int(row["line_no"]), row["detection_id"]),
    )
    signature = sensitive_signature(representative["text"])
    return {
        "schema_version": SCHEMA_VERSION,
        "record_type": "CanonicalClinicalClaimCandidate",
        "claim_id": candidate_id,
        "origin": "candidate_from_unlinked_detector_occurrence",
        "equivalence_policy": "exact_normalized_text_and_sensitive_signature",
        "equivalence_key_sha256": hashlib.sha256(key.encode("utf-8")).hexdigest(),
        "normalized_statement": normalized_text(representative["text"]),
        "representative_statement": representative["text"],
        "category": representative["category"],
        "sensitive_signature": signature,
        "population": signature["population_markers"] or ["unknown_not_inferred"],
        "scenario_context": signature["context_markers"] or ["unknown_not_inferred"],
        "jurisdiction": signature["jurisdiction_markers"] or ["unknown_not_inferred"],
        "clinical_validity": "pending",
        "adjudication_state": "not_adjudicated",
        "practice_current_eligibility": "blocked",
        "candidate_reason": "no_unique_existing_registry_claim_link",
        "occurrence_count": len(members),
        "occurrence_ids": [row["detection_id"] for row in sorted(members, key=lambda item: item["detection_id"])],
    }


def build_inventory(
    rows: list[dict[str, str]], registry: dict[str, dict[str, Any]], detections_sha256: str
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    occurrences = [occurrence_record(row, detections_sha256) for row in rows]
    candidate_members: dict[str, list[dict[str, str]]] = defaultdict(list)
    dispositions_by_id: dict[str, dict[str, Any]] = {}

    for row in rows:
        links = linked_claim_ids(row, registry)
        if len(links) == 1:
            dispositions_by_id[row["detection_id"]] = {
                "schema_version": SCHEMA_VERSION,
                "record_type": "OccurrenceDisposition",
                "detection_id": row["detection_id"],
                "disposition": "canonical_claim",
                "target_claim_id": links[0],
                "target_origin": "read_only_registry_reference",
                "decision_basis": "unique_inherited_detector_registry_link",
                "link_evidence": row["link_basis"],
                "clinical_adjudication": "not_performed_by_inventory_pipeline",
            }
            continue

        key = candidate_key(row)
        candidate_members[key].append(row)
        dispositions_by_id[row["detection_id"]] = {
            "schema_version": SCHEMA_VERSION,
            "record_type": "OccurrenceDisposition",
            "detection_id": row["detection_id"],
            "disposition": "candidate_claim_pending",
            "target_claim_id": "",  # filled once stable candidate IDs are assigned
            "target_origin": "candidate_inventory",
            "decision_basis": (
                "no_detector_registry_link" if not links
                else "ambiguous_detector_registry_link_not_auto_resolved"
            ),
            "link_evidence": row["link_basis"],
            "clinical_adjudication": "not_performed_by_inventory_pipeline",
        }

    candidates: list[dict[str, Any]] = []
    key_to_id: dict[str, str] = {}
    for key in sorted(candidate_members):
        candidate_id = stable_id("candidate-claim", key)
        key_to_id[key] = candidate_id
        candidates.append(candidate_claim(candidate_id, key, candidate_members[key]))

    for key, members in candidate_members.items():
        for row in members:
            dispositions_by_id[row["detection_id"]]["target_claim_id"] = key_to_id[key]

    dispositions = [dispositions_by_id[row["detection_id"]] for row in rows]
    canonical = [registry_reference(registry[claim_id]) for claim_id in sorted(registry)] + candidates
    canonical.sort(key=lambda record: record["claim_id"])
    return occurrences, dispositions, canonical, candidates


def lexical_tokens(text: str) -> set[str]:
    masked = SENSITIVE_NUMERIC_RE.sub(" ", normalized_text(text))
    return {token for token in WORD_RE.findall(masked) if len(token) > 2}


def jaccard(left: set[str], right: set[str]) -> float:
    union = left | right
    return len(left & right) / len(union) if union else 0.0


def negative_merge_sample(rows: list[dict[str, str]], limit: int = 24) -> list[dict[str, Any]]:
    """Find similar-looking pairs rejected because material fields differ.

    This is an audit sample, not the criterion used for clustering.  Pairs are
    sorted deterministically by lexical resemblance then IDs.
    """
    signatures = {row["detection_id"]: sensitive_signature(row["text"]) for row in rows}
    token_sets = {row["detection_id"]: lexical_tokens(row["text"]) for row in rows}
    row_by_id = {row["detection_id"]: row for row in rows}
    # Candidate pairs come from a bounded inverted index rather than an O(n²)
    # scan of a large category.  The sample is evidence of rejected merges, not
    # a prevalence estimate; bounded deterministic selection is enough and
    # keeps the inventory practical in CI.
    seen_by_token: dict[tuple[str, str], list[str]] = defaultdict(list)
    candidate_pairs: set[tuple[str, str]] = set()
    for row in sorted(rows, key=lambda item: item["detection_id"]):
        row_id = row["detection_id"]
        for token in sorted(token_sets[row_id]):
            bucket = seen_by_token[(row["category"], token)]
            # Three preceding matches per token cap the audit sampler while
            # retaining lexical near-neighbours across the full corpus.
            for prior_id in bucket:
                candidate_pairs.add(tuple(sorted((prior_id, row_id))))
            if len(bucket) < 3:
                bucket.append(row_id)

    candidates: list[tuple[float, str, str, dict[str, Any]]] = []
    for left_id, right_id in sorted(candidate_pairs):
        left, right = row_by_id[left_id], row_by_id[right_id]
        if left["category"] != right["category"]:
            continue
        left_signature = signatures[left_id]
        right_signature = signatures[right_id]
        differing = [field for field in sorted(left_signature) if left_signature[field] != right_signature[field]]
        if not differing:
            continue
        score = jaccard(token_sets[left_id], token_sets[right_id])
        if score < 0.35:
            continue
        record = {
            "schema_version": SCHEMA_VERSION,
            "sample_type": "negative_merge",
            "category": left["category"],
            "left_detection_id": left_id,
            "right_detection_id": right_id,
            "lexical_jaccard_without_numbers": round(score, 6),
            "rejected_merge_reason": "different_sensitive_signature",
            "differing_sensitive_fields": differing,
            "left_signature": left_signature,
            "right_signature": right_signature,
            "left_text": left["text"],
            "right_text": right["text"],
        }
        candidates.append((score, left_id, right_id, record))
    candidates.sort(key=lambda item: (-item[0], item[1], item[2]))
    return [record for _, _, _, record in candidates[:limit]]


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def validate_inventory(
    rows: list[dict[str, str]],
    occurrences: list[dict[str, Any]],
    dispositions: list[dict[str, Any]],
    canonical: list[dict[str, Any]],
) -> dict[str, int]:
    expected = {row["detection_id"] for row in rows}
    occurrence_ids = {row["detection_id"] for row in occurrences}
    disposition_ids = {row["detection_id"] for row in dispositions}
    targets = {row["claim_id"] for row in canonical}
    if occurrence_ids != expected or len(occurrences) != len(expected):
        raise ValueError("ClaimOccurrence coverage is not exactly one per detector occurrence")
    if disposition_ids != expected or len(dispositions) != len(expected):
        raise ValueError("OccurrenceDisposition coverage is not exactly one per detector occurrence")
    if any(not row["target_claim_id"] for row in dispositions):
        raise ValueError("anonymous pending occurrence found")
    if any(row["target_claim_id"] not in targets for row in dispositions):
        raise ValueError("OccurrenceDisposition target is absent from canonical inventory")
    return {
        "occurrences": len(occurrences),
        "dispositions": len(dispositions),
        "targets": len(targets),
    }


def build_summary(
    rows: list[dict[str, str]],
    dispositions: list[dict[str, Any]],
    canonical: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
    negative_sample: list[dict[str, Any]],
    detections_sha256: str,
    claims_sha256: str,
) -> dict[str, Any]:
    by_disposition = Counter(row["disposition"] for row in dispositions)
    disposition_by_risk: dict[str, dict[str, int]] = {}
    row_by_id = {row["detection_id"]: row for row in rows}
    for risk in sorted({row["risk"] for row in rows}):
        mine = [d for d in dispositions if row_by_id[d["detection_id"]]["risk"] == risk]
        disposition_by_risk[risk] = dict(sorted(Counter(d["disposition"] for d in mine).items()))
    candidate_high_risk = sum(
        1 for candidate in candidates
        if any(row_by_id[detection_id]["risk"] == "high" for detection_id in candidate["occurrence_ids"])
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "purpose": "structural_inventory_and_conservative_candidate_clustering_only",
        "input": {
            "detector_schema_version": INPUT_SCHEMA_VERSION,
            "detections_sha256": detections_sha256,
            "claims_registry_sha256": claims_sha256,
        },
        "coverage": {
            "primary_occurrences_total": len(rows),
            "primary_occurrences_accounted": len(dispositions),
            "primary_occurrences_unaccounted": len(rows) - len(dispositions),
            "high_risk_occurrences_total": sum(row["risk"] == "high" for row in rows),
            "high_risk_occurrences_accounted": sum(
                row_by_id[item["detection_id"]]["risk"] == "high" for item in dispositions
            ),
            "high_risk_occurrences_unaccounted": 0,
        },
        "dispositions": {
            "by_type": dict(sorted(by_disposition.items())),
            "by_risk": disposition_by_risk,
            "anonymous_unregistered_pending": 0,
        },
        "canonical_targets": {
            "total": len(canonical),
            "registry_references": sum(row["origin"] == "read_only_registry_reference" for row in canonical),
            "candidate_pending_claims": len(candidates),
            "candidate_pending_claims_with_high_risk_occurrence": candidate_high_risk,
        },
        "candidate_clustering": {
            "policy": "exact_normalized_text_and_sensitive_signature",
            "candidate_clusters": len(candidates),
            "candidate_occurrences": by_disposition["candidate_claim_pending"],
            "clusters_with_multiple_occurrences": sum(item["occurrence_count"] > 1 for item in candidates),
            "negative_merge_sample_count": len(negative_sample),
        },
        "limitations": [
            "This inventory does not adjudicate clinical correctness, currentness, source quality, or harm tier.",
            "A unique inherited detector link is preserved as a registry reference, not revalidated as material clinical equivalence.",
            "Ambiguous detector links (two or more registry IDs) are deliberately routed to named pending candidates rather than arbitrarily choosing a claim.",
            "Exact-text clustering intentionally produces false splits for paraphrases, formatting variants, and semantically equivalent statements; clinical adjudication may merge them later with evidence.",
            "Pending candidates are blocked from current-practice promotion until a separate adjudication workstream supplies evidence.",
        ],
    }


def render_report(summary: dict[str, Any]) -> str:
    coverage = summary["coverage"]
    dispositions = summary["dispositions"]
    targets = summary["canonical_targets"]
    clusters = summary["candidate_clustering"]
    return "\n".join(
        [
            "# INVENTORY_CLUSTERING_REPORT — P7 v1.5.0",
            "",
            "## Deterministic result",
            "",
            f"- Primary occurrence coverage: **{coverage['primary_occurrences_accounted']}/{coverage['primary_occurrences_total']}**.",
            f"- High-risk occurrence coverage: **{coverage['high_risk_occurrences_accounted']}/{coverage['high_risk_occurrences_total']}**.",
            f"- Anonymous `unregistered_pending`: **{dispositions['anonymous_unregistered_pending']}**.",
            f"- Destinations: `canonical_claim`={dispositions['by_type'].get('canonical_claim', 0)}; "
            f"`candidate_claim_pending`={dispositions['by_type'].get('candidate_claim_pending', 0)}.",
            f"- Canonical targets in this inventory: {targets['total']} "
            f"({targets['registry_references']} read-only registry references; "
            f"{targets['candidate_pending_claims']} named pending candidates).",
            f"- Conservative candidate clusters: {clusters['candidate_clusters']}; "
            f"multi-occurrence clusters: {clusters['clusters_with_multiple_occurrences']}.",
            f"- Negative merge audit sample: {clusters['negative_merge_sample_count']} pairs.",
            "",
            "## Policy",
            "",
            "Candidate claims are grouped only when category, normalized source text, and the extracted sensitive signature are identical. "
            "The signature records numeric values, route, population markers, context markers, and jurisdiction markers. "
            "Any difference prevents an automatic merge. This is deliberately a false-split-biased policy.",
            "",
            "A uniquely inherited detector link is retained as a read-only registry reference. Zero or multiple inherited links become a named "
            "candidate claim with `clinical_validity: pending`, `adjudication_state: not_adjudicated`, and `practice_current_eligibility: blocked`. "
            "This pipeline does not edit `clinical_claims.jsonl` and does not promote any claim to `current`.",
            "",
            "## Files",
            "",
            "- `CLAIM_OCCURRENCES.jsonl`: lossless primary-denominator occurrence records.",
            "- `OCCURRENCE_DISPOSITIONS.jsonl`: one unique destination per `detection_id`.",
            "- `CANONICAL_CLINICAL_CLAIMS.jsonl`: read-only registry references plus named pending candidates.",
            "- `CANDIDATE_CLAIM_CLUSTERS.csv`: candidate cluster index.",
            "- `NEGATIVE_MERGE_SAMPLE.jsonl`: similar lexical pairs deliberately not merged.",
            "",
            "## Limits",
            "",
            *[f"- {item}" for item in summary["limitations"]],
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--detections", type=Path, default=Path("qualification/reports/CRITICAL_CLAIM_DETECTIONS.csv"))
    parser.add_argument("--claims", type=Path, default=Path("p7-study-skill/registry/clinical_claims.jsonl"))
    parser.add_argument("--out", type=Path, default=Path("qualification/reports/v1.5.0"))
    args = parser.parse_args()

    detections = args.detections.resolve()
    claims = args.claims.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    rows = load_primary_occurrences(detections)
    registry = load_registry(claims)
    occurrences, dispositions, canonical, candidates = build_inventory(rows, registry, sha256_file(detections))
    validate_inventory(rows, occurrences, dispositions, canonical)
    negative_sample = negative_merge_sample(rows)
    summary = build_summary(
        rows, dispositions, canonical, candidates, negative_sample, sha256_file(detections), sha256_file(claims)
    )

    write_jsonl(out / "CLAIM_OCCURRENCES.jsonl", occurrences)
    write_jsonl(out / "OCCURRENCE_DISPOSITIONS.jsonl", dispositions)
    write_jsonl(out / "CANONICAL_CLINICAL_CLAIMS.jsonl", canonical)
    write_jsonl(out / "NEGATIVE_MERGE_SAMPLE.jsonl", negative_sample)
    write_csv(
        out / "CANDIDATE_CLAIM_CLUSTERS.csv",
        [
            {
                "claim_id": item["claim_id"],
                "category": item["category"],
                "occurrence_count": item["occurrence_count"],
                "clinical_validity": item["clinical_validity"],
                "practice_current_eligibility": item["practice_current_eligibility"],
                "normalized_statement": item["normalized_statement"],
                "numeric_values": " ; ".join(item["sensitive_signature"]["numeric_values"]),
                "routes": " ; ".join(item["sensitive_signature"]["routes"]),
                "population_markers": " ; ".join(item["sensitive_signature"]["population_markers"]),
                "context_markers": " ; ".join(item["sensitive_signature"]["context_markers"]),
                "jurisdiction_markers": " ; ".join(item["sensitive_signature"]["jurisdiction_markers"]),
            }
            for item in candidates
        ],
        [
            "claim_id", "category", "occurrence_count", "clinical_validity", "practice_current_eligibility",
            "normalized_statement", "numeric_values", "routes", "population_markers", "context_markers",
            "jurisdiction_markers",
        ],
    )
    write_json(out / "INVENTORY_CLUSTERING_SUMMARY.json", summary)
    (out / "INVENTORY_CLUSTERING_REPORT.md").write_text(render_report(summary), encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
