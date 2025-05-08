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
        
    def show_history(self):
        print(f"\nTsk History for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")

# --- Coordinater Agent ---
class Coordinator:
    def __init__(self, name):
        self.name = name
        self.workflow_log = []

    def manage_workflow(self, planner,optimizer):
        task = planner.create_task()
        if task:
            optimized_task = optimizer.optimize_task(task)
            self.workflow_log.append({
                "original": taksk,
                "optimized": optimized_task
            })
            print(f"{self.name} logged the optimized task.")

    def show_log(self):
        print(f"\nWorkflow log by {self.name}:")
        for entry in self.workflow_log:
            print(f"- Original: {entry['original']} / Optimized: {entry['optimized']}")
     
# --- MAIN PROGRAM ---
print("Hello from the MultiAgent workflow optimizer!")
print("Running intelligent agent simulation...\n")

astra = Agent("Astra", "planner")
kaizen = Agent("Kaizen", "optimizer")
nova = Coordinator("Nova")
#Run a single cycle
nova.manage_workflow(astra, kaizen)
#Show logs
astra.show_history()
kaizen.show_history()
nova.show_log()

initial_task = astra.create_task()
if initial_task:
    final_task = kaizen.optimize_task(initial_task)

