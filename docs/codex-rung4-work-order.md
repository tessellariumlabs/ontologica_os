# Codex Rung 4 Work Order

This work order converts the finalization ladder's next rung into bounded implementation tasks.

## Rung

```text
rung: 4
label: backroom intake packets
status: ready_for_codex_candidate_work
authority_ceiling: candidate_only
```

## Objective

Create synthetic backroom intake packet examples for the repositories that should receive deeper consolidation, runtime-spine, and Tessera-builder candidates.

## Target Packet Sets

### 1. Emphera OS consolidation intake

Repository:

```text
tessellariumlabs/emphera-os
```

Files:

```text
examples/consolidation_intake_packet.md
sample_outputs/reviews/consolidation_intake_disclosure_critic_receipt.json
sample_outputs/reports/consolidation_intake_release_report.md
```

Required final gate:

```text
decision: hold_for_review
authority_ceiling: candidate_only
production_authority: not_granted
merge_authority: not_granted
```

### 2. local-loom runtime-spine intake

Repository:

```text
tessellariumlabs/local-loom
```

Files:

```text
examples/runtime_spine_intake_packet.md
sample_outputs/reviews/runtime_spine_disclosure_critic_receipt.json
sample_outputs/reports/runtime_spine_release_report.md
```

Required final gate:

```text
decision: hold_for_review
authority_ceiling: candidate_only
runtime_authority: not_granted
production_authority: not_granted
merge_authority: not_granted
```

### 3. tessera-builder build candidate intake

Repository:

```text
tessellariumlabs/tessera-builder
```

Files:

```text
examples/build_candidate_packet.md
sample_outputs/reviews/build_candidate_disclosure_critic_receipt.json
sample_outputs/reports/build_candidate_release_report.md
```

Required final gate:

```text
decision: hold_for_review
authority_ceiling: candidate_only
hardware_authority: not_granted
actuator_authority: not_granted
production_authority: not_granted
merge_authority: not_granted
```

## Completion Receipt

After the three packet sets land, add this in `ontologica_os`:

```text
sample_outputs/reviews/rung4_backroom_intake_packets_receipt.json
```

It should include:

```text
status: rung4_backroom_intake_packets_landed
emphera_os_packet: present
local_loom_packet: present
tessera_builder_packet: present
final_gate: hold_for_review
release_authority: not_granted
production_authority: not_granted
```

## Anti-Leak Requirements

All packet examples must be synthetic and noncanonical.

Do not include:

- private source code
- private sprint corpora
- private branch/worktree topology
- private routing
- private scoring
- private math-engine internals
- private runtime internals
- hardware or actuator authority paths
- real manifests or receipts
- production release process

## Validation

A packet set is valid only if a reviewer can answer:

1. What is the packet for?
2. Which repository owns the next review?
3. Which protected materials are absent?
4. Which authority is explicitly not granted?
5. Why does the report hold for human review?

## Fail-Closed Instruction

If a target repo file already exists, do not overwrite casually. Fetch, review, then update only if the change preserves the same boundary.

If uncertain, create a hold receipt instead of implementation.
