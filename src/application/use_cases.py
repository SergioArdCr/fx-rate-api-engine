from config.settings import API_PROVIDERS_PRIORITY, TARGET_CURRENCIES
from src.integration.provider_factory import get_provider
from src.domain.validators import validate_rates, validate_variation
from src.domain.models import build_exchange_rate_model
from src.infrastructure.repositories import save_exchange_rates, get_last_exchange_rates
from src.infrastructure.excel_writer import write_exchange_rates_to_excel
from src.observability.logger import logger

def process_exchange_rates(base_currency):
    last_data = get_last_exchange_rates()
    final_rates = {}
    timestamp = None

    for currency in TARGET_CURRENCIES:
        obtained = False
        for provider_name in API_PROVIDERS_PRIORITY:
            provider = get_provider(provider_name)
            try:
                data = provider.fetch_rates(base_currency,currency)  # pasamos la lista de monedas
                rate = data["rates"].get(currency)
                if rate is None:
                    raise Exception(f"{currency} no disponible en {provider_name}")
                final_rates[currency] = rate
                timestamp = data["timestamp"]
                obtained = True
                logger.info(f"{currency} obtenido desde {provider_name} con valor de {rate}")
                break
            except Exception as e:
                logger.warning(f"Fallo {currency} en {provider_name}: {e}")

        if not obtained:
            logger.warning(f"No se pudo obtener {currency} de ningún proveedor")

    if not final_rates:
        logger.warning("No se pudo obtener ninguna tasa, usando fallback")
        if last_data:
            final_rates = last_data["quotes"]
            timestamp = last_data["timestamp"]
            provider_used = "fallback_local"
            is_fallback = True
        else:
            raise Exception("No hay datos históricos para fallback")
    else:
        provider_used = "multi_api"
        is_fallback = False

    if not validate_rates(final_rates):
        raise Exception("Valores inválidos en quotes")

    if last_data and not validate_variation(final_rates, last_data["rates"]):
        logger.warning("Variación fuera de rango")

    model = build_exchange_rate_model(base_currency, final_rates, timestamp, is_fallback, provider_used)
    save_exchange_rates(model)
    write_exchange_rates_to_excel(base_currency, final_rates, timestamp, provider_used, is_fallback)
    logger.info(f"Tasas procesadas correctamente: {final_rates}")
