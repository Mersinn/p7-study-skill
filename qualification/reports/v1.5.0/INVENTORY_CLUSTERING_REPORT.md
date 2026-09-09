# INVENTORY_CLUSTERING_REPORT — P7 v1.5.0

## Deterministic result

- Primary occurrence coverage: **3602/3602**.
- High-risk occurrence coverage: **2817/2817**.
- Anonymous `unregistered_pending`: **0**.
- Destinations: `canonical_claim`=66; `candidate_claim_pending`=3536.
- Canonical targets in this inventory: 3588 (52 read-only registry references; 3536 named pending candidates).
- Conservative candidate clusters: 3536; multi-occurrence clusters: 0.
- Negative merge audit sample: 24 pairs.

## Policy

Candidate claims are grouped only when category, normalized source text, and the extracted sensitive signature are identical. The signature records numeric values, route, population markers, context markers, and jurisdiction markers. Any difference prevents an automatic merge. This is deliberately a false-split-biased policy.

A uniquely inherited detector link is retained as a read-only registry reference. Zero or multiple inherited links become a named candidate claim with `clinical_validity: pending`, `adjudication_state: not_adjudicated`, and `practice_current_eligibility: blocked`. This pipeline does not edit `clinical_claims.jsonl` and does not promote any claim to `current`.

## Files

- `CLAIM_OCCURRENCES.jsonl`: lossless primary-denominator occurrence records.
- `OCCURRENCE_DISPOSITIONS.jsonl`: one unique destination per `detection_id`.
- `CANONICAL_CLINICAL_CLAIMS.jsonl`: read-only registry references plus named pending candidates.
- `CANDIDATE_CLAIM_CLUSTERS.csv`: candidate cluster index.
- `NEGATIVE_MERGE_SAMPLE.jsonl`: similar lexical pairs deliberately not merged.

## Limits

- This inventory does not adjudicate clinical correctness, currentness, source quality, or harm tier.
- A unique inherited detector link is preserved as a registry reference, not revalidated as material clinical equivalence.
- Ambiguous detector links (two or more registry IDs) are deliberately routed to named pending candidates rather than arbitrarily choosing a claim.
- Exact-text clustering intentionally produces false splits for paraphrases, formatting variants, and semantically equivalent statements; clinical adjudication may merge them later with evidence.
- Pending candidates are blocked from current-practice promotion until a separate adjudication workstream supplies evidence.
