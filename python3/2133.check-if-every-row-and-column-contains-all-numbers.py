#
# @lc app=leetcode id=2133 lang=python3
#
# [2133] Check if Every Row and Column Contains All Numbers
#

# @lc code=start
from tkinter import Y


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        h_check = [[0] * n for i in range(n)]
        v_check = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if h_check[i][matrix[i][j] - 1] == 1 or v_check[j][matrix[i][j] - 1] == 1: return False
                h_check[i][matrix[i][j] - 1] = 1
                v_check[j][matrix[i][j] - 1] = 1
        return True
# @lc code=end

