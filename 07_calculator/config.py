import json
import os
from pathlib import Path

os.chdir(Path(__file__).parent)


with open("./data/config.json", mode="r", encoding="UTF-8") as file:
    config_dict = json.load(file)

APP_TITLE = config_dict.get("app_title")
APP_WIDTH = config_dict.get("app_width")
APP_HEIGHT = config_dict.get("app_height")
