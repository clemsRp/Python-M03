#!/usr/bin/env python3

def common(game: dict, players: list) -> set:
    res = game[players[0]]
    for player in players[1:]:
        res = res.intersection(game[player])
    return res


def all_unique(game: dict) -> set:
    res = set()
    for player in game:
        res = res.union(game[player])
    return res


def rare_unique(game: dict) -> set:
    res = all_unique(game)
    for player1 in game:
        for player2 in game:
            if player1 != player2:
                res = res.difference(game[player1].intersection(game[player2]))
    return res


def display_statistics(game: dict) -> None:
    '''
    Show the analytics of the achievement functions
    '''
    print("=== Achievement Analytics ===")

    all_uniques = all_unique(game)
    print("All unique achievements:", all_uniques)
    print("Total unique achievements:", len(all_uniques))
    print()

    all_common = common(game, [key for key in game.keys()])
    print("Common to all players:", all_common)

    rare = rare_unique(game)
    print("Rare achievements (1 player):", rare)
    print()


def comparaison(game: dict, player1: str, player2: str) -> None:
    '''
    Compare 2 different player achievements
    '''
    print(f"{player1} vs {player2} common:", common(game, [player1, player2]))

    print(f"{player1} unique:", game[player1].difference(game[player2]))
    print(f"{player2} unique:", game[player2].difference(game[player1]))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    game = {}
    game["Alice"] = {'first_kill', 'level_10',
                     'treasure_hunter', 'speed_demon'}
    game["Bob"] = {'first_kill', 'level_10',
                   'boss_slayer', 'collector'}
    game["Charlie"] = {'level_10', 'treasure_hunter',
                       'boss_slayer', 'speed_demon', 'perfectionist'}

    for player in game:
        print(f"Player {player} achievements: {game[player]}")
    print()

    display_statistics(game)
    comparaison(game, "Alice", "Bob")
