import os
import sys


def degreesToCardinal(degrees):
    direction = ""
    if degrees == 0:
        direction = "N"
    elif degrees == 90:
        direction = "E"
    elif degrees == 180:
        direction = "S"
    elif degrees == 270:
        direction = "W"
    return direction


def cardinalToDegrees(curDir):
    degrees = 0
    if curDir == "N":
        degrees = 0
    elif curDir == "E":
        degrees = 90
    elif curDir == "S":
        degrees = 180
    elif curDir == "W":
        degrees = 270
    return degrees


def rotate(action, degreesToRotate, curDir):
    degrees = cardinalToDegrees(curDir)

    if action == "L":
        direction = degrees - degreesToRotate
        while direction < 0:
            direction = direction + 360
    elif action == "R":
        direction = degrees + degreesToRotate
        while direction >= 360:
            direction = direction - 360

    newDir = degreesToCardinal(direction)
    return newDir


def move(action, value, curLoc):
    oppositeAction = curLoc[action][1]
    if curLoc[action][0] >= 0 and curLoc[oppositeAction][0] == 0:
        curLoc[action][0] += value
    else:
        diff = curLoc[oppositeAction][0] - value
        if diff >= 0:
            curLoc[oppositeAction][0] = diff
        else:
            curLoc[oppositeAction][0] = 0
            curLoc[action][0] = abs(diff)

    return curLoc


def shipMovement(action, value, curDir, curLoc):
    if action == "N" or action == "S" or action == "E" or action == "W":
        curLocAndDir = [move(action, value, curLoc), curDir]

    elif action == "L" or action == "R":
        curLocAndDir = [curLoc, rotate(action, value, curDir)]

    elif action == "F":
        curLocAndDir = [move(curDir, value, curLoc), curDir]

    return curLocAndDir


def main():
    curDirection = "E"
    curLocation = {"N": [0, "S"], "S": [0, "N"], "E": [0, "W"], "W": [0, "E"]}

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        action = line[:1]
        value = int(line[1:])
        curLocAndDir = shipMovement(action, value, curDirection, curLocation)
        curLocation = curLocAndDir[0]
        curDirection = curLocAndDir[1]

    northSouth = curLocation["N"][0] + curLocation["S"][0]
    eastWest = curLocation["E"][0] + curLocation["W"][0]

    print(northSouth + eastWest)


if __name__ == "__main__":
    main()
