import os
import sqlite3
from pathlib import Path

os.chdir(Path(__file__).parent.parent)
conn = sqlite3.connect("./data/europcar.db")
cursor = conn.cursor()
GREETING_MSG = "Welcome to Europcar!"
RESET_AVAIL = False


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
    sql = "SELECT title FROM Brand;"
    cursor.execute(sql)
    for brand in cursor.fetchall():
        brand_names.append(brand[0])
    return brand_names


def get_user_order():
    while True:
        user_car = int(input("Which Car do you want to order (Number): "))

        if is_available(user_car):
            break
    user_days = int(input("For how long: "))
    return user_car, user_days


def is_available(car_id: int):
    sql = "SELECT COUNT(*) FROM Car WHERE CarID = ? AND StatusID = 1;"
    cursor.execute(sql, [car_id])
    return cursor.fetchone()[0]


def calc_total(user_car: int, user_days: int):
    sql = "SELECT DayPrice FROM Car WHERE CarID = ?;"
    cursor.execute(sql, [user_car])
    day_price = cursor.fetchone()
    return user_days * day_price[0]


def updating_availability(change_to: int, user_car: int):
    sql = "UPDATE Car SET StatusID = ? WHERE CarID LIKE ?;"
    with conn:
        cursor.execute(sql, [change_to, user_car])


def main():
    if RESET_AVAIL:
        updating_availability(1, "%")
    print(GREETING_MSG)

    for _ in get_brands():
        print("\n", get_catalog_string(_))

    user_input = get_user_order()
    print("Your Total is: {}€".format(calc_total(*user_input)))
    if user_input[1]:
        updating_availability(2, user_input[0])


if __name__ == "__main__":
    main()

conn.close()
