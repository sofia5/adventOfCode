from collections import Counter


def getLowestAndHighest(x, y):
    if(x <= y):
        return {"low": x, "high": y}
    elif(y < x):
        return {"low": y, "high": x}


def addSegments(diagram, match, lowAndHigh, matchPosition):
    for number in range(lowAndHigh.get("low"), lowAndHigh.get("high") + 1):
        if matchPosition == 0:
            diagram.append(match + ',' + str(number))
        elif matchPosition == 1:
            diagram.append(str(number) + ',' + match)
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
        x1y1 = xys[0].split(',')
        x2y2 = xys[1].split(',')

        if x1y1[0] == x2y2[0]:
            lowAndHigh = getLowestAndHighest(int(x1y1[1]), int(x2y2[1]))
            diagram = addSegments(diagram, x1y1[0], lowAndHigh, 0)
        elif x1y1[1] == x2y2[1]:
            lowAndHigh = getLowestAndHighest(int(x1y1[0]), int(x2y2[0]))
            diagram = addSegments(diagram, x1y1[1], lowAndHigh, 1)

    overlap = getOverlappingSegments(diagram)
    print(overlap)


if __name__ == "__main__":
    main()
