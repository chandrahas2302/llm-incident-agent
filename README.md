# 🚀 Self-Healing Infrastructure Agent

> An autonomous, explainable, LLM-powered infrastructure remediation system built with FastAPI and Python.

---

## 📌 Overview

The **Self-Healing Infrastructure Agent** is a closed-loop, intelligent remediation system that:

- Observes infrastructure signals (metrics, logs, events)
- Detects incidents using time-window correlation
- Executes automated healing actions
- Verifies post-remediation health
- Learns from outcomes
- Uses LLM reasoning for explainability and advisory decisions

This project demonstrates **agentic DevOps architecture** combining deterministic safety with AI reasoning.

---

## 🧠 System Architecture

```
Signal Ingestion
      ↓
Incident Detection (Context Builder)
      ↓
Memory-Based Reasoning
      ↓
LLM Advisory Layer
      ↓
Policy Guardrails
      ↓
Remediation Executor
      ↓
Verification Engine
      ↓
Learning & Memory Store
```

---

## 🏗 Project Structure

```
self-healing-agent/
├── agent/
│   ├── ingestion/        # Signal intake
│   ├── context/          # Incident detection
│   ├── healing/          # Remediation logic
│   ├── verification/     # Post-heal validation
│   ├── memory/           # Persistent learning
│   ├── reasoning/        # Memory-based decisions
│   ├── llm/              # Hugging Face LLM advisor
│   └── config/           # Centralized configuration
├── data/
│   ├── signals.json
│   └── incident_memory.json
└── requirements.txt
```

---

## ⚙️ Core Capabilities

### ✅ Closed-Loop Automation
Observe → Detect → Heal → Verify → Learn

### ✅ Deterministic Safety
- Policy guardrails prevent unsafe actions
- LLM suggestions are advisory only

### ✅ Learning System
- Stores incident outcomes
- Improves action selection over time

### ✅ LLM Explainability
- Uses Hugging Face Inference API
- Provides human-readable reasoning
- Supports open-source instruction models

### ✅ No Vendor Lock-in
- No Azure dependency
- No environment variable requirement
- Fully configurable in-code

---

## 🔌 LLM Integration

Powered by **Hugging Face Inference API**.

Supported models:
- `mistralai/Mistral-7B-Instruct`
- `meta-llama/Llama-2-7b-chat`
- `google/gemma-7b-it`
- Any instruction-tuned model

The LLM:
- Suggests safest remediation action
- Explains reasoning
- Never bypasses policy controls

---

## 🛠 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/self-healing-agent.git
cd self-healing-agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
.\venv\Scripts\Activate.ps1
```

**Linux/macOS**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Agent

```bash
python -m agent.main
```

Open Swagger UI:

```
http://localhost:8000/docs
```

---

## 🧪 End-to-End Testing

### 1️⃣ Ingest Signal

POST `/ingest`

```json
{
  "source": "prometheus",
  "type": "metric",
  "service": "payments-api",
  "severity": "critical",
  "timestamp": "2026-01-31T16:10:00",
  "payload": { "cpu": 97 },
  "metadata": {}
}
```

---

### 2️⃣ Detect Incident

GET `/incidents`

---

### 3️⃣ Heal Incident

POST `/heal`

Expected response includes:

- Deterministic decision
- LLM advisory explanation
- Execution result
- Verification outcome
- Memory update

---

## 🔐 Safety Model

| Layer | Purpose |
|-------|--------|
| Rules | Baseline deterministic decisions |
| Memory | Experience-based optimization |
| LLM | Advisory reasoning only |
| Policies | Hard safety constraints |
| Verification | Closed-loop validation |

LLM suggestions are never executed directly without policy approval.

---

## 📊 Example Output

```json
{
  "decision": {
    "action": "restart",
    "llm_advice": {
      "enabled": true,
      "suggested_action": "restart",
      "explanation": "Based on CPU saturation and crash events..."
    }
  },
  "execution_result": {
    "status": "success"
  },
  "evaluation": {
    "status": "resolved",
    "confidence": 0.8
  }
}
```

---

## 🧠 Learning Mechanism

The agent stores:

- Incident symptoms
- Action taken
- Verification result
- Confidence score

Stored in:

```
data/incident_memory.json
```

Used for:
- Future action optimization
- Avoiding repeated failures
- Experience-based decisions

---

## 🚀 Future Enhancements

- Async LLM execution
- Vector memory (FAISS/Chroma)
- Kubernetes-native healing
- Multi-agent planner/executor architecture
- Grafana dashboard
- GitOps integration
- Circuit breaker for LLM failures

---

## 🎯 Use Cases

- DevOps automation
- Platform engineering
- SRE experimentation
- AI-powered incident management
- Autonomous infrastructure systems
- Research in agentic AI for operations

---

## 🏁 Why This Project Matters

This project demonstrates:

- Agentic system design
- Safe AI integration
- Deterministic + probabilistic reasoning
- Closed-loop automation
- Real-world DevOps architecture patterns

This is production-style infrastructure intelligence — not a toy demo.

---

## 👨‍💻 Author

Built as an exploration of self-healing infrastructure systems combining:

- Python
- FastAPI
- DevOps automation
- LLM reasoning
- Autonomous agent design
