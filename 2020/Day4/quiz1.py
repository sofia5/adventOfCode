import os
import sys


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
            passport.append("byr")

        elif passport_fields[i][:3] == "iyr":
            passport.append("iyr")

        elif passport_fields[i][:3] == "eyr":
            passport.append("eyr")

        elif passport_fields[i][:3] == "hgt":
            passport.append("hgt")

        elif passport_fields[i][:3] == "hcl":
            passport.append("hcl")

        elif passport_fields[i][:3] == "ecl":
            passport.append("ecl")

        elif passport_fields[i][:3] == "pid":
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
    for line in lines:

        if line != "":
            passport_fields = passport_fields + " " + line

        else:
            passport_fields = passport_fields.split()
            passport = check_passport_fields(passport_fields)
            passport_fields = ""

            if check_passport_validity(passport) == True:
                valid_passports_count += 1

    print(valid_passports_count)


if __name__ == "__main__":
    main()
