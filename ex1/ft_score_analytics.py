#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    argc = len(sys.argv)
    state = True
    for elem in sys.argv[1:]:
        try:
            int(elem)
        except ValueError as e:
            state = False
            print("Error", e)

    if argc == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    elif state:
        scores = [int(elem) for elem in sys.argv[1:]]
        print("Scores processed:", scores)
        print("Total players:", argc - 1)
        print("Total score:", sum(scores))
        print("Average score:", sum(scores) / (argc - 1))
        print("High score:", max(scores))
        print("Low score:", min(scores))
        print("Score range:", max(scores) - min(scores))
        print()
