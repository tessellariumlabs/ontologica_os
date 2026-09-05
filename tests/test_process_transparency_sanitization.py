from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = (
    ROOT
    / "sample_outputs"
    / "reviews"
    / "process_transparency_sanitization_ledger.json"
)
DOC_PATH = ROOT / "docs" / "process-transparency-and-sanitization.md"


def load_ledger() -> dict[str, object]:
    return json.loads(LEDGER_PATH.read_text(encoding="utf-8"))


def test_public_ledger_is_candidate_only_and_held() -> None:
    ledger = load_ledger()

    assert ledger["ledger_class"] == "synthetic_noncanonical_public_summary"
    assert ledger["status"] == "hold_for_review"
    assert ledger["authority_ceiling"] == "candidate_only"
    assert ledger["emphera_intake"] == "human_controlled_candidate"


def test_source_material_never_crosses_the_public_membrane() -> None:
    source_boundary = load_ledger()["source_boundary"]

    assert source_boundary["authorship_basis"] == (
        "newly_authored_public_boundary_language"
    )
    for field, value in source_boundary.items():
        if field != "authorship_basis":
            assert value is False


def test_every_prospective_gate_fails_closed() -> None:
    gates = load_ledger()["prospective_gates"]

    assert gates
    assert all(gate["failure_outcome"] == "exclude_and_hold" for gate in gates)
    assert {gate["posture"] for gate in gates} <= {
        "pass_public_boundary",
        "hold_for_review",
    }


def test_dwell_rotates_without_scoring_or_self_promotion() -> None:
    dwell = load_ledger()["dwell"]
    rounds = dwell["review_rounds"]

    assert dwell["mode"] == "bounded_qualitative_review"
    assert dwell["numeric_scoring_used"] is False
    assert dwell["thresholds_used"] is False
    assert dwell["automatic_promotion_on_repetition"] is False
    assert dwell["strong_binding_claimed"] is False
    assert dwell["repetition_response"] == "rotate_to_an_adjacent_review_lens"
    assert dwell["bounded_exhaustion_outcome"] == "hold_for_review"
    assert len(rounds) >= 2
    assert len({round_["lens"] for round_ in rounds}) == len(rounds)
    assert all(round_["question"] and round_["backfill"] for round_ in rounds)


def test_publication_authority_remains_false() -> None:
    publication = load_ledger()["publication"]

    assert publication == {
        "target": "review_branch_only",
        "merge_allowed": False,
        "visibility_change_allowed": False,
        "publication_authority_granted": False,
        "history_review": "required_before_visibility_change",
        "current_tree_removal_counts_as_history_clearance": False,
        "rights_holder_review_required": True,
        "technical_boundary_review_required": True,
    }


def test_new_public_packet_has_no_obvious_secret_or_local_path_markers() -> None:
    candidate_paths = [ROOT / path for path in load_ledger()["public_candidate_files"]]
    assert all(path.is_file() for path in candidate_paths)
    packet = "\n".join(path.read_text(encoding="utf-8") for path in candidate_paths)
    forbidden_patterns = (
        r"(?i)github_" + r"pat_",
        r"(?i)gh[opsu]_[A-Za-z0-9]",
        r"(?i)sk-[A-Za-z0-9]",
        r"AKIA[0-9A-Z]",
        r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
        r"(?i)Bearer\s+[A-Za-z0-9._-]+",
        r"(?i)api[_-]?key\s*[:=]",
        r"[A-Za-z]:\\",
    )

    assert not any(re.search(pattern, packet) for pattern in forbidden_patterns)


def test_document_disclaims_scrubbing_and_clearance_authority() -> None:
    document = DOC_PATH.read_text(encoding="utf-8")
    normalized_document = " ".join(document.split())

    assert "does not implement a scrubber" in document
    assert "Redaction alone is never evidence" in normalized_document
    assert "Copyrighted source text is not made publishable" in normalized_document
    assert "does not approve public release" in document
    assert "does not sanitize prior Git" in normalized_document
    assert "status: hold_for_review" in document
