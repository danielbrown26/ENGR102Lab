# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: NOAH DOUGHERTY
#        DANIEL BROWN
#        TYLER BAKER
#        WILLIAM SCHOENBERGER
# Section: 571
# Assignment: Lab 4 (team)
# Date: 11 SEPTEMBER 2026
#

pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = float(pay - cost)
print(f"You recieved ${change:.2f} in change. That is...")

cents = round(change * 100)

# quaters
quarters = cents // 25
cents %= 25
# dimes
dimes = cents // 10
cents %= 10
# nickels
nickels = cents // 5
cents %= 5
# pennies
pennies = cents

if quarters > 0 and quarters <=1:
    print(f"{quarters} quarter")
if quarters > 1:
    print(f"{quarters} quarters")
if dimes > 0 and dimes <= 1:
    print(f"{dimes} dime")
if dimes > 1:
    print(f"{dimes} dimes")
if nickels > 0 and nickels <=1:
    print(f"{nickels} nickel")
if nickels > 1:
    print(f"{nickels} nickels")
if pennies > 0 and pennies <=1:
    print(f"{pennies} penny")
if pennies > 1:
    print(f"{pennies} pennies")