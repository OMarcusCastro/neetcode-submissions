class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [7,1,6,5,8,10,2]-> 
        # [7,12,2,100,4]->100,4,96
        # [1,1,1]->0
        # [1]/[]->0
        max_delta = 0
        #mission: start=0, load de diff i'th and i+1'th and if i+1'th>i'th change delta
        if not prices:
            return 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            
            delta = prices[i] - min_price
            if delta > max_delta:
                max_delta = delta
                
        return max_delta