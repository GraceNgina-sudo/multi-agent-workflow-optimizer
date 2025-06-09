from app_orchestrator import AppOrchestrator

def handle_user_request(input_data):
    orchestrator_instance = AppOrchestrator()
    return orchestrator_instance.run_workflow_cycle(input_data=input_data)
