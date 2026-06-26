from .manifest import sha256_json

FIELD_ORDER = ("novelty", "risk", "coherence", "embodiment")
KERNEL_ID = "public_reference_kernel"
KERNEL_VERSION = "0.1.0"


def tessera_sha(tessera: dict) -> str:
    fields = {name: float(tessera.get("fields", {}).get(name, 0.0)) for name in FIELD_ORDER}
    return sha256_json({
        "id": tessera["id"],
        "label": tessera.get("label", ""),
        "fields": fields,
        "noncanonical": True,
    })


def project_tesserae(tesserae: list[dict]) -> dict:
    if not tesserae:
        vector = [0.0 for _ in FIELD_ORDER]
    else:
        vector = []
        for name in FIELD_ORDER:
            total = sum(float(t.get("fields", {}).get(name, 0.0)) for t in tesserae)
            vector.append(round(total / len(tesserae), 6))

    projection = {
        "kernel_id": KERNEL_ID,
        "kernel_version": KERNEL_VERSION,
        "field_order": list(FIELD_ORDER),
        "tessera_ids": [t["id"] for t in tesserae],
        "vector": vector,
        "noncanonical": True,
    }
    projection["sha256"] = sha256_json(projection)
    return projection
