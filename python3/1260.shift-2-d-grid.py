#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)
        new = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                t = (i * n + j + k) % (m * n)
                print(t)
                n_i = t // n
                n_j = t % n
                new[n_i][n_j] = grid[i][j]
        return new
                
# @lc code=end

