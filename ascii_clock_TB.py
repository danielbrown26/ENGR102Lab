# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
# Section: 571
# Assignment: Lab 8 team
# Date: 20 October 2026
#
timeprint = {'row1': '', 'row2': '', 'row3': '', 'row4': '', 'row5': ''}
cl_type = 'defined in earlier code'
pref_charog = 'defined in earlier code'
time = 'defined in earlier code'
timeprint = 'defined in earlier code'

# all of the different number commands
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