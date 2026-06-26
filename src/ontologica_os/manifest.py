import hashlib
import json
from typing import Any


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_json(value: Any) -> str:
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def build_manifest(manifest_id: str, kernel_id: str, kernel_version: str, inputs: list[dict], outputs: list[dict], receipts: list[dict], prior_manifests: list[str] | None = None) -> dict:
    manifest = {
        "manifest_id": manifest_id,
        "schema_version": "ontologica.manifest.v1",
        "authority_ceiling": "candidate_only",
        "kernel": {
            "id": kernel_id,
            "version": kernel_version,
            "sha256": hashlib.sha256(f"{kernel_id}:{kernel_version}".encode("utf-8")).hexdigest(),
        },
        "inputs": inputs,
        "outputs": outputs,
        "receipts": receipts,
        "prior_manifests": prior_manifests or [],
        "promotion": {"status": "hold", "reason": "public reference; noncanonical"},
        "noncanonical": True,
    }
    manifest["sha256"] = sha256_json(manifest)
    return manifest
