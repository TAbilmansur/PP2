def spy_game(nums):
    j = len(nums)
    for i in range(2,j):
        if (nums[i] == 7 and nums[i-1] == nums[i-2] == 0):
            return True 
    return False
nums = list(map(int,input().split()))
print(spy_game(nums))