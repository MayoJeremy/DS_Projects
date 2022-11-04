from acasa.restaurant.dish import Dish


class Menu:
    def __init__(self, menu) -> None:
        self.menu_dishes = {}
        self.menu = menu

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
