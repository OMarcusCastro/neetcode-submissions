class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [-1] * len(s)
        def dfs(i):

            if i == len(s):
                return 1
            if i>len(s)-1:
                return 0
            if s[i]=='0':
                return 0
            
            if dp[i]>=0:
                return dp[i]
            
            resp =0
            
            resp+=dfs(i+1)

            if i+1<len(s):
                curr = int(s[i:i+2])
                if curr <= 26:
                   resp+= dfs(i+2)
            dp[i] = resp
            return resp

        return dfs(0)
