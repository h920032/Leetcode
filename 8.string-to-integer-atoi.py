#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        l = len(s)
        if l == 0: return 0
        is_positive = 1
        is_digit = True
        out = 0
        for c in s:
            if c == '-' and is_digit:
                is_positive = -1
                is_digit = False
            elif c == '+' and is_digit: 
                is_digit = False
            elif c == ' ' and is_digit: continue
            elif c.isdigit():
                is_digit = False
                out *= 10
                out += int(c)
            elif not c.isdigit():
                break
        out = is_positive * out
        if out > 2**31 - 1:
            return 2**31 -1
        if out < -2**31:
            return -2**31
        return out
# @lc code=end

