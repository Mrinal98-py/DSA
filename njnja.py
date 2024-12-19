arr = [1,0,0,1,1,0]

# ex_arr = []
ct = 0
size = len(arr)
for i in arr:
    if i == 1:
        ct +=1
zero = size-ct

for j in range(zero):
    arr[j] = 0
    
for k in range(zero,size):
    arr[k] = 1

# print(ct)
print(arr)