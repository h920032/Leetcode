#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l_1, l_2 = len(text1), len(text2)
        @cache
        def dp(t_1, t_2):
            if t_1 == l_1 or t_2 == l_2: return 0
            max_len = 0
            max_len = max(max_len, dp(t_1 + 1, t_2))
            for i in range(t_2, l_2):
                if text1[t_1] == text2[i]:
                    max_len = max(max_len, 1 + dp(t_1 + 1, i + 1))
                    break
            return max_len
        return dp(0, 0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l_1, l_2 = len(text1), len(text2)
        @cache
        def dp(t_1, t_2):
            if t_1 == l_1 or t_2 == l_2: return 0
            if text1[t_1] == text2[t_2]: return 1 + dp(t_1 + 1, t_2 + 1)
            return max(dp(t_1 + 1, t_2), dp(t_1, t_2 + 1))
        return dp(0,0)

# @lc code=end

