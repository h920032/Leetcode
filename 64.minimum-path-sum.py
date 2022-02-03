#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        @cache
        def dp(i: int, j: int) -> int:
            if i == 0 and j == 0: return grid[0][0]
            if i == 0: return dp(i, j-1) + grid[i][j]
            elif j == 0: return dp(i-1, j) + grid[i][j]
            else: return min(dp(i, j-1), dp(i-1, j)) + grid[i][j]
        return dp(m-1,n-1)
# @lc code=end

