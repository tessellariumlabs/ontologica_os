import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class BoundaryTests(unittest.TestCase):
    def read(self, path: str) -> str:
        return (ROOT / path).read_text(encoding="utf-8")

    def test_readme_boundary(self):
        text = self.read("README.md")
        self.assertIn("not the canonical implementation", text)
        self.assertIn("not a source of durable truth", text)
        self.assertIn("clean-room reference implementation", text)

    def test_no_backflow_boundary(self):
        text = self.read("SANITIZATION.md")
        self.assertIn("No-Backflow", text)
        self.assertIn("synthetic and noncanonical", text)

    def test_project_boundary(self):
        text = self.read("BOUNDARY.md")
        self.assertIn("not canonical", text)
        self.assertIn("manual review", text)


if __name__ == "__main__":
    unittest.main()
