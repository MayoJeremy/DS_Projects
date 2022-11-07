import mysql.connector


class Dbman:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="12345",
            port="3306",
            database="urlshortener",
        )
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def get_user_id_from_db(self, user_name: str, user_password: str) -> int:
        """Query DB for existing User via Username and Password

        Args:
            user_name (string): Username
            user_password (string): Password

        Returns:
            int: UserID
        """
        sql = "SELECT UserID FROM user WHERE Username = %s AND Password = %s"
        self.cursor.execute(sql, (user_name, user_password))
        try:
            user_id = self.cursor.fetchone()[0]
        except TypeError:
            return 0
        else:
            return user_id

    def get_user_saved_urls(self, user_id: int) -> list[tuple[str, str]]:
        sql = """
        SELECT OriginalUrL, ShortUrL
        FROM url
        WHERE UserID = %s
        """

        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchall()

    def save_url_to_db(self, user_urL):
        sql = """
        INSERT INTO url (DomainName, OriginalUrL, ShortUrL, UserID)
        VALUES (%s,%s,%s,%s)
        """

        self.cursor.execute(sql, (user_urL))
        self.db.commit()
