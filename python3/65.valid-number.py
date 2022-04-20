#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        with_e = False
        with_sign = False
        with_dot = False
        in_digit = False
        for i in s:
            if not in_digit and i.isdigit():
                in_digit = True
            if i == '+' or i == '-':
                if in_digit or with_sign or (with_dot and not with_e): return False
                else: with_sign = True
            if i == '.': 
                if with_dot: return False
                with_dot = True
            if i == 'E' or i == 'e':
                if not in_digit or with_e: return False
                with_e = True
                with_dot = True
                with_sign = False
                in_digit = False
            elif i.isalpha(): return False
        if not in_digit: return False
        return True
                
# @lc code=end

