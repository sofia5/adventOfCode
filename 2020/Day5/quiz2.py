import os
import sys
import math


def getSeatNumber(index, input, position):
    if index == len(input) and position[0] == position[1]:
        return position[0]
    else:
        if input[index] == "B" or input[index] == "R":
            position[0] = math.ceil(
                position[0] + (position[1] - position[0])/2)
        elif input[index] == "F" or input[index] == "L":
            position[1] = math.floor(
                position[1] - (position[1] - position[0])/2)

        return getSeatNumber(index + 1, input, position)


def getMissingSeatID(seatIDs):
    for seat in range(0, seatIDs[len(seatIDs) - 1]):
        if seat not in seatIDs:
            if (seat - 1) in seatIDs and (seat + 1) in seatIDs:
                exit(0)
    return seat


def main():
    seatIDs = []
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        seatRow = getSeatNumber(0, line[: 7], [0, 127])
        seatColumn = getSeatNumber(0, line[7:], [0, 7])

        seatIDs.append(seatRow * 8 + seatColumn)

    seatIDs.sort()
    seat = getMissingSeatID(seatIDs)
    print(seat)


if __name__ == "__main__":
    main()
