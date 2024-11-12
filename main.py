from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get("/")
async def index() -> Dict[str, str]:
    return {"hello": "world"}

@app.get("/about")
async def about() :
    return " thsi is nithin varkey"