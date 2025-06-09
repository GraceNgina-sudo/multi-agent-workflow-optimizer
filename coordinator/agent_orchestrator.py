from datetime import datetime
from db.db_logger import log_task, log_agent
from data_types.agent import Agent
from fastapi import APIRouter
from agent.planner.planner_agent import plannerAgent
from agent.optimizer.optimizer_agent import OptimizerAgent
from agent.executor.executor_agent import ExecutorAgent

class coordinatorAgent(Agent):
    def __init__(self, name="orion", role="coordinator"):
        super().__init__(name, role)
        self.workflow_log = []

    def run(self, input_data=None):
        """Runs the coordinator agent."""
        # The coordinator's run method might be used for more complex orchestration
        # in the future. For now, its main role in main.py is logging.
        log_agent(self.name, "Coordinator Active", "Monitoring workflow")
        # We keep manage_workflow as a separate method if it's intended for a different type of simulation run
        pass

    def manage_workflow(self, planner, optimizer, executor):
        task = planner.run()
        if task:
            optimized_task = optimizer.run(task)
            result = executor.run(optimized_task)
            executor.send_message("Orion", f"Execution result: {result}")
            self.workflow_log.append({
                "original": task,
                "optimized": optimized_task,
                "executed_result": result,
                "timestamp": datetime.now().isoformat()
            })
            print(f"{self.name} logged the optimized task.")
            return{
                "task": task,
                "optimized_task": optimized_task,
                "result": result
            }
    
    def show_log(self):
        print(f"\nWorkflow log by {self.name}:")
        for entry in self.workflow_log:
            print(f"- Original: {entry['original']} / Optimized: {entry['optimized']} / Result: {entry['executed_result']}")


class apporchestrator:
    def __init__(self, name="apporchestrator", role="orchestrator"):
        self.name = name
        self.role = role
        self.planner = plannerAgent(name="Astra", role="planner")
        self.optimizer = OptimizerAgent(name="Kaizen", role="optimizer")
        self.executor = ExecutorAgent(name="Nova", role="executor")

router = APIRouter()

@router.get("/coordinator/test")
def test():
    return {"message": "Coordinator route working!"}

            