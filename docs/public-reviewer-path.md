# Public Reviewer Path

This is the plain-English path for evaluating Ontologica OS without treating it as a production framework.

## One-Sentence Product View

Ontologica OS is a source-visible, rights-reserved proof-language and proofing-lane demonstrator for disciplined agentic cognition.

It shows how candidate outputs can be bounded by kernel contracts, passed through a toy deterministic projection, identified by synthetic manifests, checked for drift and disclosure risk, and held at a promotion gate without exporting private machinery.

## Read These First

1. `README.md`
2. `docs/v1-conceptual-whole.md`
3. `docs/braided-development-loop.md`
4. `docs/proofing-demo.md`
5. `docs/proof-packet-anatomy.md`
6. `docs/disclosure-critic.md`
7. `docs/public-readiness-scorecard.md`

## Run One Command

```bash
make proofing-demo
```

If `make` is unavailable:

```bash
PYTHONPATH=src python examples/run_proofing_demo.py
```

## Open These Outputs

```text
sample_outputs/proofing_demo/drift_receipt.json
sample_outputs/proofing_demo/proof_packet.json
sample_outputs/proofing_demo/disclosure_critic_receipt.json
sample_outputs/proofing_demo/promotion_report.md
sample_outputs/review_scorecard/v1_public_readiness_scorecard.json
```

## What To Notice

The proofing lane should show:

- synthetic inputs only
- toy projection only
- manifest identity, not truth
- drift evidence, not promotion
- disclosure critic review, not private detection machinery
- `candidate_only` authority
- `hold_for_review` instead of durable truth

## What Should Be Absent

A reviewer should not find:

- production math kernels
- private dimensions or thresholds
- private scoring/ranking
- private model routing
- real manifests
- real SHA lineage
- real receipts
- private traces
- production validators
- runtime authority
- hardware authority
- durable-truth promotion

## Reviewer Verdicts

### Valid Public Artifact

The repo is valid if it helps a reviewer understand:

```text
candidate cognition
  -> boundary
  -> identity
  -> drift evidence
  -> disclosure review
  -> hold decision
```

### Too Thin

The repo is too thin if it only contains boundary language and no proof lane.

### Too Leaky

The repo is too leaky if it reveals private scoring, routing, math, receipt topology, workspace topology, real lineage, or production authority.

## Current Intended Verdict

Current target verdict:

```text
reviewable public proof-language demonstration
```

Not intended verdict:

```text
open-source framework
production runtime
agent SDK
private system reconstruction guide
```
