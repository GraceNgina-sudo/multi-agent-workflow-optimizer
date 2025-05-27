from datetime import datetime
from data_types.agent import Agent
from db.db_logger import log_agent

class OptimizerAgent(Agent):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.name = "Kaizen"
        self.role = "optimizer"
        self.task_history = []

    def run(self, input_data):
        """Optimizes a given task based on its priority."""
        description = input_data.get("description", "unknown task")
        priority = input_data.get("priority", "medium")

        method = {
            "high": "fastest algorithm",
            "medium": "resource-saving algorithm"
        }.get(priority, "default algorithm")

        optimized = {
            "optimized_description": f"{description} using {method}",
            "original_task": input_data,
            "optimized_by": self.name,
            "timestamp": datetime.now().isoformat()
        }
        self.task_history.append(optimized)
        log_agent(agent_name=self.name, action="optimized task", output=optimized)
        return optimized
    
    def get_history(self):
        return self.task_history
    
    def optimize_workflow(input: str)-> str:
        return f"Executor is executing tasks from: {input}"
    
    