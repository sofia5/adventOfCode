import os
import sys


def getSum(numbers, index1, index2):
    return numbers[index1] + numbers[index2]


def getCorrectSum(numbers, index, sumValue):
    sumExists = False
    sumOfNumbers = 0
    i1 = 0

    while i1 < len(numbers):
        i2 = 0

        while i2 < len(numbers):

            if i1 != i2:
                sumOfNumbers = getSum(numbers, i1, i2)

            if sumOfNumbers == sumValue:
                sumExists = True
                break

            i2 += 1

        i1 += 1

    return sumExists


def main():
    preamble = 25
    index = preamble

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [int(line.rstrip()) for line in f]

    # print(lines)
    while index < len(lines):
        sumValue = lines[index]
        lowerLimit = index - preamble
        upperLimit = index
        numbers = lines[lowerLimit:upperLimit].copy()
        sumExists = getCorrectSum(numbers, index, sumValue)
        if not sumExists:
            break
        index += 1

    print(sumValue)


if __name__ == "__main__":
    main()
