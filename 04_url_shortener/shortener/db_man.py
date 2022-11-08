import mysql.connector
from random import randint
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
        try:
            entry = self.cursor.fetchone()[0]
        except TypeError:
            return 0
        else:
            return entry

    def save_to_db(self, sql: str, data: tuple) -> None:
        self.cursor.execute(sql, data)
        self.db.commit()

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
