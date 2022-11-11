import json
import os
from pathlib import Path
from sqlalchemy.orm import declarative_base

os.chdir(Path(__file__).parent.parent)


with open("./data/config.json", mode="r", encoding="UTF-8") as file:
    config_dict = json.load(file)


DB_BASE = declarative_base()
