from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.session import SessionLocal
from app.db.models.weather import WeatherData


router = APIRouter(
    prefix="/weather",
    tags=["weather"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/latest")
def get_latest_weather(db: Session = Depends(get_db)):
    record = db.query(WeatherData).order_by(WeatherData.time.desc()).first()
    return record

@router.get("/stats")
def get_weather_stats(db: Session = Depends(get_db)):
    avg_temp = db.query(func.avg(WeatherData.temperature)).scalar()
    max_temp = db.query(func.max(WeatherData.temperature)).scalar()
    min_temp = db.query(func.min(WeatherData.temperature)).scalar()
    
    return {
        "average_temperature": avg_temp,
        "max_temperature": max_temp,
        "min_temperature": min_temp,
    }
    
@router.get("/above_avg_count")
def get_above_avg_count(db: Session = Depends(get_db)):
    records = (db.query(WeatherData).filter(WeatherData.temp_above_avg.is_(True)).all())
    return records
        