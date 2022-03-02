import json


def read_config():
    config = json.loads(open("config.json", "r", encoding="utf-8").read())

    return config
