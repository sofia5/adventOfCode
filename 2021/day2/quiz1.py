import os
import sys


def main():
    horizontalPosition = 0
    depth = 0
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        positions = line.split(' ')
        if(positions[0] == 'forward'):
            horizontalPosition += int(positions[1])
        elif(positions[0] == 'up'):
            depth -= int(positions[1])
        if(positions[0] == 'down'):
            depth += int(positions[1])

    multiplied = horizontalPosition * depth
    print(multiplied)


if __name__ == "__main__":
    main()
