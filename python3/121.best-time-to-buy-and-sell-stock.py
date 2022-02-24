#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        c = []
        for i in range(1, len(prices)):
            c.append(prices[i] - prices[i - 1])
        @cache
        def dp(i: int) -> int:
            if i < 0: return 0
            return max(c[i], dp(i - 1) + c[i], 0)
        return max(dp(i) for i in range(len(c)))
# @lc code=end

