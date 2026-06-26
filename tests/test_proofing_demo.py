from __future__ import annotations

from pathlib import Path

from ontologica_os_public.proofing import (
    build_drift_receipt,
    build_manifest,
    parse_tesserae,
    project_tesserae,
    read_json,
    run_proofing_demo,
)

ROOT = Path(__file__).resolve().parents[1]
PRIOR = ROOT / "fixtures" / "proofing" / "prior_tesserae.json"
CANDIDATE = ROOT / "fixtures" / "proofing" / "candidate_tesserae.json"


def test_toy_projection_is_deterministic() -> None:
    payload = read_json(PRIOR)
    projection = project_tesserae(parse_tesserae(payload))

    assert projection["authority_ceiling"] == "candidate_only"
    assert projection["dimensions"] == ["novelty", "risk", "coherence", "embodiment"]
    assert projection["vector"] == [0.35, 0.166667, 0.906667, 0.59]


def test_toy_drift_receipt_warns_without_promoting() -> None:
    prior_payload = read_json(PRIOR)
    candidate_payload = read_json(CANDIDATE)
    prior_projection = project_tesserae(parse_tesserae(prior_payload))
    candidate_projection = project_tesserae(parse_tesserae(candidate_payload))
    prior_manifest = build_manifest("prior", prior_payload, prior_projection)
    candidate_manifest = build_manifest("candidate", candidate_payload, candidate_projection)

    receipt = build_drift_receipt(prior_manifest, candidate_manifest, prior_projection, candidate_projection)

    assert receipt["decision"] == "warn"
    assert receipt["authority_ceiling"] == "candidate_only"
    assert receipt["checks"]["authority_drift"] == "pass"
    assert receipt["drift"]["projection_delta_l2"] == 0.069041


def test_proofing_demo_writes_expected_artifacts(tmp_path: Path) -> None:
    summary = run_proofing_demo(PRIOR, CANDIDATE, tmp_path)

    assert summary["drift_decision"] == "warn"
    assert summary["promotion_status"] == "hold_for_review"
    assert (tmp_path / "prior_manifest.json").exists()
    assert (tmp_path / "candidate_manifest.json").exists()
    assert (tmp_path / "drift_receipt.json").exists()
    assert (tmp_path / "promotion_report.md").exists()
