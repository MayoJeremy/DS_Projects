"""Invoice File"""

from menu import loadData


def calcTotal(order: list, menu_dict: dict):
    total_cost = 0.0
    for sorder in order:
        total_cost += menu_dict[str(sorder)]["Price"]
    return total_cost


def main():
    menu_dict = loadData("acasa.json")
    order = [10, 11, 10]
    print(calcTotal(order, menu_dict))


if __name__ == "__main__":
    main()
