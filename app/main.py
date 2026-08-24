"""FastAPI application entry point for LeadScore Service."""

from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="LeadScore Service",
    description="Sample lead scoring service — Advanced Batch training repository.",
    version="0.1.0",
)

app.include_router(router)


@app.get("/")
def health_check():
    return {"status": "ok", "service": "leadscore-service"}
