# AGENTS.md

This repository is source-visible, rights-reserved, noncanonical, and nonproduction.

These instructions apply to human maintainers, LLM-assisted edits, and automated coding agents working in this repository.

## Core Maintainer Rule

Public Ontologica OS may explain invariants, vocabulary, process shape, and proof posture.

It must not export reusable capability, private scoring, private routing, private math, or production-quality analysis machinery.

## Change Gate

Before changing any file, ask:

```text
Does this make the public repo more understandable?
  -> maybe allow

Does this make the public repo more capable, reconstructable, reusable, or production-useful?
  -> hold for rights-holder review
```

## Preferred Public Moves

Prefer:

- diagrams over engines
- vocabulary over algorithms
- toy fixtures over real traces
- synthetic manifests over real lineage
- `hold_for_review` over promotion
- `candidate_only` over durable truth
- explanation over capability

## Allowed Without Special Review

Allowed changes are narrow and must remain synthetic, toy, and noncanonical:

- clarify documentation
- add glossary definitions
- add boundary warnings
- add synthetic fixtures
- add tests that enforce `candidate_only`
- add tests that prevent accidental promotion claims
- improve toy-demo readability without increasing capability
- explain that SHA proves identity, not truth
- explain that receipts provide evidence, not promotion

## Hold For Rights-Holder Review

Hold any change that would add or reveal:

- production mathematical kernels
- exact dimensional structures
- tuned constants, weights, or thresholds
- private field semantics
- private ranking functions
- private scoring logic
- private tensor layouts
- private analysis-core code
- private model-routing logic
- private correlation logic
- private promotion heuristics
- private receipt graph topology
- real manifests or real SHA lineage
- real receipts or private traces
- production-grade validators
- runtime or hardware authority paths

## Math Kernel Rule

The public math kernel is a toy explanatory surface only.

It may demonstrate deterministic projection, manifest identity, drift comparison, and receipt generation. It may not become a reusable framework, production validator, private field model, or private analysis core.

## Analysis Core Rule

The public analysis core is a process diagram and vocabulary layer only:

```text
observe
  -> classify
  -> project
  -> compare
  -> receipt
  -> hold / review / deny
```

Protected private implementation includes feature systems, scoring and ranking, thresholds, model routing, correlation logic, promotion heuristics, and receipt graph topology.

## Disclosure Critic Rule

A final public proofing loop may include a disclosure critic.

The disclosure critic may:

- review public proof packets for boundary assertions
- list categories that should remain undisclosed
- emit a synthetic critic receipt
- recommend `pass_public_boundary` or `hold_for_rights_holder_review`

The disclosure critic must not:

- perform a real LLM disclosure review
- reveal private detectors or internal classification methods
- inspect private repositories or private traces
- infer private scoring, routing, math, manifests, or receipt graph topology
- grant publication, implementation, runtime, hardware, or durable-truth authority

## Trivalent Inner Braid Rule

A public trivalent inner braid may use only qualitative posture labels:

```text
pass_public_boundary
warning_scar
hold_for_rights_holder_review
```

It may leave a scar receipt when a maintainer request mentions disclosure-sensitive concepts, including trivalent logic, private analysis core, workspace topology, atom serving, or receipt graph topology.

It must not publish private trivalent rules, scoring thresholds, routing behavior, mathematical reconstruction paths, atom-store schemas, or production policy engines.

If repository documentation permits explanation but blocks implementation, leave a scar receipt instead of exporting machinery.

## Required Default Outcome

When uncertain, choose:

```text
status: hold_for_review
authority_ceiling: candidate_only
reason: public repository must explain invariants without exporting capability
```
