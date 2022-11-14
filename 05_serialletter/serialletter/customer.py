from dbman import Dbman
import config as cfg


class Customer:
    def __init__(self, first_name, last_name, mail, street, city) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.street = street
        self.city = city
        self.db = Dbman()
        self.set_customer_id()

    def set_customer_id(self):
        try:
            self.id = self.get_customer_id_from_db()
        except TypeError:
            self.export_customer_to_db()
            self.id = self.db.cursor.lastrowid

    def get_customer_id_from_db(self):
        sql = "SELECT id FROM customer WHERE firstname = %s AND lastname = %s AND mail = %s AND street = %s AND city_id = %s;"
        customer_id_from_db = self.db.get_one_entry(
            sql,
            (self.first_name, self.last_name, self.mail, self.street, self.city),
        )
        return customer_id_from_db[0]

    def get_customer_id(self):
        if not self.id:
            self.set_customer_id()

        return self.id

    def export_customer_to_db(self):
        sql = "INSERT INTO customer (firstname, lastname, mail, street, city_id) VALUES (%s,%s,%s,%s,%s)"


cust = Customer("tesst", "test", "test", "test", 1)
print(cust.id)
