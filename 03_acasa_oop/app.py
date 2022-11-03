"""
Hauptprogramm Neuversuch
"""
from acasa.restaurant.menu import Menu
from acasa.restaurant.customer import Customer
from acasa.restaurant.menu import Menu


WELCOME_MSG = "Welcome to Acasa Restaurant"
DB_NAME = "acasa.db"


def get_customer_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    tel = input("Enter your telephone: ")

    return first_name, last_name, tel


def main():
    menu = Menu("acasa.db")
    menu.import_menu_items_from_db()
    menu.initialize_menu_items()

    print(WELCOME_MSG)
    print()

    customer = Customer(*get_customer_info(), DB_NAME)
    customer.input_customer()

    print(customer)
    menu.print_menu()

    while True:
        break


if __name__ == "__main__":
    main()
