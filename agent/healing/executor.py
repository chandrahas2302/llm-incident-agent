from agent.healing.actions import restart_service, scale_service
from agent.healing.policies import is_action_allowed
from agent.healing.decision import decide_action
from agent.reasoning.analyzer import analyze_past_incidents
from agent.reasoning.selector import select_action
from agent.llm.advisor import llm_advise


def execute_healing(incident):
    memory_analysis = analyze_past_incidents(
        incident.service,
        incident.symptoms
    )

    action_plan = select_action(incident, memory_analysis)

    if action_plan["action"] == "none":
        return {"status": "no_action"}

    if not is_action_allowed(action_plan):
        return {
            "status": "blocked_by_policy",
            "action_plan": action_plan
        }

    if action_plan["action"] == "restart":
        return restart_service(incident.service)

    if action_plan["action"] == "scale":
        return scale_service(
            incident.service,
            action_plan.get("replicas", 3)
        )

    return {"status": "unknown_action"}
