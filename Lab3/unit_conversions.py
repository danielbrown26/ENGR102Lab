# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: DANIEL BROWN
#        TYLER BAKER
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 3a (team)
# Date: 4 SEPTEMBER 2026
#

import math
convertVar = float(input("Please enter the quantity to be converted: "))
#Dictionary containing all of the unique parts of every different calculation
convertFormulas = {round(convertVar * 4.44822, 2) : ["pounds force", "newtons"],
                   round(convertVar * 3.28084, 2) : ["meters", "feet"],
                   round(convertVar * 101.325, 2) : ["atmospheres", "kilopascals"],
                   round(convertVar * 3.41214163, 2) : ["watts", "BTU per hour"],
                   round(convertVar * 0.264172052 * 60, 2) : ["liters per second", "US gallons per minute"],
                   round((convertVar * (9/5)) + 32, 2) : ["degrees Celsius", "degrees Fahrenheit"]}
for x in convertFormulas.keys():
    print(f"{convertVar:.2f} {(convertFormulas[x])[0]} is equivalent to {x:.2f} {(convertFormulas[x])[1]}")
