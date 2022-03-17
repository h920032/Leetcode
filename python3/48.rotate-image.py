#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        for i in range(l // 2):
            for j in range(l - 2 * i - 1):
                temp = matrix[i][i + j]
                matrix[i][i + j] = matrix[l - (i + j) - 1][i]
                matrix[l - (i + j) - 1][i] = matrix[l - i - 1][l - (i + j) - 1]
                matrix[l-i-1][l-(i+j)-1] = matrix[i+j][l-i-1]
                matrix[i+j][l-i-1] = temp

# reverse + transpose
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        for i in range(l):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(l):
            for j in range(l // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][l - j - 1]
                matrix[i][l - j - 1] = temp

# @lc code=end

