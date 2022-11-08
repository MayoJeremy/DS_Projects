import json
import os
from pathlib import Path

os.chdir(Path(__file__).parent)


with open("./config.json", mode="r", encoding="UTF-8") as file:
    config_dict = json.load(file)


DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "12345"
DB_PORT = "3306"
DB_NAME = "urlshortener"
