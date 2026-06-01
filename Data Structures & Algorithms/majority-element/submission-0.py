class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hash = {}
        for ele in nums:
            hash[ele]=hash.get(ele,0)+1
            if hash[ele]> (n/2):
                return ele