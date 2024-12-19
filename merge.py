# def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

nums1 = [1,2,3,6]
nums2 = [8,10]

m = len(nums1)
n = len(nums2)

sorted_arr = []
i = j = 0

# Only consider the first m elements of nums1 and first n elements of nums2
while i < m and j < n:
    if nums1[i] < nums2[j]:
        sorted_arr.append(nums1[i])
        i += 1
    else:
        sorted_arr.append(nums2[j])
        j += 1

# Append any remaining elements of nums1
while i < m:
    sorted_arr.append(nums1[i])
    i += 1

# Append any remaining elements of nums2
while j < n:
    sorted_arr.append(nums2[j])
    j += 1

# Copy the sorted elements back into nums1
for k in range(len(sorted_arr)):
    nums1[k] = sorted_arr[k]

print(sorted_arr)
    