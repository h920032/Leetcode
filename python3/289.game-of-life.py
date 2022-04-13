#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                s = 0
                for x in range(3):
                    for y in range(3):
                        x_t = i - 1 + x
                        y_t = j - 1 + y
                        if x_t >= 0 and x_t < m and y_t >=0 and y_t < n:
                            s += 1 if board[x_t][y_t] > 0 else 0
                s -= board[i][j]
                if board[i][j] == 1 and (s > 3 or s < 2):
                    board[i][j] = 2
                if board[i][j] == 0 and s == 3:
                    board[i][j] = -1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 0
                if board[i][j] == -1: board[i][j] = 1
                
# @lc code=end

