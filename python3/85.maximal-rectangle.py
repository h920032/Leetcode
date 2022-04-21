#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 2)
        max_area = 0
        for i in range(0, m):
            stack = []
            for j in range(n + 2):
                if j > 0 and j < n + 1:
                    if int(matrix[i][j - 1]) > 0: heights[j] = int(matrix[i][j - 1]) + heights[j]
                    else: heights[j] = 0
                while len(stack) > 0 and heights[stack[-1]] > heights[j]:
                    max_area = max(max_area, heights[stack.pop()] * (j - stack[-1] - 1))
                stack.append(j)
        return max_area
                
# @lc code=end

