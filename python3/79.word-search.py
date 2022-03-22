#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        def triverse(i, j, c):
            if c == l - 1:
                return True
            t = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for x in t:
                if x[0] + i >= 0 and x[0] + i < m and x[1] + j >= 0 and x[1] + j < n and board[x[0] + i][x[1] + j] == word[c + 1]:
                    board[x[0] + i][x[1] + j] = ""
                    if triverse(x[0] + i, x[1] + j, c + 1):
                        return True
                    board[x[0] + i][x[1] + j] = word[c + 1]
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = ""
                    if triverse(i,j,0):
                        return True
                    board[i][j] = word[0]
                            
# @lc code=end

