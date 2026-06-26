# Noncanonical toy example.
# Demonstrates public Ontologica OS vocabulary only.
# Not production code; no implementation rights are granted.

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from math import sqrt
from pathlib import Path
from typing import Any, Iterable, Mapping

DIMS = ("novelty", "risk", "coherence", "embodiment")
KERNEL_ID = "toy_public_math_kernel"
KERNEL_VERSION = "1.0.0rc1"
AUTHORITY_CEILING = "candidate_only"


@dataclass(frozen=True)
class Tessera:
    id: str
    label: str
    fields: Mapping[str, float]


def stable_json_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_tesserae(payload: Iterable[Mapping[str, Any]]) -> list[Tessera]:
    tesserae: list[Tessera] = []
    for item in payload:
        tesserae.append(
            Tessera(
                id=str(item["id"]),
                label=str(item["label"]),
                fields={str(k): float(v) for k, v in dict(item.get("fields", {})).items()},
            )
        )
    return tesserae


def project_tesserae(tesserae: list[Tessera], dims: tuple[str, ...] = DIMS) -> dict[str, Any]:
    if not tesserae:
        vector = [0.0 for _ in dims]
    else:
        vector = []
        for dim in dims:
            total = sum(float(t.fields.get(dim, 0.0)) for t in tesserae)
            vector.append(round(total / len(tesserae), 6))

    projection = {
        "projection_type": "toy_lattice_projection",
        "kernel_id": KERNEL_ID,
        "kernel_version": KERNEL_VERSION,
        "authority_ceiling": AUTHORITY_CEILING,
        "dimensions": list(dims),
        "tessera_ids": [t.id for t in tesserae],
        "vector": vector,
    }
    projection["projection_sha256"] = stable_json_sha256(projection)
    return projection


def build_manifest(label: str, source_payload: Any, projection: Mapping[str, Any]) -> dict[str, Any]:
    source_sha = stable_json_sha256(source_payload)
    projection_sha = stable_json_sha256(projection)
    manifest = {
        "manifest_id": f"toy_manifest_{label}",
        "schema_version": "toy.manifest.v1",
        "authority_ceiling": AUTHORITY_CEILING,
        "kernel": {
            "id": KERNEL_ID,
            "version": KERNEL_VERSION,
        },
        "inputs": [
            {
                "id": f"toy_tessera_set_{label}",
                "sha256": source_sha,
            }
        ],
        "outputs": [
            {
                "id": f"toy_projection_{label}",
                "sha256": projection_sha,
            }
        ],
        "receipts": [],
        "promotion": {
            "status": "hold",
            "reason": "public proofing demo is noncanonical",
        },
    }
    manifest["manifest_sha256"] = stable_json_sha256(manifest)
    return manifest


def l2_delta(prior: list[float], candidate: list[float]) -> float:
    if len(prior) != len(candidate):
        raise ValueError("projection vectors must have equal length")
    return round(sqrt(sum((a - b) ** 2 for a, b in zip(prior, candidate))), 6)


def build_drift_receipt(
    prior_manifest: Mapping[str, Any],
    candidate_manifest: Mapping[str, Any],
    prior_projection: Mapping[str, Any],
    candidate_projection: Mapping[str, Any],
) -> dict[str, Any]:
    delta = l2_delta(list(prior_projection["vector"]), list(candidate_projection["vector"]))
    if delta >= 0.15:
        drift_decision = "hold_for_review"
    elif delta >= 0.05:
        drift_decision = "warn"
    else:
        drift_decision = "pass"

    receipt = {
        "receipt_id": "toy_drift_receipt_001",
        "receipt_type": "drift_guard",
        "authority_ceiling": AUTHORITY_CEILING,
        "prior_manifest": prior_manifest["manifest_id"],
        "prior_manifest_sha256": prior_manifest["manifest_sha256"],
        "candidate_manifest": candidate_manifest["manifest_id"],
        "candidate_manifest_sha256": candidate_manifest["manifest_sha256"],
        "checks": {
            "schema_drift": "pass",
            "projection_drift": drift_decision,
            "authority_drift": "pass",
            "receipt_completeness": "pass",
        },
        "drift": {
            "projection_delta_l2": delta,
            "prior_vector": prior_projection["vector"],
            "candidate_vector": candidate_projection["vector"],
            "dimensions": prior_projection["dimensions"],
        },
        "decision": drift_decision,
        "notes": [
            "Synthetic public receipt.",
            "A receipt provides evidence; it does not crown truth.",
        ],
    }
    receipt["receipt_sha256"] = stable_json_sha256(receipt)
    return receipt


