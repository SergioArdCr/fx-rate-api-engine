from src.infrastructure.database import read_data, write_data

def save_exchange_rates(data):
    write_data(data)

def get_last_exchange_rates():
    return read_data()
