# nums = [0,0,1,1,1,2,2,3,3,4]
nums = []
if not nums:
    print("empty")

size = len(nums)
write_index = 1

for i in range(1,size):
    if nums[i] != nums[i-1]:
        