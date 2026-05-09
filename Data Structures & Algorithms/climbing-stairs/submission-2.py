class Solution:
    def climbStairs(self, n: int) -> int:
        
        def countEdges(n,curr_n,count,cache):

            if curr_n == n :
                count+=1
                return count
            
            if curr_n > n:
                return 0
            if not cache.get(curr_n+1):
                cache[curr_n+1] = countEdges(n,curr_n+1,count,cache)
            if not cache.get(curr_n+2):
                cache[curr_n+2] = countEdges(n,curr_n+2,count,cache)

            count = cache[curr_n+1]+cache[curr_n+2]
            return count

        return countEdges(n,0,0,{})