import os
import sys


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [int(line.rstrip()) for line in f]

    lines.sort()

    for line1 in lines:
        indexLine1 = lines.index(line1)
        for line2 in lines[indexLine1 + 1:]:
            if(line1 + line2) <= 2020:
                indexLine2 = lines.index(line2)
                for line3 in lines[indexLine2 + 1:]:
                    if(line1 + line2 + line3) == 2020:
                        print(line1 * line2 * line3)


if __name__ == "__main__":
    main()
