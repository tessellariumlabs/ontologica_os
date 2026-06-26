# Noncanonical toy example.
# Category-marker warning only.
# Does not explain reserved concepts.

from __future__ import annotations

import hashlib
import json
from typing import Any

AUTHORITY_CEILING = "candidate_only"


def stable_json_sha256(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_category_warning_receipt(text: str, category: str, markers: list[str]) -> dict[str, Any]:
    lowered = text.lower()
    hits = [marker for marker in markers if marker.lower() in lowered]
    decision = "hold_for_rights_holder_review" if hits else "pass_public_boundary"
    receipt = {
        "receipt_id": "toy_category_warning_001",
        "receipt_type": "category_boundary_warning",
        "authority_ceiling": AUTHORITY_CEILING,
        "category": category,
        "decision": decision,
        "severity": "warning" if hits else "none",
        "markers_detected": hits,
        "notes": [
            "Synthetic public warning receipt.",
            "This guard detects category markers only.",
            "It does not explain the reserved concept.",
        ],
    }
    receipt["receipt_sha256"] = stable_json_sha256(receipt)
    return receipt
