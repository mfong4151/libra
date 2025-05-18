import json
def open_json(file):
    with open(file, 'r') as config_file:
        return json.load(config_file)
    
def save_json(file, data):
    with open(file, 'w') as config_file:
        json.dump(data, config_file, indent=4)