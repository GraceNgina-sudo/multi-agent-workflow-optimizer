from fastapi import FastAPI
from agents import PlannerAgent, OptimizerAgent, ExecutorAgent, Coordinator, AGENTS
from datetime import datetime
import json

app = FastAPI(title="MultiAgent Workflow Optimizer")
# --- AGENT REGISTRY ---
planner = PlannerAgent("Astra")
optimizer = OptimizerAgent("Kaizen")
executor = ExecutorAgent("Nova")
coordinator = Coordinator("Orion")
AGENTS["Astra"] = planner
AGENTS["Kaizen"] = optimizer
AGENTS["Nova"] = executor
AGENTS["Orion"] = coordinator

@app.post("/Workflow")
def run_workflow():
    task = planner.create_task()
    if task:
        optimized_task = optimizer.optimize_task(task)
        optimizer.send_message(executor.name, f"optimized task: {optimized_task}")

        result = executor.execute_task(optimized_task)
        executor.send_message(coordinator.name, f"Execution result: {result}")

        coordinator.workflow_log.append({
            "original": task,
            "optimized": optimized_task,
            "executed_result": result,
            "timestamp": datetime.now().isoformat()
        })
        with open("workflow_log.json", "w") as f:
            json.dump(coordinator.workflow_log, f, indent=4)

        return{
            "status": "success",
            "workflow": {
                "original": task,
                "optimized": optimized_task,
                "result": result
            }
        }
    else:
        return {
            "status": "error",
            "message": "Task creation failed."
        }



