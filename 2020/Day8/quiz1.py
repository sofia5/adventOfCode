import os
import sys


def main():
    acc = 0
    index = 0
    visitedInstructions = []

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    while index < len(lines):
        visitedInstructions.append(index)

        if lines[index][:3] == "acc":
            acc += int(lines[index][4:])
        elif lines[index][:3] == "jmp":
            index += int(lines[index][4:]) - 1

        index += 1
        if index in visitedInstructions:
            break

    print(acc)


if __name__ == "__main__":
    main()
