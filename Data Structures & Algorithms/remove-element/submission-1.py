class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left,right = 0,len(nums)-1
        cont = 0

        while left<=right:
            if nums[right] == val:
                right-=1
            elif nums[left] == val:
                temp = nums[left]
                nums[left]=nums[right]
                nums[right] = temp
                right-=1
                left += 1
            elif nums[left]!=val:
                left+=1

        return left