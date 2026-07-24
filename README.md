# Data Platform – Weather Analytics

## Overview
End-to-end data engineering platform built with Python, FastAPI and PostgreSQL.

## Architecture
API → RAW → PROCESSED → PostgreSQL → Analytics API → Charts

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pandas / NumPy
- APScheduler

## Features
- Automated data ingestion from external API
- Data processing and feature engineering
- Relational data storage (PostgreSQL)
- Analytics REST API
- Background scheduler
- Data visualization

## How to Run

### Locally
1. Create a virtualenv and install requirements: `pip install -r requirements.txt`
2. Create a `.env` file in the project root (see below)
3. Run the API: `uvicorn app.main:app --reload`
4. The scheduler starts automatically with the app and runs the ingestion/processing pipeline every hour

### With Docker
1. Create a `.env` file in the project root (see below)
2. Run `docker-compose up --build`
3. The API will be available at `http://localhost:8000`

### Environment Variables
Create a `.env` file with:
```
APP_NAME=Data Platform
ENV=dev
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/data_platform
```
When running via `docker-compose`, `DATABASE_URL` is already set to point at the `db` service, but `.env` must still exist for `env_file` to load.

## Running Tests
```
pytest
```
Tests use an isolated SQLite database and do not require PostgreSQL to be running.

## Example Endpoints
- /weather/latest
- /weather/stats
- /weather/above_avg_count

## Author
Mateusz Poręba
