# Ontologica OS

Ontologica OS is a public lens for drift-guarded, receipt-backed agentic cognition.

It demonstrates how language-model proposals can be bounded by kernel contracts, stabilized by deterministic mathematical transforms, identified through SHA manifests, checked for drift, and held behind promotion gates.

This repository is **not** the canonical implementation of any private system. It is not the canonical implementation, not the implementation of Tessera Ontologica, and not a source of durable truth. It contains only synthetic examples, toy schemas, simplified mathematical demonstrations, and explanatory documents.

> Models propose. Math stabilizes. Manifests identify. Drift guards warn. Receipts prove. Promotion decides.

## Governing boundary

Ontologica OS publishes the grammar of the architecture, not the machinery of the architecture.

The public repo may explain invariants, but it must not export capability. It has no canonical authority over any private repository, private runtime, private manifest graph, private receipt corpus, private mathematical kernel, private model roster, private prompt set, hardware path, or sealed release artifact.

## Public thesis

Ontologica OS is a public modeling vocabulary and toy reference harness for designing agentic systems where language-model cognition is bounded by mathematical kernels, drift-guarded manifests, receipt evidence, and explicit promotion gates.

LLMs may propose or classify. Deterministic kernels stabilize replayable transforms. SHA manifests identify artifacts and lineage. Drift guards detect silent change. Receipts preserve evidence. Promotion gates decide whether candidate work remains held, is denied, or becomes durable truth in an authorized system.

## Six public pillars

1. **Kernel contracts** define what a worker may read, change, claim, and prove.
2. **Truth layers** separate candidate work from durable truth.
3. **Mathematical substrate** provides deterministic, replayable transforms underneath language-model proposals.
4. **Drift guards** detect schema, semantic, projection, model, receipt, manifest, authority, and promotion drift.
5. **SHA manifest receipts** bind artifacts to identity and replay evidence.
6. **Promotion gates** prevent candidate outputs from becoming durable truth without explicit review.

## What this repository is

Ontologica OS is:

- a public explanatory lens
- a noncanonical specification layer
- a clean-room toy harness
- a vocabulary for drift-guarded, mathematically bounded agentic systems
- a set of synthetic fixtures and simplified examples

## What this repository is not

Ontologica OS is not:

- the canonical implementation of any private system
- the implementation of Tessera Ontologica
- a source of durable truth
- a production runtime
- a public release of private algorithms
- a hardware control system
- a public release of private prompts, manifests, receipts, model routing, sealed artifacts, or evaluation corpora

## Architecture sketch

```text
                      ┌──────────────────────┐
                      │ LLM Cognition Layer   │
                      │ propose / classify    │
                      └───────────┬──────────┘
                                  v
                      ┌──────────────────────┐
                      │ Kernel Contract Gate  │
                      │ law / work / proof    │
                      └───────────┬──────────┘
                                  v
                      ┌──────────────────────┐
                      │ Mathematical Kernel   │
                      │ deterministic project │
                      └───────────┬──────────┘
                                  v
                      ┌──────────────────────┐
                      │ SHA Manifest Layer    │
                      │ identity / lineage    │
                      └───────────┬──────────┘
                                  v
                      ┌──────────────────────┐
                      │ Drift Guard           │
                      │ compare / detect      │
                      └───────────┬──────────┘
                                  v
                      ┌──────────────────────┐
                      │ Receipt Layer         │
                      │ evidence / replay     │
                      └───────────┬──────────┘
                                  v
                      ┌──────────────────────┐
                      │ Promotion Gate        │
                      │ hold / promote / deny │
                      └───────────┬──────────┘
                                  v
                      ┌──────────────────────┐
                      │ Durable Truth         │
                      │ private-only in canon │
                      └──────────────────────┘
```

Public examples stop at synthetic diagrams, toy schemas, and noncanonical harness code. They do not include private canonical transitions.

## Repository layout

```text
ontologica_os/
├── README.md
├── NOTICE.md
├── SANITIZATION.md
├── OWNERSHIP_BOUNDARY.md
├── docs/
│   ├── doctrine.md
│   ├── mathematical-kernel.md
│   ├── drift-guarding.md
│   ├── sha-manifest-model.md
│   ├── truth-layers.md
│   ├── kernel-contracts.md
│   ├── receipt-model.md
│   ├── promotion-gates.md
│   └── noncanonical-status.md
├── schemas/
│   ├── toy_receipt.schema.json
│   ├── toy_manifest.schema.json
│   ├── toy_drift_guard.schema.json
│   └── toy_math_kernel.schema.json
├── examples/
│   ├── toy_lattice_projection.py
│   ├── toy_manifest_hash_chain.py
│   ├── toy_drift_guard.py
│   └── toy_candidate_promotion.py
└── tests/
    ├── test_toy_lattice_projection.py
    ├── test_toy_manifest_hash_chain.py
    ├── test_toy_drift_guard.py
    └── test_noncanonical_boundaries.py
```

The repeated `toy_` prefix is intentional. It signals synthetic scope and prevents the public harness from being mistaken for production machinery.

## Running the toy tests

The examples use only the Python standard library.

```bash
python -m pytest tests
```

The tests verify deterministic projection, synthetic manifest identity, drift-guard decisions, and boundary language. Passing tests do not constitute proof of any private system.
