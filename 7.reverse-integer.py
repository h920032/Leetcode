#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: return -self.reverse(-x)
        if x == 0: return 0
        out = 0
        while x > 0:
            out *= 10
            out += x%10
            x = x//10
        if out >= 2**31 or out < -2**31: return 0
        return out
# @lc code=end

