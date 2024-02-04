def has_33(nums):
    j = len(nums)
    for i in range(1,j):
        if (nums[i] == nums[i-1] == 3):
            return True 
    return False
nums = list(map(int,input().split()))
print(has_33(nums))