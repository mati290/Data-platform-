import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/data_platform"
)

def create_engine_with_retry(
    db_url: str,
    retries: int = 10,
    delay: int = 3,
):
    for attempt in range(1, retries + 1):
        try:
            engine = create_engine(db_url)
            connection = engine.connect()
            connection.close()
            print("✅ Database connection established")
            return engine
        except OperationalError:
            print(f"⏳ Database not ready (attempt {attempt}/{retries})")
            time.sleep(delay)

    raise RuntimeError("❌ Could not connect to the database")

engine = create_engine_with_retry(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
