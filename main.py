import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI, Query
from agent.planner.planner_agent import plannerAgent
from agent.optimizer.optimizer_agent import OptimizerAgent
from agent.executor.executor_agent import ExecutorAgent
from coordinator.agent_orchestrator import coordinatorAgent
from db.db_logger import init_db, log_task, log_agent, log_workflow_history
from datetime import datetime
from coordinator.agent_orchestrator import apporchestrator
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MultiAgent Workflow Optimizer")
orchestrator = apporchestrator()
# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the database
init_db()

class TaskRequest(BaseModel):
    description: str
    category: str = "general"
    priority: str = "medium"

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
@app.post("/ai-simulate")
def simulate_agents(request: TaskRequest):
    user_input = f"{request.description} with category {request.category} and priority {request.priority}"

    print("\n--- Agent Simulation Started ---")

    # Step 1: Planning
    task = planner.run(user_input)
    print(f"[Planner: {planner.name}] Planned Task: {task}")
    
    # Added check to prevent KeyError if task is not a dict or lacks 'description'
    if isinstance(task, dict) and "description" in task:
        log_task(task["description"], status="created")
    else:
        # Assuming the task itself can be logged if it's not in the expected dict format.
        log_task(str(task), status="created")

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

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running smoothly."}


