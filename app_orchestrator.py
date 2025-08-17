import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent.planner.planner_agent import plannerAgent
from agent.executor.executor_agent import ExecutorAgent
from db.db_logger import log_task, log_agent
from agent.optimizer.optimizer_agent import OptimizerAgent
from agent.planner.gpt_planner import GPTPlannerAgent

class apporchestrator:
    def __init__(self):
        self.planner_agent = GPTPlannerAgent(model_name="planner-GPT")
        # Initialize agents
        self.planner = plannerAgent(name="Astra")
        self.optimizer = OptimizerAgent(name="Kaizen", role="optimizer")
        self.executor = ExecutorAgent(name="Nova")

    def run_workflow_cycle(self, input_data=None):
        #Step 1: Planner creates task
        try:
            task = self.planner.run(input_data=input_data)
            if not isinstance(task, dict):
                print("Error:Plnner did not return a valid task.")
                return {"error": "Planner did not return a valid task."}
            log_task(name=task["description"], status="created")
            log_agent(agent_name=self.planner.name, action="planned task",output=str(task))
        except Exception as e:
            print(f"Error during planning phase:{e}")#Handle error, maybe log it and exit or try a recovery step
            return {"error": str(e)}

        #step 2: optimizer refines the task
        optimized_task = self.optimizer.run(task)
        log_agent(agent_name=self.optimizer.name, action="optimized task",output=str(optimized_task))
        
        # Step 3: Executoe performs the task
        result = self.executor.run(optimized_task)
        log_agent(agent_name=self.executor.name, action="Executed task", output=result) 
        return {
            "original_task": task,
            "optimized_task": optimized_task,
            "execution_result": result
        }

    def get_task_history(self):
        return {
            "planned_tasks": self.planner.get_history(),
            "optimized_tasks": self.optimizer.task_history,
            "executed_tasks": self.executor.completed_tasks
        }