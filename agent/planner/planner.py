import random

class PlannerAgent:
    def __init__(self, name):
        self.name = name
        self.role = "planner"
        self.task_history = []

    def create_task(self):
        task_pool = ["Clean raw data", "Sort entries", "Analyze logs", "Label data", "Merge datasets"]
        task = random.choice(task_pool)
        priority = random.choice(["high", "medium", "low"])
        task_details = {"description": task, "priority": priority}
        print(f"{self.name} created task: {task_details}")
        self.task_history.append(f"Created task: {task_details}")
        return task_details

    def show_history(self):
        print(f"\nTask history for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")
