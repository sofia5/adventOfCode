import os
import sys
import math


def getNumber(index, input, position):
    if index == len(input) and position[0] == position[1]:
        return position[0]
    else:
        if input[index] == "B" or input[index] == "R":
            position[0] = math.ceil(
                position[0] + (position[1] - position[0])/2)
        elif input[index] == "F" or input[index] == "L":
            position[1] = math.floor(
                position[1] - (position[1] - position[0])/2)

        return getNumber(index + 1, input, position)


def main():
    maxSeatID = 0
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        seatRow = getNumber(0, line[: 7], [0, 127])
        seatColumn = getNumber(0, line[7:], [0, 7])

        seatID = seatRow * 8 + seatColumn

        if seatID > maxSeatID:
            maxSeatID = seatID

    print(maxSeatID)


if __name__ == "__main__":
    main()
