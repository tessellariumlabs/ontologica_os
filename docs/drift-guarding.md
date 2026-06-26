# Drift Guarding

A drift guard compares manifest-bound states across time, branches, models, kernels, or releases.

The goal is not to prevent all change. The goal is to prevent silent change.

A drift guard asks:

- What changed?
- Which kernel produced the change?
- Which manifest identifies the prior state?
- Which manifest identifies the new state?
- Is the change expected?
- Is the change within tolerance?
- Does the change require review?
- Is promotion allowed, held, quarantined, or denied?

## Public drift classes

- `schema_drift`: the shape of the data changed.
- `semantic_drift`: the interpreted meaning changed.
- `projection_drift`: the mathematical projection changed.
- `model_drift`: a model produced materially different candidate behavior.
- `receipt_drift`: proof artifacts changed or became incomplete.
- `manifest_drift`: content identity, dependency identity, or lineage changed.
- `authority_drift`: a worker appears to gain permissions it should not have.
- `promotion_drift`: candidate work is being treated as durable truth.

## Guard decisions

- `pass`: no relevant drift detected.
- `warn`: drift exists but remains within reviewable tolerance.
- `hold_for_review`: promotion cannot proceed without human review.
- `quarantine`: the candidate must be isolated from durable state.
- `deny`: the transition is blocked.
