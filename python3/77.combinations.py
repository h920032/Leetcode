#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        @cache
        def triverse(m, k):
            out = []
            if k == 0: return [[]]
            for i in range(m, n):
                out += [[i + 1] + s for s in triverse(i + 1, k - 1)]
            return out
        return triverse(0, k)
                
# @lc code=end

