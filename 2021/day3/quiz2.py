
def getLine(lines, mostOrFewest):
    index = 0

    while len(lines) > 1:
        bits = transposeBits(lines)
        lines = countBinaries(lines, index, bits, mostOrFewest)
        index += 1
    return lines


def transposeBits(lines):
    bits = [[0 for x in range(len(lines))] for y in range(len(lines[0]))]
    for x, line in enumerate(lines):
        for y, word in enumerate(line):
            bits[y][x] = int(word)
    return bits


def countBinaries(lines, index, bits, mostOrFewest):
    sumZeros = 0
    sumOnes = 0
    for binary in bits[index]:
        if binary == 0:
            sumZeros += 1
        elif binary == 1:
            sumOnes += 1

    if mostOrFewest == 'most':
        if sumZeros == sumOnes:
            lines = selectBits(lines, index, 1)
        elif sumZeros > sumOnes:
            lines = selectBits(lines, index, 0)
        elif sumOnes > sumZeros:
            lines = selectBits(lines, index, 1)

    if mostOrFewest == 'fewest':
        if sumZeros == sumOnes:
            lines = selectBits(lines, index, 0)
        elif sumZeros > sumOnes:
            lines = selectBits(lines, index, 1)
        elif sumOnes > sumZeros:
            lines = selectBits(lines, index, 0)

    return lines


def selectBits(lines, index, binary):
    newLines = []
    for line in lines:
        if int(line[index]) == binary:
            newLines.append(line)
    return newLines


def bitToInt(bit):
    return int(bit, 2)


def main():
    with open("input.txt") as f:
        lines = [line.rstrip() for line in f]

    line = getLine(lines, 'most')
    oxygenGeneratorRating = bitToInt(line[0])

    line = getLine(lines, 'fewest')
    CO2ScrubberRating = bitToInt(line[0])

    print(oxygenGeneratorRating * CO2ScrubberRating)


if __name__ == "__main__":
    main()
