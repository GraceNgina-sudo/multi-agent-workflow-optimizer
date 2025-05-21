import random
from datetime import datetime

class ExecutorAgent(Agent):
    def __init__(self, name, role="executor"):
        super().__init__(name, role)
        self.name = name
        self.role = "executor"
        self.task_history = []

    def execute_task(self, task):
        print(f"{self.name} is executing: {task}")
        result = random.choice(["success", "failure"])
        self.task_history.append({
            "action": "executed",
            "task": task,
            "result": result,
            "timestamp": datetime.now().isoformat()
        })
        print(f"{self.name} execution result: {result}")
        return result
    def show_history(self):
        print(f"\nTask History for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")
        