from management.dbman import Dbman


class User:
    def __init__(self, dbman: Dbman, name: str, id: int) -> None:
        self.dbman = dbman
        self.name = name

    @classmethod
    def register_user_from_form(cls, dbman, user_name):
        sql_statement = "INSERT INTO user (name) VALUES(%s)"
        user_id = dbman.insert_entry_and_retrieve_id(
            sql_statement, (user_name,))
        return User(dbman, user_name, user_id)
