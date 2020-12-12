import os
import sys


def isInfiniteLoop(lines):
    acc = 0
    index = 0
    visitedInstructions = []
    # print(lines)

    while index < len(lines):
        visitedInstructions.append(index)

        if lines[index][:3] == "acc":
            acc += int(lines[index][4:])
        elif lines[index][:3] == "jmp":
            index += int(lines[index][4:]) - 1

        index += 1
        if index in visitedInstructions:
            acc = 0
            break

    return acc


def main():
    index = 0

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    while index < len(lines):
        newLines = lines.copy()

        if newLines[index][:3] == "nop" or newLines[index][:3] == "jmp":
            if newLines[index][:3] == "nop":
                newLines[index] = newLines[index].replace("nop", "jmp")
            elif newLines[index][:3] == "jmp":
                newLines[index] = newLines[index].replace("jmp", "nop")

            # print(newLines)
            acc = isInfiniteLoop(newLines)
            if acc != 0:
                print(acc)
                break

        index += 1


if __name__ == "__main__":
    main()
