import os
import sys


def main():
    timesIncreased = 0
    index = 0

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    while index + 3 < len(lines):
        currentWindow = int(lines[index]) + \
            int(lines[index + 1]) + int(lines[index + 2])
        nextWindow = int(lines[index + 1]) + \
            int(lines[index + 2]) + int(lines[index + 3])

        if nextWindow > currentWindow:
            timesIncreased += 1

        index += 1
        print(timesIncreased)


if __name__ == "__main__":
    main()
