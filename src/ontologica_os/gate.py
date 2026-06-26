def decide(status: str, approved: bool) -> dict:
    if status == "deny":
        result = "deny"
    elif approved:
        result = "promote"
    else:
        result = "hold"
    return {"status": result, "noncanonical": True}
