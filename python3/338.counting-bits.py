#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        @cache
        def dp(n):
            if n == 0: return 0
            if n == 1: return 1
            return dp(n//2) + n%2
        return [dp(i) for i in range(n + 1)]
        
# @lc code=end

