# arr = [11,2,23,1]

# n = len(arr)
 
# for i in range(n):
#     for j in range(n-i-1):
#         print("value of i:",i,"|value of j:",j,"|value of arr[j]:",arr[j],"|value of arr[j+1]:",arr[j+1])
#         # check and swap
#         if arr[j]> arr[j+1]:
#             print("B-Swap:","arr[j]:",arr[j],"arr[j+1]:",arr[j+1])
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             print("A-Swap:","arr[j]:",arr[j],"arr[j+1]:",arr[j+1])
#         else: print("-No-Swap-")
# print(arr)

arr = [2,45,66,34,234,23,345,657,87]

size = len(arr)

for i in range(size):
    for j in range(size - i - 1):
        if arr[j]> arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(" with bubble ")
print(arr)