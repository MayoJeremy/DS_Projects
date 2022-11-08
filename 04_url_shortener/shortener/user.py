from shortener.db_man import Dbman


class User:
    def __init__(self, user_id, user_name, password) -> None:
        self.user_id = user_id
        self.user_name = user_name
        self.password = password

        self.db = Dbman()

    def __repr__(self) -> str:
        return f"{self.user_id}, {self.user_name}"

    def get_all_saved_urls(self):
        sql = """
            SELECT DomainName, ShortUrl, Username
            FROM url
            INNER JOIN user
            USING (UserID)
            WHERE UserID = %s
        """
        return self.db.get_all_entries(sql, (self.user_id,))
