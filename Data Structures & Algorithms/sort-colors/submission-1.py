class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hash = [0,0,0]
        for element in nums:
            hash[element]+=1

        j =0
        val = 0
        for i in range(len(nums)):
            while hash[j]==0:
                j+=1
                val+=1
            nums[i] = val
            hash[j]-=1

