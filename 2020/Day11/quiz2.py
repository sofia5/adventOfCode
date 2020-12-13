import os
import sys


def indexValidation(occupied, free, lines, index, i):
    validations = []
    tempIndex1 = index
    tempIndex2 = i

    while tempIndex1 != 0:
        if lines[tempIndex1 - 1][i] == occupied:
            validations.append(True)
            break
        elif lines[tempIndex1 - 1][i] == free:
            break
        tempIndex1 -= 1

    tempIndex1 = index

    while tempIndex2 != 0:
        if lines[index][tempIndex2 - 1] == occupied:
            validations.append(True)
            break
        elif lines[index][tempIndex2 - 1] == free:
            break
        tempIndex2 -= 1

    tempIndex2 = i

    while tempIndex1 != len(lines) - 1:
        if lines[tempIndex1 + 1][i] == occupied:
            validations.append(True)
            break
        elif lines[tempIndex1 + 1][i] == free:
            break
        tempIndex1 += 1

    tempIndex1 = index

    while tempIndex2 != len(lines[index]) - 1:
        if lines[index][tempIndex2 + 1] == occupied:
            validations.append(True)
            break
        elif lines[index][tempIndex2 + 1] == free:
            break
        tempIndex2 += 1

    tempIndex1 = index
    tempIndex2 = i

    while tempIndex1 != 0 and tempIndex2 != 0:
        if lines[tempIndex1 - 1][tempIndex2 - 1] == occupied:
            validations.append(True)
            break
        elif lines[tempIndex1 - 1][tempIndex2 - 1] == free:
            break
        tempIndex1 -= 1
        tempIndex2 -= 1

    tempIndex1 = index
    tempIndex2 = i

    while tempIndex1 != 0 and tempIndex2 != len(lines[index]) - 1:
        if lines[tempIndex1 - 1][tempIndex2 + 1] == occupied:
            validations.append(True)
            break
        elif lines[tempIndex1 - 1][tempIndex2 + 1] == free:
            break
        tempIndex1 -= 1
        tempIndex2 += 1

    tempIndex1 = index
    tempIndex2 = i

    while tempIndex1 != len(lines) - 1 and tempIndex2 != 0:
        if lines[tempIndex1 + 1][tempIndex2 - 1] == occupied:
            validations.append(True)
            break
        elif lines[tempIndex1 + 1][tempIndex2 - 1] == free:
            break
        tempIndex1 += 1
        tempIndex2 -= 1

    tempIndex1 = index
    tempIndex2 = i

    while tempIndex1 != len(lines) - 1 and tempIndex2 != len(lines[index]) - 1:
        if lines[tempIndex1 + 1][tempIndex2 + 1] == occupied:
            validations.append(True)
            break
        elif lines[tempIndex1 + 1][tempIndex2 + 1] == free:
            break
        tempIndex1 += 1
        tempIndex2 += 1

    return validations


def fillIfEmpty(lines, line, index):
    newLine = []
    for i, pos in enumerate(line):

        if pos == "L":
            validations = indexValidation(
                '#', 'L', lines, index, i)
            if validations.count(True) == 0:
                newLine.append("#")
            else:
                newLine.append("L")

        elif pos == "#":
            validations = indexValidation(
                '#', 'L', lines, index, i)
            if validations.count(True) >= 5:
                newLine.append("L")
            else:
                newLine.append("#")
        else:
            newLine.append(".")
    return newLine


def countTakenSeats(lines):
    count = 0
    for line in lines:
        for char in line:
            if char == '#':
                count += 1
    return count


def main():
    newLines = []

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    while newLines != lines:
        for index, line in enumerate(lines):
            newLines.append(fillIfEmpty(lines, line, index))

        if newLines == lines:
            break
        else:
            lines = newLines.copy()
            newLines = []

    takenSeats = countTakenSeats(lines)
    print(takenSeats)


if __name__ == "__main__":
    main()
