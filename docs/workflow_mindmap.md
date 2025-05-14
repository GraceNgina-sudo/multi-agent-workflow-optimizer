#  Multi-Agent Workflow Optimizer – Mind Map

## Agents & Roles

### 1. Planner Agent – **Astra**
- **Role:** Create tasks
- **Task Pool:** 
  - Clean data  
  - Analyze logs  
  - Sort entries  
  - Label data  
  - Merge datasets  
- **Assigns Priority:** 
  - High  
  - Medium  
  - Low

---

### 2. Optimizer Agent – **Kaizen**
- **Role:** Optimize tasks based on priority
- **Strategies:**  
  - High → Fastest Algorithm  
  - Medium → Balanced Approach  
  - Low → Resource-Saving Algorithm

---

### 3. Executor Agent – **Nova**
- **Role:** Simulate task execution  
- **Duties:**  
  - Log task completion  
  - Handle execution feedback  
  - Pass results back to coordinator  

---

### 4. Evaluator Agent – _(Future Addition)_
- **Role:** Evaluate task quality  
- **Duties:**  
  - Suggest improvements  
  - Flag poor optimizations  

---

## 🔄 Communication Flow
- Agents pass tasks in sequence: **Astra → Kaizen → Nova → Evaluator**
- Shared history tracker across agents
- Central coordinator can monitor and redirect flow

---

## Future Considerations
- Visualization using Mermaid or actual graph tools
- Integration with async messaging or APIs
- Add learning behavior per agent (ML module)

