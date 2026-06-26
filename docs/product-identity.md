# Product Identity

Ontologica OS is a local-first disclosure proofing lane for ontology-heavy agentic systems.

It helps a builder transform private conceptual architecture into a public-safe explanation packet by separating vocabulary, invariants, toy/noncanonical demonstrations, protected machinery, and release decisions.

## Core Product Sentence

> Ontologica OS is a local ontology firewall for public-facing agentic architecture.

Expanded:

> Ontologica OS is a local-first disclosure proofing workbench for ontology-heavy agentic systems. It helps transform private conceptual architectures into public-safe explanations by separating vocabulary, invariants, toy demonstrations, protected machinery, and release decisions.

## What It Does

The product shape is:

```text
private ontology / architecture notes / term graph / repo concepts
        |
        v
local Ontologica proofing lane
        |
        +--> classify public vs protected concepts
        +--> map private terms to public vocabulary
        +--> generate toy/noncanonical representation
        +--> attach synthetic manifest identity
        +--> run drift/disclosure critic
        +--> produce hold/review/deny report
        |
        v
public-safe explanation packet
```

## What It Does Not Do

It does not approve disclosure automatically.

It does not claim to detect every leak.

It does not publish the private ontology, private math, private routing, private scoring, private receipt graph, private workspace topology, or production machinery.

The default release result remains:

```text
decision: hold_for_rights_holder_review
authority_ceiling: candidate_only
```

## Core Loop

```text
load ontology
  -> mark sensitive terms
  -> derive public vocabulary
  -> generate public diagram
  -> create toy proof packet
  -> run disclosure critic
  -> produce release report
  -> hold_for_review
```

## Concept State Classes

Every concept should be forced into one of these public release states:

```text
public vocabulary
public invariant
toy/noncanonical demo
private/protected
requires review
do not disclose
```

## CLI Shape

The future CLI may look like this, but this repository does not yet provide a production CLI:

```bash
ontologica proof ontology.yaml \
  --profile public-lens \
  --emit packet \
  --emit diagrams \
  --emit disclosure-report
```

Expected output shape:

```text
outputs/
  public_vocabulary.md
  public_process_diagram.mmd
  protected_terms_report.md
  toy_manifest.json
  disclosure_critic_receipt.json
  release_review.md
```

## Product Category

Ontologica OS sits at the intersection of:

- ontology proofing
- anti-leak review
- public/private boundary compilation
- agentic architecture disclosure review
- concept release gating

## Primary User

For builders of complex agentic systems who need to explain their work publicly without leaking the machinery.

## Sharpest Positioning

> A proofing workbench for deciding what can be safely said.

## Release Rule

The private ontology never becomes the public artifact.

Private material is loaded locally, inspected locally, transformed locally, and only a bounded public packet is emitted.
