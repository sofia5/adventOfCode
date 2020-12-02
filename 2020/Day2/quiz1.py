import os
import sys


def main():
    acceptedPasswords = 0

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        lineParts = line.split()
        frequency = lineParts[0].split("-")
        letter = lineParts[1][0]
        password = lineParts[2]
        if password.count(letter) >= int(frequency[0]) and password.count(letter) <= int(frequency[1]):
            acceptedPasswords += 1

    print(acceptedPasswords)


if __name__ == "__main__":
    main()
