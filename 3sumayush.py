arr = [40,6,2,3,4,5,6,2,4,2,1]
le = len(arr)
set = le // 3
sumw = []

# print(rem)
for i in range(le):
    if le >=3:
        sumw.append([arr[0],arr[1],arr[2]])
        arr.remove(arr[0])
        arr.remove(arr[0])
        arr.remove(arr[0])
    elif le >= 2:
        sumw.append([arr[0],arr[1]])
        arr.remove(arr[0])
        arr.remove(arr[0])
    elif le >= 1:
        sumw.append([arr[0]])
        arr.remove(arr[0])
        # print("no")
    
    le = len(arr)  #update the length


#to merge the last two sub array    
if (len(sumw[-1]) < 3):
    sumw[-2] = sumw[-2] + sumw [-1]
    # print('sumw -2',sumw[-2])
elif (len(sumw[-1]) < 3):
    sumw[-2] = sumw[-2]
    
    
for i in range(set): #to remove the last sub-array
    arr.append(sumw[i])   

n = len(arr)
for i in range(n):
    for j in range(n - i - 1):
        if sum(arr[j]) > sum(arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

         
# print("sumw -1",sumw[-1])
print("sun is",sumw)
# print("main:",mainar)

print("arra:",arr)
# print("sort",sorted_arr)

# print("ans",arr)