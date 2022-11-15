from pymongo import MongoClient
import json
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

DB_NAME = "acasa"
COLLECTION_NAME_DISH = "dish"
COLLECTION_NAME_CUSTOMER = "customer"

server = "mongodb://localhost:27017"
client = MongoClient(server)

db = client[DB_NAME]
dish_collection = db[COLLECTION_NAME_DISH]
customer_collection = db[COLLECTION_NAME_CUSTOMER]


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
    insert_multiple_records_with_id(dish_collection, data)


def insert_multiple_records_with_id(collection, data):
    collection.insert_many(data)


def insert_one_record_without_id(collection, data):
    return collection.insert_one(data).inserted_id


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


def get_multiple_entries_via_category(collection, category):

    return dish_collection.find({"category": category})


def get_one_entry_via_id(collection, id):
    return collection.find_one({"_id": id})


def check_customer_registration(customer_data):
    return customer_collection.find_one(customer_data)


def get_user_wishes():
    user_in = 1
    order_list = []
    print("Your Order please.")
    while user_in:
        user_in = int(input("0 to quit >> "))
        dish = get_one_entry_via_id(dish_collection, user_in)
        if dish:
            order_list.append(dish)
    return order_list


def print_receipt(order_list):
    for order in order_list:
        print(f"{order['_id']} {order['title']} {order['price']} €")


def get_customer_info():
    customer_data = {}
    customer_data["first_name"] = input("First Name: ")
    customer_data["last_name"] = input("Last Name: ")
    return customer_data


def main():
    # import_old_json_menu()
    menu_list = list(dish_collection.find({}))

    # Get Customer info and save to DB if new customer
    customer = get_customer_info()
    db_customer = check_customer_registration(customer)
    if not db_customer:
        customer["_id"] = insert_one_record_without_id(customer_collection, customer)
    else:
        customer = db_customer

    display_menu(menu_list)

    user_wishes = get_user_wishes()
    print_receipt(user_wishes)


if __name__ == "__main__":
    main()
