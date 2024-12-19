arr= [10, 35, 1, 10, 33, 1]

n = len(arr)

large = -1
sec_large = -1

#  check using the index    //i was checking with th
# find hte greatest in the array
for i in range(n):
    if arr[i] > large:
        large = arr[i]
        
        # find the 2nd greatest in the array
for i in range(n):
    if arr[i] > sec_large and arr[i] != large:
        sec_large = arr[i]
        
print(sec_large)