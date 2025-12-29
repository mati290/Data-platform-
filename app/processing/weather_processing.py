import json
from pathlib import Path
import pandas as pd
import numpy as np

RAW_DATA_DIR = Path("data/raw/weather")
PROCESSED_DATA_DIR = Path("data/processed/weather")

def get_latest_raw_data() -> Path:
    files = list(RAW_DATA_DIR.glob("weather_data_*.json"))
    
    if not files:
        raise FileNotFoundError("No raw data files found.")
    
    return max(files, key=lambda f: f.stat().st_mtime)


def load_raw_weather_data(file_path: Path) -> pd.DataFrame:
    with open(file_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        
    hourly = raw_data.get("hourly")
    
    df = pd.DataFrame({
        "time": hourly["time"],
        "temperature": hourly["temperature_2m"],
    })
    
    df["time"] = pd.to_datetime(df["time"])
    return df

def process_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    
    df["temperature"] = df["temperature"].astype(float)
    df["temp_above_avg"] = df["temperature"] > np.mean(df["temperature"])
    
    return df

def save_processed_data(df: pd.DataFrame, source_file: Path) -> Path:
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = source_file.stem.replace("weather_", "")
    output_path = PROCESSED_DATA_DIR / f"processed_weather_{timestamp}.CSV"

    df.to_csv(output_path, index=False)
    
    return output_path


def run():
    raw_file = get_latest_raw_data()
    print(f"Loading raw data from {raw_file}")
    
    df_raw = load_raw_weather_data(raw_file)
    df_processed = process_weather_data(df_raw)
    
    output_file = save_processed_data(df_processed, raw_file)
    print(f"Saved processed data to {output_file}")
    
if __name__ == "__main__":
    run()