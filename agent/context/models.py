from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class IncidentContext(BaseModel):
    incident_id: str
    service: str
    severity: str
    start_time: datetime
    end_time: datetime
    signals: List[Dict]
    symptoms: List[str]
