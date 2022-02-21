#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        match = "IVXLCDM"
        out = ""
        for i in range(0, 6, 2):
            t = num % 10
            num = num // 10
            if t == 9: out = match[i] + match[i + 2] + out
            elif t == 4: out = match[i] + match[i + 1] + out
            else: out = match[i + 1] * (t // 5) + match[i]*(t - 5*(t // 5)) + out
        out = num * match[6] + out
        return out
# @lc code=end

