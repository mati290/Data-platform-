from unittest.mock import patch
from app.ingestion.weather_ingestion import fetch_weather_data

def test_fetch_weather_data():
    mock_response = {
        "hourly": {
            "temperature_2m": [10, 15, 20]
        }
    }

    with patch(
        "app.ingestion.weather_ingestion.requests.get"
    ) as mock_get:
        mock_get.return_value.json.return_value = mock_response
        mock_get.return_value.status_code = 200

        data = fetch_weather_data()

        assert "hourly" in data
        assert "temperature_2m" in data["hourly"]
