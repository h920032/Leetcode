#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m - 1
        t_index = -1
        while left <= right:
            middle = ((right - left) // 2) + left
            if matrix[middle][0] == target:
                t_index = middle
                break
            if matrix[middle][0] > target:
                right = middle - 1
            else:
                left = middle + 1
        if t_index == -1: t_index = right
        left = 0
        right = n - 1
        while left <= right:
            middle = ((right - left) // 2) + left
            if matrix[t_index][middle] == target:
                return True
            if matrix[t_index][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False
                    
# @lc code=end

