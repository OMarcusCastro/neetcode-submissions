class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])

        prev1 = 0
        prev2 = nums[0]
        temp = prev2
        for i in range(1, len(nums) - 1):
            temp = max(prev1 + nums[i], prev2)
            prev1 = prev2
            prev2 = temp
        resp1 = temp

        prev1 = 0
        prev2 = nums[1]
        temp = prev2
        for i in range(2, len(nums)):
            temp = max(prev1 + nums[i], prev2)
            prev1 = prev2
            prev2 = temp
        return max(resp1, temp)