def histogram(nums):
    for i in nums:
        for j in range(i):
            print('*',end = '')
        print()
a = list(map(int,input().split()))
histogram(a)