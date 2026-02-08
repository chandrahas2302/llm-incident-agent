from datetime import datetime
from agent.memory.models import IncidentMemory
from agent.memory.store import save_memory

def learn_from_incident(incident, healing_result, evaluation):
    memory = IncidentMemory(
        incident_id=incident.incident_id,
        service=incident.service,
        action_taken=healing_result.get("action", "none"),
        outcome=evaluation["status"],
        confidence=evaluation["confidence"],
        timestamp=datetime.utcnow(),
        metadata={
            "symptoms": incident.symptoms
        }
    )

    save_memory(memory.dict())
