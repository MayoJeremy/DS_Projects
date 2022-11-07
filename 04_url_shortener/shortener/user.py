class User:
    def __init__(self, user_id, user_name, password) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.password = password

    def __repr__(self) -> str:
        return f"{self.user_id}, {self.user_name}"
