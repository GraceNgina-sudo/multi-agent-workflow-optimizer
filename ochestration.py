from datetime import datetime
import json
from db import log_task, log_agent

def run_workflow(planner, optimizer, executor, coordinator):
    #Step 1: Planner creates task
    task = planner.create_task()
    if not task:
        return{
            "status": "error",
            "message": "Task creation failed."
        }
    log_task(name=task["description"], status="created")
    log_agent(agent_name=optimizer.name, action="executed task", output=result)

    #step 2: Optimizer optimizes task
    optimized_task = optimizer.optimize_task(task)
    log_agent(agent_name=optimizer.name, action="optimized task", output=optimized_task)

    # Step 3: Executor executes task
    result = executor.execute_task(optimized_task)
    log_agent(agent_name=executor.name, action="executed task", output=result)

    # Step 4: Coordinator logs workflow summary
    coordinator.workflow_log.append({
        "original": task,
        "optimized": optimized_task,
        "executed_result": result,
        "timestamp": datetime.now().isoformat()
    })

    with open("workflow_log.json", "w") as f:
        json.dump(coordinator.workflow_log, f, indent=4)

    return {
        "status": "success",
        "workflow": {
            "original": task,
            "optimized": optimized_task,
            "result": result
        }
    }
