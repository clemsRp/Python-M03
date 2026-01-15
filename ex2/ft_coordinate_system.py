#!/usr/bin/env python3

import sys
import math


def get_distance(pos: tuple) -> float:
    '''
    Return the distance between 2 points
    '''
    sum = pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2
    return (math.sqrt(sum))


def parsing_pos(param: str) -> None:
    '''
    Handle the case where all points are in the same string
    '''
    state = True
    res = []
    if "," not in param:
        print("Invalid arguments")
        return
    res = param.split(',')

    if len(res) != 3:
        state = False
    for s in res:
        try:
            int(s)
        except ValueError:
            state = False

    if state:
        print(f'Parsing coordinates: "{param}"')
    else:
        print(f'Parsing invalids coordinates: "{param}"')

    try:
        pos = tuple(int(elem) for elem in res)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return

    print("Parsed position:", pos)
    print(f"Distance between (0, 0, 0) and {pos}: {get_distance(pos)}")


def direct_pos(params: list) -> None:
    '''
    Handle the case where the points are not in the same string
    '''
    try:
        pos = tuple(int(elem) for elem in params)
    except ValueError as e:
        print("Error parsing coordinates:", e)
        return

    print("Parsed position:", pos)
    print(f"Distance between (0, 0, 0) and {pos}: {get_distance(pos)}")


def unpacking(pos: tuple) -> None:
    '''
    Show how unpacking tuples
    '''
    print(f"Player at x={pos[0]}, y={pos[1]}, z={pos[2]}")
    x, y, z = pos
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    argc = len(sys.argv)
    if argc == 1:
        print("Missing coordinates.")
    elif argc == 2:
        parsing_pos(sys.argv[1])
    elif argc == 4:
        direct_pos(sys.argv[1:])
    else:
        print("Invalid number of params.")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    main()
