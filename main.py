from fastapi import FastAPI, Query
from agent.planner.planner_agent import plannerAgent
from agent.optimizer.optimizer_agent import OptimizerAgent
from agent.executor.executor_agent import ExecutorAgent
from coordinator.agent_orchestrator import coordinatorAgent
from db.db_logger import init_db, log_task, log_agent, log_workflow_history
import uvicorn
from datetime import datetime
from coordinator.agent_orchestrator import apporchestrator

app = FastAPI(title="MultiAgent Workflow Optimizer")
orchestrator = apporchestrator()

# Initialize the database
init_db()

# Instantiate Agents
planner = plannerAgent(name="Astra")
optimizer = OptimizerAgent(name="Kaizen", role="optimizer")
executor = ExecutorAgent(name="Nova")
coordinator = coordinatorAgent(name="Orion")

# /Endpoint(Health Check)
@app.get("/")
def root():
    return {"message": "Multi-Agent Workflow System running."}

# /simulate Endpoint(Main Workflow Simulation)
@app.get("/simulate")
def simulate_agents():
    print("\n--- Agent Simulation Started ---")

    # Step 1: Planning
    task = planner.run()
    print(f"[Planner: {planner.name}] Planned Task: {task}")
    log_task(task["description"], status="created")

    # Step 2: Optimization
    optimized = optimizer.run(task)
    print(f"[Optimizer: {optimizer.name}] Optimized Task: {optimized}")
    log_agent(optimizer.name, "Optimized Task", str(optimized))

    # Step 3: Execution
    result = executor.run(optimized)
    print(f"[Executor: {executor.name}] Execution Result: {result}")
    log_agent(executor.name, "Executed Task", result)

    # Step 4: Coordinator Logs
    coordinator.workflow_log.append({
        "original": task,
        "optimized": optimized,
        "executed_result": result,
        "timestamp": datetime.now().isoformat()
    })
    log_workflow_history(task, optimized, result)

    print(f"[coordinator: {coordinator.name}] Logged workflow.")
    print("--- Agent Simulation Completed ---\n")

    return {
        "original_task": task,
        "optimized_task": optimized,
        "execution_result": result
    }

@app.get("/history")
def history():
    return coordinator.workflow_log


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

from db.db_logger import get_task_logs, get_agent_logs, fetch_workflow_history


@app.get("/logs/tasks")
def get_tasks():
    tasks = get_task_logs()
    return {"task_logs": tasks}

@app.get("/logs/agents")
def get_agents():
    agents = get_agent_logs()
    return {"agent_logs": agents}

@app.get("/logs/workflows")
def get_workflows():
    workflows = fetch_workflow_history()
    return {"workflow_history": workflows}

@app.get("/ai-simulate")
def simulate_ai_planner(user_input: str = Query(..., description="Describe what you want done")):
    task = orchestrator.planner.create_task(user_input)
    return{
        "Generated Task": task
    }




