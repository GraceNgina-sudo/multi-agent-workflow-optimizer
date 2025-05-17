from fastapi import FastAPI
from agents import run_workflow

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from the FastAPI workflow optimizer!"}

@app.post("/workflow")
def workflow():
    result = run_workflow()
    return{"result": result}


