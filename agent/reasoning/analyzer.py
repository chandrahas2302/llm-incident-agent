from agent.memory.store import load_memory

def analyze_past_incidents(service: str, symptoms: list) -> dict:
    memory = load_memory()

    relevant = [
        m for m in memory
        if m["service"] == service
        and set(symptoms).issubset(set(m["metadata"].get("symptoms", [])))
    ]

    if not relevant:
        return {
            "found": False
        }

    # Score actions based on success
    scores = {}
    for entry in relevant:
        action = entry["action_taken"]
        score = entry["confidence"]
        scores[action] = scores.get(action, 0) + score

    best_action = max(scores, key=scores.get)

    return {
        "found": True,
        "best_action": best_action,
        "scores": scores
    }
