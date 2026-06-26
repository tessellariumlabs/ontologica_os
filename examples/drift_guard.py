from ontologica_os.drift import compare_projections
from ontologica_os.kernel import project_tesserae


def main() -> None:
    prior = project_tesserae([{"id": "prior", "fields": {"novelty": 0.5, "risk": 0.2, "coherence": 0.8, "embodiment": 0.1}}])
    candidate = project_tesserae([{"id": "candidate", "fields": {"novelty": 0.55, "risk": 0.22, "coherence": 0.77, "embodiment": 0.1}}])
    print(compare_projections(prior, candidate))


if __name__ == "__main__":
    main()
