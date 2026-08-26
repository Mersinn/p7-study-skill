# Active study — question-first view

This is the complete delivery contract for the **first intervention** in
active study mode. It is intentionally self-contained: the executor can
produce the first response from this file without reading or reconstructing
the post-attempt reveal view.

## When to use this view

Use it for `Estudar Tema`, `quero estudar`, `vamos estudar`, `quero
praticar/testar` or `quero aprender ativamente`, unless the learner explicitly
asks for exposition first (`explique`, `resuma`, `faça uma revisão expositiva`,
`ensine primeiro e teste depois`). Do not ask a routing question when the
intent is already clear.

## First response contract

Before the learner attempts anything, deliver only these elements, in this
order:

1. why the topic matters for the active target;
2. how it tends to appear in the assessment;
3. the minimum operational concept, limited to the **type of decision** the
   learner must make; it must not contain the answer or any treatment name,
   drug, dose, cutoff, classification label, protocol sequence, or completed
   diagnostic conclusion that resolves the item;
4. the clinical or decision pivot as an **open question** — name the decisive
   variable, but do not apply it to the case or reveal the filled cutoff/table;
5. exactly **one** active question or mini-case without a visible solution.

End immediately after item 5 and wait. The first intervention must not contain
the answer, applied pivot, **any treatment names or treatment sequence**, doses, cutoffs, traps,
distractors, cards, or a stopping rubric that gives away the solution. Do not
load or quote `ACTIVE_STUDY_REVEAL_AFTER_ATTEMPT.md` or equivalent reveal-only
capsule fields for this intervention.

The question must be answerable from the minimum concept and the available
source context. If the source is weak or conflicted, label that limitation;
do not compensate by revealing the solution.

Pre-send check: if a learner could copy a clinical statement from the preamble
as the answer to item 5, delete that statement and keep it for the post-attempt
view. A multiple-choice option may contain treatment names when needed, but the
preamble must not endorse one option or restate the correct sequence.

## Transition rule

The gate opens only after the learner submits an attempt, says they do not
know, or explicitly requests exposition. A declaration of `não sei` is still a
response event, but it is not evidence of mastery. If the learner explicitly
requested exposition before practice, the reveal view may be used immediately,
but the answer must still end with an unsolved practice item and must not treat
exposure as an evaluated attempt.
