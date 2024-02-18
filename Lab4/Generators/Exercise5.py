def Des(n):
    while n >= 0:
        yield n
        n-=1
n = int(input()) 
for i in Des(n):
    print(i,end = ' ')