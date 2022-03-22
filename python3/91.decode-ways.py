#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
# DP like solution
class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        @cache
        def backtrack(n):
            if n == l: return 1
            if s[n] == '0': return 0
            count = backtrack(n + 1)
            if n + 1 < l:
                if 10*(ord(s[n]) - 48) + (ord(s[n + 1]) - 48) <= 26:
                    count += backtrack(n + 2)
            return count
        return backtrack(0)

# @lc code=end

