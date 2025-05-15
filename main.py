from datetime import datetime
import random
import json

print("Hello from the MultiAgent workflow optimizer!")

# --- Shared Agent Registry ---
AGENTS = {}

# --- Base Agent Class ---
class Agent:
    def __init__(self, name, role=None):
        self.name = name
        self.role = role
        self.task_history = []

    def perform_task(self, task):
        print(f"{self.name} is working on: {task}")

    def create_task(self):
        if self.role == "planner":
            task_pool = ["clean raw data", "sort entries", "analyze logs", "label data", "merge datasets"]
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
        else:
            print(f"{self.name} cannot create tasks.")
            return None

    def optimize_task(self, task):
        if self.role == "optimizer":
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
        else:
            print(f"{self.name} cannot optimize tasks.")
            return task

    def execute_task(self, task):
        if self.role == "executor":
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
        else:
            print(f"{self.name} cannot execute tasks.")
            return None

    def show_history(self):
        print(f"\nTask History for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")

    def send_message(self, recipient_name, message):
        if recipient_name in AGENTS:
            print(f"{self.name} sent a message to {recipient_name}: {message}")
            AGENTS[recipient_name].receive_message(self.name, message)
        else:
            print(f"{self.name} tried to message {recipient_name}, but they don't exist.")

    def receive_message(self, sender_name, message):
        print(f"{self.name} received message from {sender_name}: {message}")
        self.task_history.append({
            "action": "message_received",
            "from": sender_name,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })

# --- Specialized Agent Classes ---
class PlannerAgent(Agent):
    def __init__(self, name):
        super().__init__(name, role="planner")

class OptimizerAgent(Agent):
    def __init__(self, name):
        super().__init__(name, role="optimizer")

class ExecutorAgent(Agent):
    def __init__(self, name):
        super().__init__(name, role="executor")

# --- Coordinator Class (Not a subclass of Agent) ---
class Coordinator:
    def __init__(self, name):
        self.name = name
        self.workflow_log = []

    def manage_workflow(self, planner, optimizer, executor):
        task = planner.create_task()
        if task:
            optimized_task = optimizer.optimize_task(task)
            optimizer.send_message(executor.name, f"optimized task: {optimized_task}")

            result = executor.execute_task(optimized_task)
            executor.send_message(self.name, f"Execution result: {result}")

            self.workflow_log.append({
                "original": task,
                "optimized": optimized_task,
                "executed_result": result,
                "timestamp": datetime.now().isoformat()
            })
            print(f"{self.name} logged the optimized task.")

    def receive_message(self, sender_name, message):
        print(f"{self.name} (Coordinator) received message from {sender_name}: {message}")
        self.workflow_log.append({
            "action": "message_received",
            "from": sender_name,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })

    def show_log(self):
        print(f"\nWorkflow log by {self.name}:")
        for entry in self.workflow_log:
            print(f"- Original: {entry['original']} / Optimized: {entry['optimized']} / Result: {entry['executed_result']}")

# --- MAIN PROGRAM ---
def main():
    # Create agents
    planner = PlannerAgent("Astra")
    optimizer = OptimizerAgent("Kaizen")
    executor = ExecutorAgent("Nova")
    coordinator = Coordinator("Orion")

    # Register agents in shared registry
    AGENTS["Astra"] = planner
    AGENTS["Kaizen"] = optimizer
    AGENTS["Nova"] = executor
    AGENTS["Orion"] = coordinator  # Even though not subclass of Agent, added for messaging

    # Run one cycle
    coordinator.manage_workflow(planner, optimizer, executor)

    # Show task history
    planner.show_history()
    optimizer.show_history()
    executor.show_history()
    coordinator.show_log()

    # Save to file
    with open("workflow_log.json", "w") as f:
        json.dump(coordinator.workflow_log, f, indent=4)
        print("Workflow log saved to workflow_log.json")

# Run the program
if __name__ == "__main__":
    main()
