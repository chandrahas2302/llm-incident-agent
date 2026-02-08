def build_prompt(incident, memory_analysis):
    return f"""
You are an SRE assistant.

Incident:
Service: {incident.service}
Severity: {incident.severity}
Symptoms: {incident.symptoms}

Past Analysis:
{memory_analysis}

Question:
What is the safest corrective action and why?
"""
