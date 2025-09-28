import requests  # type: ignore

# Example payload for crop yield prediction
payload = {
    "prediction_type": "crop_yield",
    "data": {
        "crop": "wheat",
        "soil_type": "loamy",
        "weather": {"temperature_avg": 25, "rainfall": 100},
        "fertilizer_amount": 120
    }
}

url = "http://127.0.0.1:8000/predict"

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())
