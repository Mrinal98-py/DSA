hash_map = []

arr = [1]

for i in range(0,len(arr)):
    # hash_map[i] = 0
    hash_map.append(0)


for num in arr:
    hash_map[num-1] += 1
    
print(hash_map)