import json
from pathlib import Path

MEMORY_FILE = Path("data/incident_memory.json")
MEMORY_FILE.parent.mkdir(exist_ok=True)

if not MEMORY_FILE.exists():
    MEMORY_FILE.write_text("[]")

def load_memory():
    return json.loads(MEMORY_FILE.read_text())

def save_memory(entry: dict):
    memory = load_memory()
    memory.append(entry)
    MEMORY_FILE.write_text(json.dumps(memory, indent=2, default=str))
