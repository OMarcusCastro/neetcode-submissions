class Solution:
    def dfs(self,i,nums,total = 0):
        if i >= len(nums):
            return total

        return self.dfs(i+1,nums,total^nums[i])+self.dfs(i+1,nums,total)
        

    def subsetXORSum(self, nums: List[int]) -> int:
        return self.dfs(0,nums)