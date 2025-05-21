from fastapi import FastAPI
from orchestrator import run_workflow as orchestrate
from agents import PlannerAgent, OptimizerAgent, ExecutorAgent, Coordinator, AGENTS
from coordinator.routes import router as coordinator_router

app = FastAPI(title="MultiAgent Workflow Optimizer")

# Initialize the database
init_db()

#Register API routes from coordinator
app.include_router(coordinator_router)

# --- Agent Initialization ---
planner = PlannerAgent("Astra")
optimizer = OptimizerAgent("Kaizen")
executor = ExecutorAgent("Nova")
coordinator = Coordinator("Orion")

#Register agents globally
AGENTS["Astra"] = planner
AGENTS["Kaizen"] = optimizer
AGENTS["Nova"] = executor
AGENTS["Orion"] = coordinator

@app.post("/Workflow")
def trigger_workflow():
    """
    Initiates a full multi-agent workflow: planning → optimizing → execution → coordination.
    """
    return orchestrate(planner, optimizer, executor, coordinator)

    