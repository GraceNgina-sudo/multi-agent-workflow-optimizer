import sqlite3

def init_db():
    conn = sqlite3.connect('workflow.db')
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
    conn.close()
def log_task(name, status):
    conn = sqlite3.connect('workflow.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO tasks (agent_name, action, output, timestamp) VALUES (?, ?, ?)",
        (name, status,datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
def log_agent(agent_name, action, output):
    conn = sqlite3.connect('workflow.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO logs (agent_name, action, output, timestamp) VALUES (?, ?, ?, ?)",
        (agent_name, action, output, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

    
    