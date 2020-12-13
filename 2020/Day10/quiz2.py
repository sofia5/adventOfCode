import os
import sys
import math

""" 
Comments (example):
1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19

3,1,1,1,3,1,1,3,1,3

- 3,2,1,3,1,1,3,1,3
- 3,3,3,1,1,3,1,3

4 solutions: 1,1,1 -> 2,1 or 1,2 or 3
2 solutions: 1,1 -> 2
"""


def getJolts(lines):
    curPos = 0
    joltList = ""

    for line in lines:
        if curPos == line - 1:
            joltList = joltList + "1"

        elif curPos == line - 3:
            joltList = joltList + "3"

        curPos = line

    return joltList


def getJoltCombinations(joltList):
    quadruples = 0
    triples = 0
    doubles = 0
    oneJoltGroups = joltList.split("3")
    for item in oneJoltGroups:
        if item == '1111':
            quadruples += 1
        elif item == '111':
            triples += 1
        elif item == '11':
            doubles += 1

    total = int(math.pow(7, quadruples) *
                math.pow(4, triples) * math.pow(2, doubles))
    return total


def main():

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [int(line.rstrip()) for line in f]

    lines.sort()
    joltList = getJolts(lines)
    combinations = getJoltCombinations(joltList)
    print(combinations)


if __name__ == "__main__":
    main()
