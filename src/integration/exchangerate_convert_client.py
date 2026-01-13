import requests
import time
from config.settings import API_BASE_URL, TIMEOUT, API_KEY

class ExchangeRateClient:
    
    def fetch_rates(self, source, target, amount: float = 1.0, retries: int = 3):
        url = f"{API_BASE_URL}/convert"
        params = {
            "access_key": API_KEY,
            "from": source,
            "to": target,
            "amount": amount
        }   
    
        for attempt in range(1, retries + 1):
            response = requests.get(url, params=params, timeout=TIMEOUT)

            if response.status_code == 429:
                wait_time = attempt * 2
                time.sleep(wait_time)
                continue

            if response.status_code != 200:
                raise Exception(f"API error HTTP: {response.status_code}")

            data = response.json()

            if not data.get("success"):
                raise Exception(f"Error API externa: {data}")

            return {
            "rate": data["info"]["quote"],
            "timestamp": data["info"]["timestamp"],
            "provider": "ExchangeRate"
            }

        raise Exception("Rate limit excedido despues de varios intentos")
