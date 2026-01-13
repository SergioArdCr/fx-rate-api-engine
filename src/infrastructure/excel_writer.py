import pandas as pd
from config.settings import EXCEL_PATH

def write_exchange_rates_to_excel(base_code, rates, timestamp, provider, is_fallback):
    rows = []
    for cur, rate in rates.items():
        rows.append({
            "Base": base_code,
            "Target": cur,
            "Rate": rate,
            "Timestamp": timestamp,
              "Fallback": is_fallback
        })
    df = pd.DataFrame(rows)
    df.to_excel(EXCEL_PATH, index=False)
