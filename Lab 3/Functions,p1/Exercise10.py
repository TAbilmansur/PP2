def unique(a):
    di = dict()
    result = list()
    for i in a:
        if (di.get(i)):
            continue
        di[i] = True
        result.append(i)
    return result
a = list(input().split())
print(unique(a))