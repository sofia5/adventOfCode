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

    overlap = getOverlappingSegments(diagram)
    print(overlap)


if __name__ == "__main__":
    main()
