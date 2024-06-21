import numpy as np
import random
import math
import statistics as st

#INIT
# dimentions of walk
d = 2
# number of trials
n = 500000
# steps per trial
s = 50
# Nonreversable
r = False
# Current position
pos = np.zeros((1, d),dtype='int')
# List of positions walks end in
endingPos = np.zeros((n, d),dtype='int')
endingDists = np.zeros((n, 1),dtype='float')
allPos = np.zeros((n, s+1, d),dtype='int')
# Direction Variables
prevdir = 0
direction = 0

def distFromOrigin(position):
    global d
    if(d == 1):
        return math.fabs(position[0])
    elif(d == 2):
        return math.fabs(math.sqrt((position[0])**2 + (position[1])**2))
    elif(d == 3):
        return math.fabs(math.sqrt((position[0])**2 + (position[1])**2 + (position[2])**2))
    elif (d == 4):
        return math.fabs(math.sqrt((position[0])**2 + (position[1])**2 + (position[2])**2 + (position[3])**2))

returnedToOrigin = 0
for i in np.arange(0, n):
    pos = np.zeros((1, d),dtype='int')
    walkReturned = False
    # Save positions used in current walk, will be useful later
    walkDists = np.zeros((s+1, 1),dtype='float')
    allPos[i][0] = pos
    prevdir = 0
    for j in np.arange(1, s+1):
        direction = random.randint(-d, d)
        while((r and direction*-1 == prevdir) or (direction == 0)):
            direction = random.randint(-d, d)
        if(direction == -1): #LEFT
            pos[0][0] -= 1
        elif(direction == 1): #RIGHT
            pos[0][0] += 1
        elif(direction == -2): # DOWN
            pos[0][1] -= 1
        elif(direction == 2): # UP
            pos[0][1] += 1
        elif(direction == -3): # BACK
            pos[0][2] -= 1
        elif(direction == 3): # FORWARDS
            pos[0][2] += 1
        elif(direction == 4): # 4D POSITIVE
            pos[0][3] += 1
        elif(direction == -4): # 4D NEGATIVE
            pos[0][3] -= 1
        allPos[i][j] = pos
        prevdir = direction
        walkDists[j] = distFromOrigin(pos[0])
        if (walkDists[j] == 0):
            walkReturned = True
    endingPos[i] = pos
    endingDists[i] = distFromOrigin(pos[0])
    if(walkReturned):
        returnedToOrigin += 1

print(f'Max: {endingDists.max()}')
print(f'Min: {endingDists.min()}')
# Need to convert to list to do the stats that I know how to do
distsList = np.ndarray.tolist(endingDists)
distsList = [item for sublist in distsList for item in sublist]
print(f'Mean: {st.mean(distsList)}')
print(f'Mode: {st.mode(distsList)}')
print(f'Median: {st.median(distsList)}')
print(f'Standard Deviation: {st.stdev(distsList)}')
print(f'{returnedToOrigin} returned to the origin, which is {(returnedToOrigin/n)*100} percent.')




