from src.integration.exchangerate_convert_client import ExchangeRateClient
from src.integration.open_er_latest_client import OpenERClient

def get_provider(name: str):
    if name == "exchangerate":
        return ExchangeRateClient()
    elif name == "open_er":
        return OpenERClient()
    else:
        raise Exception(f"Proveedor desconocido: {name}")
