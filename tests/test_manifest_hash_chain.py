import unittest

from ontologica_os.kernel import project_tesserae, tessera_sha
from ontologica_os.manifest import build_manifest


class ManifestHashChainTests(unittest.TestCase):
    def test_manifest_sha_changes_with_lineage(self):
        tessera = {"id": "x", "fields": {"novelty": 0.2, "risk": 0.1, "coherence": 0.9, "embodiment": 0.3}}
        projection = project_tesserae([tessera])
        first = build_manifest("m1", projection["kernel_id"], projection["kernel_version"], [{"id": "x", "sha256": tessera_sha(tessera)}], [{"id": "p", "sha256": projection["sha256"]}], [])
        second = build_manifest("m2", projection["kernel_id"], projection["kernel_version"], [{"id": "x", "sha256": tessera_sha(tessera)}], [{"id": "p", "sha256": projection["sha256"]}], [], [first["sha256"]])
        self.assertNotEqual(first["sha256"], second["sha256"])
        self.assertEqual(second["prior_manifests"], [first["sha256"]])
        self.assertTrue(first["noncanonical"])


if __name__ == "__main__":
    unittest.main()
