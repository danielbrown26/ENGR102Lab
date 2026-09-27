# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 6a team
# Date: 27 September 2026
#
import math
sideL = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))
area = 0
# Loop to find area of foil
for x in range(1, layers+1):
    area += ((sideL**2) * x * 4) + (((x * sideL)**2)-(((x-1) * sideL)**2))
print(f"You need {area:.2f} m^2 of gold foil to cover the pyramid")
