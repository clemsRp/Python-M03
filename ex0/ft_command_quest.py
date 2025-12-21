#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("== Command Quest ===")

    argc = len(sys.argv)
    if argc == 1:
        print("No arguments provided!")

    print("Program name:", sys.argv[0])
    if argc > 1:
        print("Arguments received:", argc - 1)
        for k in range(1, argc):
            print(f"Argument {k}:", sys.argv[k])

    print("Total arguments:", argc)
