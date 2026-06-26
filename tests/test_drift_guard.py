import unittest

from ontologica_os.drift import compare_projections
from ontologica_os.kernel import project_tesserae


class DriftGuardTests(unittest.TestCase):
    def test_identical_projection_passes(self):
        prior = project_tesserae([{"id": "a", "fields": {"novelty": 0.5}}])
        candidate = project_tesserae([{"id": "a", "fields": {"novelty": 0.5}}])
        report = compare_projections(prior, candidate)
        self.assertEqual(report["decision"], "pass")
        self.assertEqual(report["projection_delta_l2"], 0)

    def test_large_projection_drift_denies(self):
        prior = project_tesserae([{"id": "a", "fields": {"risk": 0.0}}])
        candidate = project_tesserae([{"id": "b", "fields": {"risk": 1.0}}])
        report = compare_projections(prior, candidate)
        self.assertEqual(report["decision"], "deny")


if __name__ == "__main__":
    unittest.main()
