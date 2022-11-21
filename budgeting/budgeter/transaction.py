from management.dbman import Dbman
from datetime import datetime


class Transaction:
    dbman = Dbman()

    def __init__(self, id, wallet_id, category_id, date, amount) -> None:
        self.id = id
        self.wallet_id = wallet_id
        self.category_id = category_id
        self.date = date
        self.amount = amount

    @classmethod
    def create_and_add_transaction_to_db(cls, wallet_id, category_id, amount):
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        trans_id =
        return cls(trans_id, wallet_id, category_id, date, amount)

    @staticmethod
    def save_transaction_to_db(wallet_id, category_id, date, amount):
        sql_statement = "INSERT INTO transaction (wallet_id,category_transaction_id,date,amount) VALUES(%s,%s,%s,%s)"
        return Transaction.dbman.insert_entry_and_retrieve_id(
            sql_statement, (wallet_id, category_id, date, amount))
