import os
import sys


def main():
    prevLine = None
    timesIncreased = 0
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        if prevLine != None:
            if int(line) > int(prevLine):
                timesIncreased += 1
        prevLine = line
        print(timesIncreased)


if __name__ == "__main__":
    main()
