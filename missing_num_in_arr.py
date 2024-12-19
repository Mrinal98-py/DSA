nums = [3,0,1]


length = len(nums)
ogtotal = 0
for i in range(length+1):
    ogtotal = ogtotal + i
    
total = 0

for i in nums:
    total = total + i

print(ogtotal-total)    