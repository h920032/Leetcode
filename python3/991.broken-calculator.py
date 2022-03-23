#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        def dp(s, t):
            if s >= t: return s - t
            if t % 2 == 0:
                return 1 + dp(s, t // 2)
            else:
                return 1 + dp(s, t + 1)
        return dp(startValue, target)
                
# @lc code=end

