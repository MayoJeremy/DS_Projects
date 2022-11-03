class Dish:
    def __init__(self, dish_id, title, price) -> None:
        self.dish_id = dish_id
        self.title = title
        self.price = price

    def __repr__(self) -> str:
        return f"[ {self.dish_id} ]: {self.title}\t- {self.price}"


class Pizza(Dish):
    def __init__(self, dish_id, title, price) -> None:
        super().__init__(dish_id, title, price)


class Auflauf(Dish):
    def __init__(self, dish_id, title, price) -> None:
        super().__init__(dish_id, title, price)


class Salat(Dish):
    def __init__(self, dish_id, title, price) -> None:
        super().__init__(dish_id, title, price)
