# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 4 Team
# Date: 12 September 2026
#
#
a_val = input('Please enter the coefficient A: ' )
b_val = input('Please enter the coefficient B: ' )
c_val = input('Please enter the coefficient C: ' )

#this code will decide how to treat the variable a based on its sign and value
if a_val == '0':
    a_plug = ''
elif a_val == '1':
    a_plug = 'x^2'
elif a_val == '-1':
    a_plug = '- x^2'
elif a_val < '0':
    a_plug = (f' - {(int(a_val) * -1)}x^2')
else:
    a_plug = (f'{a_val}x^2')

#this code decides if the first sign is + or - , or if it should be deleted altogether
if b_val >= '0' and a_val != '0':
    sign1 = '+'
elif b_val < '0' and a_val != '0':
    sign1 = ''
else:
    sign1 = ''


#this code will decide how to treat the variable b based on its sign and value
if b_val == '0':
    b_plug = ''
elif b_val == '1':
    b_plug = 'x^2'
elif b_val == '-1':
    b_plug = '- x^2'
elif b_val < '0':
    b_plug = (f' - {(int(b_val) * -1)}x')
else:
    b_plug = (f'{b_val}x')

#this code decides if the second sign is + or - , or if it should be deleted altogether
if c_val >= '0' and a_val != '0':
    sign2 = '+'
elif c_val < '0' and a_val != '0':
    sign2 = ''
else:
    sign2 = ''


#this code will decide how to treat the variable c based on its sign and value
if c_val == '0':
    c_plug = ''
elif c_val == '1':
    c_plug = 'x^2'
elif c_val == '-1':
    c_plug = '- x^2'
elif c_val < '0':
    c_plug = (f' - {(int(c_val) * -1)}x')
else:
    c_plug = (f'{c_val}x')

if a_val == '0' and b_val == '0' and c_val == '0':
    print('The equation is 0 = 0')
else:
    print(f'The equation is {a_plug}{sign1}{b_plug}{sign2}{c_plug} = 0')
