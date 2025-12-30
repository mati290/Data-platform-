import matplotlib.pyplot as plt
import pandas as pd

from app.db.session import SessionLocal
from app.db.models.weather import WeatherData

def load_weather_data():
    session = SessionLocal()
    try:
        records = session.query(WeatherData).order_by(WeatherData.time).all()
        data = [{
            "time": record.time,
            "temperature": record.temperature,
        } for record in records]
        
        return pd.DataFrame(data)
    finally:
        session.close()
        
def plot_temperature():
    df = load_weather_data()
    
    plt.figure(figsize=(10, 5))
    plt.plot(df["time"], df["temperature"])
    plt.title("Temperature Over Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.tight_layout()
    
    plt.savefig("temperature_over_time.png")
    plt.show()
    
if __name__ == "__main__":
    plot_temperature()
