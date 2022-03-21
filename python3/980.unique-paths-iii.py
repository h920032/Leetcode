#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#

# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def triverse(grid, i, j, r):
            count = 0
            if r > 0:
                if i + 1 < m and grid[i+1][j] == 0:
                    grid[i+1][j] = -1
                    count += triverse(grid, i+1, j, r - 1)
                    grid[i+1][j] = 0
                if i - 1 >= 0 and grid[i-1][j] == 0:
                    grid[i-1][j] = -1
                    count += triverse(grid, i-1, j, r - 1)
                    grid[i-1][j] = 0
                if j + 1 < n and grid[i][j+1] == 0:
                    grid[i][j+1] = -1
                    count += triverse(grid, i, j+1, r - 1)
                    grid[i][j+1] = 0
                if j - 1 >= 0 and grid[i][j-1] == 0:
                    grid[i][j-1] = -1
                    count += triverse(grid, i, j-1, r - 1)
                    grid[i][j-1] = 0
            elif r == 0:
                
                if i + 1 < m and grid[i+1][j] == 2:
                    return 1
                elif i - 1 >= 0 and grid[i-1][j] == 2:
                    return 1
                elif j + 1 < n and grid[i][j+1] == 2:
                    return 1
                elif j - 1 >= 0 and grid[i][j-1] == 2:
                    return 1
            return count
        x, y, r = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x = i
                    y = j
                if grid[i][j] == 0:
                    r += 1
        return triverse(grid, x, y, r)
                
# @lc code=end

