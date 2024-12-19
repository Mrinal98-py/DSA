arr = [1,2,3,4,5,8]
rev = []
def reverseArray(arr):
    left = 0
    right = len(arr)-1
    while(left <= right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    print(arr)

def rev(arr):
        # 1 pointer + extra space
    rev = []
    n = len(arr) - 1
    
    while (n >= 0):
        rev.append(arr[n])
        n -= 1
    print(rev)
        
rev(arr)
# reverseArray(arr)
        
    