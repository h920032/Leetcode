#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1: return cost[0]
        if n == 0: return 0
        @cache
        def dp(i: int) -> int:
            if n - i <= 2:
                return cost[i]
            else:
                return cost[i] + min(dp(i + 1), dp(i + 2))
        return min(dp(0),dp(1))
# @lc code=end

