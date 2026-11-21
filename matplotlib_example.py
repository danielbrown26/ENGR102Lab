# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:  TYLER BAKER
#.       DANIEL BROWN
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 12 team
# Date: 20 November 2026

# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material

import numpy as np
import matplotlib.pyplot as plt

################## plot 1 #######################
# x values
x = np.linspace(-2, 2, 100)

# y values
y1 = x**2 / (4*2)
y2 = x**2 / (4*6)

# create figure
plt.figure()

# plot both parabolas
plt.plot(x, y1, color='red', linewidth=2, label='f = 2')
plt.plot(x, y2, color='blue', linewidth=6, label='f = 6')

# add titel and labels
plt.title('Parabolas with Different Focal Lengths')
plt.xlabel('x')
plt.ylabel('y')

# add legend
plt.legend()

# display graph
plt.show()

################## plot 2 #######################
# x values
x = np.linspace(-4, 4, 25)

# y values
y = 2*x**3 + 3*x**2 - 11*x - 6

# create figure
plt.figure()

# plot points
plt.plot(x, y, 'ro', label='Cubic Polynomial')

# add title and labels
plt.title('Cubic Polynomial')
plt.xlabel('x values')
plt.ylabel('y values')

# add legend
plt.legend()

# display graph
plt.show()

################## plot 3 #######################
# x values
x = np.linspace(-2*np.pi, 2*np.pi, 100)

# y values
y1 = np.sin(x)
y2 = np.cos(x)

# create two subplots
plt.subplot(2, 1, 1)
plt.plot(x, y1, color='blue', label='sin(x)')
plt.title('Sine Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, y2, color='red', label='cos(x)')
plt.title('Cosine Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()

# adjust spacing
plt.tight_layout()

# display graph
plt.show()
