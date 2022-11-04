"""
Hauptprogramm Neuversuch
"""
from acasa.restaurant.menu import Menu
from acasa.restaurant.customer import Customer
from acasa.restaurant.order import Order
from acasa.management.export_db import SQLExporter


WELCOME_MSG = "Welcome to Acasa Restaurant"
DB_NAME = "acasa.db"


def get_customer_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    tel = input("Enter your telephone: ")

    return first_name, last_name, tel


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
    db_exporter = SQLExporter(DB_NAME, {})
    menu = Menu(DB_NAME)
    menu.import_menu_items_from_db()
    menu.initialize_menu_items()
    # print(menu.menu)

    print(WELCOME_MSG)
    print()

    customer = Customer(*get_customer_info(), DB_NAME)
    customer.customer_id = db_exporter.input_customer_and_retrieve_customer_id(customer)

    menu.print_menu()
    cust_order_list = get_customer_order_list(menu)
    cust_order = Order(customer, cust_order_list, DB_NAME)
    cust_order.process_dish_orders()
    cust_order.print_receipt()


if __name__ == "__main__":
    main()
