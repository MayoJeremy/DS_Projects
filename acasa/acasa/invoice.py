"""Invoice File"""

from menu import loadData
import pprint


def calcTotal(order: list[tuple[str, int]], menu_dict: dict):
    total_cost = 0.0
    for sorder in order:
        total_cost += menu_dict[str(sorder[0])]["Price"] * sorder[1]
    return total_cost


def listItems(
    order: list[tuple[str, int]],
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


def printOrder(total_cost: float, listing: list):
    for entry in listing:
        pprint.pprint("{}. {} -> {:.2f}€ x {}".format(*entry))
        print("{}. {} -> {:.2f}€ x {}".format(*entry))
    print(40 * "_")
    print(f"Total: {total_cost}€")


def main():
    menu_dict = loadData("acasa.json")
    order = [("10", 2), ("11", 1)]
    print(calcTotal(order, menu_dict))


if __name__ == "__main__":
    main()
