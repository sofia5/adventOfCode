from collections import Counter


def getLowestAndHighest(x, y):
    if(x <= y):
        return {"low": x, "high": y}
    elif(y < x):
        return {"low": y, "high": x}


def addSegments(diagram, match, lowAndHigh, matchPosition):
    for number in range(lowAndHigh.get("low"), lowAndHigh.get("high") + 1):
        if matchPosition == 0:
            diagram.append(str(match) + ',' + str(number))
        elif matchPosition == 1:
            diagram.append(str(number) + ',' + str(match))
    return diagram


def addSegmentsDiagonal(diagram, lowAndHigh1, lowAndHigh2, reverse):
    if not reverse:
        y = lowAndHigh2.get("low")
        for x in range(lowAndHigh1.get("low"), lowAndHigh1.get("high") + 1):
            diagram.append(str(x) + ',' + str(y))
            y += 1
    else:
        y = lowAndHigh2.get("high")
        for x in range(lowAndHigh1.get("low"), lowAndHigh1.get("high") + 1):
            diagram.append(str(x) + ',' + str(y))
            y -= 1

    return diagram


def getOverlappingSegments(diagram):
    overlap = 0
    occurrences = Counter(diagram)
    for occurence in occurrences:
        if occurrences[occurence] > 1:
            overlap += 1
    return overlap


def main():
    with open('input.txt', 'r') as f:
        input = f.read()

    lineSegments = input.split('\n')
    diagram = []

    for lineSegment in lineSegments:
        xys = lineSegment.split(' -> ')
        x1 = int(xys[0].split(',')[0])
        y1 = int(xys[0].split(',')[1])
        x2 = int(xys[1].split(',')[0])
        y2 = int(xys[1].split(',')[1])

        if x1 == x2:
            lowAndHigh = getLowestAndHighest(y1, y2)
            diagram = addSegments(diagram, x1, lowAndHigh, 0)
        elif y1 == y2:
            lowAndHigh = getLowestAndHighest(x1, x2)
            diagram = addSegments(diagram, y1, lowAndHigh, 1)
        elif x1 + y1 == x2 + y2 or abs(x2 - x1) == abs(y2 - y1):
            lowAndHigh1 = getLowestAndHighest(x1, x2)
            lowAndHigh2 = getLowestAndHighest(y1, y2)
            if str(lowAndHigh1.get("low")) + str(lowAndHigh2.get("low")) == str(x1) + str(y1) or str(lowAndHigh1.get("low")) + str(lowAndHigh2.get("low")) == str(x2) + str(y2):
                diagram = addSegmentsDiagonal(
                    diagram, lowAndHigh1, lowAndHigh2, False)
            else:
                diagram = addSegmentsDiagonal(
                    diagram, lowAndHigh1, lowAndHigh2, True)

    overlap = getOverlappingSegments(diagram)
    print(overlap)


if __name__ == "__main__":
    main()
