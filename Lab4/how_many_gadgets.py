# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: DANIEL BROWN
# Section: 571
# Assignment: Lab 4b (individual)
# Date: 10 SEPTEMBER 2026
#
import math
days = int(input("Please enter a positive value for day: "))
#Conditional that checks input and calculates accordingly
if (days >= 0):
    if(days <=10):
        gadgets = days * 10
    elif(days <= 50):
        gadgets = 100
        gadgets += (1/2)*(11 + days)*(days-10)
    elif(days >= 50):
        gadgets = 1320 + (50*(days-50))
    if(days > 101):
        gadgets = 3820
    print(f"The sum total number of gadgets produced on day {int(days)} is {int(gadgets)}")
else:
    print("You entered an invalid number!")
