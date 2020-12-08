import os
import sys


def main():

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    print()


if __name__ == "__main__":
    main()
