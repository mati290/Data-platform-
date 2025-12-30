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
1. Create virtualenv
2. Install requirements
3. Run FastAPI
4. Scheduler runs automatically

## Example Endpoints
- /weather/latest
- /weather/stats
- /weather/above-average

## Author
Mateusz Poręba
