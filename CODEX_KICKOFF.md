# Codex Kickoff

This is the starting surface for Codex or any coding assistant working in the Ontologica / Emphera / Tessera repository ecosystem.

## Status

```text
current_rung: 3
completed: frontdoor examples for Emphera and Ontologica Forge
next_rung: 4
next_focus: backroom intake packets
```

This file does not grant production authority, release authority, merge authority, runtime authority, hardware authority, or private-canon authority.

## Required First Read

Before editing, read in order:

1. `AGENTS.md`
2. `README.md`
3. `docs/finalization-ladder.md`
4. `docs/ecosystem-kernel-map.md`
5. `docs/development-gantt-flow.md`
6. `docs/development-butterfly-map.md`
7. `docs/repository-structure-strategy.md`
8. `docs/runtime-shard-kernel-strategy.md`
9. `docs/math-engine-landing-policy.md`

## Current Mission

Build Rung 4 without leaking machinery.

Rung 4 requires synthetic, noncanonical backroom intake packets for:

```text
1. Emphera OS intake packet example
2. local-loom runtime-spine intake packet example
3. tessera-builder build packet example
```

Each packet must include:

```text
proof_packet: present
disclosure_critic: present
protected_terms_review: present
source_repository: declared
target_repository: declared
human_review: required
final_gate: hold / review / deny
```

## Allowed Work

Allowed:

- create synthetic packet examples
- create disclosure critic receipts
- create hold/review/deny release reports
- update planning receipts
- add reviewer paths
- improve diagrams
- clarify what belongs in each repo
- clarify what must not land in each repo

## Blocked Work

Do not add:

- private source code
- private branch/worktree topology
- private routing
- private scoring or ranking
- private math-engine internals
- private shard stores
- real manifests
- real receipts
- runtime execution authority
- hardware or actuator authority
- automatic merge or promotion logic
- production claims

## Rung 4 Target Repositories

### Emphera OS

Role:

```text
deep consolidation operating layer
backroom intake for consolidation candidates
```

Expected output shape:

```text
examples/consolidation_intake_packet.md
sample_outputs/reviews/consolidation_intake_disclosure_critic_receipt.json
sample_outputs/reports/consolidation_intake_release_report.md
```

### local-loom

Role:

```text
private runtime OS spine lane
runtime-spine candidate intake
```

Expected output shape:

```text
examples/runtime_spine_intake_packet.md
sample_outputs/reviews/runtime_spine_disclosure_critic_receipt.json
sample_outputs/reports/runtime_spine_release_report.md
```

### tessera-builder

Role:

```text
backroom builder lane
Tessera-targeted build candidate intake
```

Expected output shape:

```text
examples/build_candidate_packet.md
sample_outputs/reviews/build_candidate_disclosure_critic_receipt.json
sample_outputs/reports/build_candidate_release_report.md
```

## Required Default Outcome

Every Rung 4 packet must end with:

```text
decision: hold_for_review
authority_ceiling: candidate_only
production_authority: not_granted
release_authority: not_granted
```

For Tessera-targeted work, also require:

```text
hardware_authority: not_granted
actuator_authority: not_granted
```

## Completion Receipt

After the three packet sets are landed, add:

```text
sample_outputs/reviews/rung4_backroom_intake_packets_receipt.json
```

The receipt must state:

```text
status: rung4_backroom_intake_packets_landed
final_gate: hold_for_review
release_authority: not_granted
production_authority: not_granted
```

## Fail-Closed Rule

If a requested change appears to require protected machinery, leave a receipt and hold instead of implementing it.

```text
decision: hold_for_rights_holder_review
authority_ceiling: candidate_only
reason: requested change may export capability or protected machinery
```
