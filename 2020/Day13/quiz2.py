import os
import sys
import math


def getBusPos(buses):
    busPositions = {}
    for index, bus in enumerate(buses):
        if bus != 'x':
            busPositions[index] = int(bus)
    return busPositions


def timeT(busPos):
    print((maxValue + busPos[maxValue]))
    print()
    inc = math.lcm((maxValue + busPos[maxValue]),
                   (minValue + busPos[minValue]))
    print(inc)
    return inc


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    buses = lines[1].split(",")

    busPositions = getBusPos(buses)
    minValue = getMin(busPositions)
    maxValue = getMax(busPositions)

    inc = timeT(busPositions)
    #timeT = timeT(busPositions, increase, minValue, maxValue)

    print(timeT)


if __name__ == "__main__":
    main()
