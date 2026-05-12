class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def solve(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in dp:
                return dp[i]

            result = solve(i + 1)

            if i + 1 < len(s):
                two = int(s[i:i+2])
                if 10 <= two <= 26:
                    result += solve(i + 2)

            dp[i] = result
            return result

        return solve(0)