import math


def dist(xa, ya, xb, yb):
    '''
    Function that calculates the distance  between two points.
    This comment is shown with help(dist).
    '''
    return math.sqrt((xa-xb)**2+(ya-yb)**2)


print(dist(1, 1, 10, 10))
