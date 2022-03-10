#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def check_finish(l):
            for c in l:
                if c > 1:
                    return False
            return True
        def poure(l):
            if l > 1:
                return (l - 1) / 2
            return 0
        poure_list = [[poured]]
        if query_row == 0:
            if poured >= 1: return 1
            else: return poured
        row = 0
        while True:
            if check_finish(poure_list[row]):
                break
            row += 1
            poure_list.append([0] * (row + 1))
            poure_list[row][0] = poure(poure_list[row - 1][0])
            poure_list[row][-1] = poure(poure_list[row - 1][-1])
            for c in range(1, row):
                poure_list[row][c] = poure(poure_list[row - 1][c]) + poure(poure_list[row - 1][c - 1])
            if row >= query_row:
                if poure_list[query_row][query_glass] > 1: return 1
                else: return poure_list[query_row][query_glass]
        return 0

# by dynamic programming
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        def poure(l):
            if l > 1:
                return (l - 1) / 2
            return 0
        @cache
        def dp(row, glass):
            if row == 0:
                return poured
            if glass == row:
                return poure(dp(row - 1, glass - 1))
            if glass == 0:
                return poure(dp(row - 1, 0))
            return poure(dp(row - 1, glass - 1)) + poure(dp(row - 1, glass))
        out = dp(query_row, query_glass)
        if out > 1: return 1
        return out
            
        
# @lc code=end

