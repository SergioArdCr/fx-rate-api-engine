from config.settings import MAX_VARIATION

def validate_rates(rates: dict):
    return all(v > 0 for v in rates.values())

def validate_variation(current: dict, previous: dict):
    for key in current:
        if key not in previous:
            continue
        if abs(current[key] - previous[key]) / previous[key] > MAX_VARIATION:
            return False
    return True
