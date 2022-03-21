#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        @cache
        def recursive(m, n):
            if obstacleGrid[m][n] == 1: return 0
            if m == 0 and n == 0: return 1
            if m == 0: return recursive(0, n - 1)
            if n == 0: return recursive(m - 1, 0)
            return recursive(m - 1, n) + recursive(m, n - 1)
        return recursive(m - 1, n - 1)
                
# @lc code=end

