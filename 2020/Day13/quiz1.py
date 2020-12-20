import os
import sys


def findEarliestBus(waitTimes):
    return min(waitTimes, key=waitTimes.get)


def getWaitTimes(readyTime, buses):
    waitTimes = {}
    for bus in buses:
        waitTime = bus - (readyTime % bus)
        waitTimes[bus] = waitTime
    return waitTimes


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    readyTime = int(lines[0])
    buses = []
    line = lines[1].split(",")

    for word in line:
        if word != 'x':
            buses.append(int(word))

    waitTimes = getWaitTimes(readyTime, buses)
    earliestBus = findEarliestBus(waitTimes)

    print(earliestBus * waitTimes[earliestBus])


if __name__ == "__main__":
    main()
