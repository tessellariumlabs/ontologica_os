from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


DIMS = ("novelty", "risk", "coherence", "embodiment")


@dataclass(frozen=True)
class Tessera:
    id: str
    label: str
    fields: Mapping[str, float]


def project_tesserae(tesserae: list[Tessera]) -> tuple[float, ...]:
    """Toy deterministic projection. Noncanonical and intentionally simple."""
    if not tesserae:
        return tuple(0.0 for _ in DIMS)

    values: list[float] = []
    for dim in DIMS:
        total = sum(float(t.fields.get(dim, 0.0)) for t in tesserae)
        values.append(round(total / len(tesserae), 6))
    return tuple(values)


if __name__ == "__main__":
    sample = [
        Tessera("t1", "operator choice", {"novelty": 0.6, "risk": 0.2, "coherence": 0.9, "embodiment": 0.4}),
        Tessera("t2", "surface preview", {"novelty": 0.4, "risk": 0.1, "coherence": 0.8, "embodiment": 0.7}),
    ]
    print(project_tesserae(sample))
