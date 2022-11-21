from management.dbman import Dbman


class Wallet:
    dbman = Dbman()

    def __init__(self, id: int, user_id: int, name: str) -> None:
        self.id = id
        self.user_id = user_id
        self.name = name
