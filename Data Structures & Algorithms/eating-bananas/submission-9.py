class Solution:

    def totalTimeForK(self,piles: List[int],k:int):
        totalTime =0
        
        for pile in piles:
            
            time = pile//k
            print(pile,time,"time")
            totalTime += time
            if time ==0 or pile%k!=0:
                totalTime+=1
        print(k,totalTime)
        return totalTime

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #h<len(piles) -> impossible
        #time for on pile : p[i]/k 
        # binary search for k
        # calculate total time for each K till possible k between 1 and max(piles)
        left =1
        right = max(piles)
        res = right

        while left<=right:
            k_mid = (left+right)//2
            totalTime = self.totalTimeForK(piles,k_mid)

            if totalTime>h:
                left = k_mid+1
            else:
                res = k_mid
                right = k_mid-1
        return res

                
            

            