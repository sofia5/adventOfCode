import os
import sys

# correctAns: 26841


def degreesToCardinal(degrees):
    direction = ""
    if degrees == 0:
        direction = "NE"
    elif degrees == 90:
        direction = "SE"
    elif degrees == 180:
        direction = "SW"
    elif degrees == 270:
        direction = "NW"
    return direction


def cardinalToDegrees(curDir):
    degrees = 0
    if curDir == "NE":
        degrees = 0
    elif curDir == "SE":
        degrees = 90
    elif curDir == "SW":
        degrees = 180
    elif curDir == "NW":
        degrees = 270
    return degrees


def rotate(action, degreesToRotate, wpLoc):
    curDir = ""
    values = []
    for key, value in wpLoc.items():
        if value[2]:
            curDir += key
            values.append(value[0])
            wpLoc[key][0] = 0
            wpLoc[key][2] = False

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
    if newDir == 'SE':
        newDir = 'ES'
    elif newDir == 'NW':
        newDir = 'WN'

    for i, key in enumerate(newDir):
        wpLoc[key][0] = values[i]
        wpLoc[key][2] = True

    return wpLoc


def moveWaypoint(action, value, wpLoc):
    oppositeAction = wpLoc[action][1]
    if wpLoc[action][0] >= 0 and wpLoc[oppositeAction][0] == 0:
        wpLoc[action][0] += value
    else:
        diff = wpLoc[oppositeAction][0] - value
        if diff >= 0:
            wpLoc[oppositeAction][0] = diff
        else:
            wpLoc[oppositeAction][0] = 0
            wpLoc[oppositeAction][2] = False
            wpLoc[action][0] = abs(diff)
            wpLoc[oppositeAction][2] = True
    return wpLoc


def moveShip(inc, wpLoc, shipLoc):
    for key, value in wpLoc.items():
        # print(value)
        if value[2]:
            newValue = value[0] * inc
            oppositeAction = shipLoc[key][1]
            if shipLoc[key][0] >= 0 and shipLoc[oppositeAction][0] == 0:
                shipLoc[key][0] += newValue
            else:
                diff = shipLoc[oppositeAction][0] - newValue
                if diff >= 0:
                    shipLoc[oppositeAction][0] = diff
                else:
                    shipLoc[oppositeAction][0] = 0
                    shipLoc[key][0] = abs(diff)

    return shipLoc


def movement(action, value, shipLoc, wpLoc):
    if action == "N" or action == "S" or action == "E" or action == "W":
        wpLoc = moveWaypoint(action, value, wpLoc)

    elif action == "L" or action == "R":
        wpLoc = rotate(action, value, wpLoc)

    elif action == "F":
        shipLoc = moveShip(value, wpLoc, shipLoc)

    newLocs = [wpLoc, shipLoc]
    return newLocs


def main():
    shipLocation = {"N": [0, "S"], "S": [0, "N"], "E": [0, "W"], "W": [0, "E"]}
    waypointLocation = {"N": [1, "S", True], "S": [
        0, "N", False], "E": [10, "W", True], "W": [0, "E", False]}

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        action = line[:1]
        value = int(line[1:])
        locations = movement(
            action, value, shipLocation, waypointLocation)

        waypointLocation = locations[0]
        shipLocation = locations[1]
        print(line)
        print(waypointLocation)
        print(shipLocation)

    northSouth = shipLocation["N"][0] + shipLocation["S"][0]
    eastWest = shipLocation["E"][0] + shipLocation["W"][0]

    print("The Manhattan distance between current position and the ship's starting position is: " +
          str(northSouth + eastWest))


if __name__ == "__main__":
    main()
