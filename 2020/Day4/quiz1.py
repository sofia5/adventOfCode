import os
import sys
import re


def check_passport_validity(passport):
    passport_validity = False
    if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
        passport_validity = True
    return passport_validity


def check_passport_fields(passport_fields):
    passport = []
    i = 0

    while i < len(passport_fields):
        if passport_fields[i][:3] == "byr":
            if int(passport_fields[i][4:8]) >= 1920 and int(passport_fields[i][4:8]) <= 2002:
                passport.append("byr")

        elif passport_fields[i][:3] == "iyr":
            if int(passport_fields[i][4:8]) >= 2010 and int(passport_fields[i][4:8]) <= 2020:
                passport.append("iyr")

        elif passport_fields[i][:3] == "eyr":
            if int(passport_fields[i][4:8]) >= 2020 and int(passport_fields[i][4:8]) <= 2030:
                passport.append("eyr")

        elif passport_fields[i][:3] == "hgt":
            match = re.match(r"([0-9]+)([a-z]+)", passport_fields[i][4:], re.I)
            if match:
                height = match.groups()
                if (int(height[0]) >= 150 and int(height[0]) <= 193 and height[1] == "cm") or (int(height[0]) >= 59 and int(height[0]) <= 76 and height[1] == "in"):
                    passport.append("hgt")

        elif passport_fields[i][:3] == "hcl":
            match = re.match(r"(#[0-9, a-f]{6})", passport_fields[i][4:], re.I)
            if match:
                passport.append("hcl")

        elif passport_fields[i][:3] == "ecl":
            match = re.match(r"^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$",
                             passport_fields[i][4:], re.I)
            if match:
                passport.append("ecl")

        elif passport_fields[i][:3] == "pid":
            match = re.match(r"([0-9]{9,9}$)", passport_fields[i][4:], re.I)
            if match:
                passport.append("pid")

        elif passport_fields[i][:3] == "cid":
            passport.append("cid")

        i += 1

    return passport


def main():
    valid_passports_count = 0
    with open(os.path.join(sys.path[0], "input.txt")) as f:
        lines = [line.rstrip() for line in f]

    passport_fields = ""
    i = 0
    for line in lines:

        passport_fields = passport_fields + " " + line

        if line == "" or i == len(lines) - 1:
            passport_fields = passport_fields.split()
            print(sorted(passport_fields))
            passport = check_passport_fields(passport_fields)
            passport_fields = ""

            if check_passport_validity(passport) == True:
                valid_passports_count += 1
                print("true")

        i += 1

    print(valid_passports_count)


if __name__ == "__main__":
    main()
