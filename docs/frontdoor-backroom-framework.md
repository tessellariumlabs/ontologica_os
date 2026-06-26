# Frontdoor / Backroom Framework

The frontdoor / backroom framework defines how Ontologica OS, Emphera, and future private consolidation work should relate.

## Core Distinction

```text
frontdoor
  public explanation surface
  public review packets
  public diagrams
  public noncanonical artifacts
  public-safe release posture

backroom
  private consolidation work
  private sprint material
  private source history
  private implementation details
  private tooling migration
  private production hardening
```

## Repository Roles

### Ontologica OS

Ontologica OS is the proofing lane.

It exists to classify, bound, and receipt public-facing explanation packets before any material moves toward a public frontdoor.

Default posture:

```text
authority_ceiling: candidate_only
decision: hold_for_review
```

### Emphera

Emphera is the public frontdoor for complex agentic branch-sprawl consolidation and general data-analytics tooling.

It should start public and become the place where cleaned, bounded, public-safe consolidation tooling can be presented.

Default posture:

```text
public_frontdoor: true
production_claim: only after explicit review
```

### Emphera OS

Emphera OS is the deeper operating layer for future consolidation tooling.

It may receive candidate concepts from Ontologica OS and public-facing surfaces from Emphera, but production authority remains human-controlled.

Default posture:

```text
backroom_candidate: true
human_controlled_intake: true
```

## Conceptual Flow

```mermaid
flowchart TD
    A[Private sprint material] --> B[Ontologica OS proofing lane]
    B --> C[Disclosure critic]
    C --> D[Governed review packet]
    D --> E{Gate}
    E -- public-safe --> F[Emphera frontdoor]
    E -- needs private work --> G[Backroom consolidation]
    G --> H[Emphera OS candidate]
    H --> B
```

## Frontdoor Rules

A frontdoor artifact may contain:

- public vocabulary
- public diagrams
- synthetic examples
- review packets
- noncanonical demonstrations
- release notes
- public-safe tooling concepts

A frontdoor artifact must not contain:

- private source code
- private implementation history
- private routing
- private scoring
- private branch/worktree topology
- real private manifests
- real private receipts
- private production release process

## Backroom Rules

Backroom work may consolidate serious tooling from private systems only under human review.

Backroom work remains outside this public repository until transformed into a public-safe packet.

## Product Position

Emphera targets an underdeveloped space:

> complex agentic branch-sprawl consolidation and general data-analytics tooling.

Ontologica OS validates what can be safely said and moved toward that frontdoor.

## Release Gate

All movement from backroom to frontdoor requires:

```text
proof_packet: present
disclosure_critic: present
protected_terms_review: present
human_review: required
final_gate: hold / review / deny
```
