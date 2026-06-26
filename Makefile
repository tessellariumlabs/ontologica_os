.PHONY: proofing-demo test

proofing-demo:
	PYTHONPATH=src python examples/run_proofing_demo.py

test:
	PYTHONPATH=src pytest
