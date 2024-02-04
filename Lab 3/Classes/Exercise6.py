import sympy
filter = lambda nums: [x for x in nums if sympy.isprime(x)]
nums = list(map(int,input().split()))
for i in filter(nums):
    print(i,end = ' ')