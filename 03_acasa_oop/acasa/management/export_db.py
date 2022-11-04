import sqlite3


class SQLExporter:
    def __init__(self, db_name: str) -> None:
        self.conn = sqlite3.connect("./data/" + db_name)
        self.cursor = self.conn.cursor()

    def insert_dish_json_dict(self, json_file):
        sql = "INSERT INTO Menu (DishID, Title, Category, Price) VALUES (?,?,?,?);"
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


def main():
    # dbImport = JsonImporter("menu.json")
    # dbImport.get_content()
    # sExport = SQLExporter("acasa.db", dbImport.menu)
    # sExport.insert_dish_json_dict()
    pass


if __name__ == "__main__":
    main()
