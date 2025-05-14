class ExecutorAgent:
    def __init__(self, name):
        self.name = name
        self.role = "executor"
        self.task_history = []

    def execute_task(self, task):
        print(f"{self.name} is executing: {task}")
        self.task_history.append(f"Executed task: {task}")

    def show_history(self):
        print(f"\nTask history for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")
