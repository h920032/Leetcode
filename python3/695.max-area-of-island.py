#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        index = 0
        count = [0]
        m = len(grid)
        n = len(grid[0])
        is_find = [[0 for i in range(n)] for i in range(m)]
        max_area = 0
        def triverse(x, y):
            if x - 1 >= 0 and grid[x-1][y] == 1 and is_find[x-1][y] == 0:
                is_find[x-1][y] = index
                count[index] += 1
                triverse(x-1, y)
            if x + 1 < m and grid[x+1][y] == 1 and is_find[x+1][y] == 0:
                is_find[x+1][y] = index
                count[index] += 1
                triverse(x+1, y)
            if y - 1 >= 0 and grid[x][y-1] == 1 and is_find[x][y-1] == 0:
                is_find[x][y-1] = index
                count[index] += 1
                triverse(x, y-1)
            if y + 1 < n and grid[x][y+1] == 1 and is_find[x][y+1] == 0:
                is_find[x][y+1] = index
                count[index] += 1
                triverse(x, y+1)
            return None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and is_find[i][j] == 0:
                    index += 1
                    is_find[i][j] = index
                    count.append(1)
                    triverse(i,j)
        return max(count)        
# @lc code=end

