#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0: return 0
        return n % 2 + self.hammingWeight(n//2)

class Solution:
    def hammingWeight(self, n: int) -> int:
        if n <= 1: return n
        return (n & 1) + self.hammingWeight(n >> 1)

# @lc code=end

