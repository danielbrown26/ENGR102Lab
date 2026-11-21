# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 10 team
# Date: 3 November 2026
# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material

import numpy as np
a = np.arange(12).reshape(3, 4)
print(f'A = {a}')

b = np.arange(8).reshape(4, 2)
print(f'\nB = {b}')

c = np.arange(6).reshape(2, 3)
print(f'\nC = {c}')

d = a @ b @ c
print(f'\nD = {d}')

dt = np.transpose(d) # found transpose function under universal funtions part of numpy website
print(f'\nD^T = {dt}')

e = (np.sqrt(d)) / 2
print(f'\nE = {e}')