import os
import sys


def getYesResponses(groupAnswer):
    yesResonses = []
    for question in groupAnswer:
        if question not in yesResonses:
            yesResonses.append(question)
    print(yesResonses)
    return(len(yesResonses))


def main():
    allResponses = 0
    groupAnswer = ""

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for index, line in enumerate(lines):
        groupAnswer = groupAnswer + line

        if line == "" or index == len(lines) - 1:
            allResponses += getYesResponses(groupAnswer)
            groupAnswer = ""

    print(allResponses)


if __name__ == "__main__":
    main()
