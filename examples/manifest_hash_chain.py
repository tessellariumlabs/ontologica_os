from ontologica_os.kernel import project_tesserae, tessera_sha
from ontologica_os.manifest import build_manifest


def main() -> None:
    tessera = {"id": "public_chain_001", "label": "manifest", "fields": {"novelty": 0.5, "risk": 0.1, "coherence": 0.9, "embodiment": 0.2}}
    projection = project_tesserae([tessera])

    first = build_manifest(
        "public_manifest_001",
        projection["kernel_id"],
        projection["kernel_version"],
        [{"id": tessera["id"], "sha256": tessera_sha(tessera)}],
        [{"id": "public_projection_001", "sha256": projection["sha256"]}],
        [],
    )

    second = build_manifest(
        "public_manifest_002",
        projection["kernel_id"],
        projection["kernel_version"],
        [{"id": tessera["id"], "sha256": tessera_sha(tessera)}],
        [{"id": "public_projection_001", "sha256": projection["sha256"]}],
        [],
        [first["sha256"]],
    )

    print(first["sha256"])
    print(second["prior_manifests"])
    print(second["sha256"])


if __name__ == "__main__":
    main()
