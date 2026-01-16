#!/usr/bin/env python3

import sys


def display_inventory(inventory: dict, nb_items: int) -> None:
    sorted_dict = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for (item, quantity) in sorted_dict:
        percent = round(quantity / nb_items * 100, 1)
        print(f"{item}: {quantity} units ({percent}%)")
    print()


def display_stats(inventory: dict) -> None:
    maxi = [list(inventory.keys())[0], list(inventory.values())[0]]
    mini = [list(inventory.keys())[0], list(inventory.values())[0]]

    for (item, quantity) in inventory.items():
        if quantity > maxi[1]:
            maxi = [item, quantity]
        if quantity < mini[1]:
            mini = [item, quantity]

    is_s_maxi = "s" if maxi[1] > 1 else ""
    print(f"Most abundant: {maxi[0]} ({maxi[1]} unit{is_s_maxi})")
    is_s_mini = "s" if mini[1] > 1 else ""
    print(f"Least abundant: {mini[0]} ({mini[1]} unit{is_s_mini})")
    print()


def display_categories(inventory: dict, nb_items: int) -> None:
    excellent, good, moderate, scarce = {}, {}, {}, {}
    for (elem, num) in inventory.items():
        per = round(num / nb_items * 100, 2)
        if per > 75:
            excellent[elem] = num
        elif per > 50:
            good[elem] = num
        elif per > 25:
            moderate[elem] = num
        else:
            scarce[elem] = num

    if len(excellent) > 0:
        print("Excellent:", excellent)
    if len(good) > 0:
        print("Good:", good)
    if len(moderate) > 0:
        print("Moderate:", moderate)
    if len(scarce) > 0:
        print("Scarce:", scarce)
    print()


def display_sugestion(invent: dict) -> None:
    print("Restock needed:", [ele for ele, num in invent.items() if num <= 1])
    print()


def display_demo(inventory: dict) -> None:
    print("Dictionary keys:", list(inventory.keys()))
    print("Dictionary values:", list(inventory.values()))
    elem = list(inventory.keys())[0]
    print(f"Sample lookup - '{elem}' in inventory: {elem in inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory = {}
    nb_items = 0
    argc = len(sys.argv)
    try:
        for arg in sys.argv[1:]:
            object, quantity = arg.split(":")
            if object == "":
                raise Exception("Object name should not be empty")
            inventory[object] = int(quantity)
            nb_items += int(quantity)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)

    print("Total items in inventory:", nb_items)
    print("Unique item types:", argc - 1)

    if nb_items != 0:
        print()
        print("=== Current Inventory ===")
        display_inventory(inventory, nb_items)

        print("=== Inventory Statistics ===")
        display_stats(inventory)

        print("=== Item Categories ===")
        display_categories(inventory, nb_items)

        print("=== Management Suggestions ===")
        display_sugestion(inventory)

        print("=== Dictionary Properties Demo ===")
        display_demo(inventory)
