#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        dp = [0 for _ in range(len(prices))]
        for t in range(k):
            pos = -prices[0]
            profit = 0
            for i in range(len(prices)):
                pos = max(pos, dp[i] - prices[i])
                profit = max(profit, prices[i] + pos)
                dp[i] = profit
        return dp[-1]
                
# @lc code=end

