import os
import sys


def findBags(bags, bagToLookFrom, foundBags):
    if bagToLookFrom in bags:
        for bag in bags[bagToLookFrom]:
            if bagToLookFrom in foundBags:
                foundBags[bagToLookFrom].append(bag)
            else:
                foundBags[bagToLookFrom] = [bag]
            findBags(bags, bag[0], foundBags)
    return foundBags


""" def countRequiredBags(bags, bagToLookFrom, count, inc):
    if bagToLookFrom in bags:
        for bag in bags[bagToLookFrom]:
            print(bagToLookFrom)
            print(inc)
            print(bag)
            countRequiredBags(bags, bag[0], count, inc + 1)

 """


def main():
    bags = {}
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        words = line.split()

        containedBag = " ".join(words[: 2])

        for index, word in enumerate(words):
            if word.isdigit():
                numberOfBags = word
                bag = " ".join(words[index + 1: index + 3])

                if containedBag in bags:
                    bags[containedBag].append((bag, numberOfBags))
                else:
                    bags[containedBag] = [(bag, numberOfBags)]

    foundBags = findBags(bags, 'shiny gold', {})
    print(foundBags)
    #gatherRequiredBags(foundBags, 'shiny gold', [0], 0)


if __name__ == "__main__":
    main()
