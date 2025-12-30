def test_weather_stats(client):
    response = client.get("/weather/stats")
    assert response.status_code == 200
    data = response.json()
    
    assert "average_temperature" in data
    assert "min_temperature" in data
    assert "max_temperature" in data
    