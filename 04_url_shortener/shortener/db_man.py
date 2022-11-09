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
        """Retrieves every entry from DB

        Args:
            sql (str): SQL Query to filter results
            data (tuple, optional): Placeholdervalues. Defaults to None.

        Returns:
            list: _description_
        """
        self.cursor.execute(sql, data)
        return self.cursor.fetchall()

    def get_one_entry(self, sql: str, data: tuple = None) -> tuple | int:
        """Retrieves single entry from DB

        Args:
            sql (str): SQL Query to filter result
            data (tuple, optional): Placeholdervalues. Defaults to None.

        Returns:
            tuple | int: Found result or 0
        """
        self.cursor.execute(sql, data)
        try:
            entry = self.cursor.fetchone()[0]
        except TypeError:
            return 0
        else:
            return entry

    def save_to_db(self, sql: str, data: tuple) -> None:
        """Save/Update Entry in DB

        Args:
            sql (str): SQL Query
            data (tuple): Placeholdervalues
        """
        self.cursor.execute(sql, data)
        self.db.commit()

