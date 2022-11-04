class Dish:
    def __init__(self, dish_id, title, category, price) -> None:
        self.dish_id = dish_id
        self.title = title
        self.category = category
        self.price = price

    def __repr__(self) -> str:
        return f"[ {self.dish_id} ]: {self.title}\t- {self.price}"
