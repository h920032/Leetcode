#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        is_count = [[0 for i in range(n)] for i in range(m)]
        count = 0
        def triverse(x, y):
            if x - 1 >= 0 and grid[x-1][y] == "1" and is_count[x-1][y] == 0:
                is_count[x-1][y] = 1
                triverse(x-1, y)
            if x + 1 < m and grid[x+1][y] == "1" and is_count[x+1][y] == 0:
                is_count[x+1][y] = 1
                triverse(x+1, y)
            if y - 1 >= 0 and grid[x][y-1] == "1" and is_count[x][y-1] == 0:
                is_count[x][y-1] = 1
                triverse(x, y-1)
            if y + 1 < n and grid[x][y+1] == "1" and is_count[x][y+1] == 0:
                is_count[x][y+1] = 1
                triverse(x, y+1)
            return None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and is_count[i][j] == 0:
                    is_count[i][j] = 1
                    count += 1
                    triverse(i,j)
        return count        
# @lc code=end

