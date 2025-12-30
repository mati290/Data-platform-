from sqlalchemy import Column, Integer, Float, Boolean, DateTime
from app.db.session import base

class WeatherData(base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True,)
    time = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
    temperature_c = Column(Float, nullable=False)
    temp_above_avg = Column(Boolean, nullable=False)
    