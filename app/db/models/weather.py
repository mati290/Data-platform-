from sqlalchemy import Column, Integer, Float, Boolean, DateTime
from app.db.session import Base

class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True,)
    time = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
    temp_above_avg = Column(Boolean, nullable=False)
