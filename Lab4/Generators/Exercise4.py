def squares(a,b):
    i = a
    while i <= b:
        yield i**2 
        i+=1
a,b = map(int,input().split())
for i in squares(a,b):
    print(i,end = ' ')