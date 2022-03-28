#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for c in range(31):
            out += (n & 1)
            n = n >> 1
            out = out << 1
        out += (n & 1)
        return out
                
# @lc code=end

