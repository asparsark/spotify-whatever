import json

cfg_json = 'config.json'

def load(cfg_path=cfg_json):
    with open(cfg_path, 'r') as j:
        cfg = json.load(j)

    return cfg


def update(payload: dict, cfg_path=cfg_json):
    cfg = load()

    for i in payload:
        if i in cfg:
            cfg[i] = payload[i]

    with open(cfg_path, 'w') as j:
        json.dump(cfg, j, indent=4)

    return