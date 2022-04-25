#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)
        @cache
        def dp(s):
            if len(s) == 1: return 1
            max_len = 0
            for i in range(1,len(s) + 1):
                if s[:i-1] + s[i:] in words_set:
                    max_len = max(dp(s[:i-1] + s[i:]), max_len)
            return max_len + 1
        return max([dp(w) for w in words])
                
# @lc code=end

