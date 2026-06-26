# Receipt Model

A receipt is a structured proof artifact produced by a deterministic tool, validation pass, replay, test, or review gate.

Receipts do not make a candidate true by themselves. They provide evidence for promotion.

A receipt records:

- receipt id
- task id
- source inputs
- authority ceiling
- kernel responsible
- tools invoked
- validation result
- denied capabilities
- replay instructions
- promotion recommendation

## Decisions

Common public receipt decisions:

- `pass`
- `warn`
- `hold_for_review`
- `quarantine`
- `deny`

## Noncanonical rule

Receipts in this repository are synthetic examples. They are not private proof and do not substantiate any private canonical repository.
