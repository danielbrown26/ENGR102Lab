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
#This is a style comment. It is not necessary to include it in the code, but it can be helpful for understanding the purpose of the code.
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'cid']

with open(filename, 'r') as infile:
    data = infile.read()

# Separate passports using blank lines
passports = data.strip().split('\n\n')

valid_passports = []

for passport in passports:

    fields = passport.split()
    passport_data = {}

    for field in fields:
        key, value = field.split(':')
        passport_data[key] = value

    valid = True

    for field in required_fields:
        if field not in passport_data:
            valid = False

    if valid:
        valid_passports.append(passport)

## and saves valid passports to a new file.
with open('valid_passports.txt', 'w') as outfile:
    outfile.write('\n\n'.join(valid_passports))

print(f"There are {len(valid_passports)} valid passports")
#In this code, we read a file containing passport data, separate the passports using blank lines, and check if each passport contains all the required fields. If a passport is valid, it is added to the list of valid passports, which is then written to a new file called 'valid_passports.txt'. Finally, we print the number of valid passports found.