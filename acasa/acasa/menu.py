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
        item_menu_id = menuID(menu_dict, item_category)
        menu_dict[item_menu_id] = {
            "Item_ID": item_name,
            "Category": item_category,
            "Price": float(item_price),
        }

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


def loadData(file_name: str) -> dict:
    menu_dict = {}
    if (DATA_DIR / file_name).is_file():
        with open(DATA_DIR / file_name, "r") as f:
            menu_dict = json.load(f)
    else:
        saveData(DATA_DIR / file_name, menu_dict)
    return menu_dict


def saveData(file_name: str, menu_dict: dict) -> None:
    with open(DATA_DIR / file_name, "w") as f:
        json.dump(menu_dict, f, indent=4, ensure_ascii=False)


def main():
    file_name = "acasa.json"
    test_dict = loadData(file_name)
    addEntry(
        test_dict,
        item_category="Pizza",
        item_price=1.25,
        item_name="Pizza Thuenfisch",
    )
    print(test_dict)
    # print(test_dict["10"])
    saveData(file_name, test_dict)


if __name__ == "__main__":
    main()
