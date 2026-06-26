# Math Kernel and Analysis-Core Boundary

This document guides future maintainers and LLM-assisted repository changes.

Ontologica OS may explain the role of mathematical stabilization and analysis flow. It must not publish private mathematical machinery or private analysis-core implementation.

## Decision

Public v1 should include:

- a toy mathematical proofing demo
- public vocabulary for mathematical stabilization
- synthetic tessera fixtures
- toy projections
- toy manifests
- toy drift receipts
- noncanonical promotion reports
- documentation explaining what the math layer does in the architecture

Public v1 should not include:

- production mathematical kernels
- exact dimensional structures
- exact constants or thresholds
- private field semantics
- private ranking functions
- private tensor layouts
- private analysis-core code
- private analysis-routing logic
- private manifests or receipt graphs
- real SHA lineage
- private evaluation traces
- private promotion evidence

## Contextual Assessment

The existing repository doctrine says the public project is a lens, not a canonical implementation. The proofing demo is therefore appropriate because it demonstrates the vocabulary path without exporting private capability.

The public demo answers: can a reader see the process flow?

```text
candidate input
  -> deterministic projection
  -> manifest identity
  -> drift receipt
  -> promotion hold
```

It should not answer: can a reader reconstruct the private system?

## Unbiased Future-Maintainer Assessment

A future LLM or human maintainer should treat math-kernel requests as high-risk unless the change is clearly toy, synthetic, and noncanonical.

Allowed examples:

- improve comments around the toy projection
- add synthetic fixtures
- add tests that verify candidate-only authority
- add docs explaining that SHA proves identity, not truth
- add docs explaining that receipts provide evidence, not promotion

Not allowed without explicit rights-holder review:

- adding new dimensions that appear private or domain-specific
- adding tuned constants, weights, or thresholds
- adding hidden heuristics
- adding model-routing analysis logic
- adding production-quality validators
- adding private branch, runtime, model, manifest, or receipt names
- making the proofing demo strong enough to function as a reusable framework

## Analysis Core Boundary

The analysis core should be represented publicly as a process diagram and vocabulary layer, not as reusable machinery.

Public representation:

```text
observe
  -> classify
  -> project
  -> compare
  -> receipt
  -> hold / review / deny
```

Protected implementation:

```text
private feature system
private scoring/ranking
private thresholds
private model routing
private correlation logic
private promotion heuristics
private receipt graph topology
```

## Future Change Rule

If a proposed change makes Ontologica OS more understandable, it may be considered.

If a proposed change makes Ontologica OS more capable, reconstructable, or production-useful, it should be held for rights-holder review.

The public repository may explain invariants, but it must not export capability.
