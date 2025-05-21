from datetime import datetime
from db import log_task, log_agent

class WorkflowCoordinator:
    def __init__(self, astra):
        self.astra = astra
    def start_workflow(self, task_name, input_daya):
        log_task(name=task_name, status="started")
        result = self.astra.run(input_data)
        log_agent(agent_name="Astra", action="Analyzed input", output=result)

class CoordinatorAgent(Agent):  
    def __init__(self, name, role="coordinator"):
        super().__init__(name, role)
        self.name = name
        self.worlflow_log = []

    def manage_workflow(self, planner, optimizer, executor):
        task = planner.create_task()
        if task:
            optimized_task = optimizer.optimize_task(task)
            result = executor.execute_task(optimized_task)
            executor.send_message("Orion", f"Execution result: {result}")
            self.workflow_log.append({
                "original": task,
                "optimized": optimized_task,
                "executed_result": result,
                "timestamp": datetime.now().isoformat()
            })
            print(f"{self.name} logged the optimized task.")
    
    def show_log(self):
        print(f"\nWorkflow log by {self.name}:")
        for entry in self.workflow_log:
            print(f"- Original: {entry['original']} / Optimized: {entry['optimized']} / Result: {entry['executed_result']}")

            