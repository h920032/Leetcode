#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l_s, l_p = len(s), len(p)
        @cache
        def match(i, j):
            if j == l_p: return i == l_s
            if l_p - j == 1 or p[j+1] != '*':
                if i == l_s or (p[j] != s[i] and p[j] != '.'): return False
                else: return match(i + 1, j + 1)
            if i == l_s or (s[i] != p[j] and p[j] != '.'): return match(i, j + 2)
            return match(i, j + 2) or match(i + 1, j)
        return match(0,0)
                    
# @lc code=end

