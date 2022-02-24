#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 1
        j = 0
        max_len = 1
        if len(s) <= 1: return len(s)
        while i < len(s):
            if s[i] in s[j:i]:
                j += s[j:i].index(s[i]) + 1
            else:
                i += 1
                max_len = max(max_len, len(s[j:i]))
        return max_len
            



# @lc code=end

