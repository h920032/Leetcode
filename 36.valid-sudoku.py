#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board) -> bool:
        l = len(board)
        v_set = []
        h_set = []
        s_set = []
        for i in range(l):
            v_set.append(set())
            h_set.append(set())
            s_set.append(set())
        for i in range(l):
            for j in range(l):
                s = i//3 + (j//3)*3
                if board[i][j] in v_set[i] or board[i][j] in h_set[j] or board[i][j] in s_set[s]:
                    return False
                if board[i][j] != '.':
                    h_set[j].add(board[i][j])
                    v_set[i].add(board[i][j])
                    s_set[s].add(board[i][j])
        return True


# @lc code=end

