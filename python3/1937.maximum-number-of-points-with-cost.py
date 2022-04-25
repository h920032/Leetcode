#
# @lc app=leetcode id=1937 lang=python3
#
# [1937] Maximum Number of Points with Cost
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        max_points = [p for p in points[0]]
        for i in range(1, m):
            for j in range(1, n):
                max_points[j] = max(max_points[j - 1] - 1, max_points[j])
            for j in reversed(range(n - 1)):
                max_points[j] = max(max_points[j + 1] - 1, max_points[j])
            for j in range(n):
                max_points[j] += points[i][j]
        return max(max_points)
                
# @lc code=end

