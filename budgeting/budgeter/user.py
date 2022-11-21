from management.dbman import Dbman


class User:
    dbman = Dbman()

    def __init__(self, id: int, name: str) -> None:
        self.name = name
        self.id = id

    def __repr__(self) -> str:
        return f"{self.name}|{self.id}"

    @staticmethod
    def is_user_in_db(user_name):
        sql_statement = "SELECT * FROM user WHERE name=%s"
        return User.dbman.get_one_entry(sql_statement, (user_name,))

    @classmethod
    def register_user_from_form(cls,  user_name):
        user_id = User.save_user_to_db(user_name)
        return User(user_id, user_name)

    @staticmethod
    def save_user_to_db(user_name):
        sql_statement = "INSERT INTO user (name) VALUES(%s)"
        return User.dbman.insert_entry_and_retrieve_id(
            sql_statement, (user_name,))
