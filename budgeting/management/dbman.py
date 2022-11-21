import mysql.connector
import management.config as cfg


class Dbman:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(**cfg.DB_CRED)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
