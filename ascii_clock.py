# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
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

# time commands
for i in range(len(time)):
    if pref_charog == '': # this will use the actual number if there is no preffered character
        pref_char = time[i]
    if time[i] == '0': # all the below code will add a number to the output by addding characters to the sperate rows
        timeprint['row1'] = timeprint['row1'] + (pref_char * 3)
        timeprint['row2'] = timeprint['row2'] + pref_char + ' ' +pref_char
        timeprint['row3'] = timeprint['row3'] + pref_char + ' ' +pref_char
        timeprint['row4'] = timeprint['row4'] + pref_char + ' ' +pref_char
        timeprint['row5'] = timeprint['row5'] + (pref_char * 3)
    elif time[i] == '1':
        timeprint['row1'] = timeprint['row1'] + ' ' + pref_char + ' '
        timeprint['row2'] = timeprint['row2'] + (pref_char * 2) + ' '
        timeprint['row3'] = timeprint['row3'] + ' ' + pref_char + ' '
        timeprint['row4'] = timeprint['row4'] + ' ' + pref_char + ' '
        timeprint['row5'] = timeprint['row5'] + (pref_char * 3)
    elif time[i] == '2':
        timeprint['row1'] = timeprint['row1'] + (pref_char * 3)
        timeprint['row2'] = timeprint['row2'] + '  ' + pref_char
        timeprint['row3'] = timeprint['row3'] + (pref_char * 3)
        timeprint['row4'] = timeprint['row4'] + pref_char + '  '
        timeprint['row5'] = timeprint['row5'] + (pref_char * 3)
    elif time[i] == '3':
        timeprint['row1'] = timeprint['row1'] + (pref_char * 3)
        timeprint['row2'] = timeprint['row2'] + '  ' + pref_char
        timeprint['row3'] = timeprint['row3'] + (pref_char * 3)
        timeprint['row4'] = timeprint['row4'] + '  ' + pref_char
        timeprint['row5'] = timeprint['row5'] + (pref_char * 3)
    elif time[i] == '4':
        timeprint['row1'] = timeprint['row1'] + pref_char + ' ' + pref_char
        timeprint['row2'] = timeprint['row2'] + pref_char + ' ' + pref_char
        timeprint['row3'] = timeprint['row3'] + (pref_char * 3)
        timeprint['row4'] = timeprint['row4'] + '  ' + pref_char
        timeprint['row5'] = timeprint['row5'] + '  ' + pref_char
    elif time[i] == '5':
        timeprint['row1'] = timeprint['row1'] + (pref_char * 3)
        timeprint['row2'] = timeprint['row2'] + pref_char + '  '
        timeprint['row3'] = timeprint['row3'] + (pref_char * 3)
        timeprint['row4'] = timeprint['row4'] + '  ' + pref_char
        timeprint['row5'] = timeprint['row5'] + (pref_char * 3)
    elif time[i] == '6':
        timeprint['row1'] = timeprint['row1'] + (pref_char * 3)
        timeprint['row2'] = timeprint['row2'] + pref_char + '  '
        timeprint['row3'] = timeprint['row3'] + (pref_char * 3)
        timeprint['row4'] = timeprint['row4'] + pref_char + ' ' + pref_char
        timeprint['row5'] = timeprint['row5'] + (pref_char * 3)
    elif time[i] == '7':
        timeprint['row1'] = timeprint['row1'] + (pref_char * 3)
        timeprint['row2'] = timeprint['row2'] + '  ' + pref_char
        timeprint['row3'] = timeprint['row3'] + '  ' + pref_char
        timeprint['row4'] = timeprint['row4'] + '  ' + pref_char
        timeprint['row5'] = timeprint['row5'] + '  ' + pref_char
    elif time[i] == '8':
        timeprint['row1'] = timeprint['row1'] + (pref_char * 3)
        timeprint['row2'] = timeprint['row2'] + pref_char + ' ' + pref_char
        timeprint['row3'] = timeprint['row3'] + (pref_char * 3)
        timeprint['row4'] = timeprint['row4'] + pref_char + ' ' + pref_char
        timeprint['row5'] = timeprint['row5'] + (pref_char * 3)
    elif time[i] == '9':
        timeprint['row1'] = timeprint['row1'] + (pref_char * 3)
        timeprint['row2'] = timeprint['row2'] + pref_char + ' ' + pref_char
        timeprint['row3'] = timeprint['row3'] + (pref_char * 3)
        timeprint['row4'] = timeprint['row4'] + '  ' + pref_char
        timeprint['row5'] = timeprint['row5'] + (pref_char * 3)
    elif time[i] == ':':
        timeprint['row1'] = timeprint['row1'] + ' '
        timeprint['row2'] = timeprint['row2'] + ':'
        timeprint['row3'] = timeprint['row3'] + ' '
        timeprint['row4'] = timeprint['row4'] + ':'
        timeprint['row5'] = timeprint['row5'] + ' '
    if (i != (len(time)) - 1) and cl_type == '24':
        timeprint['row1'] = timeprint['row1'] + ' '
        timeprint['row2'] = timeprint['row2'] + ' '
        timeprint['row3'] = timeprint['row3'] + ' '
        timeprint['row4'] = timeprint['row4'] + ' '
        timeprint['row5'] = timeprint['row5'] + ' '
        
    if (i != (len(time)) + 1) and cl_type == '12':
        timeprint['row1'] = timeprint['row1'] + ' '
        timeprint['row2'] = timeprint['row2'] + ' '
        timeprint['row3'] = timeprint['row3'] + ' '
        timeprint['row4'] = timeprint['row4'] + ' '
        timeprint['row5'] = timeprint['row5'] + ' '

# adds the AM or PM
if cl_type == '12':
    if ampm == 'am':
        timeprint['row1'] = timeprint['row1'] + ' A '
        timeprint['row2'] = timeprint['row2'] + 'A A'
        timeprint['row3'] = timeprint['row3'] + 'AAA'
        timeprint['row4'] = timeprint['row4'] + 'A A'
        timeprint['row5'] = timeprint['row5'] + 'A A'
    if ampm == 'pm':
        timeprint['row1'] = timeprint['row1'] + 'PPP'
        timeprint['row2'] = timeprint['row2'] + 'P P'
        timeprint['row3'] = timeprint['row3'] + 'PPP'
        timeprint['row4'] = timeprint['row4'] + 'P  '
        timeprint['row5'] = timeprint['row5'] + 'P  '
    timeprint['row1'] = timeprint['row1'] + ' ' + 'M   M'
    timeprint['row2'] = timeprint['row2'] + ' ' + 'MM MM'
    timeprint['row3'] = timeprint['row3'] + ' ' + 'M M M'
    timeprint['row4'] = timeprint['row4'] + ' ' + 'M   M'
    timeprint['row5'] = timeprint['row5'] + ' ' + 'M   M'

# final print statements for each row
final = (f"{timeprint['row1']}\n{timeprint['row2']}\n{timeprint['row3']}\n{timeprint['row4']}\n{timeprint['row5']}")
print()
print(final)
