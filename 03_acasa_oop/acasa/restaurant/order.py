import os
import sqlite3
from pathlib import Path
from customer import Customer
from dish import Pizza

os.chdir(Path(__file__).parent.parent.parent)


class Order:
    def __init__(self, customer, dish_order_list, db_name) -> None:
        self.customer = customer
        self.dish_order_list = dish_order_list
        self.total = 0

        self.conn = sqlite3.connect("./data/" + db_name)
        self.cursor = self.conn.cursor()

    def process_dish_orders(self):
        for dish_order in self.dish_order_list:
            self.input_order()

    def input_order(self):
        sql = "INSERT INTO 'Order' (CustomerID, DishID) VALUES (?,?);"
        data = []
        for dish_order in self.dish_order_list:
            data.append((self.customer.customer_id, dish_order.dish_id))
        self.cursor.executemany(sql, data)
        self.conn.commit()

    def print_receipt(self):
        print(self.customer)
        for dish_order in self.dish_order_list:
            print(dish_order)
            self.total += dish_order.price
        print(f"Total = {self.total}")


def main():
    test_Customer = Customer("Test", "Mest", "+49151515151", "acasa.db", 1)
    test_Customer.input_customer()
    test_order = Order(test_Customer, [(Pizza(100, "Pizza Margeritta", 5))], "acasa.db")
    test_order.print_receipt()
    test_order.input_order()


if __name__ == "__main__":
    main()
