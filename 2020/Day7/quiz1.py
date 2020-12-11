import os
import sys


def findBags(bags, bagToLookFrom, foundBags):
    if bagToLookFrom in bags:
        for bag in bags[bagToLookFrom]:
            if bag not in foundBags:
                foundBags.append(bag)
                findBags(bags, bag, foundBags)

    return foundBags


def main():
    bags = {}
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        words = line.split()

        surroundingBag = " ".join(words[: 2])

        for index, word in enumerate(words):
            if word.isdigit():
                bag = " ".join(words[index + 1: index + 3])
                if bag in bags:
                    bags[bag].append(surroundingBag)
                else:
                    bags[bag] = [surroundingBag]

    res = findBags(bags, 'shiny gold', [])
    print(len(res))


if __name__ == "__main__":
    main()
