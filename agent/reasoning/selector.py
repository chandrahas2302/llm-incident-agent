from agent.healing.decision import decide_action

def select_action(incident, memory_analysis: dict) -> dict:
    # If memory has a proven action → use it
    if memory_analysis.get("found"):
        return {
            "action": memory_analysis["best_action"]
        }

    # Otherwise fall back to rule-based decision
    return decide_action(incident)
