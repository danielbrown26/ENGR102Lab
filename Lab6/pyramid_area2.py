# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Tyler Baker
#       DANIEL BROWN
#       WILLIAM SCHOENNBERGER
#       NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 6
# Date: 29 September 2026
#
#
sidel = float(input('Enter the side length in meters: '))
layers = float(input('Enter the number of layers: '))

cube = sidel ** 2 #area of each cube
sumn = (layers * (layers + 1)) / 2 #this just sums up the number of layers put together
area = (sumn * 4 * cube) + (layers ** 2 * cube)
''' technically each bottom side negates the are of the top side above it,
    so by squaring only the last are you can account for all the areas above it
    because they get negated anyway'''
print (f'You need {area:.2f} m^2 of gold foil to cover the pyramid')