#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_x = set()
        zero_y = set()
        l_y = len(matrix)
        l_x = len(matrix[0])
        for i in range(l_y):
            for j in range(l_x):
                if matrix[i][j] == 0:
                    zero_y.add(i)
                    zero_x.add(j)
        for i in zero_y:
            for j in range(l_x):
                matrix[i][j] = 0
        for i in zero_x:
            for j in range(l_y):
                matrix[j][i] = 0
                        
# @lc code=end

