from __future__ import annotations

from ontologica_os_public import proofing


def test_public_math_kernel_stays_candidate_only() -> None:
    assert proofing.AUTHORITY_CEILING == "candidate_only"


def test_public_math_kernel_uses_only_toy_dimensions() -> None:
    assert proofing.DIMS == ("novelty", "risk", "coherence", "embodiment")


def test_public_promotion_report_never_promotes_truth() -> None:
    receipt = {
        "decision": "warn",
        "drift": {"projection_delta_l2": 0.1},
        "receipt_sha256": "synthetic_receipt_sha",
    }
    report = proofing.build_promotion_report(receipt)

    assert "hold_for_review" in report
    assert "cannot promote durable truth" in report
    assert "does not publish private math" in report


def test_drift_receipt_is_evidence_only() -> None:
    prior_projection = {
        "dimensions": list(proofing.DIMS),
        "vector": [0.1, 0.1, 0.9, 0.2],
    }
    candidate_projection = {
        "dimensions": list(proofing.DIMS),
        "vector": [0.12, 0.12, 0.88, 0.22],
    }
    prior_manifest = {
        "manifest_id": "toy_manifest_prior",
        "manifest_sha256": "prior_sha",
    }
    candidate_manifest = {
        "manifest_id": "toy_manifest_candidate",
        "manifest_sha256": "candidate_sha",
    }

    receipt = proofing.build_drift_receipt(
        prior_manifest,
        candidate_manifest,
        prior_projection,
        candidate_projection,
    )

    assert receipt["authority_ceiling"] == "candidate_only"
    assert receipt["decision"] in {"pass", "warn", "hold_for_review"}
    assert "A receipt provides evidence; it does not crown truth." in receipt["notes"]
