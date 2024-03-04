def calc(k):
    return sum(1 for i in k if bool(i))==len(k)
k = (True,[1,2],5,9)
l = (False,[1,2],5,9)
print(calc(k),calc(l))