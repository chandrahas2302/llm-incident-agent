def decide_action(incident):
    # Simple rule-based decisions

    if incident.severity == "critical":
        if "metric" in incident.symptoms:
            return {
                "action": "scale",
                "replicas": 3
            }

        if "event" in incident.symptoms:
            return {
                "action": "restart"
            }

    return {
        "action": "none"
    }
