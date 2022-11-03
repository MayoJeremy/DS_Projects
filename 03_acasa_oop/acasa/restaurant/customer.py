import os
import sqlite3
from pathlib import Path

os.chdir(Path(__file__).parent.parent.parent)


class Customer:
    def __init__(self, first_name, last_name, tel, db_name, customer_id=0) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.customer_id = customer_id

        self.conn = sqlite3.connect("./data/" + db_name)
        self.cursor = self.conn.cursor()

    def input_customer(self):
        sql = "INSERT INTO Customer (FirstName, LastName, Tel) VALUES (?,?,?);"
        data = [self.first_name, self.last_name, self.tel]
        self.cursor.execute(sql, data)
        self.conn.commit()
        self.customer_id = self.cursor.lastrowid


def main():
    pass


if __name__ == "__main__":
    main()
