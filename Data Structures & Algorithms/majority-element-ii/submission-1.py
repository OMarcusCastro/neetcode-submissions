class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1,cont1 =None,0
        cand2,cont2 =None,0 

        for element in nums:

            if element == cand1:
                cont1+=1
            elif element == cand2:
                cont2+=1
            elif cont1==0:
                cand1=element
                cont1=1
            elif cont2 == 0:
                cand2=element
                cont2+=1
            else:
                cont1-=1
                cont2-=1

        cont1=0
        cont2=0

        for element in nums:
            if element ==cand1:
                cont1+=1
            if element ==cand2:
                cont2+=1
        ans = []
        if cont1>len(nums)//3:
            ans.append(cand1)
        if cont2>len(nums)//3:
            ans.append(cand2)

        return ans
