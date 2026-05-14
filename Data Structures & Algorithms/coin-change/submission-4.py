class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def resolve(amt):
            if amt in dp:
                return dp[amt]
            if amt == 0:
                return 0
            if amt < 0:
                return -1

            min_coins = float('inf')
            for coin in coins:
                res = resolve(amt - coin)
                if res != -1:
                    min_coins = min(min_coins, res + 1)

            dp[amt] = min_coins if min_coins != float('inf') else -1
            return dp[amt]

        return resolve(amount)