# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: DANIEL BROWN
#        TYLER BAKER
#        WILLIAM SCHOENNBERGER
#        NOAH DOUGHERTY
# Section: 571
# Assignment: Lab 3b (team)
# Date: 4 SEPTEMBER 2026
#

import math
class stationData:
    posDict = {"x" : [], "y" : [], "z": []}
    slopes = []
    solutions = []
    t1 = 0
    t2 = 0
    tDiff = 0
    tdict = {1: t1, 2: t2}
    tIntervals = []

for x in stationData.tdict.keys():
    stationData.tdict[x] =  float(input(f"Enter time {x}: "))
    for y in stationData.posDict.keys():
        stationData.posDict[y].insert(x, float(input(f"Enter the {y} position of the object at time {x}: ")))
stationData.tDiff = stationData.tdict.get(2) - stationData.tdict.get(1)

for x in range(5):
    stationData.tIntervals.append(stationData.tdict[1] + (x * (stationData.tDiff/4)))

#Function that performs interpolation and puts slopes and solutions in a list
def interpolateData3D(t):
    i = 0
    for x in stationData.posDict.keys():
        stationData.slopes.append((((stationData.posDict[x])[1] - (stationData.posDict[x])[0]) / stationData.tDiff))
        stationData.solutions.append((((t - stationData.tdict[1]) * stationData.slopes[i]) + (stationData.posDict[x])[0]))
        i += 1
print("")
for x in range(5):
    stationData.solutions = []
    stationData.slopes = []
    interpolateData3D(stationData.tIntervals[x])
    print(f"At time {(stationData.tIntervals[x]):.2f} seconds the object is at ({(stationData.solutions[0]):.3f}, {(stationData.solutions[1]):.3f}, {(stationData.solutions[2]):.3f})")
