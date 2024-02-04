import math
def filter_prime(a):
    u = []
    for i in a:
        prime = i > 1
        for l in range(2,int(math.sqrt(i))+1):
            if i%l == 0:
                prime = False
                break
        if prime:
            u.append(i)
    return u
a = list(map(int,input().split()))
print(filter_prime(a))