def build_promotion_report(receipt: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Toy Promotion Report",
            "",
            "Status: `hold_for_review`",
            "",
            "This report is synthetic and noncanonical.",
            "",
            "## Drift Evidence",
            "",
            f"- Drift decision: `{receipt['decision']}`",
            f"- Projection delta L2: `{receipt['drift']['projection_delta_l2']}`",
            f"- Receipt SHA-256: `{receipt['receipt_sha256']}`",
            "",
            "## Public Gate Decision",
            "",
            "The public gate holds the candidate for review because this repository cannot promote durable truth.",
            "",
            "## Boundary",
            "",
            "This demo proves the public vocabulary path only: projection, manifest identity, drift receipt, and gate decision.",
            "It does not publish private math, private manifests, private receipts, private routing, private runtime logic, or private authority paths.",
            "",
        ]
    )


def build_proof_packet(
    prior_manifest: Mapping[str, Any],
    candidate_manifest: Mapping[str, Any],
    drift_receipt: Mapping[str, Any],
) -> dict[str, Any]:
    packet = {
        "packet_id": "toy_proof_packet_001",
        "schema_version": "toy.proof_packet.v1",
        "status": "noncanonical",
        "authority_ceiling": AUTHORITY_CEILING,
        "inputs": [
            {
                "id": "prior_tessera_fixture",
                "path": "fixtures/proofing/prior_tesserae.json",
                "synthetic": True,
                "notes": "Synthetic prior candidate material.",
            },
            {
                "id": "candidate_tessera_fixture",
                "path": "fixtures/proofing/candidate_tesserae.json",
                "synthetic": True,
                "notes": "Synthetic candidate material with small drift.",
            },
        ],
        "projections": [
            {
                "id": "prior_projection",
                "path": "sample_outputs/proofing_demo/prior_projection.json",
                "synthetic": True,
                "notes": "Toy projection generated by the public math demo.",
            },
            {
                "id": "candidate_projection",
                "path": "sample_outputs/proofing_demo/candidate_projection.json",
                "synthetic": True,
                "notes": "Toy projection generated by the public math demo.",
            },
        ],
        "manifests": [
            {
                "id": "prior_manifest",
                "path": "sample_outputs/proofing_demo/prior_manifest.json",
                "sha256": prior_manifest["manifest_sha256"],
                "synthetic": True,
                "notes": "Synthetic manifest identity only; not truth.",
            },
            {
                "id": "candidate_manifest",
                "path": "sample_outputs/proofing_demo/candidate_manifest.json",
                "sha256": candidate_manifest["manifest_sha256"],
                "synthetic": True,
                "notes": "Synthetic manifest identity only; not truth.",
            },
        ],
        "receipt": {
            "id": "drift_receipt",
            "path": "sample_outputs/proofing_demo/drift_receipt.json",
            "sha256": drift_receipt["receipt_sha256"],
            "synthetic": True,
            "notes": "Synthetic evidence receipt; does not crown truth.",
        },
        "gate_decision": {
            "decision": "hold_for_review",
            "reason": "Public packet cannot promote durable truth or claim private authority.",
        },
        "boundary_assertions": {
            "contains_private_math": False,
            "contains_real_manifest_lineage": False,
            "contains_real_receipts": False,
            "contains_private_routing": False,
            "contains_runtime_authority": False,
            "contains_hardware_authority": False,
            "grants_implementation_rights": False,
        },
    }
    packet["packet_sha256"] = stable_json_sha256(packet)
    return packet


def run_proofing_demo(prior_path: Path, candidate_path: Path, out_dir: Path) -> dict[str, Any]:
    prior_payload = read_json(prior_path)
    candidate_payload = read_json(candidate_path)

    prior_projection = project_tesserae(parse_tesserae(prior_payload))
    candidate_projection = project_tesserae(parse_tesserae(candidate_payload))

    prior_manifest = build_manifest("prior", prior_payload, prior_projection)
    candidate_manifest = build_manifest("candidate", candidate_payload, candidate_projection)
    drift_receipt = build_drift_receipt(prior_manifest, candidate_manifest, prior_projection, candidate_projection)
    proof_packet = build_proof_packet(prior_manifest, candidate_manifest, drift_receipt)
    report = build_promotion_report(drift_receipt)

    write_json(out_dir / "prior_projection.json", prior_projection)
    write_json(out_dir / "candidate_projection.json", candidate_projection)
    write_json(out_dir / "prior_manifest.json", prior_manifest)
    write_json(out_dir / "candidate_manifest.json", candidate_manifest)
    write_json(out_dir / "drift_receipt.json", drift_receipt)
    write_json(out_dir / "proof_packet.json", proof_packet)
    (out_dir / "promotion_report.md").write_text(report, encoding="utf-8")

    return {
        "prior_manifest": prior_manifest["manifest_id"],
        "candidate_manifest": candidate_manifest["manifest_id"],
        "drift_decision": drift_receipt["decision"],
        "promotion_status": "hold_for_review",
        "proof_packet": proof_packet["packet_id"],
        "output_dir": str(out_dir),
    }
