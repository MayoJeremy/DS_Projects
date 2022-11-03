import os
import sqlite3
from pathlib import Path
from dish import Pizza, Auflauf, Salat

os.chdir(Path(__file__).parent.parent.parent)


class Menu:
    def __init__(self, db_name) -> None:
        self.list_pizza = []
        self.list_auflauf = []
        self.list_salat = []
        self.conn = sqlite3.connect("./data/" + db_name)
        self.cursor = self.conn.cursor()

    def import_menu_items_from_db(self):
        sql = "SELECT * FROM Menu;"
        self.cursor.execute(sql)
        self.menu = self.cursor.fetchall()

    def initialize_menu_items(self):
        for dish in self.menu:
            if dish[2] == "Pizza":
                self.list_pizza.append(
                    Pizza(
                        dish[0],
                        dish[1],
                        dish[3],
                    )
                )
            if dish[2] == "Auflauf":
                self.list_auflauf.append(
                    Auflauf(
                        dish[0],
                        dish[1],
                        dish[3],
                    )
                )
            if dish[2] == "Salat":
                self.list_salat.append(
                    Salat(
                        dish[0],
                        dish[1],
                        dish[3],
                    )
                )

    def print_menu(self):
        print("Pizza:\n")
        for pizza in self.list_pizza:
            print(pizza)
        print("\nAuflauf:\n")
        for auflauf in self.list_auflauf:
            print(auflauf)
        print("\nSalat:\n")
        for salat in self.list_salat:
            print(salat)


def main():
    testmenu = Menu("acasa.db")
    testmenu.import_menu_items_from_db()
    testmenu.initialize_menu_items()
    testmenu.print_menu()


if __name__ == "__main__":
    main()
