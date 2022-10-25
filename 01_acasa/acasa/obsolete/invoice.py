"""Invoice File"""

from menu import loadData
import pprint
from collections import Counter


def listItems(
    order: list[tuple[int, int]],
    menu_dict: dict,
) -> tuple[float, list]:
    total_cost = 0.0
    listing = []
    for s_order in order:
        total_cost += menu_dict[str(s_order[0])]["Price"] * s_order[1]
        listing.append(
            (
                s_order[0],
                menu_dict[str(s_order[0])]["Item"],
                menu_dict[str(s_order[0])]["Price"],
                s_order[1],
            )
        )
    return total_cost, listing


def getOrder():
    counter = Counter()
    order_list = []
    order = []
    while 1:
        user_in = int(input("0 to quit | choice >> "))
        if not user_in:
            break
        counter[user_in] += 1
        order_list.append(user_in)
    for order_id, order_name in counter.items():
        order.append((order_id, order_name))
    return order


def printOrder(total_cost: float, listing: list):
    for entry in listing:
        pprint.pprint("{}. {} -> {:.2f}€ x {}".format(*entry))
        # print("{}. {} -> {:.2f}€ x {}".format(*entry))
    print(40 * "_")
    print(f"Total: {total_cost}€")



def main():
    menu_dict = loadData("acasa.json")
    order = [("10", 2), ("11", 1)]
    print(listItems(order, menu_dict))


if __name__ == "__main__":
    main()
