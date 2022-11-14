import json
import os
from pathlib import Path

os.chdir(Path(__file__).parent.parent)


with open("./data/config.json", mode="r", encoding="UTF-8") as file:
    config_dict = json.load(file)


# Database credentials
DB_HOST = config_dict.get("db_host")
DB_USER = config_dict.get("db_user")
DB_PASSWORD = config_dict.get("db_password")
DB_NAME = config_dict.get("db_database")
