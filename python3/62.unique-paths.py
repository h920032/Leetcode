#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def recursive(m, n):
            if m + n == 0: return 1
            if m == 0 or n == 0: return 1
            return recursive(m, n-1) + recursive(m-1, n)
        return recursive(m - 1, n - 1)

# with combination formula

class Solution:
    @cache
    def fractional(self, n):
        if n <= 0: return 1
        return n * self.fractional(n - 1)
    
    def uniquePaths(self, m: int, n: int) -> int:
        steps = m + n - 2
        down = m - 1
        return self.fractional(steps) // self.fractional(down) // self.fractional(steps - down)

# @lc code=end

