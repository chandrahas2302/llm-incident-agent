def is_incident(incident) -> bool:
    if incident.severity == "critical":
        return True

    if len(incident.signals) >= 3:
        return True

    return False
