import json

def load_specification(version_number):
    file_name = f"v{version_number}.json"
    data = {}
    with open(f"program/config/specifications/{file_name}") as f:
        data = json.load(f)
    return data
    
