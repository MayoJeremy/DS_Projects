import os
import sqlite3
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
conn = sqlite3.connect("./data/europcar.db")
cursor = conn.cursor()
GREETING_MSG = "Welcome to Europcar!"


def get_catalog_string(brand: str) -> str:
    car_catalog = [brand + ": "]
    sql = "SELECT CarID, Model.Title, Color.Title \
FROM Car \
LEFT JOIN Model USING(ModelID) \
LEFT JOIN Color USING(ColorID) \
LEFT JOIN Brand USING(BrandID) \
WHERE StatusID = 1 AND Brand.Title = ?\
;"
    cursor.execute(sql, [brand])
    for entry in cursor.fetchall():
        car_catalog.append("{}. | {} | {}".format(*entry))
    return "\n".join(car_catalog)


def main():
    print(GREETING_MSG)
    car_catalog = get_catalog_string("bmw")
    print(car_catalog)


if __name__ == "__main__":
    main()

conn.close()
