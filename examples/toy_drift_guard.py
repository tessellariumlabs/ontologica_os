from __future__ import annotations

from math import sqrt


def l2_delta(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    if len(a) != len(b):
        raise ValueError("projection vectors must have equal length")
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def drift_decision(prior: tuple[float, ...], candidate: tuple[float, ...], warn: float = 0.05, hold: float = 0.15) -> dict[str, object]:
    delta = round(l2_delta(prior, candidate), 6)
    if delta >= hold:
        decision = "hold_for_review"
    elif delta >= warn:
        decision = "warn"
    else:
        decision = "pass"
    return {
        "receipt_type": "toy_drift_guard",
        "authority_ceiling": "candidate_only",
        "projection_delta_l2": delta,
        "decision": decision,
    }


if __name__ == "__main__":
    print(drift_decision((0.5, 0.2, 0.8, 0.4), (0.52, 0.25, 0.76, 0.43)))
