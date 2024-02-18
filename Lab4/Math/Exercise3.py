import math
def Area(n,l):
    angle = ((n-2)*180/n/2)/180*math.pi 
    a = math.tan(angle)*l/2
    print(a)
    return a/2*n*l
n,l = map(float,input().split())
print(Area(n,l))