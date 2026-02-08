from pydantic import BaseModel
from datetime import datetime
from typing import Dict

class IncidentMemory(BaseModel):
    incident_id: str
    service: str
    action_taken: str
    outcome: str          # resolved / unresolved
    confidence: float
    timestamp: datetime
    metadata: Dict = {}
