import json
import os
from pathlib import Path
from sqlalchemy.orm import declarative_base

os.chdir(Path(__file__).parent.parent)


with open("./data/config.json", mode="r", encoding="UTF-8") as file:
    config_dict = json.load(file)


DB_BASE = declarative_base()

# Database credentials
DB_HOST = config_dict.get("db_host")
DB_USER = config_dict.get("db_user")
DB_PASSWORD = config_dict.get("db_password")
DB_NAME = config_dict.get("db_database")

# Database connectionstring for sqlalchemy
DB_CONNECTION_STRING = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
