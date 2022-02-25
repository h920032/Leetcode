#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start

# Dynamic Programming Like
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = len(candidates)
        @cache
        def dp(r, c):
            if r - candidates[c] == 0: return [[candidates[c]]]
            if r - candidates[c] > 0:
                s = []
                for i in range(c + 1):
                    if len(dp(r - candidates[c], i)) > 0:
                        s += dp(r - candidates[c], i)
                for i in range(len(s)):
                    s[i] = [candidates[c]] + s[i]
                return s
            return [] 
        out = []
        for i in range(l):
            out += dp(target, i)
        return out        


# @lc code=end

