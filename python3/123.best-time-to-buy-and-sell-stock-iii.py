#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
# two DP solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i - 1])
        lr_dp = [0] * len(diff)
        rl_dp = [0] * len(diff)
        max_sum_l, max_sum_r = 0, 0
        local_count_l, local_count_r = 0, 0
        for i in range(len(diff)):
            if local_count_l + diff[i] > 0: local_count_l += diff[i]
            else: local_count_l = 0 if diff[i] < 0 else diff[i]
            max_sum_l = max(max_sum_l, local_count_l)
            lr_dp[i] = max_sum_l
            if local_count_r + diff[-i-1] > 0: local_count_r += diff[-i-1]
            else: local_count_r = 0 if diff[-i-1] < 0 else diff[-i-1]
            max_sum_r = max(max_sum_r, local_count_r)
            rl_dp[-i-1] = max_sum_r
        rl_dp += [0]
        max_all = 0
        for i in range(len(diff)):
            max_all = max(max_all, lr_dp[i] + rl_dp[i + 1])
        return max_all

# one pass
class Solution(object):
    def maxProfit(self, prices):
        t1_cost, t2_cost = float('inf'), float('inf')
        t1_profit, t2_profit = 0, 0

        for price in prices:
            # the maximum profit if only one transaction is allowed
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)
            # reinvest the gained profit in the second transaction
            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)
            
        return t2_profit

# @lc code=end

