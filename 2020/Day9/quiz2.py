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


def checkContigouosSet(lines, sumValue):
    windowSize = 2
    numbersBetween = []

    while windowSize < len(lines):
        index1 = 0
        index2 = index1
        addedNumbers = 0

        while index2 < len(lines):

            if addedNumbers == sumValue:
                numbersBetween = [index1, index2]
                break

            while index2 < index1 + windowSize:
                addedNumbers += lines[index2]
                index2 += 1

            else:
                addedNumbers += lines[index2]
                addedNumbers -= lines[index1]
                index1 += 1
                index2 += 1

        windowSize += 1

    return numbersBetween


def getSmallestAndBiggest(lines, numbersBetween):
    numberList = []
    index = numbersBetween[0]
    smallAndBig = []

    while index <= numbersBetween[1]:
        numberList.append(lines[index])
        index += 1

    smallAndBig.append(min(numberList))
    smallAndBig.append(max(numberList))

    return smallAndBig


def main():
    preamble = 25
    index = preamble
    sumValue = 0

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

    numbersBetween = checkContigouosSet(lines[:index], sumValue)
    smallAndBig = getSmallestAndBiggest(lines, numbersBetween)
    print("The sum of the smallest and biggest contigouos numbers generating " +
          str(sumValue) + " is: " + str(smallAndBig[0] + smallAndBig[1]))


if __name__ == "__main__":
    main()
