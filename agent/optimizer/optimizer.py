class OptimizerAgent:
    def __init__(self, name):
        self.name = name
        self.role = "optimizer"
        self.task_history = []

    def optimize_task(self, task):
        description = task["description"]
        priority = task["priority"]

        if priority == "high":
            method = "fastest algorithm"
        elif priority == "medium":
            method = "balanced algorithm"
        else:
            method = "resource-saving algorithm"

        optimized = f"{description} using {method}"
        print(f"{self.name} optimized task to: {optimized}")
        self.task_history.append(f"Optimized task: {optimized}")
        return optimized

    def show_history(self):
        print(f"\nTask history for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")
