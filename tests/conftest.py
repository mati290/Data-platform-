import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
os.environ.setdefault("DATABASE_URL", SQLALCHEMY_DATABASE_URL)
os.environ.setdefault("ENABLE_SCHEDULER", "false")

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.db.session import Base, get_db

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        
@pytest.fixture(scope="session")
def client():
    Base.metadata.create_all(bind=engine)

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    Base.metadata.drop_all(bind=engine)
