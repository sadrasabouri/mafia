import json
from typing import Dict


config_path : str = "config/"

def load_data(filename : str) -> Dict:
    with open(config_path + filename) as f:
        data = json.load(f)
        return data
