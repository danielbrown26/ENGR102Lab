# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 11 team
# Date: 11/12/2026

filename = input("Enter the name of the file: ")
#In this code, we read a file containing passport data, separate the passports using blank lines, and check if each passport contains all the required fields. If a passport is valid, it is added to the list of valid passports, which is then written to a new file called 'valid_passports.txt'. Finally, we print the number of valid passports found.
with open(filename, "r") as infile:
    data = infile.read()
#This is a style comment. It is not necessary to include it in the code, but it can be helpful for understanding the purpose of the code.
data = data.replace("\r\n", "\n").replace("\r", "\n").strip()

if data == "":
    passports = []
else:
    passports = data.split("\n\n")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "cid"]

valid_passports = []

for passport in passports:
    fields = passport.split()
    passport_data = {}

    for field in fields:
        key, value = field.split(":", 1)
        passport_data[key] = value

    valid = True

    for field in required_fields:
        if field not in passport_data:
            valid = False

    if valid:

        byr = passport_data["byr"]
        if len(byr) != 4 or not byr.isdigit():
            valid = False
        elif int(byr) < 1922 or int(byr) > 2010:
            valid = False

        iyr = passport_data["iyr"]
        if len(iyr) != 4 or not iyr.isdigit():
            valid = False
        elif int(iyr) < 2016 or int(iyr) > 2026:
            valid = False

        eyr = passport_data["eyr"]
        if len(eyr) != 4 or not eyr.isdigit():
            valid = False
        elif int(eyr) < 2026 or int(eyr) > 2036:
            valid = False

        hgt = passport_data["hgt"]

        if hgt.endswith("cm"):
            height = hgt[:-2]

            if not height.isdigit():
                valid = False
            elif int(height) < 150 or int(height) > 193:
                valid = False

        elif hgt.endswith("in"):
            height = hgt[:-2]

            if not height.isdigit():
                valid = False
            elif int(height) < 59 or int(height) > 76:
                valid = False

        else:
            valid = False

        hcl = passport_data["hcl"]

        if len(hcl) != 7 or hcl[0] != "#":
            valid = False
        else:
            for character in hcl[1:]:
                if character not in "0123456789abcdef":
                    valid = False

        ecl = passport_data["ecl"]
        eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if ecl not in eye_colors:
            valid = False

        cid = passport_data["cid"]

        if len(cid) != 3 or not cid.isdigit():
            valid = False
        elif cid[0] == "0":
            valid = False

    if valid:
        valid_passports.append(passport)
# to validate each passport value before saving valid passports.
with open("valid_passports2.txt", "w") as outfile:
    outfile.write("\n\n".join(valid_passports))

print(f"There are {len(valid_passports)} valid passports")
