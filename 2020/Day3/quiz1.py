import os
import sys


def main():
    totalTrees = 0

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    position = 0
    for line in lines:
        lastElement = len(line) - 1
        if position > lastElement:
            position = (position % lastElement) - 1
        if line[position] == "#":
            totalTrees += 1
        position += 3

    print(totalTrees)


if __name__ == "__main__":
    main()
