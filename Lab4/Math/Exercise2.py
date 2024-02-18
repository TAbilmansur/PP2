import math
def Area(H,B1,B2):
    return (B1+B2)/2*H 
H,B1,B2 = map(float,input().split())
print(Area(H,B1,B2))