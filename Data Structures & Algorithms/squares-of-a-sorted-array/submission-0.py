class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        ans = [0]*len(nums)
        l = 0
        r = len(nums)-1

        i = len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                ans[i]=nums[l]**2
                l+=1
            else:
                ans[i]=nums[r]**2
                r-=1
            i-=1
        return ans