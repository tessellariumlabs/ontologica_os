# Public Release Checklist

This checklist must pass before changing repository visibility to public.

## Repository Identity

- [ ] Confirm this is the intended repository: `tessellariumlabs/ontologica_os`.
- [ ] Confirm the repository description says source-visible, rights-reserved, and not open source.
- [ ] Confirm topics do not imply open-source framework adoption.
- [ ] Confirm default branch is the intended public branch.

## Content Boundary

- [ ] Confirm no canonical private code is present.
- [ ] Confirm no production mathematical kernels are present.
- [ ] Confirm no exact constants, thresholds, field semantics, tensor layouts, or ranking functions are present.
- [ ] Confirm no real manifests, receipts, traces, prompts, sealed artifacts, or model routes are present.
- [ ] Confirm no private hostnames, keys, credentials, paths, serial configs, or model names are present.
- [ ] Confirm no private repository links are present.
- [ ] Confirm every example is labeled toy and noncanonical.
- [ ] Confirm every schema is labeled toy and noncanonical.

## Rights and Contact

- [ ] Confirm `LICENSE.md` has been reviewed.
- [ ] Confirm `COMMERCIAL.md` has a usable contact path.
- [ ] Confirm `AI_USE_POLICY.md` is present.
- [ ] Confirm `TRADEMARKS.md` is present.
- [ ] Confirm no file grants unintended open-source, model-training, production-use, or derivative-work rights.

## Public Operating Surface

- [ ] Confirm `SECURITY.md` is present.
- [ ] Confirm `CONTRIBUTING.md` discourages unsolicited PRs unless prior written agreement exists.
- [ ] Confirm issues are disabled or tightly templated.
- [ ] Confirm discussions are disabled or scoped to inquiry and Q&A.
- [ ] Confirm wiki is disabled unless intentionally used.
- [ ] Confirm GitHub Pages is disabled unless intentionally used.
- [ ] Confirm Actions are disabled unless intentionally used.
- [ ] Confirm no GitHub Actions logs expose private names or paths.

## Visibility Consequence Review

- [ ] Confirm the operator understands that public visibility enables public viewing and forking through GitHub functionality.
- [ ] Confirm the operator understands that public visibility may expose repository activity and any retained public logs or metadata.
- [ ] Confirm the operator has treated the visibility flip as a public disclosure event.

## Final Gate

- [ ] Human rights-holder review complete.
- [ ] Human technical boundary review complete.
- [ ] Human public-release approval complete.
