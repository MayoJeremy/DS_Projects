class Order:
    def __init__(self, customer, dish_order_list) -> None:
        self.customer = customer
        self.dish_order_list = dish_order_list
        self.total = 0

    def print_receipt(self):
        print(self.customer)
        for dish_order in self.dish_order_list:
            print(dish_order)
            self.total += dish_order.price
        print(f"Total = {self.total}")
