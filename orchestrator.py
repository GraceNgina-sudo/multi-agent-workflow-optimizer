from agent.planner.planner_agent import PlannerAgent
from agent.executor.executor_agent import ExecutorAgent
from db.db_logger import log_task, log_agent
from agent.optimizer.optimizer_agent import OptimizerAgent



class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent(name="Astra")
        self.optimizer = OptimizerAgent(name="Kaizen")
        self.executor = ExecutorAgent(name="Nova")

    def run_workflow_cycle(self):
        #Step 1: Planner creates task
        task = self.planner.run()
        log_task(name=task["description"], status="created")
        log_agent(agent_name=self.planner.name, action="planned task", output=str(task))

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
    

    

