import os
import sys


def main():
    acceptedPasswords = 0

    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    for line in lines:
        lineParts = line.split()
        position = lineParts[0].split("-")
        letter = lineParts[1][0]
        password = lineParts[2]
        print(password[int(position[0]) - 1], password[int(position[1]) - 1])
        if password[int(position[0]) - 1] == letter and password[int(position[1]) - 1] != letter:
            acceptedPasswords += 1
        elif password[int(position[0]) - 1] != letter and password[int(position[1]) - 1] == letter:
            acceptedPasswords += 1

    print(acceptedPasswords)


if __name__ == "__main__":
    main()
