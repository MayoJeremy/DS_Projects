import os
import json
from pathlib import Path

os.chdir(Path(__file__).parent.parent)

DATADIR = "./data/"
MANAGEDIR = "./management"
APPDIR = "./budgeter"

CONFIG_FILE_NAME = "config.json"
CATEGORY_FILE_NAME = "categories.json"


with open(DATADIR+CONFIG_FILE_NAME, mode="r", encoding="UTF-8") as file_in:
    data_dict = json.load(file_in)

with open(DATADIR+CATEGORY_FILE_NAME, mode="r", encoding="UTF-8") as file_in:
    category_dict = json.load(file_in)


DB_CRED = data_dict.get("db_cred")
CAT_INCOME = category_dict.get("Income")
CAT_EXPENSE = category_dict.get("Expense")
