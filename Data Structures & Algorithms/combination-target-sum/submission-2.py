class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i,nums,cur,curSum,target):
            if curSum == target:
                self.combs.append(cur.copy())
                return

            if i>=len(nums) or curSum>target:
                return

            cur.append(nums[i])
            helper(i,nums,cur,curSum+nums[i],target)
            cur.pop()
            helper(i+1,nums,cur,curSum,target)
        
        self.combs = []
        
        helper(0,nums,[],0,target)
        return self.combs