import os
import sqlite3
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
conn = sqlite3.connect("./data/europcar.db")
cursor = conn.cursor()
GREETING_MSG = "Welcome to Europcar!"


def get_catalog_string(brand: str, availability: int = 1) -> str:
    car_catalog = [brand.capitalize() + ": "]
    sql = "SELECT CarID, Model.Title, Color.Title \
FROM Car \
LEFT JOIN Model USING(ModelID) \
LEFT JOIN Color USING(ColorID) \
LEFT JOIN Brand USING(BrandID) \
WHERE StatusID = ? AND Brand.Title = ?\
;"
    cursor.execute(sql, [availability, brand])
    for entry in cursor.fetchall():
        car_catalog.append("{}. | {} | {}".format(*entry))
    return "\n".join(car_catalog)


def get_brands():
    brand_names = []
    sql = "SELECT title FROM Brand"
    cursor.execute(sql)
    for brand in cursor.fetchall():
        brand_names.append(brand[0])
    return brand_names


def get_user_order():
    user_model = input("Which Car do you want to order (Number): ")
    user_days = input("For how long: ")
    return int(user_model), int(user_days)


def main():
    print(GREETING_MSG)

    for _ in get_brands():
        print("\n", get_catalog_string(_))

    user_input = get_user_order()


if __name__ == "__main__":
    main()

conn.close()
