from shortener.db_man import Dbman


class User:
    def __init__(self, user_id, user_name, password) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.password = password

        self.db = Dbman()

    def __repr__(self) -> str:
        return f"{self.user_id} {self.user_name}"

    @staticmethod
    def get_user_id_from_db(user_name: str, user_password: str) -> int:
        """Retrieves UserID of User, specified via Username and Password

        Args:
            user_name (str): Users Username
            user_password (str): Users Password

        Returns:
            int: UserID
        """
        db = Dbman()
        sql = "SELECT UserID FROM user WHERE Username = %s AND Password = %s"
        return db.get_one_entry(sql, (user_name, user_password))

    @classmethod
    def user_login(cls):
        """
        Prompts user to input username and passwort. Loops
        until Login successful and Userobject created.

        Returns:
            User: Logged in Userobject
        """

        print("Loginmask!\n")
        while True:
            username = input("Username >> ")
            password = input("Password >> ")
            user_id = User.get_user_id_from_db(username, password)
            if user_id:
                return User(user_id, username, password)
            else:
                print("Wrong credentials. Try again\n")

    def get_all_saved_urls(self):
        """Retrieves every URL registered"""
        sql = """
            SELECT DomainName, ShortUrl, Username
            FROM url
            INNER JOIN user
            USING (UserID)
            WHERE UserID = %s
        """
        return self.db.get_all_entries(sql, (self.user_id,))
