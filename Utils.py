import math

def calculateAngle(coor1, coor2, scroll):
    adjustedCoor1 = (coor1[0] - scroll[0], coor1[1] - scroll[1])
    return math.atan2(coor2[1] - adjustedCoor1[1], coor2[0] - adjustedCoor1[0])