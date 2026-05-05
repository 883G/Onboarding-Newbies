import re

def clean_str_from_spicel_characters(string: str) -> str:
    # Removes all special characters except spaces and alphanumeric characters
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', string)
    return cleaned
