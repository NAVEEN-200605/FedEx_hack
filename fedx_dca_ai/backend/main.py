from fastapi import FastAPI
from backend.decision import assign_dca

app = FastAPI()

@app.post("/assign_case")
def assign_case(case: dict):
    return assign_dca(case)
