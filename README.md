# Ontologica OS

Ontologica OS is a public lens for drift-guarded, receipt-backed agentic disclosure proofing.

It demonstrates how candidate proposals can be bounded by kernel contracts, stabilized by deterministic toy transforms, identified through SHA manifests, checked for drift, reviewed by a disclosure critic, and held behind promotion gates.

This repository is not the canonical implementation of any private system. It contains synthetic examples, toy schemas, simplified demonstrations, public diagrams, and explanatory documents.

> Candidates enter. Boundaries classify. Toy transforms stabilize. Manifests identify. Drift guards warn. Receipts prove. Critics check disclosure. Promotion holds.

## License and Use Boundary

Ontologica OS is source-visible, rights-reserved, noncanonical, and nonproduction.

It is **not open source**.

Use, implementation, redistribution, commercial use, research use, publication beyond ordinary citation, benchmark use, or derivative permissions require a separate written agreement. See [LICENSE.md](LICENSE.md), [COMMERCIAL.md](COMMERCIAL.md), [AI_USE_POLICY.md](AI_USE_POLICY.md), and [TRADEMARKS.md](TRADEMARKS.md).

## Product Shape

Ontologica OS is a local ontology firewall and sprint-consolidation proofing lane for public-facing agentic architecture.

It helps turn private ontology notes, architecture terms, and coding-sprint outputs into bounded review packets without publishing the private material itself.

Start with [docs/product-identity.md](docs/product-identity.md) and [docs/pipeline-connector-scope.md](docs/pipeline-connector-scope.md).

## Public Scope

Ontologica OS publishes the grammar of the architecture, not the machinery of the architecture.

The public scope is limited to:

- agentic disclosure-proofing vocabulary
- bounded kernel contracts
- deterministic toy-transform demonstrations
- SHA/manifest identity patterns
- drift-guard patterns
- receipt-backed validation examples
- disclosure-critic review vocabulary
- promotion-gated truth vocabulary
- polyp, cluster, and shard vocabulary as public context-movement metaphors
- workspace-lane, policy-shard, atom-packet, and sliding-polytope metaphors as public policy-exchange vocabulary
- synthetic examples and toy schemas

## Proofing Demo

The v1 proofing demo is the first technical substance layer.

It runs a complete synthetic flow:

```text
prior tessera fixture
  -> toy projection
  -> prior manifest
candidate tessera fixture
  -> toy projection
  -> candidate manifest
prior + candidate manifests
  -> drift receipt
  -> proof packet
  -> disclosure critic receipt
  -> public promotion report
  -> hold_for_review
```

Run it with:

```bash
make proofing-demo
```

Or directly:

```bash
PYTHONPATH=src python examples/run_proofing_demo.py
```

Start here:

- [docs/proofing-demo.md](docs/proofing-demo.md)
- [docs/proof-packet-anatomy.md](docs/proof-packet-anatomy.md)
- [docs/disclosure-critic.md](docs/disclosure-critic.md)
- [src/ontologica_os_public/proofing.py](src/ontologica_os_public/proofing.py)
- [fixtures/proofing/prior_tesserae.json](fixtures/proofing/prior_tesserae.json)
- [fixtures/proofing/candidate_tesserae.json](fixtures/proofing/candidate_tesserae.json)
- [sample_outputs/proofing_demo/drift_receipt.json](sample_outputs/proofing_demo/drift_receipt.json)
- [sample_outputs/proofing_demo/proof_packet.json](sample_outputs/proofing_demo/proof_packet.json)
- [sample_outputs/proofing_demo/disclosure_critic_receipt.json](sample_outputs/proofing_demo/disclosure_critic_receipt.json)
- [sample_outputs/proofing_demo/promotion_report.md](sample_outputs/proofing_demo/promotion_report.md)

## Visual Clarifications

The repository includes Mermaid diagrams for public process shape only. These diagrams explain candidate flow, kernel contract surfaces, polyp / cluster / shard vocabulary, workspace policy shards, atom packets, and disclosure review without exposing private topology, scoring, routing, promotion, math, atom-serving infrastructure, or receipt-graph machinery.

Start with:

- [docs/polyp-cluster-shard-boundary.md](docs/polyp-cluster-shard-boundary.md)
- [docs/workspace-policy-shard-boundary.md](docs/workspace-policy-shard-boundary.md)
- [docs/disclosure-critic.md](docs/disclosure-critic.md)

