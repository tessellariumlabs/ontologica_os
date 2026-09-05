"""Checks for one synthetic public example, not a blinding validator."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_PATH = (
    ROOT / "sample_outputs" / "reviews" / "blind_review_boundary_example.json"
)
DOC_PATH = ROOT / "docs" / "blind-review-and-public-disclosure.md"

EXPECTED_EXAMPLE = {
    "example_id": "blind_review_boundary_synthetic_v1",
    "example_class": "synthetic_noncanonical_example",
    "status": "hold_for_review",
    "authority_ceiling": "candidate_only",
    "information_barriers": {
        "worker": "scoring_labels_and_judgments_withheld_in_proposed_design",
        "reviewer": "identity_and_assignment_withheld_in_proposed_design",
        "custodian": "separate_unassigned_role",
    },
    "observations": {
        "actors_assigned": False,
        "assignment_resolver_present": False,
        "raw_evidence_present": False,
        "judgments_locked": False,
        "blinding_verified": False,
        "effects_measured": False,
    },
    "public_surface": {
        "newly_authored_boundary_language": True,
        "synthetic_examples_only": True,
        "private_source_imported": False,
        "private_join_keys_included": False,
        "private_linkage_hashes_included": False,
        "actual_results_included": False,
    },
    "authority": {
        "execution": False,
        "unblinding": False,
        "publication": False,
        "visibility_change": False,
        "private_runtime": False,
    },
}


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        assert key not in result, "Synthetic example contains a duplicate key"
        result[key] = value
    return result


def _load_example() -> dict[str, object]:
    return json.loads(
        EXAMPLE_PATH.read_text(encoding="utf-8"),
        object_pairs_hook=_unique_object,
    )


def test_example_has_only_the_exact_synthetic_contract() -> None:
    # Serialized comparison distinguishes false from 0 and true from 1.
    assert json.dumps(_load_example(), sort_keys=True) == json.dumps(
        EXPECTED_EXAMPLE, sort_keys=True
    )


def test_example_does_not_claim_observations_or_grant_authority() -> None:
    example = _load_example()
    assert example["status"] == "hold_for_review"
    assert example["authority_ceiling"] == "candidate_only"
    assert all(value is False for value in example["observations"].values())
    assert all(value is False for value in example["authority"].values())


def test_example_has_no_real_references_linkage_hashes_or_paths() -> None:
    text = EXAMPLE_PATH.read_text(encoding="utf-8")
    forbidden_markers = (
        r'"[A-Za-z0-9_]*(?:_ref|_digest|_sha256|_url|_path)"\s*:',
        r"(?i)(?:https?|ssh|git|file)://",
        r"(?i)\bwww\.",
        r"(?i)\b[A-Z]:[\\/]",
        r"\\\\",
        r"/",
        r"(?i)(?<![A-Za-z0-9])[0-9a-f]{16,}(?![A-Za-z0-9])",
    )
    assert not any(re.search(pattern, text) for pattern in forbidden_markers)


def test_document_describes_a_proposal_not_verified_blinding() -> None:
    document = " ".join(DOC_PATH.read_text(encoding="utf-8").split())
    assert (
        "It does not run an evaluation, implement an assignment resolver, "
        "attest an actor, or prove that a real study is double blind."
    ) in document
    assert "These roles are unassigned." in document
    assert (
        "No access control, assignment, or human observation is implemented "
        "or verified by this document."
    ) in document


def test_document_warns_that_content_and_hashes_can_defeat_blinding() -> None:
    document = " ".join(DOC_PATH.read_text(encoding="utf-8").split())
    assert (
        "Content can reveal an assignment even when identifying fields "
        "are removed."
    ) in document
    assert "Digests identify content; they are not anonymization." in document
    assert (
        "Do not export private linkage hashes as a substitute for "
        "confidential custody."
    ) in document


def test_document_preserves_history_and_separate_publication_gates() -> None:
    document = " ".join(DOC_PATH.read_text(encoding="utf-8").split())
    assert "No actual aggregate is included or authorized here." in document
    assert "Approval applies to its stated artifacts and actions." in document
    assert (
        "History review is required separately; removing text from the "
        "current tree does not clear earlier versions."
    ) in document
    assert (
        "This candidate does not grant publication authority, change "
        "repository visibility, unblind an evaluation, or promote a private result."
    ) in document
    assert "`hold_for_review`" in document
    assert "`candidate_only`" in document
