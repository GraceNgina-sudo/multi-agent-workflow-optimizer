# Multi-Agent Workflow Optimizer 
An experimental multi-agent system built in python that simulates how specialized agents can plan, optimize, and execute tasks collaboratively.

This project started as a leraning exercise and has since grown into a more strucutured application with a backened (FastAPI), database logging, and a frontend interface for user interaction

## Purpose 
The project's core purpose is to explore multi-agent systems in a practical way while learning modern development practices. 

### Key goals:
- Understand object-oriented programming (oop) and agent-based design in python
- Simulate collaborative workflows between different agents (planner, Optimizer, Executor, Coordinator).
- Gain hands-on experience with FastAPI, databases, and frontend-backend integration.
- Practice software engineering principles: logging, modularity, and system design.
- Lay the foundation for future integration with AI/LLMs for smarter decision-making.

## What it does:
- Accepts a user query via the frontend (form input).

- Planner Agent: Interprets the query and creates a task plan.

- Optimizer Agent: Refines the plan for efficiency.

- Executor Agent: Simulates carrying out the task.

- Coordinator Agent: Logs the full workflow and maintains history.

- All actions are logged into a SQLite database for traceability.

- Users can view task history and workflow logs via API endpoints.

## Tech stack:
- Backend: FastAPI (Python)
- Frontend:  JS + Bootstrap (form-based interface)
- Database: SQLite (lightweight logging & workflow storage)
- Server: Uvicorn (ASGI server for FastAPI)
- Architecture: Modular agent-based design with orchestrator

## Usage
1. Run the FastAPI app:
uvicorn main:app --reload

2. Open the frontend (with form connected to /ai-simulate)

3. Enter a query

4. Agents collaborate to: Plan-optimize-execute-log

5. View results in the UI or query logs via endpoints

## Current Features
- Multi-agent collaboration (Planner, Optimizer, Executor, Coordinator).

- API endpoints for simulation, history, and logs.

- Frontend with query input and response display.

- Database-backed logging for transparency.

- CORS-enabled middleware for smooth frontend-backend interaction.

## Next Steps
- LLM/GPT integration for smarter planning and task understanding.

- Polish UI with better workflow visualization and dashboards.

- Cloud Deployment (e.g., Render, Vercel, or AWS).

- Subscription Model for monetization (SaaS-like offering).

- Expand agents with new specialized roles.

## What i've learnt
- Building APIs with FastAPI.

- Designing modular agent architectures.

- Setting up frontend-backend communication.

- Using SQLite for logging and persistence.

- Handling CORS, validation, and request models in APIs.

## project Structure
multi-agent-workflow-optimizer/
├── .gitignore                   # Ignore Python cache, venv, db, logs, etc.
├── LICENSE                      # Project's software license
├── README.md                    # Project overview, setup, and usage
├── requirements.txt             # Python dependencies
├── main.py                      # FastAPI entry point (launches app & endpoints)
├── notes.code-workspace         # VS Code workspace settings
├── workflow.db                  # SQLite database (local persistence)

│
├── agent/                       # Core agent implementations
│   ├── __init__.py
│   ├── planner/                 # Planner Agent (task generation)
│   │   ├── __init__.py
│   │   └── planner_agent.py
│   ├── optimizer/               # Optimizer Agent (task improvement)
│   │   ├── __init__.py
│   │   └── optimizer_agent.py
│   ├── executor/                # Executor Agent (task execution)
│   │   ├── __init__.py
│   │   └── executor_agent.py
│   ├── coordinator/             # Coordinator Agent (task assignment & flow)
│   │   ├── __init__.py
│   │   └── coordinator_agent.py
│   └── services/                # Shared agent services/utilities
│       ├── __init__.py
│       └── task_service.py
│
├── coordinator/                 # System-level orchestrator
│   └── agent_orchestrator.py    # Manages cross-agent workflows
│
├── core/                        # Core infrastructure
│   └── router.py                # Message passing / event routing
│
├── data_types/                  # Custom data models
│   ├── __init__.py
│   └── agent.py                 # Agent data type definition
│
├── db/                          # Database logging + persistence
│   ├── __init__.py
│   └── db_logger.py             # Handles logging to SQLite
│
├── docs/                        # Documentation
│   └── workflow_mindmap.md      # Visual workflow design
│
├── logs/                        # Execution logs
│   └── progress_log.md











