import os
import sys


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [int(line.rstrip()) for line in f]

    lines.sort()

    for line in lines:
        lastEntry = len(lines) - 1
        while (line + lines[lastEntry]) >= 2020:
            if(line + lines[lastEntry] == 2020):
                print(line * lines[lastEntry])
                exit(0)

            lastEntry -= 1


if __name__ == "__main__":
    main()
