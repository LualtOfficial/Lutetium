from configparser import ConfigParser

config = ConfigParser()


def read(path: str):
    config.read(path)
    return config["DEFAULT"]


def write(path: str, settings: dict):
    config["DEFAULT"] = settings
    with open(path, "w+") as file:
        config.write(file)
