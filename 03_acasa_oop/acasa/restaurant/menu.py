import os
import sqlite3
from pathlib import Path
from acasa.restaurant.dish import Dish

os.chdir(Path(__file__).parent.parent.parent)


class Menu:
    def __init__(self, db_name) -> None:
        self.menu_dishes = {}
        self.conn = sqlite3.connect("./data/" + db_name)
        self.cursor = self.conn.cursor()

    def import_menu_items_from_db(self):
        sql = "SELECT * FROM Menu;"
        self.cursor.execute(sql)
        self.menu = self.cursor.fetchall()

    def initialize_menu_items(self):
        for dish in self.menu:
            self.menu_dishes[dish[0]] = Dish(*dish)

    def print_menu(self):
        print("Pizza:\n")
        for dish in self.menu_dishes.values():
            if dish.category == "Pizza":
                print(dish)
        print("\nAuflauf:\n")
        for dish in self.menu_dishes.values():
            if dish.category == "Auflauf":
                print(dish)
        print("\nSalat:\n")
        for dish in self.menu_dishes.values():
            if dish.category == "Salat":
                print(dish)


def main():
    testmenu = Menu("acasa.db")
    testmenu.import_menu_items_from_db()
    testmenu.initialize_menu_items()
    testmenu.print_menu()


if __name__ == "__main__":
    main()
