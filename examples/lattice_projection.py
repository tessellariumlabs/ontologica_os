from ontologica_os.kernel import project_tesserae


def main() -> None:
    tesserae = [
        {"id": "public_001", "label": "proposal", "fields": {"novelty": 0.7, "risk": 0.2, "coherence": 0.9, "embodiment": 0.1}},
        {"id": "public_002", "label": "evidence", "fields": {"novelty": 0.4, "risk": 0.3, "coherence": 0.8, "embodiment": 0.2}},
    ]
    print(project_tesserae(tesserae))


if __name__ == "__main__":
    main()
