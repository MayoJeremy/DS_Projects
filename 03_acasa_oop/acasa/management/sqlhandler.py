import sqlite3


class SQLHandler:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.conn = sqlite3.connect("./data/" + self.db_name)
        self.cursor = self.conn.cursor()

    def import_menu_items_from_db(self):
        sql = "SELECT * FROM Menu;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert_dish_json_dict(self, json_file):
        sql = """
        INSERT INTO Menu (DishID, Title, Category, Price) VALUES (?,?,?,?);
        """
        data = []
        for category, dishes in json_file.items():
            for dish in dishes:
                data.append(
                    (
                        dish["id"],
                        dish["title"],
                        category,
                        dish["price"],
                    )
                )
        self.cursor.executemany(sql, data)
        self.conn.commit()

    def insert_dish(self, dish):
        sql = """
        INSERT INTO MENU (DishID, Title, Category, Price)
        VALUES (:dish_id, :title, :category, :price)
        """
        self.cursor.execute(sql, dish.__dict__)

    def input_customer_and_retrieve_customer_id(self, customer):
        sql = """
        INSERT INTO Customer (FirstName, LastName, Tel)
        VALUES (:first_name, :last_name, :tel);
        """
        self.cursor.execute(sql, customer.__dict__)
        self.conn.commit()
        return self.cursor.lastrowid

    def get_customer_data(self, customer_id: int):
        sql = """
        SELECT FirstName, LastName, Tel
        FROM Customer
        WHERE CustomerID = ?
        """
        self.cursor.execute(sql, (customer_id,))
        return self.cursor.fetchone()

    def input_order(self, order):
        sql = "INSERT INTO 'Order' (CustomerID, DishID) VALUES (?,?);"
        data = []
        for dish_order in order.dish_order_list:
            data.append((order.customer.customer_id, dish_order.dish_id))
        self.cursor.executemany(sql, data)
        self.conn.commit()
