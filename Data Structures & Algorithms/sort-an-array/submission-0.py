def mergeSort(nums):
    if len(nums)<=1:
        return nums
    mid = (len(nums))//2

    sortedArray = []

    left = mergeSort(nums[0:mid])
    right = mergeSort(nums[mid:])

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]<=right[j]:
            sortedArray.append(left[i])
            i+=1
        else:
            sortedArray.append(right[j])
            j+=1

    sortedArray.extend(left[i:])
    sortedArray.extend(right[j:])

    return sortedArray

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return mergeSort(nums)