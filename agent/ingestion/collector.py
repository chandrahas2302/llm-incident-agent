from datetime import datetime
from .models import Signal

def build_metric_signal(service: str, cpu: int):
    return Signal(
        source="prometheus",
        type="metric",
        service=service,
        severity="critical" if cpu > 90 else "warning",
        timestamp=datetime.utcnow(),
        payload={"cpu": cpu},
        metadata={"threshold": 90}
    )
