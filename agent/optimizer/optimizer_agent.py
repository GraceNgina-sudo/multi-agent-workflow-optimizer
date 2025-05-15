from datetime import datetime

class OptimizerAgent(Agent):
    def __init__(self, name, role="optimizer"):
        super().__init__(name, role)
        self.name = name
        self.role = "optimizer"
        self.task_history = []

    def optimize_task(self, task):
        description = task["description"]
        priority = task["priority"]
        method = {
            "high": "fastest algorithm",
            "medium": "balanced algorithm",
            "low": "resource-saving algorithm"
        }.get(priority, "default algorithm")
        
        optimized = f"{description} using {method}"
        print(f"{self.name} optimized task to: {optimized}")
        self.task_history.append({
            "action": "optimized",
            "task": optimized,
            "timestamp": datetime.now().isoformat()
        })
        return optimized
    def show_history(self):
        print(f"\nTask History for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")