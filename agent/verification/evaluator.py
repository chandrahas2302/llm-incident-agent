def evaluate_verification(health_result: dict) -> dict:
    if health_result["healthy"]:
        return {
            "status": "resolved",
            "confidence": 0.8
        }

    return {
        "status": "unresolved",
        "confidence": 0.3
    }
