# multi-agent-workflow-optimizer
workflow Automation for small businesses in Africa
#milestone log
### milestone 1: Initial setup and Agent Framework
**Date:** [5th May 2025]
-Set up first GitHub repository:multi-agent-workflow-optimizer.
-Used Git on local machine via VS Code.
-Configured Git identity (name + email).
-Created and run first file: main.py
-Successfully committed and pushed code to GitHub

### milestone 2: Inteligent Agent Behavior
**Date**[6th May 2025]
-Task cration:Astra(planner)now generates tasks randomly from a predefined pool.
-Task prioritization:Kaizen(optimizer)adapts its approach based on task priority:
     .High:Fastest method
     .Medium:Balanced method
     .Low:Resource-saving method
-Dynamic outputs: Every run produces a unique task and optimization method, making the system more flexible.
### milestone 3:Implemented task_history
**Date**[7th May 2025]
-Fixed typos and structural errors in agent logic.
-Defined show_history() for both planner and optimizer agents.
-Verified and tested the final output
-Successfully pushed working version to GitHub.
### milestone 4: Added coordinator Agent (Nova)
**Date**[8th May 2025]
-Introduced a third agent, Coordinator, named Nova
-Nova manages the workflow between planner(Astra) and Optimizer(Kaizen)
-Logged original and optimized tasks in a structured workflow log.
### milestone 5: Added project structure
**Date**[12th May 2025]
-Created a structured mind map for the multi-agent workflow optimizer.
-Set up docs/ folder and documented the system architecture
-Restricted code into clean modular folders:
 -planner/ for Astra
 -optimizer/ for Kaizen
 -executor/ for Nova
-Created respective .py files for each agent
-Refactored main.py to import agents from their modules
### milestone 6: Fixed issues 
**Date**[14th May 2025]
-Modular agent logic
-Role-specific task handling
-Task history and centralized workflow log
-Coordinator to oversee ochestration
