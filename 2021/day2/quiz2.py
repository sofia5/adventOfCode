import os
import sys


def main():
    horizontalPosition = 0
    depth = 0
    aim = 0
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        positions = line.split(' ')
        if(positions[0] == 'forward'):
            horizontalPosition += int(positions[1])
            depth += abs(int(positions[1]) * aim)
        elif(positions[0] == 'up'):
            aim -= int(positions[1])
        if(positions[0] == 'down'):
            aim += int(positions[1])

    multiplied = horizontalPosition * depth
    print(multiplied)


if __name__ == "__main__":
    main()
