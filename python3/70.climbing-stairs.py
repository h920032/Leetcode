#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
# @lc code=end

