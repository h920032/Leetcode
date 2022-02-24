#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        if divisor == 1: return dividend
        if dividend < 0 and divisor < 0:
            out = self.divide(-dividend, -divisor)
            if out > 2147483647:
                return 2147483647
            if out < -2147483648:
                return -2147483648
            return out
        if dividend < 0 and divisor > 0:
            out = -self.divide(-dividend, divisor)
            if out > 2147483647:
                return 2147483647
            if out < -2147483648:
                return -2147483648
            return out
        if dividend > 0 and divisor < 0:
            return -self.divide(dividend, -divisor)
        
        def rec_div(dividend, divisor, count):
            if dividend >= divisor:
                r, c = rec_div(dividend, divisor + divisor, count + count)
                while r - divisor >= 0:
                    r -= divisor
                    c += count
                return (r, c)
            else:
                return (dividend, 0)
        out = rec_div(dividend, divisor, 1)[1]
        if out > 2147483647:
            return 2147483647
        if out < -2147483648:
            return -2147483648
        return out
                        
# @lc code=end

