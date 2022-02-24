#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def solveSudoku(self, board) -> None:
        def dp(i, j, v, c, v_set, h_set, s_set):
            s = i//3 + (j//3)*3
            t = str(v)
            if (t not in v_set[i]) and (t not in h_set[j]) and (t not in s_set[s]):
                board[i][j] = t
                in_h_set = [r.copy() for r in h_set]
                in_v_set = [r.copy() for r in v_set]
                in_s_set = [r.copy() for r in s_set]
                in_h_set[j].add(t)
                in_v_set[i].add(t)
                in_s_set[s].add(t)
                in_cache = c.copy()
                clean = True
                for in_i in range(9):
                    for in_j in range(9):
                        if board[in_i][in_j] == '.':
                            clean = False
                            for in_v in range(9):
                                if (in_i, in_j, in_v+1) not in c:
                                    if not dp(in_i, in_j, in_v+1, in_cache, in_v_set, in_h_set, in_s_set):
                                        in_cache.add((in_i, in_j, in_v+1))
                                    else:
                                        return True
                            board[i][j] = '.'
                            return False
                if clean:
                    return clean
            return False
        
        v_set = [set() for i in range(9)]
        h_set = [set() for i in range(9)]
        s_set = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                s = i//3 + (j//3)*3
                if board[i][j] != '.':
                    h_set[j].add(board[i][j])
                    v_set[i].add(board[i][j])
                    s_set[s].add(board[i][j])
        
        cache = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for v in range(9):
                        print(v)
                        if not dp(i, j, v+1, cache, v_set, h_set, s_set):
                            cache.add((i, j, v+1))
                        else:
                            return None
                    return None


# @lc code=end

