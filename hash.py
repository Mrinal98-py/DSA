hash_map = {}

arr = [2,10,1,10, 500]
# 1 TO 20 in key of hash

for i in arr:
    if i in  hash_map:
        hash_map[i] += 1 
        
    else: 
        hash_map[i] = 0
        hash_map[i] += 1 
    

# for i in range(1,len(arr)+1):
    

# for num in arr:
#     hash_map[num] += 1 
    
    

print(hash_map)


# # insert the value
# hash_map['name'] = 'Milkshake'
# hash_map['age'] = 99
# hash_map['city'] = 'ele'

# print(hash_map['age'])

# print(type(hash_map['name']))