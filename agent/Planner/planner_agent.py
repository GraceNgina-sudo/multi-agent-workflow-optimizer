import random
from datetime import datetime
from data_types.agent import Agent
from db.db_logger import log_agent

class plannerAgent(Agent):
    """An agent responsible for planning tasks."""
    def __init__(self, name="Astra", role="planner"):
        super().__init__(name, role)
        self.task_history = []
        self.task_pool = ["clean raw data", "sort entries", "Analyze logs", "Label data", "merge datasets"]
        
    def run(self, input_data=None):
        """Runs the planner agent to create a task."""
        return self.create_task(input=input_data)

    def create_task(self, input=None):
        if input:
            task = input
        else:
            task = random.choice(self.task_pool)
        task = random.choice(self.task_pool)
        priority = random.choice(["high", "medium", "low"])
        task_details = {
            "description": task,
            "priority": priority,
            "created_by": self.name,
            "timestamp": datetime.now().isoformat()
        }
        self.task_history.append(task_details)

        log_agent(agent_name=self.name, action="created Task", output=task_details["description"])
        return task_details

    def get_history(self):
        return self.task_history

    def plan_tasks(self, input:str) -> str:
        task = self.create_task(input=input)
        return f"planner received input: '{input}': {task['description']} with priority {task['priority']}"
    

