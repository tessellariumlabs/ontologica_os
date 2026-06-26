# Development Butterfly Maps

This document maps the project as a butterfly: public frontdoors on one wing, private/backroom kernels on the other, with Ontologica OS as the body that proofs movement between them.

It is a visual planning artifact, not production authority.

## Butterfly 1 — Ecosystem Body And Wings

```mermaid
flowchart LR
    subgraph LeftWing[Public Frontdoor Wing]
        E[Emphera<br/>branch-sprawl analytics]
        F[Ontologica Forge<br/>worldbuilder + campaign UI]
    end

    subgraph Body[Proofing Body]
        O[Ontologica OS<br/>disclosure proofing lane]
        P[Proof packets]
        C[Disclosure critic]
        G[Release gate]
    end

    subgraph RightWing[Backroom / Embodiment Wing]
        EOS[Emphera OS<br/>deep consolidation]
        LL[local-loom<br/>runtime spines]
        SB[shardbench<br/>shards + grammar + routes]
        TB[tessera-builder<br/>build lane]
        T[Tessera<br/>physical tabletop OS]
    end

    E --> O
    F --> O
    O --> P --> C --> G
    G --> E
    G --> F
    G --> EOS
    G --> LL
    G --> SB
    G --> TB
    G --> T
```

## Butterfly 2 — Development Climb

```mermaid
flowchart BT
    L0[0. Repo roles named] --> L1[1. Ontologica leases present]
    L1 --> L2[2. Proofing lane runnable]
    L2 --> L3[3. Frontdoor examples]
    L3 --> L4[4. Backroom packet intake]
    L4 --> L5[5. Shard + runtime rehearsal]
    L5 --> L6[6. Tessera embodiment inventory]
    L6 --> L7[7. Cross-repo exchange rehearsal]
    L7 --> L8[8. Public/private audit]
    L8 --> L9[9. Finalized project candidate]
```

## Butterfly 3 — Public And Private Artifact Movement

```mermaid
flowchart TD
    A[Private material] --> B{Ontologica proofing lane}
    B --> C[Public vocabulary]
    B --> D[Protected terms report]
    B --> E[Toy / noncanonical demo]
    B --> F[Disclosure critic receipt]
    F --> G{Gate}

    G -- public-safe --> H[Frontdoor packet]
    H --> I[Emphera]
    H --> J[Ontologica Forge]

    G -- backroom candidate --> K[Backroom packet]
    K --> L[Emphera OS]
    K --> M[local-loom]
    K --> N[shardbench]
    K --> O[tessera-builder]

    G -- embodiment-only --> P[Tessera candidate]
    P --> Q[Tessera]

    G -- protected --> R[hold_for_rights_holder_review]
```

## Butterfly 4 — Milestone Wing Balance

The ecosystem should climb by keeping public and private wings balanced.

| Development band | Public wing | Backroom wing | Proofing body |
| --- | --- | --- | --- |
| Band 1 | Repo identity docs | Repo identity docs | Ontologica lease docs |
| Band 2 | Public-safe examples | Candidate intake docs | Proof packet scaffold |
| Band 3 | Frontdoor reviewer paths | Backroom intake packets | Disclosure critic receipts |
| Band 4 | Public demo packets | Runtime / shard rehearsals | Cross-repo exchange receipts |
| Band 5 | Release candidate surfaces | Production-adjacent candidates | Final boundary audit |

## Map Rules

1. Public wings cannot ingest private material directly.
2. Backroom wings cannot promote without human review.
3. Tessera-targeted movement cannot grant actuator or hardware authority from a public packet.
4. shardbench cannot become a hidden runtime promotion path.
5. local-loom cannot become uncontrolled execution machinery.
6. Ontologica OS remains the proofing body, not a production runtime.

## Final Butterfly Shape

```text
            Emphera                    Emphera OS
              \                         /
               \                       /
          Ontologica Forge -- Ontologica OS -- local-loom
               /                       \
              /                         \
       Public campaign frontdoor      shardbench / tessera-builder / Tessera
```

This is valid when every movement across the butterfly body leaves a proof packet, a disclosure critic receipt, and a human-reviewed gate decision.