## Trivalent Boundary

Trivalent-specific public disclosure remains blocked unless the rights holder explicitly reviews and accepts the boundary. The current accepted surface allows posture labels and hard-hold receipts only; it does not disclose protected trivalent logic.

See:

- [docs/trivalent-inner-braid.md](docs/trivalent-inner-braid.md)
- [sample_outputs/reviews/rights_holder_trivalent_acceptance_receipt.json](sample_outputs/reviews/rights_holder_trivalent_acceptance_receipt.json)
- [sample_outputs/reviews/trivalent_inner_braid_hard_hold_receipt.json](sample_outputs/reviews/trivalent_inner_braid_hard_hold_receipt.json)

## Noncanonical Boundary

This repository does not modify, substantiate, patch, or define any private canonical repository.

Public artifacts may inspire private hardening only through manual human review. They are not private proof, not private receipts, not private manifests, and not canonical implementation material.

See [OWNERSHIP_BOUNDARY.md](OWNERSHIP_BOUNDARY.md), [SANITIZATION.md](SANITIZATION.md), [AGENTS.md](AGENTS.md), and [PUBLIC_RELEASE_CHECKLIST.md](PUBLIC_RELEASE_CHECKLIST.md).

## Process Transparency

The publication posture is deny-by-default and prospective: only newly authored,
allowlisted public-boundary material enters a candidate. Unknown-rights,
secret-bearing, confidential, or capability-bearing material is omitted and
held; it is never treated as cleared merely because it was redacted.

See [docs/process-transparency-and-sanitization.md](docs/process-transparency-and-sanitization.md)
and the synthetic, noncanonical
[process transparency ledger](sample_outputs/reviews/process_transparency_sanitization_ledger.json).

## Recommended Read Order

1. [LICENSE.md](LICENSE.md)
2. [COMMERCIAL.md](COMMERCIAL.md)
3. [AI_USE_POLICY.md](AI_USE_POLICY.md)
4. [TRADEMARKS.md](TRADEMARKS.md)
5. [OWNERSHIP_BOUNDARY.md](OWNERSHIP_BOUNDARY.md)
6. [SANITIZATION.md](SANITIZATION.md)
7. [docs/process-transparency-and-sanitization.md](docs/process-transparency-and-sanitization.md)
8. [AGENTS.md](AGENTS.md)
9. [SECURITY.md](SECURITY.md)
10. [PUBLIC_RELEASE_CHECKLIST.md](PUBLIC_RELEASE_CHECKLIST.md)
11. [CHANGELOG.md](CHANGELOG.md)
12. [docs/product-identity.md](docs/product-identity.md)
13. [docs/pipeline-connector-scope.md](docs/pipeline-connector-scope.md)
14. [docs/emphera-production-validation.md](docs/emphera-production-validation.md)
15. [docs/doctrine.md](docs/doctrine.md)
16. [docs/architecture.md](docs/architecture.md)
17. [docs/glossary.md](docs/glossary.md)
18. [docs/proofing-demo.md](docs/proofing-demo.md)
19. [docs/proof-packet-anatomy.md](docs/proof-packet-anatomy.md)
20. [docs/disclosure-critic.md](docs/disclosure-critic.md)
21. [docs/math-and-analysis-boundary.md](docs/math-and-analysis-boundary.md)
22. [docs/mathematical-kernel.md](docs/mathematical-kernel.md)
23. [docs/toy-math-kernel-contract.md](docs/toy-math-kernel-contract.md)
24. [docs/polyp-cluster-shard-boundary.md](docs/polyp-cluster-shard-boundary.md)
25. [docs/workspace-policy-shard-boundary.md](docs/workspace-policy-shard-boundary.md)
26. [docs/sha-manifest-model.md](docs/sha-manifest-model.md)
27. [docs/drift-guarding.md](docs/drift-guarding.md)
28. [docs/kernel-contracts.md](docs/kernel-contracts.md)
29. [docs/receipt-model.md](docs/receipt-model.md)
30. [docs/promotion-gates.md](docs/promotion-gates.md)

## Status

Ontologica OS is a v1 public-lens release candidate. The rights holder has accepted the current trivalent boundary surface while preserving the hard-hold rule for future trivalent-specific changes. Repository visibility should still change only after [PUBLIC_RELEASE_CHECKLIST.md](PUBLIC_RELEASE_CHECKLIST.md) is completed.
