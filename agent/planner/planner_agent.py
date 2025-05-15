import random
from datetime import datetime

class PlannerAgent(Agent):
    def __init__(self, name, role="planner"):
        super().__init__(name, role)
        self.name = name
        self.role = role
        self.task_history = []

    def create_task(self):
        task_pool = ["clean raw data", "sort entries", "Analyze logs", "Label data", "merge datasets"]
        task = random.choice(task_pool)
        priority = random.choice(["high", "medium", "low"])
        task_details = {"description": task, "priority": priority}
        print(f"{self.name} created task: {task}")
        self.task_history.append({
            "action": "created",
            "task": task_details,
            "timestamp": datetime.now().isoformat()
    })
        return task_details
    def show_history(self):
        print(f"\nTask History for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")
