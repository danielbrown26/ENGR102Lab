# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  DANIEL BROWN
# Section: 571
# Assignment: Lab 8 team
# Date: 20 October 2026
#
# inputs for variables
time = input('Enter the time: ')
cl_type = input('Choose the clock type (12 or 24): ')
pref_char = input('Enter your preferred character: ')
ampm = None # stores the value for AM or PM if 12 hour format
timeprint = {'row1': '', 'row2': '', 'row3': '', 'row4': '', 'row5': ''}


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
