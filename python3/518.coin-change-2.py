#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change 2
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(n, amount):
            if n < 0 and amount != 0: return 0
            if amount == 0: return 1
            count = 0
            while amount >= 0:
                count += dp(n - 1, amount)
                amount -= coins[n]
            return count
        return dp(len(coins) - 1, amount)

# bottom dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for a in range(c, amount+1):
                dp[a] += dp[a - c]
        return dp[amount]
                
# @lc code=end

