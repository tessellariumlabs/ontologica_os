# Kernel Contracts

A kernel is a bounded worker contract.

Each kernel defines Law, Work, and Proof.

## Law

Law describes what the worker must never do. It includes authority limits, forbidden claims, hard stop conditions, and escalation rules.

## Work

Work describes what the worker may read, inspect, propose, compute, route, or validate.

## Proof

Proof describes what receipt, test, manifest, replay, review bundle, or validation artifact is required before progress can be claimed.

## Public kernel classes

- `root_safety`: global stop conditions and forbidden claims.
- `meaning`: semantic interpretation, ontology, vector or field coverage, and ranking.
- `scenario`: candidate scenario generation.
- `memory`: candidate memory writes, lineage, and snapshot validity.
- `surface`: UI, board, or embodied display preview contracts.
- `actuation`: external-world action gates.
- `local_model`: local model roster, probes, and assignment evidence.
- `deterministic_math`: replayable computation and receipt-backed transforms.
- `artifact_forge`: candidate asset or artifact preparation without deployment authority.
- `promotion`: candidate-to-durable-state validation and sealing.

## Fail-closed rule

If a worker cannot map a task to Law, Work, and Proof, it should stop with `needs_info`, `no_safe_revision`, `hold_for_review`, or another explicit denial state rather than improvising.
