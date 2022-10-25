"""
Hauptprogramm
"""
import os
import sqlite3
from pathlib import Path
import json
import pprint
from collections import Counter

os.chdir(Path(__file__).parent)

conn = sqlite3.connect("../data/store.db")
cursor = conn.cursor()


def get_menu():
    sql = "SELECT  * FROM Menu;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return results


def insert_dish(data):
    sql = "INSERT INTO Menu (Dish_ID, Title, Category, Price) VALUES (?,?,?,?);"
    with conn:
        cursor.execute(sql, data)


def import_json_db(file):
    with open(file, "r") as f:
        menu = json.load(f)
    for category, values in menu.items():
        for value in values:
            insert_dish(
                (
                    value["id"],
                    value["title"],
                    category,
                    value["price"],
                )
            )


def get_order():
    counter = Counter()
    order_list = []
    order = []
    while 1:
        user_in = int(input("0 to quit | choice >> "))
        if not user_in:
            break
        counter[user_in] += 1
        order_list.append(user_in)
    for order_id, order_name in counter.items():
        order.append((order_id, order_name))
    return order


def make_receipt(orders: list):
    receipt = []
    receipt_total = 0.0

    def get_dish(dish_id: int):
        sql = f"SELECT Dish_ID, Title, Price FROM Menu WHERE Dish_ID = {dish_id}"
        cursor.execute(sql)
        return cursor.fetchone()

    for order in orders:
        dish = get_dish(order[0])
        dish_total = dish[-1] * order[1]
        receipt.append(
            "{}. {}: {:.2f} € x {} | {:.2f} €".format(
                *dish,
                order[1],
                dish_total,
            )
        )
        receipt_total += dish_total
    return receipt, receipt_total


def string_receipt(receipt_items: list, receipt_total: float):
    message = ""
    for row in receipt_items:
        message += row + "\n"
    message += 40 * "*" + "\n"
    message += f"Total: {receipt_total:.2f} €\n"
    return message


def save_receipt(receipt: str):
    with open("../data/receipt.txt", "w", encoding="UTF-8") as file:
        file.write(receipt)


def main():
    # file = "../data/menu.json"
    # import_json_db(file)
    # pprint.pprint(get_menu())
    order = get_order()
    receipt = make_receipt(order)
    receipt_string = string_receipt(*receipt)
    print(receipt_string)
    save_receipt(receipt_string)
    conn.close()


if __name__ == "__main__":
    main()
