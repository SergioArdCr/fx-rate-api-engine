API_BASE_URL = "https://api.exchangerate.host"
API_KEY = "da531ff8723e0e7e5b1ee5a0f645c34f"
BASE_CURRENCY = "USD"

TARGET_CURRENCIES = ["COP", "EUR", "MXN", "CAD", "CNY"]  # Puedes agregar o quitar

API_PROVIDERS_PRIORITY = ["exchangerate", "open_er"] # Prioridad de APIs

DATA_PATH = "data/exchange_rates.json"
EXCEL_PATH = "data/exchange_rates.xlsx"
LOG_PATH = "logs/app.log"

TIMEOUT = 10
MAX_VARIATION = 0.05
