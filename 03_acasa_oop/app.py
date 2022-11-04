"""
Hauptprogramm Neuversuch
"""
import os
from acasa.restaurant.menu import Menu
from acasa.restaurant.customer import Customer
from acasa.restaurant.order import Order
from acasa.management.sqlhandler import SQLHandler
from pathlib import Path


os.chdir(Path(__file__).parent)


WELCOME_MSG = "Welcome to Acasa Restaurant"
DB_NAME = "acasa.db"


def get_customer_order_list(menu: Menu):
    order_list = []
    while True:
        user_in = input("(0) to end Order.\nYour Order-nr >> ")

        if user_in.isdigit():
            user_in = int(user_in)
        else:
            print("Please put in a Number.")
            continue
        user_order = menu.menu_dishes.get(user_in)
        if user_in == 0:
            return order_list
        elif not user_order:
            print("Please put a valid Order Number in.")
            continue
        order_list.append(user_order)


def main():
    db_exporter = SQLHandler(DB_NAME)
    menu_import = db_exporter.import_menu_items_from_db()
    menu = Menu(menu_import)

    menu.initialize_menu_items()

    print(WELCOME_MSG)
    print()

    is_reg = int(input("0 | new User\nID | existing User >>"))
    if is_reg:
        cust_data = db_exporter.get_customer_data(is_reg)
        customer = Customer(*cust_data)
    else:
        customer = Customer.get_customer_info_and_make_customer()
    customer.customer_id = db_exporter.input_customer_and_retrieve_customer_id(customer)

    menu.print_menu()
    cust_order_list = get_customer_order_list(menu)
    cust_order = Order(customer, cust_order_list)
    db_exporter.input_order(cust_order)
    cust_order.print_receipt()

    db_exporter.conn.close()


if __name__ == "__main__":
    main()
