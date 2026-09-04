# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: DANIEL BROWN
#        TYLER BAKER
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 2c (team)
# Date: 25 AUGUST 2026
#

import math

class stationData:
    d1 = 2030 #km
    d2 = 23030 #km
    t1 = 10 #minutes
    t2 = 55 #minutes

def interpolateDistance(x1, x2, y1, y2, t):
    m = (y2 - y1) / (x2 - x1)
    return m * (int(t) - 10) + 2030
def interpolateOffset(x1, x2, y1, y2, t):
    m = (y2 - y1) / (x2 - x1)
    distance = m * (int(t) - 10) + 2030
    return distance % (6745*2*math.pi)

print(f"Part 1:\nFor t = 25 minutes, the position p = {interpolateDistance(stationData.t2, stationData.t1, stationData.d2, stationData.d1, 25)} kilometers\nPart 2:\nFor t = 300 minutes, the position p = {interpolateOffset(stationData.t2, stationData.t1, stationData.d2, stationData.d1, 300)} kilometers")
