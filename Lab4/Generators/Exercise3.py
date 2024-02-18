def Div(n):
    i = 0
    while (i <= n):
        yield i
        i+=12
n = int(input())
print(*Div(n),sep = ' ')