#!/usr/bin/env python3


def init_dico() -> dict:
    '''
    Return the dict with all the players informations,
    and their inventory
    '''
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


def display_inventory(players: dict, name: str) -> None:
    '''
    Show the inventory of a player
    '''
    print(f"=== {name}'s Inventory ===")

    for obj in players[name]:
        obj_name = obj["name"]
        obj_type = obj["type"]
        obj_rarety = obj["rarety"]
        obj_num = obj["num"]
        obj_price = obj["price"]
        print(f"{obj_name} ({obj_type}, {obj_rarety}): {obj_num}x "
              f"@ {obj_price} gold each = {obj_num * obj_price} gold")
    print()


def display_summary(players: dict, name: str) -> None:
    '''
    Show some informations about about an inventory
    '''
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


def set_item(players: dict, src: str, dest: str, name: str, num: int) -> dict:
    '''
    Return the item setted if he exist,
    else return nothing
    '''
    if src not in players or dest not in players or num <= 0:
        return

    for item in players[src]:
        if item["name"] == name and item["num"] >= num:
            item["num"] -= num
            return item

    return


def transfere(players: dict, src: str, dest: str, name: str, num: int) -> None:
    '''
    Simulate the transfere of items from a player to another
    '''
    print(f"=== Transaction: {src} gives {dest} {num} " +
          name + "s" if num > 1 else "" + " ===")
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


def get_value(invent: list) -> int:
    '''
    Return the total value of an inventory
    '''
    value = 0
    for item in invent:
        value += item["num"] * item["price"]

    return value


def get_most_valuable(players: dict) -> list:
    '''
    Return the player with the most valuable inventory and it value
    '''
    res = [None, 0]
    for (player, invent) in players.items():
        if get_value(invent) > res[1]:
            res = [player, get_value(invent)]

    return res


def get_num_items(invent: list) -> int:
    '''
    Return the number of items in an inventory
    '''
    num = 0
    for item in invent:
        num += item["num"]

    return num


def get_most_items(players: dict) -> list:
    '''
    Return the name of the player with the most items
    and the number of items he has
    '''
    res = [None, 0]
    for (player, invent) in players.items():
        if get_num_items(invent) > res[1]:
            res = [player, get_num_items(invent)]

    return res


def get_rarest_items(players: dict) -> list:
    '''
    Return the list of the rarest items
    '''
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


def inventory_analytics() -> None:
    '''
    Show the analytics of the inventory functions
    '''
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
