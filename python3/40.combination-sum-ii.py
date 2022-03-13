#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        l = len(candidates)
        @cache
        def dp(r, c):
            if r - candidates[c] == 0: return [[candidates[c]]]
            if r - candidates[c] > 0:
                s = []
                for i in range(c - 1, -1, -1):
                    if i != c - 1 and candidates[i] == candidates[i + 1]:
                        continue
                    if len(dp(r - candidates[c], i)) > 0:
                        s += dp(r - candidates[c], i)
                for i in range(len(s)):
                    s[i] = s[i]+[candidates[c]]
                return s
            return [] 
        out = []
        for i in range(l - 1, -1, -1):
            if i != l - 1 and candidates[i] == candidates[i + 1]:
                continue
            for j in dp(target, i):
                if j not in out:
                    out.append(j)
        return out
        
# @lc code=end

