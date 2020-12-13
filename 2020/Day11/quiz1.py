import os
import sys

# Checks of prev & next rows


def indexValidation(char, lines, index, line, i, check):
    validations = []
    validation = True

    if index != 0:
        validations.append(lines[index - 1][i] == char)
    if i != 0:
        validations.append(lines[index][i - 1] == char)
    if index != len(lines) - 1:
        validations.append(lines[index + 1][i] == char)
    if i != len(line) - 1:
        validations.append(lines[index][i + 1] == char)
    if index != 0 and i != 0:
        validations.append(lines[index - 1][i - 1] == char)
    if index != 0 and i != len(line) - 1:
        validations.append(lines[index - 1][i + 1] == char)
    if index != len(lines) - 1 and i != 0:
        validations.append(lines[index + 1][i - 1] == char)
    if index != len(lines) - 1 and i != len(line) - 1:
        validations.append(lines[index + 1][i + 1] == char)

    if check == 'no occupied':
        if validations.count(True) > 0:
            validation = False
    if check == 'is occupied':
        if validations.count(True) < 4:
            validation = False
    return validation


def fillIfEmpty(lines, line, index):
    newLine = []
    for i, pos in enumerate(line):

        if pos == "L":
            validation = indexValidation(
                '#', lines, index, line, i, 'no occupied')
            if (validation):
                newLine.append("#")
            else:
                newLine.append("L")

        elif pos == "#":
            validation = indexValidation(
                '#', lines, index, line, i, 'is occupied')
            if (validation):
                newLine.append("L")
            else:
                newLine.append("#")
        else:
            newLine.append(".")
    # print(newLine)
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
    i = 0
    while newLines != lines:
        # print(i)
        for index, line in enumerate(lines):
            newLines.append(fillIfEmpty(lines, line, index))

        if newLines == lines:
            break
        else:
            lines = newLines.copy()
            newLines = []

        i += 1

    takenSeats = countTakenSeats(lines)
    print(takenSeats)


if __name__ == "__main__":
    main()
