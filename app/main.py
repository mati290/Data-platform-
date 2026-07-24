from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import logger
from app.api.routers.weather import router as weather_router
from app.scheduler.weather_scheduler import start_scheduler



app = FastAPI(title=settings.APP_NAME)

app.include_router(weather_router)


@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok", "environment": settings.ENV,}

@app.on_event("startup")
def on_startup():
    if settings.ENABLE_SCHEDULER:
        app.state.scheduler = start_scheduler()

@app.on_event("shutdown")
def on_shutdown():
    scheduler = getattr(app.state, "scheduler", None)
    if scheduler:
        scheduler.shutdown(wait=False)
