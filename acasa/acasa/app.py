"""
Hauptprogramm
"""

from menu import loadData
from invoice import listItems, printOrder, getOrder


def main():

    menu_dict = loadData("acasa.json")
    order = getOrder()

    try:
        price_total, printable_list = listItems(order, menu_dict)
    except KeyError as e:
        print(e)
        # TODO fehlenden Menüeintrag nacheintragen? oder in getOrder catchen,
        # dass nicht existiert
        print("Menu überprüfen (acasa.json)")
    else:
        printOrder(price_total, printable_list)


if __name__ == "__main__":
    main()
