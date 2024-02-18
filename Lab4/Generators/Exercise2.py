def Even(n):
    i = 0
    while (i <= n):
        yield i
        i+=2
n = int(input())
print(*Even(n),sep = ' ')