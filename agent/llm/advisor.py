from agent.llm.client import LLMClient
from agent.llm.prompt import build_prompt

def llm_advise(incident, memory_analysis):
    client = LLMClient()
    prompt = build_prompt(incident, memory_analysis)

    response = client.ask(prompt)

    return response
