# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: William Schoenberger
# NAME OF Noah Dougherty
# NAME OF Tyler Baker
# NAME OF Daniel Brown
# Section: 571
# Assignment: Team Lab: 6
# Date: 9/29/2026

import math

x = float(input("Enter a value for x: "))

while x <= 0 or x > 2:
    x = float(input("Out of range! Try again: "))

tolerance = float(input("Enter the tolerance: "))

approx = 0.0
n = 1

term = (x - 1) ** n / n

while abs(term) >= tolerance:
    if n % 2 == 1:
        approx += term
    else:
        approx -= term

    n += 1
    term = (x - 1) ** n / n

exact = math.log(x)
difference = abs(approx - exact)

print("ln(" + str(x) + ") is approximately", approx)
print("ln(" + str(x) + ") is exactly", exact)
print("The difference is", difference)
# I 1
