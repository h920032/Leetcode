#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        s_r = s[::-1]
        l = len(s)
        count = 0
        for i in range(l + 1):
            for j in range(i + 1, l + 1):
                if s[i:j] == s_r[l - j:l - i]: count += 1
        return count
                
# @lc code=end

