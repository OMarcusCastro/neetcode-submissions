class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        isIn ={}
        for i in range(len(nums)):
            isIn[nums[i]] = 1
        
        maxSeq =1
        visits = {}
        for i in range(len(nums)):
            count = 0 
            curr = nums[i]
            while isIn.get(curr,0)>0:
                
                visits[curr] = 1
                count+=1
                curr+=1
                
            
            maxSeq = max(count,maxSeq)
             
        print(visits)
        return maxSeq