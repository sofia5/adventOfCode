import os
import sys


def totalTrees(lines, increaseRight, increaseDown):
    totalTrees = 0
    position = 0
    for line in lines:
        if lines.index(line) % increaseDown == 0:
            lastElement = len(line) - 1
            if position > lastElement:
                position = (position % lastElement) - 1
            if line[position] == "#":
                totalTrees += 1
            position += increaseRight
    return totalTrees


def main():

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    print(totalTrees(lines, 1, 1) * totalTrees(lines, 3, 1) *
          totalTrees(lines, 5, 1) * totalTrees(lines, 7, 1) * totalTrees(lines, 1, 2))


if __name__ == "__main__":
    main()
