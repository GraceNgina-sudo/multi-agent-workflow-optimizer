import sqlite3
import json 
from datetime import datetime

def init_db():
    with sqlite3.connect('workflow.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tasks(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  Status TEXT,
                    timestamp TEXT
                    )''')
        c.execute('''CREATE TABLE IF NOT EXISTS logs(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  agent_name TEXT,
                  action TEXT,
                  output TEXT,
                  timestamp TEXT
                    )''')
        conn.commit()

def log_task(name, status):
    with sqlite3.connect('workflow.db') as conn:
        c = conn.cursor()
        c.execute(
            "INSERT INTO tasks (name, status, timestamp) VALUES (?, ?, ?)",
            (name, status, datetime.now().isoformat())
        )
        conn.commit()

def log_agent(agent_name, action, output):
    with sqlite3.connect('workflow.db') as conn:
        c = conn.cursor()
        # Convert output dictionary to JSON string
        output_str = json.dumps(output) if isinstance(output, dict) else output
        c.execute(
            "INSERT INTO logs (agent_name, action, output, timestamp) VALUES (?, ?, ?, ?)",
            (agent_name, action, output_str, datetime.now().isoformat())
        )
        conn.commit()

def get_task_logs():
    conn = sqlite3.connect('workflow.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    rows = c.fetchall()
    conn.close()
    return rows

def get_agent_logs():
    conn = sqlite3.connect('workflow.db')
    c = conn.cursor()
    c.execute("SELECT * FROM logs")
    rows = c.fetchall()
    conn.close()
    return rows
def log_workflow_history(original, optimized, executed_result):
    with sqlite3.connect('workflow.db') as conn:
        c = conn.cursor()
        try:
            original_str = json.dumps(original)
            optimized_str = json.dumps(optimized)
            executed_str = json.dumps(executed_result)
        except TypeError:
            original_str=str(original)
            optimized_str = str(optimized)
            executed_str = str(executed_result)
        c.execute(
            "INSERT INTO workflow_history (original, optimized, executed_result, timestamp) VALUES (?, ?, ?, ?)",
            (original_str, optimized_str, executed_str, datetime.now().isoformat())
        )
        conn.commit()
        def fetch_workflow_history():
            with sqlite3.connect('workflow.db') as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM workflow_history")
                rows = c.fetchall()
        
            history = []
            for row in rows:
                try:
                    history.append({
                        "id": row[0],
                        "original": json.loads(row[1]),
                        "optimized": json.loads(row[2]),
                        "executed_result": json.loads(row[3]),
                        "timestamp": row[4]
                    })
                except Exception:
                    history.append({
                        "id": row[0],
                        "original": row[1],
                        "optimized": row[2],
                        "executed_result": row[3],
                        "timestamp": row[4]
                    })
            return history
        
def fetch_workflow_history():
    conn = sqlite3.connect('workflow.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM logs")
        rows = c.fetchall()
        return rows
    finally:
        conn.close()
        


    
    