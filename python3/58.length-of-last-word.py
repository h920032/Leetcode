#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        t = 0
        for i in range(l-1,-1,-1):
            if s[i] == ' ' and t != 0:
                return t
            elif s[i] != ' ':
                t += 1
        return t

# @lc code=end

