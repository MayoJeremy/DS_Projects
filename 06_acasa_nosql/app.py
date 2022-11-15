from pymongo import MongoClient
import json
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

DB_NAME = "acasa"
COLLECTION_NAME = "dish"

server = "mongodb://localhost:27017"
client = MongoClient(server)

db = client[DB_NAME]
collection = db[COLLECTION_NAME]


def import_old_json_menu():
    with open("menu.json", mode="r", encoding="UTF-8") as file_in:
        menu = json.load(file_in)

    data = []
    for category, dish_list in menu.items():
        for dish in dish_list:
            data.append(
                {
                    "_id": dish["id"],
                    "title": dish["title"],
                    "price": dish["price"],
                    "category": category,
                }
            )
    insert_multiple_records_with_id(data)


def insert_multiple_records_with_id(data):
    collection.insert_many(data)


def insert_one_record_without_id(data):
    collection.insert_one(data)


def display_menu(menu_list):
    categories = set([menu_item["category"] for menu_item in menu_list])
    for category in categories:
        print(category + "\n")
        dishes_from_cat = [
            dish for dish in menu_list if dish.get("category") == category
        ]

        for dish in dishes_from_cat:
            print("{}. {} {}€".format(dish["_id"], dish["title"], dish["price"]))
        print()


def get_dishes_via_category(category):

    return collection.find({"category": category})


def get_dish_via_id(id):
    return collection.find_one({"_id": id})


def get_user_wishes():
    user_in = 1
    order_list = []
    print("Your Order please.")
    while user_in:
        user_in = int(input("0 to quit >> "))
        dish = get_dish_via_id(user_in)
        if dish:
            order_list.append(dish)
    return order_list


def main():
    # import_old_json_menu()
    menu_list = list(collection.find({}))
    display_menu(menu_list)
    user_wishes = get_user_wishes()


if __name__ == "__main__":
    main()
