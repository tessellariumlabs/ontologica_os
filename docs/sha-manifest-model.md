# SHA Manifest Model

Ontologica OS uses manifest-addressed artifacts to prevent silent drift.

A SHA does not prove truth. A SHA proves identity.

Truth still requires authority, review, receipts, and promotion.

## Manifest responsibilities

A manifest records the identity of:

- input artifacts
- kernel version
- schema version
- tool version
- output artifact
- receipt artifact
- authority ceiling
- promotion status

## Public posture

The public harness uses SHA-256 examples only. These examples are synthetic and noncanonical.

## Toy manifest shape

```yaml
manifest_id: toy_manifest_001
schema_version: toy.manifest.v1
authority_ceiling: candidate_only
kernel:
  id: toy_math_kernel
  version: 0.1.0
inputs:
  - id: toy_tessera_set_001
    sha256: synthetic_input_hash
outputs:
  - id: toy_projection_001
    sha256: synthetic_output_hash
receipts:
  - id: toy_receipt_001
    sha256: synthetic_receipt_hash
promotion:
  status: hold
  reason: toy example; noncanonical
```
