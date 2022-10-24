"""
Hauptprogramm
"""

from menu import loadData
from invoice import listItems, printOrder


def main():
    menu_dict = loadData("acasa.json")
    order = [(10, 2), (11, 1)]  # TODO whileloop for Order and Quit
    try:
        price_total, printable_list = listItems(order, menu_dict)
    except KeyError as e:
        print(e)
        # TODO fehlenden Menüeintrag nacheintragen?
        print("Menu überprüfen (acasa.json)")
    else:
        printOrder(price_total, printable_list)


if __name__ == "__main__":
    main()
