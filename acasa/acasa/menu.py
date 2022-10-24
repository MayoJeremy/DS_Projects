"""Menu-file"""
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"


def addEntry(menu_dict: dict, item_name: str, item_price: float) -> dict:
    pass


def loadData(file_path: str) -> dict:
    menu_dict = {}
    if file_path.is_file():
        with open(file_path, "r") as f:
            menu_dict = json.load(f)
    else:
        saveData(file_path, menu_dict)
    return menu_dict


def saveData(file_path: str, menu_dict: dict) -> None:
    with open(file_path, "w") as f:
        json.dump(menu_dict, f, indent=4, ensure_ascii=False)


def main():
    loadData(DATA_DIR / "test.json")


if __name__ == "__main__":
    main()
