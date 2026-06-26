from __future__ import annotations

import hashlib
import json
from typing import Any


def stable_json_sha256(value: Any) -> str:
    """Return a deterministic SHA-256 for JSON-like data."""
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def build_toy_manifest(input_payload: dict[str, Any], output_payload: dict[str, Any]) -> dict[str, Any]:
    input_sha = stable_json_sha256(input_payload)
    output_sha = stable_json_sha256(output_payload)
    manifest = {
        "manifest_id": "toy_manifest_001",
        "schema_version": "toy.manifest.v1",
        "authority_ceiling": "candidate_only",
        "kernel": {"id": "toy_math_kernel", "version": "0.1.0"},
        "inputs": [{"id": "toy_input", "sha256": input_sha}],
        "outputs": [{"id": "toy_output", "sha256": output_sha}],
        "receipts": [],
        "promotion": {"status": "hold", "reason": "synthetic example; noncanonical"},
    }
    manifest["manifest_sha256"] = stable_json_sha256(manifest)
    return manifest


if __name__ == "__main__":
    print(json.dumps(build_toy_manifest({"a": 1}, {"b": 2}), indent=2))
