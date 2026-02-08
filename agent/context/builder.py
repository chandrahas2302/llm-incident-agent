from datetime import datetime, timedelta
from uuid import uuid4
from .models import IncidentContext

TIME_WINDOW_MINUTES = 1  # testing
SEVERITY_ORDER = ["info", "warning", "critical"]

def parse_ts(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", ""))

def build_incidents(signals: list) -> list:
    incidents = []
    grouped = {}

    for signal in signals:
        service = signal.get("service")
        if not service:
            continue
        grouped.setdefault(service, []).append(signal)

    for service, service_signals in grouped.items():
        now = datetime.utcnow()
        window_start = now - timedelta(minutes=TIME_WINDOW_MINUTES)

        recent = []
        for s in service_signals:
            try:
                if parse_ts(s["timestamp"]) >= window_start:
                    recent.append(s)
            except Exception:
                continue

        if not recent:
            continue

        severity = max(
            (s.get("severity", "info") for s in recent),
            key=lambda x: SEVERITY_ORDER.index(x)
            if x in SEVERITY_ORDER else 0
        )

        symptoms = list({s.get("type", "unknown") for s in recent})

        incidents.append(
            IncidentContext(
                incident_id=str(uuid4()),
                service=service,
                severity=severity,
                start_time=min(parse_ts(s["timestamp"]) for s in recent),
                end_time=max(parse_ts(s["timestamp"]) for s in recent),
                signals=recent,
                symptoms=symptoms
            )
        )

    return incidents
