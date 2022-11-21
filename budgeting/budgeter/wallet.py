from management.dbman import Dbman


class Wallet:
    dbman = Dbman()

    def __init__(self, id: int, user, name: str) -> None:
        self.id = id
        self.user = user
        self.name = name

    def __repr__(self):
        return f"{self.name} from {self.user}"

    @classmethod
    def create_and_add_wallet_to_db(cls, user, name):
        wallet_id = Wallet.save_wallet_to_db(user, name)
        return Wallet(wallet_id, user, name)

    @staticmethod
    def save_wallet_to_db(user, name):
        sql_statement = "INSERT INTO wallet (user_id,name) VALUES(%s,%s)"
        return Wallet.dbman.insert_entry_and_retrieve_id(
            sql_statement, (user.id, name))
