from configparser import ConfigParser

config = ConfigParser()


def read():
    config.read("/home/lualt/Lutetium/system/settings.ini")
    return config["DEFAULT"]


def write(settings: dict):
    config["DEFAULT"] = settings
    with open("/home/lualt/Lutetium/system/settings.ini", "w+") as file:
        config.write(file)
