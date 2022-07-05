import json
from types import SimpleNamespace

cfg_json = 'config.json'

def load(cfg_path=cfg_json):
    with open(cfg_path, 'r') as j:
        config_dict = json.load(j)

    config = SimpleNamespace(**config_dict)

    return config

def update(payload: dict, cfg_path=cfg_json):
    with open(cfg_path, 'r+') as j:
        config_dict = json.load(j)

        j.seek(0)
        
        for i in payload:
            if i in config_dict:
                config_dict[i] = payload[i]

        json.dump(config_dict, j, indent=4)

        j.truncate()

    return load(cfg_path)
