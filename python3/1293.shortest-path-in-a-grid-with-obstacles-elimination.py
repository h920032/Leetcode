#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        start = (0, 0, k)
        visited = set([start])
        queue = [(0, start)]
        
        if k >= m + n - 2: return m + n - 2
        
        while queue:
            step, (i,j,k) = queue[0]
            queue = queue[1:]
            
            if i == m - 1 and j == n - 1: return step
            
            f = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for x, y in f:
                if 0 <= i + x < m and 0 <= j + y < n:
                    new_state = (i + x, j + y, k - grid[i + x][j + y])
                    if new_state[2] >= 0 and new_state not in visited:
                        visited.add(new_state)
                        queue.append((step + 1, new_state))       
        return -1

# with A*
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        def estimate(i, j):
            return (m - 1 - i + n - 1 - j)
        start = (0, 0, k)
        visited = set([start])
        heap = [(estimate(0, 0), 0, start)]
        f = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while heap:
            dis, step, (i,j,k) = heappop(heap)
            if k >= dis - step: return dis
            for x, y in f:
                if 0 <= i + x < m and 0 <= j + y < n:
                    new_state = (i + x, j + y, k - grid[i + x][j + y])
                    if new_state[2] >= 0 and new_state not in visited:
                        visited.add(new_state)
                        heappush(heap, (estimate(i + x,j + y) + step + 1, step + 1, new_state))
        return -1

# @lc code=end

