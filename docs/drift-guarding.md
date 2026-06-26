# Drift Guarding

A drift guard compares two manifest-bound states and reports whether change is acceptable, surprising, review-worthy, or denied.

The goal is not to prevent change. The goal is to prevent silent change.

The public reference focuses on projection drift: a deterministic vector difference between a prior state and a candidate state.

Reference decisions are:

- `pass`
- `warn`
- `hold_for_review`
- `deny`

These decisions are noncanonical and exist only for the public reference harness.
