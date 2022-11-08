import mysql.connector
from random import randint
#from shortener.url import Url
import config as cfg


class Dbman:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host=cfg.DB_HOST,
            user=cfg.DB_USER,
            password=cfg.DB_PASSWORD,
            port=cfg.DB_PORT,
            database=cfg.DB_NAME,
        )
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def get_all_entries(self, sql: str, data: tuple = None) -> list:
        self.cursor.execute(sql, data)
        return self.cursor.fetchall()

    def get_one_entry(self, sql: str, data: tuple = None) -> tuple:
        self.cursor.execute(sql, data)
        return self.cursor.fetchone()[0]

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

    def save_url_to_db_and_get_url_id(self, user_urL):
        sql = """
        INSERT INTO url (DomainName, OriginalUrL, ShortUrL, UserID)
        VALUES (%s,%s,%s,%s)
        """

        self.cursor.execute(
            sql,
            [
                user_urL.domain_name,
                user_urL.original_url,
                user_urL.short_url,
                user_urL.user,
            ],
        )
        self.db.commit()
        return self.cursor.lastrowid

    def get_new_random_short_url(self) -> str:
        """Generates new url and checks if its unique in DB

        Returns:
            str: Newly generated Url
        """
        sql = "SELECT * FROM url WHERE ShortUrL = %s"
        while True:
            new_short_url = "".join(str(randint(0, 9)) for _ in range(5))
            self.cursor.execute(sql, (new_short_url,))
            try:
                self.cursor.fetchone()[0]
            except TypeError:
                return new_short_url


