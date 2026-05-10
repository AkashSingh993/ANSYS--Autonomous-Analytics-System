from fastapi import FastAPI
from app.routes.query import router

app = FastAPI(
    title="Autonomous Analytics System",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Autonomous Analytics System Running"
    }