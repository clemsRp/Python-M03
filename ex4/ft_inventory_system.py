#!/usr/bin/env python3


def init_dico():
    players = dict()
    players["Alice"] = [
        {
            "name": "sword",
            "type": "weapon",
            "rarety": "rare",
            "num": 1,
            "price": 500
        },
        {
            "name": "potion",
            "type": "consumable",
            "rarety": "common",
            "num": 5,
            "price": 50
        },
        {
            "name": "shield",
            "type": "armor",
            "rarety": "uncommon",
            "num": 1,
            "price": 200
        }
    ]
    players["Bob"] = [
        {
            "name": "magic_ring",
            "type": "armor",
            "rarety": "rare",
            "num": 1,
            "price": 250
        }
    ]

    return players


def display_inventory(players: dict, name: str):
    print(f"=== {name}'s Inventory ===")

    for obj in players[name]:
        print(f"{obj["name"]} ({obj["type"]}, {obj["rarety"]}): {obj["num"]}x "
              f"@ {obj["price"]} gold each = {obj["num"] * obj["price"]} gold")
    print()


def display_summary(players: dict, name: str):
    total = 0
    types = [0, 0, 0]
    for obj in players[name]:
        total += obj["num"] * obj["price"]
        if obj["type"] == "weapon":
            types[0] += obj["num"]
        if obj["type"] == "consumable":
            types[1] += obj["num"]
        if obj["type"] == "armor":
            types[2] += obj["num"]
    items = types[0] + types[1] + types[2]
    print(f"Inventory value: {total} gold")
    print(f"Item count: {items} items")
    print(f"Categories: weapon({types[0]}), consumable({types[1]}), "
          f"armor({types[2]})")
    print()


def set_item(players: dict, src: str, dest: str, name: str, num: int):
    if src not in players or dest not in players or num <= 0:
        return None

    for item in players[src]:
        if item["name"] == name and item["num"] >= num:
            item["num"] -= num
            return item

    return None


def transfere(players: dict, src: str, dest: str, name: str, num: int):
    print(f"=== Transaction: {src} gives {dest} {num} "
          f"{name}{"s" if num > 1 else ""} ===")
    item = set_item(players, src, dest, name, num)

    if item is None:
        print("Transaction unsuccessful!")
    else:
        src_num = item["num"]
        dest_num = 0
        state = True

        for item2 in players[dest]:
            if item2["name"] == name:
                state = False
                item2["num"] += num
                dest_num = item2["num"]

        if state:
            new_item = {
                "name": item["name"],
                "type": item["type"],
                "rarety": item["rarety"],
                "num": num,
                "price": item["price"]
            }
            new_item["num"] = num
            dest_num = num
            players[dest].append(new_item)

        print("Transaction successful!\n\n=== Updated Inventories ===")
        print(f"{src} {name}s:", src_num)
        print(f"{dest} {name}s:", dest_num)


def get_value(invent: list):
    value = 0
    for item in invent:
        value += item["num"] * item["price"]

    return value


def get_most_valuable(players: dict):
    res = [None, 0]
    for (player, invent) in players.items():
        if get_value(invent) > res[1]:
            res = [player, get_value(invent)]

    return res


def get_num_items(invent: list):
    num = 0
    for item in invent:
        num += item["num"]

    return num


def get_most_items(players: dict):
    res = [None, 0]
    for (player, invent) in players.items():
        if get_num_items(invent) > res[1]:
            res = [player, get_num_items(invent)]

    return res


def get_rarest_items(players: dict):
    rarety = {
        "uncommon": 0,
        "common": 1,
        "rare": 2
    }
    max_rarety = 0
    items = []

    for invent in players.values():
        for item in invent:
            if len(items) == 0 or rarety[item["rarety"]] > max_rarety:
                items = [item["name"]]
                max_rarety = rarety[item["rarety"]]
            elif rarety[item["rarety"]] == max_rarety:
                items.append(item["name"])

    return items


def inventory_analytics():
    print("\n=== Inventory Analytics ===")
    valuable = get_most_valuable(players)
    items = get_most_items(players)
    rarest_items = get_rarest_items(players)

    print(f"Most valuable player: {valuable[0]} ({valuable[1]} gold)")
    print(f"Most items: {items[0]} ({items[1]} items)")
    print("Rarest items:", end="")

    for item in rarest_items[:-1]:
        print(f" {item},", end="")
    print(" " + rarest_items[-1])


if __name__ == "__main__":
    print("=== Player Inventory System ===\n")

    players = init_dico()
    display_inventory(players, "Alice")
    display_summary(players, "Alice")
    transfere(players, "Alice", "Bob", "potion", 2)
    inventory_analytics()
