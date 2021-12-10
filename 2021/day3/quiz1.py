import os
import sys


def getGammaRate(bits):
    gammaRate = [0 for i in range(len(bits))]
    strGamma = ""
    for colIndex, colValue in enumerate(bits):
        counter = 0
        for i in colValue:
            curr_frequency = bits[colIndex].count(i)
            if(curr_frequency > counter):
                counter = curr_frequency
                gammaRate[colIndex] = i
    return strGamma.join(gammaRate)


def getEpsilonRate(gammaRateInBits):
    epsilonRate = ''
    for _, bit in enumerate(gammaRateInBits):
        if bit == '1':
            epsilonRate += '0'
        elif bit == '0':
            epsilonRate += '1'
    return epsilonRate


def bitToInt(bit):
    return int(bit, 2)


def main():
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    bits = [[0 for x in range(len(lines))] for y in range(len(lines[0]))]

    for x, line in enumerate(lines):
        for y, word in enumerate(line):
            bits[y][x] = word

    gammaRateInBits = getGammaRate(bits)
    gammaRate = bitToInt(gammaRateInBits)

    epsilonRateInBits = getEpsilonRate(gammaRateInBits)
    epsilonRate = bitToInt(epsilonRateInBits)

    print(gammaRate * epsilonRate)


if __name__ == "__main__":
    main()
