from datetime import datetime

def build_exchange_rate_model(source, quotes, timestamp, is_fallback=False, provider=None):
    return {
        "source": source,
        "rates": quotes,
        "timestamp": timestamp,
        "processed_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "is_fallback": is_fallback
    }
