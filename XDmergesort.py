def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)// 2
    left_hand = merge_sort(arr[:mid])
    right_hand = merge_sort(arr[mid:])
    
    return merge(left_hand, right_hand)

#  function to merge two array with single element
def merge(left, right):
    sorted_arr = [] # extra space for merging
    i = j = 0 # pointer to access the number with index
    
    while i < len(left) and j < len(right):  # loop to check pointer is at index then length of arr
        if left[i] < right[j]:  # check left number is small then right number and || small value will only get append in second array 
            sorted_arr.append(left[i]) # add the number to array
            i +=1  #incerment of pointer for index
        else:
            sorted_arr.append(right[j])  # add hte small number to arr
            j += 1

    sorted_arr.extend(left[i:]) # CHECK IT 
    print(left[i:],"left[i:]")
    sorted_arr.extend(right[j:])
    print(right[j:],"right[j:]\n")
    # add or combile two arr in sorted_arr using '+'  
    # sorted_arr = sorted_arr + left[i:]
    # sorted_arr = sorted_arr + right[j:]
    
    return sorted_arr

arr = [1,5,7,5,4,3,2,1]

sorted_arr = merge_sort(arr)
print(sorted_arr)

#  