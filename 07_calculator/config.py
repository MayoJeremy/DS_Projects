import json
import os
from pathlib import Path

os.chdir(Path(__file__).parent)


with open("./data/config.json", mode="r", encoding="UTF-8") as file:
    config_dict = json.load(file)

APP_TITLE = config_dict.get("app_title")
APP_WIDTH = config_dict.get("app_width")
APP_HEIGHT = config_dict.get("app_height")

LABEL_WIDTH = config_dict.get("label_width")
LABEL_HEIGHT = config_dict.get("label_height")

NUM_WIDTH = config_dict.get("num_width")
NUM_HEIGHT = config_dict.get("num_height")

OPER_WIDTH = config_dict.get("oper_width")
OPER_HEIGHT = config_dict.get("oper_height")

NUMBERS_AVAILABLE = {
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (3, 0),
    "5": (3, 1),
    "6": (3, 2),
    "7": (4, 0),
    "8": (4, 1),
    "9": (4, 2),
    "0": (5, 0, 3),
}

OPERANT_AVAILABLE = {
    "+": (2, 3),
    "-": (3, 3),
    "*": (4, 3),
    "/": (5, 3),
}

