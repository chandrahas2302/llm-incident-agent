from datetime import datetime, timedelta

VERIFICATION_WINDOW_MINUTES = 3

def check_service_health(service: str, signals: list) -> dict:
    """
    Check if the service has any recent critical signals.
    """

    now = datetime.utcnow()
    window_start = now - timedelta(minutes=VERIFICATION_WINDOW_MINUTES)

    recent_critical = [
        s for s in signals
        if s["service"] == service
        and s["severity"] == "critical"
        and datetime.fromisoformat(s["timestamp"]) >= window_start
    ]

    return {
        "service": service,
        "verification_window_minutes": VERIFICATION_WINDOW_MINUTES,
        "critical_signals_found": len(recent_critical),
        "healthy": len(recent_critical) == 0
    }
