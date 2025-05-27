import random
from datetime import datetime
from data_types.agent import Agent
from db.db_logger import log_agent, log_task

class ExecutorAgent(Agent):
    def __init__(self, name="Nova", role="executor"):
        super().__init__(name, role)
        self.completed_tasks = []

    def run(self, input_data):
        """Executes a given task."""
        # Assuming input_data is the task dictionary
        task = input_data
        result = self.complete_task(task)
        log_agent(self.name, "Executed Task", result)
        log_task(task["description"], status="completed", assigned_to=self.name)
        return result

    def complete_task(self, task):
        #simulate task completion
        delay = random.uniform(0.5, 2.0) #simulate time taken
        self.completed_tasks.append({
            "task": task,
            "completed_at": datetime.now().isoformat(),
            "duration":delay
        })
        return {
            "status": "success",
            "message": f"Task '{task['description']}' completed in {delay:.2f}s",
            "duration": delay
        }
    def show_completed_tasks(self):
        print(f"\nCompleted tasks by {self.name}:")
        for t in self.completed_tasks:
            print(f"- {t['task']['description']} at {t['completed_at']} (took {t['duration']:.2f}s)")

    def execute_tasks(input: str) -> str:
        return f"Executor is executing tasks from: {input}"

            
    
                             
        
