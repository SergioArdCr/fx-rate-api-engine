import os, json
from config.settings import DATA_PATH

def read_data():
    if not os.path.exists(DATA_PATH):
        return None
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def write_data(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)
