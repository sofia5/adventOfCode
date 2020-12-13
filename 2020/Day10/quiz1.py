import os
import sys


def main():
    curPos = 0
    oneJoltDiffs = 0
    threeJoltDiffs = 0

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [int(line.rstrip()) for line in f]

    lines.sort()

    for line in lines:

        if curPos == line - 1:
            oneJoltDiffs += 1

        elif curPos == line - 3:
            threeJoltDiffs += 1

        curPos = line

    # Add 3 extra jolts
    threeJoltDiffs += 1

    print("1-jolt & 3-jolt differences multiplied is: " +
          str(oneJoltDiffs * threeJoltDiffs))


if __name__ == "__main__":
    main()
