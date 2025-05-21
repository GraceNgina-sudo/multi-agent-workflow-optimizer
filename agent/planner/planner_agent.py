import random
from datetime import datetime
from db import log_agent, log_task

class AstraAgent:
    def run(self, text):
        result = self.analyze_text(text)
        log_agent(agent_name="Astra", action="Text classification", output=result)
        return result
    def analyze_text(self, text):
        if "delay" in text.lower():
            return "Complaint detected: Delivery delay"
        elif "thank" in text.lower():
            return "Feedback: positive"
        else:
            return "Unclassified text"
from agents.base import Agent
              
class PlannerAgent(AstraAgent):
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
        from db import log_task
        log_task(name=task, status="created")
        return task_details
    
    def show_history(self):
        print(f"\nTask History for {self.name}:")
        for entry in self.task_history:
            print(f"- {entry}")
