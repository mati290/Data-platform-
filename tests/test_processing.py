import pandas as pd
from app.processing.weather_processing import process_weather_data

def test_process_weather_data():
    df = pd.DataFrame({
        "temperature": [10, 20, 30],
        "temperature_c": [10.0, 20.0, 30.0],
    })

    result = process_weather_data(df)

    assert "temp_above_avg" in result.columns
    assert result["temp_above_avg"].sum() == 1
