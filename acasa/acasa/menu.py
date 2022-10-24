"""Menu-file"""
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"


def addEntry(
    menu_dict: dict,
    item_name: str,
    item_price: float,
    item_category: str,
    item_menu_id: str,
) -> dict:
    try:
        menu_dict[item_category].update(
            {
                item_menu_id: {
                    "Item_ID": item_name,
                    "Price": float(item_price),
                }
            },
        )
    except KeyError:
        menu_dict[item_category] = {}
        addEntry(menu_dict, item_name, item_price, item_category, item_menu_id)


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
    test_dict = loadData(DATA_DIR / "test.json")
    addEntry(
        test_dict,
        item_category="Pizza",
        item_price=1.25,
        item_name="Pizza Thunfisch",
        item_menu_id="101",
    )
    saveData(DATA_DIR / "test.json", test_dict)


if __name__ == "__main__":
    main()
