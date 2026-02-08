def restart_service(service: str):
    # Simulated action (real version will call K8s / system)
    print(f"[ACTION] Restarting service: {service}")
    return {"action": "restart", "service": service, "status": "success"}


def scale_service(service: str, replicas: int):
    print(f"[ACTION] Scaling service {service} to {replicas} replicas")
    return {
        "action": "scale",
        "service": service,
        "replicas": replicas,
        "status": "success"
    }
