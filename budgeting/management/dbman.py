import mysql.connector
import management.config as cfg


class Dbman:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(**cfg.DB_CRED)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def __repr__(self) -> str:
        return f'{cfg.DB_CRED.get("user")}>{cfg.DB_CRED.get("database")}@{cfg.DB_CRED.get("host")}'

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
        return self.cursor.fetchone()

    def save_to_db(self, sql: str, data: tuple) -> None:
        """Save/Update Entry in DB

        Args:
            sql (str): SQL Query
            data (tuple): Placeholdervalues
        """
        self.cursor.execute(sql, data)
        self.db.commit()

    def insert_entry_and_retrieve_id(self, sql_statement: str, sql_data: tuple):
        """Save Entry in DB

        Args:
            sql_statement (str): SQL Query
            sql_data (tuple): Placeholdervalues

        Returns:
            _type_: Primarykey of inserted Entry
        """
        self.cursor.execute(sql_statement, sql_data)
        self.db.commit()
        return self.cursor.lastrowid
