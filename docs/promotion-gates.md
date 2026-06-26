# Promotion Gates

Promotion is the explicit decision point where candidate material may become a more durable state.

Candidate work remains candidate-only until a promotion gate says otherwise.

## Public promotion states

- `candidate_only`
- `reviewed_memory`
- `hold_for_review`
- `quarantine`
- `promoted_state`
- `denied`

## Promotion inputs

A promotion gate may inspect:

- changed-artifact manifest
- kernel ownership
- receipt evidence
- validation pass
- drift guard result
- authority map
- review bundle
- explicit promotion decision

## Rule

A manifest can identify an artifact. A receipt can provide evidence. Only a promotion gate can change durable truth.

In this public repository, promotion is always synthetic and noncanonical.
