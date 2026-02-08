ALLOWED_ACTIONS = ["restart", "scale"]

def is_action_allowed(action_plan: dict) -> bool:
    action = action_plan.get("action")

    if action not in ALLOWED_ACTIONS:
        return False

    # Safety limits
    if action == "scale" and action_plan.get("replicas", 0) > 5:
        return False

    return True
