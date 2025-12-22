import requests
import json 
from datetime import datetime
from pathlib import Path

BASE_URL = "https://api.open-meteo.com/v1/forecast"

PARMS = {
    "latitude": 52.23,
    "longitude": 21.01,
    "hourly": "temperature_2m",
}

def fetch_weather_data(parms=PARMS):
    response = requests.get(BASE_URL, params=parms, timeout=10)
    response.raise_for_status()
    return response.json()

def save_raw_data(data: dict):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    
    base_path = Path("data/raw/weather")
    base_path.mkdir(parents=True, exist_ok=True)
    
    file_path = base_path / f"weather_data_{timestamp}.json"
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    return file_path

def run():
    data = fetch_weather_data()
    file_path = save_raw_data(data)
    print(f"Saved raw data to {file_path}")
    
if __name__ == "__main__":
    run()