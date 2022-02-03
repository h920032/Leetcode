#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
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
            if c[i] > 0: return dp(i - 1) + c[i]
            else: return dp(i - 1)
        
        return max(dp(i) for i in range(len(c)))
        

# @lc code=end

