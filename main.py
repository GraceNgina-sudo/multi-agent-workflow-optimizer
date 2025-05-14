print("Hello from the MultiAgent workflow optimizer!")

import random
class Agent:
    def __init__(self, name, role=None):
        self.name = name
        self.role = role
        self.task_history = []

    def perform_task(self, task):
        print(f"{self.name} is working on: {task}")

    def create_task(self):
        if self.role == "planner":
            task_pool = ["clean raw data", "sort entries", "Analyze logs", "Label data", "Merge datasets"]
            task = random.choice(task_pool)
            priority = random.choice(["high", "medium", "low"])
            task_details = {"description": task, "priority": priority}
            print(f"{self.name} created task: {task}")
            self.task_history.append(f"created task: {task_details}")
            return task_details
        else:
            print(f"{self.name} cannot create tasks.")
            return None

    def optimize_task(self, task):
        if self.role == "optimizer":
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
                self.task_history.append(f"optimized task: {optimized}")
                return optimized
        else:
            print(f"{self.name} cannot optimize tasks.")
            return task
    def execute_task(self, task):
        if self.role == "executor":
            print(f"{self.name} is executing: {task}")
            self.task_history.append(f"executed task: {task}")
        else:
            print(f"{self.name} cannot execute tasks.")
            return None
        
    def show_history(self):
        print(f"\nTsk History for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")

# --- Coordinater Agent ---
class Coordinator:
    def __init__(self, name):
        self.name = name
        self.workflow_log = []

    def manage_workflow(self, planner,optimizer, executor):
        task = planner.create_task()
        if task:
            optimized_task = optimizer.optimize_task(task)
            result = executor.execute_task(optimized_task)
            self.workflow_log.append({
                "original": task,
                "optimized": optimized_task,
                "executed": result
            })
            print(f"{self.name} logged the optimized task.")

    def show_log(self):
        print(f"\nWorkflow log by {self.name}:")
        for entry in self.workflow_log:
            print(f"- Original: {entry['original']} / Optimized: {entry['optimized']}")
     
# --- MAIN PROGRAM ---
def main():
    # create instances of each agent
    planner = Agent("Astra", "planner")
    optimizer = Agent("Kaizen", "optiimizer")
    executor = Agent("Nova", "executor")
    coordinator = Coordinator("Orion")
#Run a single cycle
    Coordinator.manage_workflow(planner, optimizer, executor)

# --- Importing the agents ---
from planner.planner import PlannerAgent
from optimizer.optimizer import OptimizerAgent
from executor.executor import ExecutorAgent
from coordinator.coordinator import Coordinator

def main():
    # create instances of each agent
    planner = PlannerAgent("Astra")
    optimizer = OptimizerAgent("Kaizen")
    executor = ExecutorAgent("Nova")
    coordinator = Coordinator("Orion")

    coordinator.manage_workflow(planner, optimizer, executor)

    planner.show_history()
    optimizer.show_history()
    executor.show_history()
    coordinator.show_log()

    if __name__ == "__main__":
        main()
        

