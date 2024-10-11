import json
from datetime import datetime

def load_json(filename: str) -> dict:
    """
    Loads data from a JSON file.

    Args:
        filename (str): The name of the file to load.

    Returns:
        dict: The data loaded from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

def save_json(filename: str, data: dict) -> None:
    """
    Saves data to a JSON file.

    Args:
        filename (str): The name of the file to save to.
        data (dict): The data to save.
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def format_datetime(dt: datetime) -> str:
    """
    Formats a datetime object to a string.

    Args:
        dt (datetime): The datetime object to format.

    Returns:
        str: The formatted datetime string.
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")