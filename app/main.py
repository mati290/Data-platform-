from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import logger
from app.api.routers.weather import router as weather_router
from app.sheduler.weather_sheduler import start_scheduler



app = FastAPI(title=settings.APP_NAME)

app.include_router(weather_router)


@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok", "environment": settings.ENV,}

@app.on_event("startup")
def on_startup():
    start_scheduler()
