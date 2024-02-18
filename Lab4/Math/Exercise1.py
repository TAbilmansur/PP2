import math
def ToRadian(degree):
    return degree/180*math.pi
degree = float(input())
print(ToRadian(degree))