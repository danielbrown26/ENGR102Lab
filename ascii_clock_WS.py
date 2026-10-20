# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: WILLIAM SCHOENNBERGER
# Section: 571
# Assignment: Lab 8 team
# Date: 20 October 2026
#
# inputs for variables
time = input('Enter the time: ')
cl_type = input('Choose the clock type (12 or 24): ')
pref_char = input('Enter your preferred character: ')
ampm = None # stores the value for AM or PM if 12 hour format
allowed_chars = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z', '@', '$', '&', '*', '=', '', ' ']

# checks if the character works
while pref_char not in allowed_chars:
    pref_char = input('Character not permitted! Try again: ')

pref_charog = pref_char # stores the og value for the preferred character

# dictionary for the rows of the clock
timeprint = {'row1': '', 'row2': '', 'row3': '', 'row4': '', 'row5': ''}