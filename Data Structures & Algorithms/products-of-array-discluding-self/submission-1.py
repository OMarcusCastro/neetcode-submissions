
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        initalToFinal = [1]*len(nums)
        finaToinitial = [1]*len(nums)
        initalToFinal[0]=nums[0]
        finaToinitial[-1] = nums[-1]

        for i in range(1,len(nums)):
            initalToFinal[i] = initalToFinal[i-1]*nums[i]
            # print(initalToFinal,nums[i])

        for i in range(0,len(nums)-1):
            inverse = len(nums)-i-1
            finaToinitial[inverse-1] = finaToinitial[inverse]*nums[inverse-1]
            # print(finaToinitial,nums[inverse-1])
        ans = [1]*len(nums)

        for i in range(1,len(nums)-1):
            ans[i]=initalToFinal[i-1]*finaToinitial[i+1]
        ans[0] = finaToinitial[1]
        ans[-1]= initalToFinal[-2]
        # print(initalToFinal)
        # print(finaToinitial)
        return ans