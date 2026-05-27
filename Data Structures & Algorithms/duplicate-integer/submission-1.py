class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for ele in nums:
            if hash.get(ele,0)==1:
                return True
            
            hash[ele] = 1
        return False
