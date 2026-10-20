# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 8 team
# Date: 20 October 2026
#
# inputs for variables
time = input('Enter the time: ')
cl_type = input('Choose the clock type (12 or 24): ')
ampm = None # stores the value for AM or PM if 12 hour format

# dictionary for the rows of the clock
timeprint = {'row1': '', 'row2': '', 'row3': '', 'row4': '', 'row5': ''}

# subtracts 12 from 24 hour times if neccessary
if cl_type == '12':
    if (int(time[0]) == 1 and int(time[1]) > 2): # for times between 12:00 and 20:00
        time = str(int(time[1]) - 2) + time[2:]
        ampm = 'pm'
    elif int(time[0]) == 2 and time[1] != ':': # only for times after 20:00
        time = str(int(time[0]) - 1)+ str(int(time[1]) - 2) + time[2:]
        ampm = 'pm'
    elif int(time[0]) == 0 and time[1] == ':':
        time = '12' + time[1:]
        ampm = 'am'
    else:
        ampm = 'am'
