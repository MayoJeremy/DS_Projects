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
):
    try:
        """
        TODO: Check for existing item_name in menu_dict -> exit function/return
        """
        item_menu_id = menuID(menu_dict, item_category)
        menu_dict[item_category].update(
            {
                item_menu_id: {
                    "Item_ID": item_name,
                    "Price": float(item_price),
                }
            },
        )
    except KeyError:
        start, end = input(
            f"For {item_category} is no ID-Range specified.\n(start,end)>>"
        ).split(",")
        addCat(menu_dict, item_category, int(start), int(end))
        addEntry(menu_dict, item_name, item_price, item_category)


def addCat(cat_dict: dict, item_category: str, start: int, end: int):
    """adds Title and range for Item's categories to base Dictionary.

    Args:
        cat_dict (dict): Ranges with descriptional titles.
        item_category (str): Categories name.
        start (int): Startpoint.
        end (int): Endpoint.
    """
    cat_dict[item_category] = {"start": start, "end": end}


def menuID(menu_dict: dict, item_category: str) -> str:
    item_id = len(menu_dict[item_category]) - 2 + menu_dict[item_category]["start"]
    return str(item_id) if item_id < menu_dict[item_category]["end"] else "9999"


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
        item_name="Pizza Thuenfisch",
    )
    print(test_dict)
    saveData(DATA_DIR / "test.json", test_dict)


if __name__ == "__main__":
    main()
