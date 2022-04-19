#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        r, lr, rl = set(), set(), set()
        def backtrack(k):
            if k == n: return 1
            count = 0
            for i in range(n):
                if i not in r and k + i not in rl and k - i not in lr:
                    r.add(i)
                    rl.add(k + i)
                    lr.add(k - i)
                    count += backtrack(k + 1)
                    r.remove(i)
                    rl.remove(k + i)
                    lr.remove(k - i)
            return count
        return backtrack(0)
                
# @lc code=end

