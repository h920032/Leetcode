#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amount):
            if amount == 0: return 0
            min_count = float(inf)
            for c in coins:
                if c <= amount:
                    min_count = min(1 + dp(amount - c), min_count)
            return min_count
        if dp(amount) == float(inf): return -1
        return dp(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [float('inf')] * (amount + 1)
        count[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                count[x] = min(count[x], count[x - coin] + 1)
        return count[amount] if count[amount] != float('inf') else -1        
# @lc code=end

