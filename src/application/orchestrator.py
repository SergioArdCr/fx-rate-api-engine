from src.application.use_cases import process_exchange_rates
from config.settings import BASE_CURRENCY
from src.observability.logger import logger

def run():
    logger.info(f"Inicio del proceso")
    process_exchange_rates(BASE_CURRENCY)
