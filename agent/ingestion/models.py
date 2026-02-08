from pydantic import BaseModel
from typing import Dict, Optional
from datetime import datetime

class Signal(BaseModel):
    source: str
    type: str
    service: str
    severity: str
    timestamp: datetime
    payload: Dict
    metadata: Optional[Dict] = {}
