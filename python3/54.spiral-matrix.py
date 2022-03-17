#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l_row = len(matrix)
        l_col = len(matrix[0])
        out = []
        flag = True
        go_col = True
        current_r = 0
        current_c = 0
        go_rev = 1
        while flag:
            out.append(matrix[current_r][current_c])
            matrix[current_r][current_c] = None
            if go_col:
                if current_c + go_rev < l_col and current_c + go_rev >= 0 and matrix[current_r][current_c + go_rev] != None:
                    current_c += go_rev
                elif current_r + go_rev < l_row and current_r + go_rev >= 0 and matrix[current_r + go_rev][current_c] != None:
                    go_col = False
                    current_r += go_rev
                else:
                    flag = False
            else:
                if current_r + go_rev < l_row and current_r + go_rev >= 0 and matrix[current_r + go_rev][current_c] != None:
                    current_r += go_rev
                elif current_c - go_rev < l_col and current_c - go_rev >= 0 and matrix[current_r][current_c - go_rev] != None:
                    go_col = True
                    go_rev = -go_rev
                    current_c += go_rev
                else:
                    flag = False
        return out
                
# @lc code=end

