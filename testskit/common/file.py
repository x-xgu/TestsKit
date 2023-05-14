import csv
import json
from typing import Any

import yaml


def load_json(file_path: str) -> Any:
    """
    Load json file from project
    """
    with open(file_path) as f:
        json_data = json.load(f)
    return json_data


def load_yml(file_path: str) -> Any:
    """
    Load yml file from project
    """
    with open(file_path) as f:
        yml_data = yaml.safe_load(f)
    return yml_data


def load_csv(file_path: str) -> Any:
    """
    Load csv file from project and return list of lists
    """
    data = []
    with open(file_path, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            data.append(row)
    return data
