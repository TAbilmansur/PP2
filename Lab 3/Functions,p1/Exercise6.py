def rev(a):
    result = list(a.split())
    result.reverse()
    return (' ').join(result)
a = input()
print(rev(a))