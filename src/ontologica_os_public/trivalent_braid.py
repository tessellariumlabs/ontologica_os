# Noncanonical toy example.
# Demonstrates public Ontologica OS vocabulary only.
# Not production code; no implementation rights are granted.

from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping

AUTHORITY_CEILING = "candidate_only"

PUBLIC_POSTURES = (
    "pass_public_boundary",
    "warning_scar",
    "hold_for_rights_holder_review",
)

TRIVALENT_HOLD_CATEGORIES = (
    "mentions_trivalent_logic",
    "reveals_private_trivalent_rules",
)

WARNING_CATEGORIES = (
    "mentions_analysis_core",
    "mentions_workspace_topology",
    "mentions_atom_serving",
    "mentions_receipt_graph",
)

PROTECTED_CATEGORIES = (
    "reveals_private_math",
    "reveals_scoring_thresholds",
    "reveals_model_routing",
    "reveals_private_receipt_graph",
    "reveals_workspace_topology",
    "reveals_atom_store_schema",
    "reveals_production_policy_engine",
)


def stable_json_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def assess_trivalent_inner_braid(artifact_id: str, category_assertions: Mapping[str, bool]) -> dict[str, Any]:
    """Return a public leak-posture receipt.

    This is a qualitative public self-audit helper, not private trivalent logic.
    Any trivalent-logic disclosure request hard-holds for rights-holder review.
    """
    trivalent_hits = [name for name in TRIVALENT_HOLD_CATEGORIES if bool(category_assertions.get(name, False))]
    protected_hits = [name for name in PROTECTED_CATEGORIES if bool(category_assertions.get(name, False))]
    warning_hits = [name for name in WARNING_CATEGORIES if bool(category_assertions.get(name, False))]

    if trivalent_hits or protected_hits:
        posture = "hold_for_rights_holder_review"
    elif warning_hits:
        posture = "warning_scar"
    else:
        posture = "pass_public_boundary"

    receipt = {
        "receipt_id": "toy_trivalent_inner_braid_receipt_001",
        "receipt_type": "trivalent_inner_braid_public_leak_posture",
        "artifact_id": artifact_id,
        "authority_ceiling": AUTHORITY_CEILING,
        "posture": posture,
        "public_postures": list(PUBLIC_POSTURES),
        "trivalent_hold_categories_detected": trivalent_hits,
        "warning_categories_detected": warning_hits,
        "protected_categories_detected": protected_hits,
        "release_gate": "reassess_before_public_disclosure" if posture != "pass_public_boundary" else "candidate_only_no_promotion",
        "scar_required": posture in {"warning_scar", "hold_for_rights_holder_review"},
        "hold_required": posture == "hold_for_rights_holder_review",
        "notes": [
            "Synthetic public receipt.",
            "This does not publish private trivalent logic.",
            "Trivalent-logic disclosure requests hard-hold for rights-holder review.",
        ],
    }
    receipt["receipt_sha256"] = stable_json_sha256(receipt)
    return receipt
