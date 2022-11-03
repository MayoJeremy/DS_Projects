import os
import sqlite3
from pathlib import Path
from json_import import JsonImporter

os.chdir(Path(__file__).parent.parent.parent)


class SQLExporter:
    def __init__(self, db_name: str, to_export: dict) -> None:
        self.conn = sqlite3.connect("./data/" + db_name)
        self.cursor = self.conn.cursor()
        self.to_export = to_export

    def insert_dish(self):
        sql = "INSERT INTO Menu (DishID, Title, Category, Price) VALUES (?,?,?,?);"
        data = []
        for category, dishes in self.to_export.items():
            for dish in dishes:
                data.append(
                    (
                        dish["id"],
                        dish["title"],
                        category,
                        dish["price"],
                    )
                )
        print(data)
        self.cursor.executemany(sql, data)
        self.conn.commit()


def main():
    dbImport = JsonImporter("./data/menu.json")
    dbImport.get_content()
    sExport = SQLExporter("acasa.db", dbImport.menu)
    sExport.insert_dish()


if __name__ == "__main__":
    main()
