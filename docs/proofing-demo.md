# Proofing Demo

This demo turns the public Ontologica OS vocabulary into a small, inspectable proof path.

It is synthetic, noncanonical, and deliberately simple.

## What it proves

The demo proves that the public lens can express a complete evidence flow:

```text
prior tessera fixture
  -> deterministic toy projection
  -> prior manifest identity

candidate tessera fixture
  -> deterministic toy projection
  -> candidate manifest identity

prior + candidate manifests
  -> drift receipt
  -> public promotion report
  -> hold_for_review
```

## What it does not prove

The demo does not publish or imply:

- private mathematical kernels
- production constants or thresholds
- private field semantics
- canonical manifest topology
- real receipts
- private model routing
- runtime authority
- hardware authority
- durable truth promotion

## Run

```bash
PYTHONPATH=src python examples/run_proofing_demo.py
```

The command writes synthetic artifacts to:

```text
sample_outputs/proofing_demo/
```

Expected summary:

```json
{
  "candidate_manifest": "toy_manifest_candidate",
  "drift_decision": "warn",
  "output_dir": "sample_outputs/proofing_demo",
  "prior_manifest": "toy_manifest_prior",
  "promotion_status": "hold_for_review"
}
```

## Inspect

Start with:

- `fixtures/proofing/prior_tesserae.json`
- `fixtures/proofing/candidate_tesserae.json`
- `src/ontologica_os_public/proofing.py`
- `sample_outputs/proofing_demo/drift_receipt.json`
- `sample_outputs/proofing_demo/promotion_report.md`

## Design notes

The toy mathematical kernel averages four public demonstration fields:

- `novelty`
- `risk`
- `coherence`
- `embodiment`

This is intentionally not a private field system. It is a public didactic projection that makes the proofing path visible.

The SHA manifest layer identifies inputs and outputs. It does not crown truth.

The drift receipt records a warning-level projection delta. The public promotion gate then holds the candidate for review because this repository has no authority to promote durable truth.
