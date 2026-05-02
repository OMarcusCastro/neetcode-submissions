class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if nums is None:
            return False

        left =0
        right = 0

        if len(nums)<2:
            return False
        if k ==0:
            return False

        while right<len(nums)-1:
            if abs(right-left)<k:
                right +=1
            else:
                left+=1
            if nums[left]==nums[right] and left!=right:
                return True
            
            
            
        
            
        
        return False


