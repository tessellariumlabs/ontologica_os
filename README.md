# Ontologica OS

Ontologica OS is a public specification and clean-room reference implementation for drift-guarded, receipt-backed agentic cognition.

It demonstrates how language-model proposals can be bounded by kernel contracts, stabilized by deterministic mathematical transforms, identified through SHA manifests, checked for drift, and held behind promotion gates.

This repository is **not** the canonical implementation of any private system. Plainly: it is not the canonical implementation, it is not the implementation of Tessera Ontologica, and it is not a source of durable truth.

> Models propose. Math stabilizes. Manifests identify. Drift guards warn. Receipts prove. Promotion decides.

## Public thesis

Ontologica OS is a public modeling vocabulary and reference harness for agentic systems where cognition is bounded by mathematical kernels, drift-guarded manifests, receipt evidence, and explicit promotion gates.

## Six public pillars

1. Kernel contracts
2. Truth layers
3. Mathematical substrate
4. Drift guards
5. SHA manifest receipts
6. Promotion gates

## Repository shape

```text
ontologica_os/
├── BOUNDARY.md           # public boundary statement
├── docs/                 # public doctrine and specification
├── schemas/              # noncanonical public JSON schemas
├── src/ontologica_os/    # clean-room reference implementation
├── examples/             # runnable reference examples
└── tests/                # public invariant tests
```

## Boundary

Ontologica OS publishes the grammar of the architecture, not the private machinery of the architecture.

The public repo may explain invariants and provide a usable reference harness, but it must not export private capability. Public artifacts are synthetic, noncanonical, and have no authority over any private repository, runtime, manifest graph, receipt corpus, mathematical kernel, or release artifact.

## Run tests

The reference implementation uses only the Python standard library.

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

Passing tests verify only the public reference harness. They do not prove any private system.
