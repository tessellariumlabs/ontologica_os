import unittest

from ontologica_os.kernel import FIELD_ORDER, project_tesserae


class LatticeProjectionTests(unittest.TestCase):
    def test_projection_is_deterministic(self):
        data = [
            {"id": "a", "fields": {"novelty": 1.0, "risk": 0.0, "coherence": 0.5, "embodiment": 0.25}},
            {"id": "b", "fields": {"novelty": 0.0, "risk": 1.0, "coherence": 0.5, "embodiment": 0.75}},
        ]
        first = project_tesserae(data)
        second = project_tesserae(data)
        self.assertEqual(first["vector"], [0.5, 0.5, 0.5, 0.5])
        self.assertEqual(first["sha256"], second["sha256"])
        self.assertEqual(first["field_order"], list(FIELD_ORDER))
        self.assertTrue(first["noncanonical"])


if __name__ == "__main__":
    unittest.main()
