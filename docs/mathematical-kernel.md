# Mathematical Kernel

Ontologica OS assumes that language-model cognition is not sufficient as a source of durable system state.

The mathematical kernel provides deterministic transforms that can be replayed, hashed, compared, and receipt-bound.

In the public harness, the mathematical kernel is deliberately simplified, synthetic, noncanonical, and candidate-only.

See [toy-math-kernel-contract.md](toy-math-kernel-contract.md) for the allowed public boundary.

## Public responsibilities

The toy mathematical kernel demonstrates:

- bounded symbolic state
- deterministic projection
- stable vector or lattice-like coordinates
- replayable transforms
- manifest-addressed input and output
- drift comparison across versions
- receipt generation
- candidate-only authority
- promotion hold behavior

## Private responsibilities intentionally excluded

The public harness does not reveal:

- production mathematical kernels
- exact dimensional structures
- proprietary constants
- tuned weights or thresholds
- private ranking functions
- private field semantics
- canonical tensor layouts
- production drift thresholds
- production manifest topology
- private analysis-core code
- model-routing analysis logic
- private correlation logic
- private promotion heuristics

## Public vocabulary

- **Tessera**: smallest public symbolic unit.
- **Field**: named interpretive dimension.
- **Projection**: deterministic mapping from tesserae into a toy vector or lattice state.
- **Manifest**: hash-bound identity record for inputs, kernel version, and outputs.
- **Drift**: measured difference between two manifest-bound projections.
- **Receipt**: evidence record describing what was computed and whether it is promotable.

## Maintainer rule

A change to the math-kernel surface may be considered when it makes the public proofing path easier to understand.

A change must be held for rights-holder review when it makes the public math surface more capable, reconstructable, reusable, production-like, or private-system-revealing.

The public repository may explain invariants, but it must not export capability.
