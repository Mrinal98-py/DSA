nums = [3,4,5,1,2]


flag = 0
for i in range(len(nums)):
    if nums[i] > nums[i-1]:
        flag = flag 
    else:
        flag = flag + 1
    
print(flag)