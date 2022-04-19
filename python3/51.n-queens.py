#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        r, lr, rl = set(), set(), set()
        def backtrack(k):
            if k == n: return [[["." for i in range(n)] for i in range(n)]]
            out = []
            for i in range(n):
                if i not in r and k + i not in rl and k - i not in lr:
                    r.add(i)
                    rl.add(k + i)
                    lr.add(k - i)
                    for m in backtrack(k + 1):
                        m[i][k] = 'Q'
                        out.append(m)
                    r.remove(i)
                    rl.remove(k + i)
                    lr.remove(k - i)
            return out
        output = []
        for m in backtrack(0):
            output.append([''.join(l) for l in m])
        return output
                
# @lc code=end

