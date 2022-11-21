import os
import json
from pathlib import Path

os.chdir(Path(__file__).parent.parent)

DATADIR = "./data/"
MANAGEDIR = "./management"
APPDIR = "./budgeter"

CONFIG_FILE_NAME = "config.json"


with open(DATADIR+CONFIG_FILE_NAME, mode="r", encoding="UTF-8") as file_in:
    data_dict = json.load(file_in)

DB_CRED = data_dict.get("db_cred")
