"""
Hauptprogramm
"""
import os
import sqlite3
from pathlib import Path
import json
from collections import Counter

os.chdir(Path(__file__).parent)

conn = sqlite3.connect("../data/store.db")
cursor = conn.cursor()
ADMIN = False
WELCOME_MSG = "Willkommen bei Acasa!"
MODES = {"dish": "INSERT INTO Menu (DishID, Title, Category, Price) VALUES (?,?,?,?);",
         "order": "INSERT INTO 'Order' (CustomerID, DishID) VALUES (?,?);",
         "customer": "INSERT INTO Customer (FirstName, LastName, Tel) VALUES (:first_name, :last_name, :tel) ;",
         }


def get_menu():
    sql = "SELECT * FROM Menu;"
    cursor.execute(sql)
    return cursor.fetchall()


def get_menu_indexes():
    sql = "SELECT DishID From Menu;"
    cursor.execute(sql)
    result = cursor.fetchall()
    ite_result = []
    for r in result:
        ite_result.append(r[0])
    return ite_result


def string_menu(menu: str):
    menu_string = ""

    def string_category(category: str):
        return f"\n{category}\n" + 40 * "_" + "\n"

    def string_dish(dish_info: tuple):
        return "{}. {}\t|\t{}€\n".format(*dish_info)

    for _, dish in enumerate(menu):
        if not menu_string:
            menu_string += string_category(dish[2])
            menu_string += string_dish((dish[0], dish[1], dish[3]))
            continue
        if menu[_][2] != menu[_ - 1][2]:
            menu_string += string_category(dish[2])
        menu_string += string_dish((dish[0], dish[1], dish[3]))
    return menu_string


def insert_data(mode: str, data: tuple):
    with conn:
        cursor.execute(MODES.get(mode.lower()), data)





def get_customer_id(data: tuple):
    sql = "SELECT CustomerID FROM Customer WHERE FirstName = :first_name AND LastName = :last_name AND Tel = :tel "
    cursor.execute(sql, data)
    return cursor.fetchone()[0]


def import_json_db(file: str):
    with open(file, mode="r", encoding="UTF-8") as f:
        menu = json.load(f)
    for category, values in menu.items():
        for value in values:
            insert_data("dish",
                        (
                            value["id"],
                            value["title"],
                            category,
                            value["price"],
                        )
                        )
            


def get_order(customer_id: int):
    counter = Counter()
    order_list = []
    order = []
    accepted_items = get_menu_indexes()

    while 1:
        user_in = int(input("0 to quit | choice >> "))
        if not user_in:
            break
        if user_in not in accepted_items:
            print("Invalid Item selected. Try again")
            continue
        counter[user_in] += 1
        order_list.append(user_in)
        insert_data("order", (customer_id, user_in))
    for order_id, order_name in counter.items():
        order.append((order_id, order_name))
    return order


def make_receipt(orders: list):
    receipt = []
    receipt_total = 0.0

    def get_dish(dish_id: int):
        sql = f"SELECT DishID, Title, Price FROM Menu WHERE DishID = {dish_id}"
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

    return sorted(receipt), receipt_total


def string_receipt(receipt_items: list, receipt_total: float):
    message = "Quittung\n" + 40 * "_" + "\n"
    for row in receipt_items:
        message += row + "\n"
    message += 40 * "*" + "\n"
    message += f"Total: {receipt_total:.2f} €\n"
    return message


def save_receipt(receipt: str):
    with open("../data/receipt.txt", "w", encoding="UTF-8") as file:
        file.write(receipt.strip())


def register_customer():
    datapoints = ["first_name", "last_name", "tel"]
    customer = {}
    for datapoint in datapoints:
        customer[datapoint] = input(f"{datapoint.title()}: ")
    return customer


def main():
    if ADMIN:
        file = "../data/menu.json"
        import_json_db(file)

    print(WELCOME_MSG)
    customer = register_customer()
    insert_data("customer", customer)
    customer_id = get_customer_id(customer)

    print()

    menu = get_menu()
    print(string_menu(menu))

    print("Ihre Bestellung")
    order = get_order(customer_id)

    receipt = make_receipt(order)
    receipt_string = string_receipt(*receipt)
    print(receipt_string)
    save_receipt(receipt_string)


if __name__ == "__main__":
    main()

conn.close()
