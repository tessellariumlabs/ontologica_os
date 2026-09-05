# Blind Review and Public Disclosure

This is newly authored public boundary language and a synthetic, noncanonical
example. It describes a proposed separation of information. It does not run an
evaluation, implement an assignment resolver, attest an actor, or prove that a
real study is double blind.

## Two different questions

Blinding asks what an evaluator or participant can learn before a decision.
Publication asks which audience may receive an artifact. A private repository
does not establish blinding, and a public summary does not establish clearance
for the evidence behind it.

The term double blind must name the parties and the information withheld from
each. Labels alone do not establish that separation. The intended barriers in
this explanatory example are:

| Role | Proposed information boundary |
| --- | --- |
| Worker | Receives its permitted task material, without scoring labels or evaluator judgments. |
| Reviewer or juror | Receives approved anonymous comparisons, without source identity or treatment assignment. |
| Independent custodian | Holds the confidential assignment mapping, separate from execution and judging. |

These roles are unassigned. No access control, assignment, or human observation
is implemented or verified by this document.

## What can defeat blinding

Content can reveal an assignment even when identifying fields are removed.
Repeated samples, ordering, file names, timing, and earlier exposure can also
provide clues. A worker may recognize its treatment from the material it sees.
Do not infer verified double-blinding from anonymized field names alone.

Digests identify content; they are not anonymization. A digest of a small set of
possible assignments can be matched by someone who knows the candidate values.
Do not export private linkage hashes as a substitute for confidential custody.

## Private evidence and public explanation

The private evidence surface retains real identities, assignment mappings,
permitted raw observations, and confidential review records under its own
governance. This public example neither locates nor reads that surface.

The public surface contains newly authored boundary explanation and clearly
synthetic examples only. It contains no real assignments, actor names, source
links, captures, credentials, source hashes, or execution evidence.

Publishing an actual aggregate result would require a separately scoped review
of its source rights, disclosure risks, and claims. Even a summary can reveal
individual records through small groups or combination with another release.
No actual aggregate is included or authorized here.

## Decision lock and unblinding

In the proposed process, reviewers lock their decisions before a separate
custodian releases an authorized assignment join. A declared lock is not proof
of access history, trusted ordering, independence, or observed human judgment.
Unknown custody remains a hold. Neither a confirmation phrase nor a synthetic
receipt supplies missing execution evidence.

## Publication is a separate gate

Approval applies to its stated artifacts and actions. It is not a reusable
credential and does not silently expand to other files or repositories.
Repository visibility changes can expose history, branches, and associated
metadata beyond the current document. History review is required separately;
removing text from the current tree does not clear earlier versions.

This candidate does not grant publication authority, change repository
visibility, unblind an evaluation, or promote a private result. Its status is
`hold_for_review` and its authority ceiling is `candidate_only`.

See the [synthetic boundary example](../sample_outputs/reviews/blind_review_boundary_example.json),
[sanitization posture](process-transparency-and-sanitization.md), and
[public release checklist](../PUBLIC_RELEASE_CHECKLIST.md).
