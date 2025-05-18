import json
from utils.open_json import save_json

def ignore(type:str, user_input: str, config, config_path: str) -> None:
    config[f'ignore{type}'].extend([user_input.split(' ')])
    save_json(config_path, config)
    return