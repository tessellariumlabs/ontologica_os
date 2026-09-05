# Process Transparency and Sanitization

This document describes a public, synthetic, candidate-only review posture. It
does not implement a scrubber, establish copyright clearance, inspect protected
systems, or grant publication authority.

## Outcome

The public candidate set accepts only newly authored boundary language and
clearly synthetic examples. Restricted, unknown-rights, confidential, secret,
or capability-bearing material is omitted and held for human review. Redaction
alone is never evidence that excluded material became safe to publish.

Copyrighted source text is not made publishable by paraphrase, truncation, or
scrubbing. Without an explicit publication basis, it remains outside the
candidate set.

## Prospective invariant

Before material enters a public candidate, the reviewer asks:

- Is its origin and publication basis explicitly known?
- Is it free of secrets, confidential identifiers, and protected details?
- Does it explain a public invariant without exporting reusable machinery?
- Can a reviewer understand the process without seeing source content?

An unknown or adverse answer fails closed. The material is excluded, the gap is
recorded in the local custody ledger, and the public candidate remains
`hold_for_review` with an authority ceiling of `candidate_only`.

## Transparent review flow

```text
declare intent without source content
  -> allowlist newly authored candidate files
  -> check origin and rights posture
  -> check secrets and protected-surface categories
  -> dwell across independent qualitative review lenses
  -> backfill the unanswered question from each review round
  -> write a coarsened synthetic public ledger
  -> hold for human rights-holder and technical review
```

This is a deny-by-default publication membrane. It does not copy a protected
tree and then try to remove unsafe portions. It builds a small candidate from an
explicit allowlist inside this repository.

## Bounded dwell and adjacency rotation

Dwell means a deliberate pause for another independent review question. It is
not a timer, daemon, score, threshold, convergence algorithm, or production
gate.

If repeated review starts to collapse onto one comfortable conclusion, the next
round rotates to an adjacent lens, such as origin and rights, secret hygiene,
explanatory scope, or human authority. Each round records the unanswered
question it found and the conservative backfill needed before review can
continue. No round may promote itself.

The public loop is intentionally bounded by its declared qualitative lenses.
Exhausting them does not imply convergence, clearance, or strong binding; its
only automatic outcome is `hold_for_review`. A human may then deny the
candidate, request another independently scoped review, or approve a later
commit under the repository's existing release checklist.

## Two-ledger boundary

The detailed custody ledger stays outside this repository. It may identify
excluded sources, evidence gaps, local locations, and reviewer decisions.

The public ledger is only a coarsened, synthetic sample. It may name candidate
files and qualitative checks, but it must not contain private names, paths,
excerpts, source digests, repository lineage, real receipts, or protected
implementation details. It is evidence of process posture, not evidence of
rights clearance.

The sample public ledger is
[process_transparency_sanitization_ledger.json](../sample_outputs/reviews/process_transparency_sanitization_ledger.json).

## Publication boundary

Saving a candidate locally, pushing a review branch, or opening a draft review
does not approve public release. Merge, visibility changes, durable truth,
runtime use, and downstream intake all remain human-controlled and outside this
artifact's authority.

Omitting an identifier from the current tree does not sanitize prior Git
history. History review remains a separate blocking item before any visibility
change.

The default result is:

```text
status: hold_for_review
authority_ceiling: candidate_only
emphera_intake: human_controlled_candidate
```
