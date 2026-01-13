import requests
from config.settings import TIMEOUT, TARGET_CURRENCIES

class OpenERClient:
    BASE_URL = "https://open.er-api.com/v6/latest/"

    def fetch_rates(self, source: str, target: str):
        resp = requests.get(f"{self.BASE_URL}{source}", timeout=TIMEOUT)
        if resp.status_code != 200:
            raise Exception(f"HTTP {resp.status_code}")

        data = resp.json()
        if data.get("result") != "success":
            raise Exception(f"Error API OpenER: {data}")

        rates = {
            cur: data["rates"][cur]
            for cur in TARGET_CURRENCIES
            if cur in data["rates"]
        }

        return {
            "rates": rates,
            "timestamp": data["time_last_update_unix"],
            "provider": "open_er"
        }
