def reverseArray(arr):
    res = []
    
    # Loop through each item and insert
    # it at the beginning of new list
    for val in arr:
        res.insert(0, val)
    print(res)
    
def rev(arr):
    arr = arr[::-1]
    print(arr)
arr = [2,3,4,5]
# reverseArray(arr)
rev(arr)