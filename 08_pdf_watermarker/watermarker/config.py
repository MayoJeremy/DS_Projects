import os
import json
from pathlib import Path

os.chdir(Path(__file__).parent.parent)

DATADIR = "./data/"
RESULTDIR = DATADIR+"output/"
CONFIG_FILE_NAME = "config.json"


with open(DATADIR+CONFIG_FILE_NAME, mode="r", encoding="UTF-8") as file_in:
    data_dict = json.load(file_in)


WATERTEXT = data_dict.get("watermark")
FOOTER_TEMPLATE_FILE = data_dict.get("footer")
STAMP_TEMPLATE_FILE = data_dict.get("waterstamp")
