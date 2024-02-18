def Squares(n):
    i = 0
    while (i**2 <= n):
        yield i**2 
        i+=1
n = int(input())
print(*Squares(n),sep = ' ')