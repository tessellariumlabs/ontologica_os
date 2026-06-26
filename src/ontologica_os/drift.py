from math import sqrt


def compare_projections(prior: dict, candidate: dict, warn_tolerance: float = 0.05, review_tolerance: float = 0.20) -> dict:
    deltas = [b - a for a, b in zip(prior["vector"], candidate["vector"])]
    delta_l2 = round(sqrt(sum(delta * delta for delta in deltas)), 6)
    changed_fields = [field for field, delta in zip(prior["field_order"], deltas) if round(abs(delta), 6) > 0]

    if delta_l2 == 0:
        decision = "pass"
    elif delta_l2 <= warn_tolerance:
        decision = "warn"
    elif delta_l2 <= review_tolerance:
        decision = "hold_for_review"
    else:
        decision = "deny"

    return {
        "projection_delta_l2": delta_l2,
        "changed_fields": changed_fields,
        "decision": decision,
        "authority_ceiling": "candidate_only",
        "noncanonical": True,
    }
