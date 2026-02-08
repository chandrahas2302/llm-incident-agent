from fastapi import FastAPI
from .models import Signal
import json
from pathlib import Path
from agent.context.builder import build_incidents
from agent.context.detector import is_incident
from agent.healing.executor import execute_healing
from agent.verification.checker import check_service_health
from agent.verification.evaluator import evaluate_verification
from agent.memory.learner import learn_from_incident


app = FastAPI()

DATA_FILE = Path("data/signals.json")
DATA_FILE.parent.mkdir(exist_ok=True)

# Initialize file if not exists
if not DATA_FILE.exists():
    DATA_FILE.write_text("[]")

@app.post("/ingest")
def ingest_signal(signal: Signal):
    signals = json.loads(DATA_FILE.read_text())
    signals.append(signal.dict())
    DATA_FILE.write_text(json.dumps(signals, indent=2, default=str))

    return {
        "status": "received",
        "total_signals": len(signals)
    }
@app.get("/incidents")
def get_incidents():
    signals = json.loads(DATA_FILE.read_text())
    incidents = build_incidents(signals)

    return {
        "debug_signal_count": len(signals),
        "debug_signals": signals,
        "debug_incident_count": len(incidents),
        "debug_incidents_raw": [i.dict() for i in incidents]
    }

@app.post("/heal")
def heal_incidents():
    signals = json.loads(DATA_FILE.read_text())
    incidents = build_incidents(signals)

    results = []

    for incident in incidents:
        if not is_incident(incident):
            continue

        # STEP 3: Heal
        healing_result = execute_healing(incident)

        # STEP 4: Verify
        health = check_service_health(
            incident.service,
            signals
        )

        evaluation = evaluate_verification(health)
        learn_from_incident(
    incident,
    healing_result,
    evaluation
)


        results.append({
            "incident_id": incident.incident_id,
            "service": incident.service,
            "healing": healing_result,
            "verification": health,
            "evaluation": evaluation
        })

    return {
        "processed_incidents": len(results),
        "results": results
    }
