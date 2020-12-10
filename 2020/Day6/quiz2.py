import os
import sys


def getYesResponses(answers):
    yesAnswers = []
    numOfPeople = len(answers)
    allAnswers = ''.join(answers)

    for question in allAnswers:
        if question not in yesAnswers:
            if numOfPeople == allAnswers.count(question):
                yesAnswers.append(question)

    return(len(yesAnswers))


def main():
    allResponses = 0
    answers = []

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for index, line in enumerate(lines):
        if line != "":
            answers.append(line)

        if line == "" or index == len(lines) - 1:
            allResponses += getYesResponses(answers)
            answers = []

    print(allResponses)


if __name__ == "__main__":
    main()
