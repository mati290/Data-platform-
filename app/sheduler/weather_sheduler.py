from apscheduler.schedulers.background import BackgroundScheduler

from app.ingestion.weather_ingestion import run as run_ingestion
from app.processing.weather_processing import run as run_processing

def weather_pipeline_job():
    print("Starting weather data pipeline work...")
    run_ingestion()
    run_processing()
    print("Weather data pipeline work completed.")
    
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(weather_pipeline_job, 'interval', minutes=60, id='weather_pipeline_job', replace_existing=True)
    scheduler.start()
    print("Weather scheduler started, running every hour.")