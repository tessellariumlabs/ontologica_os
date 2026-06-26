# Noncanonical toy example.
# Demonstrates public Ontologica OS vocabulary only.
# Not production code; no implementation rights are granted.

from __future__ import annotations

import json
from pathlib import Path

from ontologica_os_public import run_proofing_demo


ROOT = Path(__file__).resolve().parents[1]
PRIOR = ROOT / "fixtures" / "proofing" / "prior_tesserae.json"
CANDIDATE = ROOT / "fixtures" / "proofing" / "candidate_tesserae.json"
OUT_DIR = ROOT / "sample_outputs" / "proofing_demo"


if __name__ == "__main__":
    summary = run_proofing_demo(PRIOR, CANDIDATE, OUT_DIR)
    print(json.dumps(summary, indent=2, sort_keys=True))
