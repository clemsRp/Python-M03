#!/usr/bin/env python3


def list_comprehensions(players: list) -> None:
    '''
    Test the list creation by comprehensions
    '''
    scores = [player["name"] for player in players if player["score"] > 2000]
    print("High scorers (>2000):", scores)

    doubled = [2 * player["score"] for player in players]
    print("Scores doubled:", doubled)

    active = [player["name"] for player in players if len(player["achiv"]) > 4]
    print("Active players:", active)


def dict_comprehensions(players: list) -> None:
    '''
    Test the dict creation by comprehensions
    '''
    scores = {player["name"]: player["score"] for player in players}
    print("Player scores:", scores)

    categories_type = ["low", "medium", "high"]
    categories = {categories_type[k]: k + 1 for k in range(2, -1, -1)}
    print("Score categories:", categories)

    achivs = {player["name"]: len(player["achiv"]) for player in players}
    print("Achievement counts:", achivs)


def get_occurs(region: str, players: list) -> int:
    '''
    Return the number of times a region appears in the players data
    '''
    occurs = 0
    for player in players:
        if region in player["regions"]:
            occurs += 1

    return occurs


def get_regions(players: list) -> dict:
    '''
    Return the most present regions in players data
    '''
    visited = []
    regions = []
    max_occur = 0
    for player in players:
        for region in player["regions"]:
            if region not in visited:
                visited.append(region)
                occur = get_occurs(region, players)
                if occur > max_occur:
                    max_occur = occur
                    regions = [region]
                elif occur == max_occur:
                    regions.append(region)

    return {region for region in regions}


def set_comprehensions(players: list) -> None:
    '''
    Test the set creation by comprehensions
    '''
    unique_players = {player["name"] for player in players}
    print("Unique players:", unique_players)

    unique_achivs = {player["name"] for player in players}
    print("Unique achievements:", unique_achivs)

    active_regions = get_regions(players)
    print("Active regions:", active_regions)


def get_score(player: dict) -> int:
    '''
    Return a player's score
    '''
    return player["score"]


def combined_analysis(players: list) -> None:
    '''
    Test all the comprehension creations
    '''
    total_players = len([player["name"] for player in players])
    print("Total players:", total_players)

    total_achivs = len({
        achiv
        for player in players
        for achiv in player["achiv"]
    })
    print("Total unique achievements:", total_achivs)

    total_score = sum([player["score"] for player in players])
    average_score = total_score / total_players
    print("Average score:", average_score)

    sorted_players = sorted(players, key=get_score, reverse=True)
    print(f"Total players: {sorted_players[0]["name"]}"
          f" ({sorted_players[0]["score"]} points,"
          f" {len(sorted_players[0]["achiv"])} achievements)")


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")

    players = [
        {
            "name": "Alice",
            "score": 2300,
            "achiv": {
                "first_kill",
                "level_10",
                "treasure_hunter",
                "speed_demon",
                "boss_slayer"
            },
            "regions": {
                "north",
                "west",
                "east"
            }
        },
        {
            "name": "Bob",
            "score": 1800,
            "achiv": {
                "first_kill",
                "speed_demon"
            },
            "regions": {
                "north",
                "central",
                "east"
            }
        },
        {
            "name": "Charlie",
            "score": 2150,
            "achiv": {
                "first_kill",
                "level_10",
                "boss_slayer",
                "treasure_hunter",
                "speed_demon",
                "master_explorer",
                "dragon_slayer"
            },
            "regions": {
                "north",
                "central"
            }
        },
        {
            "name": "Diana",
            "score": 2000,
            "achiv": {
                "first_kill",
                "treasure_hunter"
            },
            "regions": {
                "central",
                "east",
                "south"
            }
        }
    ]

    print("\n=== List Comprehension Examples ===")
    list_comprehensions(players)

    print("\n=== Dict Comprehension Examples ===")
    dict_comprehensions(players)

    print("\n=== Set Comprehension Examples ===")
    set_comprehensions(players)

    print("\n=== Combined Analysis ===")
    combined_analysis(players)
