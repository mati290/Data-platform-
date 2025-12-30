from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATEBASE_URL = "postgresql://postgres:gabrysia3@localhost:5432/data_platform"

engine = create_engine(DATEBASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

from app.db.models.weather import WeatherData

base.metadata.create_all(bind=engine)