from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import logger

app = FastAPI(title=settings.APP_NAME)

@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok", "environment": settings.ENV,}
