arr = [1,2,4,9,0,4,0,2,0,12,2]


for i in arr:
    if i == 0:
        arr.remove(0)
        arr.append(0)
        
print(arr)